# How this was built

Corpus built 2026-08-19 from Y Combinator's Startup School 2026 (Chase Center, San
Francisco, July 25–26, 2026), in one session, from the event's official YouTube playlist.

This is the second event in this repo, and it was deliberately built as a **port** of the
first rather than a fresh design. [`events/aiewf-2026/BUILD.md`](../aiewf-2026/BUILD.md) is
the real engineering writeup — the no-RAG architecture, the deterministic quote gate, the
caption-glue bug, the measurements. This file only records what was reused, what had to
change, and what the numbers came out to.

## What was reused from AIEWF 2026, unchanged

Copied byte-for-byte:

- `scripts/passA_prompt.md`, `scripts/passC_prompt.md` — prompt files are read, not
  rewritten
- `scripts/verify_quotes.py`, `scripts/drop_unverified_quotes.py`,
  `scripts/verify_passC_quotes.py` — the deterministic quote gates
- `scripts/harvest.sh` (one comment line differs)

Copied with small, reviewable edits:

- `scripts/run_passA.py` — `SKIP_SLUGS` emptied; an `EVENT_ADDENDUM` appended
- `scripts/run_conceptsB.py` — two strings naming the event
- `scripts/run_passC.py` — unchanged
- `scripts/build_wiki.py` — event labels, README template, stats
- `scripts/build_speaker_index.py` — optional profile/schedule inputs
- `LICENSE` / `wiki/LICENSE` — same MIT-for-code, CC-BY-for-derived-content split
- `.gitignore` — same publishing posture, same comment block

`git diff` against the aiewf originals is the intended review path for all of these.

## What differed, and why

**Title parser.** The AI Engineer channel titles talks `Talk Title — Speaker, Org`, speaker
last, dash-separated. YC titles them `Speaker Name: Talk Title`, speaker **first**,
colon-separated, with two variants: a role/org prefix (`Waymo Co-CEO Dmitri Dolgov: ...`)
and a quoted talk title (`Sam Altman: "Never a Better Time to Do a Startup"`, and the same
in curly quotes). `scripts/normalize.py` splits on the *first* colon, strips wrapping
quotes, and pulls an org out of a role prefix.

With only 14 titles, every parse was hand-verified rather than trusted. All 14 came out
correct on the first pass — including the Dolgov prefix, which yielded speaker
`Dmitri Dolgov` and org `Waymo`. `raw/title_overrides.json` exists as the correction layer
and records that review; it is intentionally empty of overrides.

Org is taken from the title only where the title states one. Everywhere else it is left
empty and filled later from Pass A's `speaker_org`, extracted from what the speaker
actually said — which is how Boris Cherny got `Anthropic` and Michael Kratsios got
`White House Office of Science and Technology Policy` without anyone guessing.

**No schedule join, no track playlists.** AIEWF needed `join_schedule.py` and
`playlist_tracks.py` to recover track/day/room from a 561-session program, plus the trap
that regenerating `index.json` wipes that enrichment. Startup School is single-track with
one official playlist, so `track` is always `""` and `playlists` is always that one
playlist. `index.json` is fully derivable from `raw/` in one step, and the AIEWF re-run
trap does not exist here.

**No livestream compilations.** AIEWF carried a measured `DUP_WORDS` / `DUP_HOURS`
constant to avoid double-counting full-day livestreams against individually-published
talks. Every video here is a single session, so words and hours in the wiki README are
plain sums over `index.json` with no offset.

**The Pass A prompt names the wrong event.** `passA_prompt.md` opens by saying it is
building a wiki of AI Engineer World's Fair talks. Prompt files are not edited in this
project, so the correction is *appended* by `run_passA.py` as an `EVENT_ADDENDUM` — the
same pattern `run_passC.py` already uses for its post-pilot disagreement addendum. The
addendum does three things: names the real event, tells the extractor that most of these
are firesides where a YC host interviews a guest (extract the guest's positions, not the
interviewer's questions), and licenses company-building concepts so a founder talk is not
forced into AI-engineering vocabulary it never used.

**Caption glue fix carried over.** `normalize.py` keeps `if txt:` rather than
`if txt.strip():`. That one character is what stops YouTube's line-break segments from
being discarded and welding words together; it cost the AIEWF build a day. A regex sweep
for camelCase-style welds across all 14 transcripts found 0.

## Concept vocabulary: shared naming across events

Decided 2026-08-19: **concept vocabularies are shared across events by name; syntheses stay
per-event.** A concept page titled `agent harness design` means the same thing in this wiki
as in the AIEWF wiki, so the two corpora are joinable on concept name — but what *this*
event concluded about it is synthesized only from this event's talks.

Phase 1 (`scripts/build_concepts_phase1.py`) is one `claude -p` call carrying both this
event's 153 raw concept strings with talk counts and the **entire 134-concept AIEWF
canonical vocabulary as reuse candidates**, with the instruction: where a cluster of raw
strings matches an existing concept's idea, copy that concept's name, definition and tier
*exactly*; mint new ones only for ideas AIEWF does not cover.

Result: **36 concepts — 11 reused, 25 new.** The script then verifies the reuse claim
deterministically rather than trusting the model's `reused` flag: it re-reads AIEWF's
canonical.json and checks that every concept marked reused matches AIEWF's name *and*
definition character for character, and that no concept marked new silently shadows an
AIEWF name. Both checks came back clean.

The split is about what you would expect. The reused eleven are the technical ones
(`agent harness design`, `context engineering`, `agentic coding workflows`,
`long-horizon agent tasks`, `prompt injection defense`, `agent memory`, …). The new
twenty-five are almost entirely company-building, which AIEWF's engineering vocabulary
does not reach: `founder psychology`, `contrarian conviction`, `founder hiring bar`,
`iteration speed`, `capital strategy and runway`, `deep tech company building`,
`regulatory navigation for startups`, `ai policy and regulation`,
`product and visual design craft`, `physical ai`, and so on.

Phase 2 reused the AIEWF `run_conceptsB.py` machinery: phase 1's aliases already covered
152 of 153 raw strings, leaving 4 for a single assignment batch. Gate results: **0
unassigned, 0 invented concepts.** Two strings were dropped by the vocabulary's own
drop guidance. All 36 canonical concepts ended up with at least one talk — no dead pages.

## Synthesis threshold

Pass C ran with `--min-talks 3`. With 14 talks, a "state of practice" synthesized from one
or two of them describes the sample, not the field, so 18 concepts were synthesized and 18
were not. The thinner 18 still get wiki pages — definition, aliases, talk links, speakers —
with an explicit note saying why there is no synthesis rather than an empty section.
`build_wiki.py` handles the missing Pass C file as a normal case, verified by building the
wiki once before Pass C had finished.

## Results

Every gate, first attempt, no retries:

| Gate | Result |
|---|---|
| Pass A | 14/14 talks, 0 failures |
| Quote verification vs. raw captions | **328/328 verbatim (100%)**, 0 dropped |
| Phase 2 concept assignment | 0 unassigned, 0 invented |
| Reuse claims matching AIEWF exactly | 11/11 |
| Pass C | 18/18 concepts, 0 failures |
| Pass C evidence quotes vs. Pass A | **63/63 verbatim (100%)** |
| Wiki page counts vs. source data | 14 talks / 36 concepts / 14 speakers, exact |
| Wiki link integrity | 1,239 relative links, **0 broken** |
| Rendered quotes vs. Pass A quotes | 328 = 328 |

The 100% Pass A verbatim rate is worth a note, because on the AIEWF build a rate in the
80s was the signal that found the caption-glue corruption. 100% here is evidence the
transcripts are clean, not just that the model behaved.

Concept maturity across the 18 synthesized concepts: **0 settled, 13 consolidating, 4
contested, 1 frontier**. The synthesis prompt is deliberately instructed to hunt for
disagreement, so the empty settled bucket is a property of the rubric as much as of the
event. Same caveat as AIEWF: do not quote it as a finding about the field.

## Model spend

All calls headless `claude -p --model claude-opus-5`, subscription auth only, with
`ANTHROPIC_API_KEY` stripped from every child environment. No metered API key at any point.

| Stage | Calls | Tokens in | Tokens out | Cost | Wall |
|---|---|---|---|---|---|
| Pass A (14 talks, concurrency 2) | 14 | 429,844 | 141,872 | $6.69 | 27.1 min |
| Vocabulary phase 1 | 1 | 25,056 | 28,035 | $0.85 | 5.2 min |
| Vocabulary phase 2 | 1 | — | — | $0.11 | 5 s |
| Pass C (18 concepts, concurrency 2) | 18 | 499,069 | 126,576 | $6.42 | 28.2 min |
| **Total** | **34** | **~954k** | **~296k** | **$14.07** | |

## Known limitations

1. **Coverage, and it is the big one.** 14 talks is what YC had published on 2026-08-19,
   not the event. Uploads were still arriving the day before the build. Any claim this
   wiki makes about "Startup School 2026" is really a claim about those 14 sessions.
2. **No refresh job.** Deliberately out of scope for this build. When one is written it
   should re-fetch the playlist, harvest only new ids, re-run Pass A on them, re-run the
   full quote gate, re-run phase 2 assignment against the *existing* vocabulary before
   considering minting new concepts, and regenerate Pass C only for concepts whose talk
   set changed — the AIEWF refresh path is the model.
3. **Small sample per concept.** The largest concept has 6 talks. Consensus and
   disagreement here rest on a handful of speakers, not a survey.
4. **Every talk has exactly one credited speaker**, taken from the video title. The YC
   hosts who conduct the firesides (Garry Tan, Diana Hu, Harj Taggar, Luther Lowe) are not
   credited as speakers except where they gave their own talk. The co-presentation
   attribution machinery is present and correct but has nothing to do in this build.
5. **Speaker metadata is thin.** YC publishes no speaker roster or schedule feed for this
   event, so there are no bios, roles, photos, or LinkedIn links — only name, company, and
   talks. Company comes from the title parser or Pass A, and is only set when a speaker's
   talks agree on exactly one org.
6. **The event dates are not in the video descriptions.** The descriptions establish the
   event name ("Startup School 2026") and the venue ("At Startup School 2026 at Chase
   Center"). July 25–26, 2026 comes from Y Combinator's own event announcements, and is
   consistent with the earliest upload (2026-07-26) and with talks referring to the event
   in the present tense.
