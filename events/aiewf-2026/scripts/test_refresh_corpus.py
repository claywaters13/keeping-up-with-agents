#!/usr/bin/env python3
"""Tests for the two refresh behaviours that fail SILENTLY rather than loudly.

    python3 scripts/test_refresh_corpus.py

Everything else in refresh_corpus.py announces its own failure: a gate that does
not pass exits nonzero with a message. These two do not, which is why they get
tests. Both concern the same trap, found on 2026-08-19.

A YouTube RE-UPLOAD keeps its own video id, and normalize.py's slug dedup keeps
the fuller existing copy, so the re-upload's id never reaches index.json. That
makes it permanently eligible and permanently un-ingestable: discovery
re-accepts it every week, forever. The unguarded run then does the whole
pipeline, finds zero new talks, and commits and pushes the enrichment drift
under a "0 newly published talks" message -- every Wednesday, on a public repo,
with nothing in the exit code to say anything was wrong.

  1. triage() must skip ids recorded in raw/known_reuploads.json, before it
     spends any network call on them.
  2. noop_all_reuploads() must put the tracked tree back and exit 0 without
     committing, so the drift never reaches a commit in the first place.

Stdlib only, no network, no model calls: the git fixture is a throwaway repo in
a temp dir and every candidate under test is a known re-upload, so the metadata
fetch is asserted never to run.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import refresh_corpus as rc  # noqa: E402


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, check=True)


def make_repo():
    """A throwaway repo shaped like the real one: refresh paths, podcast files,
    and somebody else's untracked work in the tree."""
    repo = tempfile.mkdtemp(prefix="refresh-test-")
    for rel in ("events/aiewf-2026/wiki", "events/aiewf-2026/scripts",
                ".claude-plugin", "skills", "evals", "scripts"):
        os.makedirs(os.path.join(repo, rel), exist_ok=True)
    files = {
        "README.md": "246 talks\n",
        "events/aiewf-2026/wiki/README.md": "corpus\n",
        "events/aiewf-2026/scripts/add_episode.py": "# podcast\n",
        ".claude-plugin/plugin.json": '{"version": "2.0.2"}\n',
        "feed.xml": "<rss/>\n",
        "scripts/add_episode.py": "# podcast\n",
    }
    for rel, body in files.items():
        with open(os.path.join(repo, rel), "w") as handle:
            handle.write(body)
    git(repo, "init", "-q")
    git(repo, "add", "-A")
    git(repo, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "init")
    return repo


class TriageSkipsKnownReuploads(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="refresh-known-")
        self._known = rc.KNOWN_REUPLOADS
        self._fetch = rc.fetch_meta
        rc.KNOWN_REUPLOADS = os.path.join(self.tmp, "known_reuploads.json")
        self.fetched = []
        rc.fetch_meta = lambda ids, **kw: (self.fetched.append(list(ids)) or {})
        rc.REPORT["reuploads_skipped"] = []

    def tearDown(self):
        rc.KNOWN_REUPLOADS = self._known
        rc.fetch_meta = self._fetch
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_known(self, mapping):
        with open(rc.KNOWN_REUPLOADS, "w") as handle:
            json.dump(mapping, handle)

    def test_a_known_reupload_is_never_accepted_or_even_fetched(self):
        self.write_known({"REUP123456A": {
            "absorbed_into_slug": "agents-need-receipts-not-more-tool-calls",
            "existing_video_id": "Fu45geO3zX8", "detected": "2026-08-19"}})

        accepted = rc.triage({}, ["REUP123456A"], [])

        self.assertEqual(accepted, [])
        self.assertEqual(rc.REPORT["reuploads_skipped"], ["REUP123456A"])
        # The point is not just that it is rejected later, but that it costs
        # nothing: a weekly yt-dlp call for a video that can never be ingested.
        self.assertEqual(self.fetched, [[]])

    def test_an_unknown_candidate_still_reaches_the_metadata_fetch(self):
        self.write_known({"REUP123456A": {"absorbed_into_slug": "x"}})

        rc.triage({}, ["REUP123456A", "FRESH000001"], [])

        self.assertEqual(self.fetched, [["FRESH000001"]])
        self.assertEqual(rc.REPORT["reuploads_skipped"], ["REUP123456A"])

    def test_track_only_candidates_are_filtered_too(self):
        # A re-upload can also surface in the topical playlists, where it would
        # otherwise sit in the human-review list forever.
        self.write_known({"REUP123456A": {"absorbed_into_slug": "x"}})

        rc.triage({}, [], ["REUP123456A"])

        self.assertEqual(rc.REPORT["track_only_total"], 0)
        self.assertEqual(rc.REPORT["track_only_candidates"], [])

    def test_a_corrupt_memory_file_degrades_to_empty_rather_than_crashing(self):
        with open(rc.KNOWN_REUPLOADS, "w") as handle:
            handle.write("{ not json")
        self.assertEqual(rc.load_known_reuploads(), {})


class NoopRestoresAndExitsClean(unittest.TestCase):
    def setUp(self):
        self.repo = make_repo()
        self._repo = rc.REPO
        rc.REPO = self.repo
        rc.REPORT["reuploads_detected"] = ["REUP123456A"]

    def tearDown(self):
        rc.REPO = self._repo
        shutil.rmtree(self.repo, ignore_errors=True)

    def dirty_everything(self):
        edits = {
            "README.md": "247 talks\n",                              # refresh drift
            "events/aiewf-2026/wiki/README.md": "rebuilt\n",         # refresh drift
            "feed.xml": "<rss>changed</rss>\n",                      # podcast, hands off
            "scripts/add_episode.py": "# edited\n",                  # podcast, hands off
            "events/aiewf-2026/scripts/add_episode.py": "# edited\n",  # podcast, hands off
        }
        for rel, body in edits.items():
            with open(os.path.join(self.repo, rel), "w") as handle:
                handle.write(body)
        os.makedirs(os.path.join(self.repo, "events/yc-startup-school-2026"), exist_ok=True)
        with open(os.path.join(self.repo, "events/yc-startup-school-2026/notes.md"), "w") as handle:
            handle.write("someone else's work in progress\n")

    def status(self):
        # rstrip("\n"), never .strip(): porcelain encodes staged-vs-unstaged in the
        # two leading columns, so stripping whitespace turns " M path" into
        # "M path" and quietly inverts the thing these assertions are checking.
        return sorted(
            line for line in
            git(self.repo, "status", "--porcelain").stdout.rstrip("\n").splitlines() if line)

    def test_it_exits_zero_without_committing_and_reverts_only_its_own_paths(self):
        self.dirty_everything()
        head_before = git(self.repo, "rev-parse", "HEAD").stdout.strip()

        with self.assertRaises(SystemExit) as caught:
            rc.noop_all_reuploads({"talks": 246})

        # Exit code is the contract the cron harness reads. A re-upload week is a
        # successful week, not a failure.
        self.assertEqual(caught.exception.code, 0)
        self.assertEqual(rc.REPORT["status"], "ok")
        self.assertEqual(rc.REPORT["new_talks"], 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD").stdout.strip(), head_before,
                         "the no-op path must never create a commit")

        remaining = self.status()
        # Its own drift is gone...
        self.assertNotIn(" M README.md", remaining)
        self.assertNotIn(" M events/aiewf-2026/wiki/README.md", remaining)
        # ...and nothing it does not own was touched.
        self.assertIn(" M feed.xml", remaining)
        self.assertIn(" M scripts/add_episode.py", remaining)
        self.assertIn(" M events/aiewf-2026/scripts/add_episode.py", remaining)
        self.assertIn("?? events/yc-startup-school-2026/", remaining)

    def test_it_reports_rather_than_deletes_anything_left_over(self):
        # An untracked file under a refresh path is not reverted by `checkout`.
        # Deleting it would be the job silently destroying someone's work, so the
        # run reports it and still exits 0.
        stray = os.path.join(self.repo, "events/aiewf-2026/stray.md")
        with open(stray, "w") as handle:
            handle.write("unexpected\n")

        with self.assertRaises(SystemExit) as caught:
            rc.noop_all_reuploads({"talks": 246})

        self.assertEqual(caught.exception.code, 0)
        self.assertTrue(os.path.exists(stray), "the no-op path must not delete files")


if __name__ == "__main__":
    unittest.main(verbosity=2)
