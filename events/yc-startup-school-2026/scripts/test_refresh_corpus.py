#!/usr/bin/env python3
"""Tests for the YC refresh behaviours that fail SILENTLY rather than loudly.

    python3 scripts/test_refresh_corpus.py

Same principle as events/aiewf-2026/scripts/test_refresh_corpus.py: gates that
exit nonzero with a message do not need tests, because they announce themselves.
These do not.

  1. THE FROZEN VOCABULARY'S ESCAPE VALVE. This job may never mint a canonical
     concept — that is a judgment about what the corpus is about, and an
     unattended weekly run is the wrong place for it. So unmapped strings get
     assigned or DROPped, and the silent-failure risk is that a genuinely new
     idea gets DROPped across many talks and nobody ever hears about it. The
     escalation threshold is the only thing standing between "safe" and "wrong".

  2. TRIAGE GATES. Playlist membership is this event's ONLY provenance signal —
     there is no schedule to cross-check against — so a trailer or a clip added
     to the playlist would sail straight into the corpus.

  3. THE NO-OP RESTORE. Same re-upload trap as AIEWF: a re-upload keeps its own
     video id, never reaches index.json, and would otherwise be re-ingested
     weekly and pushed as an empty refresh.

Stdlib only, no network, no model calls.
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


class TriageGates(unittest.TestCase):
    """Playlist membership is the only provenance signal, so shape is the rest."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="yc-triage-")
        self._known, self._fetch = rc.KNOWN_REUPLOADS, rc.fetch_meta
        rc.KNOWN_REUPLOADS = os.path.join(self.tmp, "known_reuploads.json")
        self.meta = {}
        rc.fetch_meta = lambda ids, **kw: {v: self.meta[v] for v in ids if v in self.meta}
        rc.REPORT["reuploads_skipped"] = []
        rc.REPORT["still_private"] = 0

    def tearDown(self):
        rc.KNOWN_REUPLOADS, rc.fetch_meta = self._known, self._fetch
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_a_real_session_is_accepted(self):
        self.meta["TALK00000001"] = ("20260807", "3422", "Max Hodak: Average Is Not Good Enough")
        accepted = rc.triage(["TALK00000001"])
        self.assertEqual([r["video_id"] for r in accepted], ["TALK00000001"])

    def test_a_short_clip_on_the_playlist_is_rejected(self):
        # The gate that matters most here: YC posts clips and trailers to the same
        # channel, and this event has no schedule to cross-check a candidate against.
        self.meta["CLIP00000001"] = ("20260807", "45", "Sam Altman on grit #shorts")
        self.assertEqual(rc.triage(["CLIP00000001"]), [])

    def test_a_pre_2026_upload_is_rejected(self):
        self.meta["OLD000000001"] = ("20250801", "1800", "Startup School 2025: something")
        self.assertEqual(rc.triage(["OLD000000001"]), [])

    def test_a_livestream_compilation_is_rejected(self):
        self.meta["LIVE00000001"] = ("20260807", "21600", "Startup School 2026 Day 1 livestream")
        self.assertEqual(rc.triage(["LIVE00000001"]), [])

    def test_an_unavailable_video_is_counted_not_failed(self):
        accepted = rc.triage(["PRIV00000001"])
        self.assertEqual(accepted, [])
        self.assertEqual(rc.REPORT["still_private"], 1)

    def test_a_known_reupload_is_skipped_before_any_fetch(self):
        with open(rc.KNOWN_REUPLOADS, "w") as handle:
            json.dump({"REUP00000001": {"absorbed_into_slug": "x"}}, handle)
        fetched = []
        rc.fetch_meta = lambda ids, **kw: (fetched.append(list(ids)) or {})
        self.assertEqual(rc.triage(["REUP00000001"]), [])
        self.assertEqual(fetched, [[]])
        self.assertEqual(rc.REPORT["reuploads_skipped"], ["REUP00000001"])


class FrozenVocabularyEscalation(unittest.TestCase):
    """A cron must not mint canonical concepts, so it has to shout instead."""

    def test_a_widely_dropped_string_is_escalated_for_human_review(self):
        raw_counts = {"vibe coding": 4, "one-off trivia": 1, "agent memory": 6}
        todo = ["vibe coding", "one-off trivia"]
        mapping = {"vibe coding": "DROP", "one-off trivia": "DROP",
                   "agent memory": "agent memory"}

        newly = [s for s in todo if mapping.get(s) == "DROP"
                 and raw_counts.get(s, 0) >= rc.NEW_CONCEPT_MIN_TALKS]

        # Appears in 4 talks and was dropped: exactly what an unnamed concept looks
        # like. One-off trivia in a single talk is correctly binned in silence.
        self.assertEqual(newly, ["vibe coding"])

    def test_the_threshold_is_talks_not_mentions(self):
        # build_raw_concepts counts DISTINCT talks per string (it de-dupes within a
        # talk), so a string one speaker says five times cannot fake a cluster.
        self.assertEqual(rc.NEW_CONCEPT_MIN_TALKS, 3)
        self.assertEqual(rc.PASSC_MIN_TALKS, 3)

    def test_build_raw_concepts_counts_each_talk_once(self):
        tmp = tempfile.mkdtemp(prefix="yc-concepts-")
        try:
            passa, concepts = os.path.join(tmp, "passA"), os.path.join(tmp, "concepts")
            os.makedirs(passa)
            os.makedirs(concepts)
            for slug, tags in (("a", ["moat", "moat", "pricing"]), ("b", ["moat"])):
                with open(os.path.join(passa, f"{slug}.json"), "w") as handle:
                    json.dump({"_meta": {"slug": slug},
                               "passA": {"concepts": tags}}, handle)
            old_passa, old_concepts = rc.PASSA, rc.CONCEPTS
            rc.PASSA, rc.CONCEPTS = passa, concepts
            try:
                counts = rc.build_raw_concepts()
            finally:
                rc.PASSA, rc.CONCEPTS = old_passa, old_concepts
            self.assertEqual(counts["moat"], 2)      # two talks, not three mentions
            self.assertEqual(counts["pricing"], 1)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


class NoopRestore(unittest.TestCase):
    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="yc-repo-")
        for rel in ("events/yc-startup-school-2026/wiki", ".claude-plugin", "scripts"):
            os.makedirs(os.path.join(self.repo, rel), exist_ok=True)
        for rel, body in {
            "README.md": "14 talks\n",
            "events/yc-startup-school-2026/wiki/README.md": "corpus\n",
            "feed.xml": "<rss/>\n",
            "scripts/add_episode.py": "# podcast\n",
        }.items():
            with open(os.path.join(self.repo, rel), "w") as handle:
                handle.write(body)
        git(self.repo, "init", "-q")
        git(self.repo, "add", "-A")
        git(self.repo, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "init")
        self._repo = rc.REPO
        rc.REPO = self.repo
        rc.REPORT["reuploads_detected"] = ["REUP00000001"]

    def tearDown(self):
        rc.REPO = self._repo
        shutil.rmtree(self.repo, ignore_errors=True)

    def test_it_exits_zero_without_committing_and_reverts_only_its_own_paths(self):
        for rel, body in {
            "README.md": "17 talks\n",
            "events/yc-startup-school-2026/wiki/README.md": "rebuilt\n",
            "feed.xml": "<rss>changed</rss>\n",
            "scripts/add_episode.py": "# edited\n",
        }.items():
            with open(os.path.join(self.repo, rel), "w") as handle:
                handle.write(body)
        os.makedirs(os.path.join(self.repo, "events/aiewf-2026"), exist_ok=True)
        with open(os.path.join(self.repo, "events/aiewf-2026/wip.md"), "w") as handle:
            handle.write("the other event's work\n")
        head = git(self.repo, "rev-parse", "HEAD").stdout.strip()

        with self.assertRaises(SystemExit) as caught:
            rc.noop_all_reuploads({"talks": 14})

        self.assertEqual(caught.exception.code, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD").stdout.strip(), head)
        # rstrip("\n"), never .strip(): porcelain encodes staged-vs-unstaged in the
        # two leading columns.
        remaining = git(self.repo, "status", "--porcelain").stdout.rstrip("\n").splitlines()
        self.assertNotIn(" M README.md", remaining)
        self.assertIn(" M feed.xml", remaining)
        self.assertIn(" M scripts/add_episode.py", remaining)
        # The sibling event is out of this orchestrator's pathspec entirely.
        self.assertIn("?? events/aiewf-2026/", remaining)


if __name__ == "__main__":
    unittest.main(verbosity=2)
