# Y Combinator Startup School 2026 Wiki

A linked, graph-style wiki built from 14 talks and firesides at Y Combinator's
Startup School 2026 (Chase Center, San Francisco, July 25-26, 2026), transcribed from
YC's own YouTube channel and distilled into summaries, extracted quotes, concepts, and
cross-talk syntheses. Every claim links back to the source video at the exact timestamp.

## Scope, and the snapshot caveat

**This is a snapshot of a corpus that is still growing.** Y Combinator was still
publishing Startup School 2026 talks the day before this wiki was built. The 14
videos in this corpus were uploaded between 2026-07-26 and 2026-08-18, and the
corpus was frozen on 2026-08-19. Membership is taken from YC's official
[Startup School 2026 playlist](https://www.youtube.com/playlist?list=PLEb7ftOB0yf0),
which held 14 videos on that date. More talks from the same event will almost
certainly appear on that playlist later and are not here. A recurring refresh has not
been built yet.

So every count on this page describes the 14 published talks, not the event's
full program. Anything said in a session YC has not published, or has not published yet,
is invisible here.

**Exclusions:** none. All 14 playlist members were vetted individually against
their video metadata — description, chapters, duration, upload date — and all 14
are talks or on-stage firesides recorded at this event, with English captions available.
No video was dropped as repackaged podcast content, channel evergreen, or caption-less.

## What this is

- **14 talks**, **111,887 words**, **10.6 hours** of source material
- **14 speakers**
- **36 concepts**, of which **18** carry a cross-talk
  synthesis: state of practice, consensus, open disagreements, and do/avoid guidance
- **328 verified quotes**, every one checked verbatim against the raw YouTube
  captions before publication (see Quote verification below)

Synthesis is gated at **3 or more tagged talks**. With only 14 talks in the
corpus, a "state of practice" distilled from one or two of them would describe the sample,
not the field. The 18 thinner concepts still have pages — definition,
talk list, speakers — they just carry no synthesis.

### Concept maturity

Across the 18 synthesized concepts:

| Maturity | Count | Meaning |
|---|---|---|
| Settled | 0 | Broad agreement, established practice |
| Consolidating | 13 | Converging practice, some open edges |
| Contested | 4 | Active, unresolved disagreement across talks |
| Frontier | 1 | Too new or sparse for consensus yet |

These labels come from a deliberately adversarial synthesis prompt that is told to hunt
for disagreement, which biases the distribution. Read them as a reading order, not a
measurement.

## Shared concept vocabulary

Concept names here are shared with the other event wikis in this repository rather than
minted fresh. Where a concept the AI Engineer World's Fair 2026 corpus already named
covers the same idea, this wiki reuses that concept's name and definition exactly, so the
same concept page title means the same thing across events. New concepts were minted only
for ideas the sibling vocabulary does not cover — which, for a founder-facing event, is
most of the company-building material. Syntheses are always per-event: a concept page here
describes what *this* event concluded.

## Publishing posture

This repo ships the derived layer only: summaries, extracted quotes with timestamps,
concepts, positions, speakers, and links back to YouTube. It does not contain full
verbatim transcripts of any talk. Those stay local as build substrate. Every notable quote
and consensus claim deep-links to `youtube.com/watch?v=<id>&t=<sec>s` on Y Combinator's own
channel, so reading this wiki drives traffic back to the original talks rather than
replacing them.

**Speaker attribution:** 0 talks have multiple credited speakers. Where
the extraction cannot tell which co-presenter said which line, quotes and positions are kept
at talk level and rendered on speaker pages under a clearly labeled "From Talks This Speaker
Co-Presented" heading. They are never attributed to one individual as their own words. Note
that most talks here are firesides with a YC host; the corpus credits the guest, and the
extraction is instructed to capture the guest's positions rather than the interviewer's
questions.

## Layout

```
wiki/
  README.md            this file
  talks/<slug>.md       14 talk pages: summary, key points, quotes, positions, concepts
  concepts/<slug>.md    36 concept pages: definition, state of practice, consensus,
                        disagreements, do/avoid guidance, full talk list, speakers
  speakers/<slug>.md    14 speaker pages: company, talks, concepts, quotes
```

Every page carries YAML frontmatter (`title`, `type`, plus type-appropriate fields like
`org`, `maturity`, `company`) so Obsidian and Quartz can filter and query on it.

## Three ways to use this repo

1. **Obsidian vault.** Clone the repo, open `wiki/` as a vault. The relative markdown links
   between talks, concepts, and speakers build Obsidian's graph view for free, with no
   plugin configuration needed.
2. **Quartz static site.** Point a [Quartz](https://quartz.jzhao.xyz/) build at `wiki/` for a
   searchable site with backlinks and a graph view, deployable to GitHub Pages.
3. **Claude Code / agent access.** Point an agent at this repo and let it `Grep`, `Glob`,
   and `Read` the markdown directly. No RAG server, no vector DB, no hosted API. The link
   graph plus the YAML frontmatter is the retrieval structure.

## Quote verification

Every quote in this wiki passed a deterministic verification pass against the raw YouTube
caption files (`raw/caps/<video_id>.en.json3`) before publication, using normalized
word-sequence matching rather than a model judgment call. Quotes that failed verbatim
verification were dropped, not edited (see `data/passA/_dropped_quotes.json` for the list).
328 quotes passed and are rendered across the 14 talk pages:
328 individually speaker-attributed, and 0
talk-level from multi-speaker sessions.

## Source data

Generated deterministically (no model calls) by `scripts/build_wiki.py` from:

- `data/index.json`, the corpus index (14 entries)
- `data/passA/<slug>.json`, per-talk extraction (summary, quotes, concepts, positions)
- `data/passC/<concept-slug>.json`, per-concept cross-talk synthesis
- `data/concepts/canonical.json` and `data/concepts/concept_talks.json`, concept vocabulary
- `data/speakers/<slug>.json` and `data/speakers/concept_speakers.json`, speaker profiles

Re-run `python3 scripts/build_wiki.py` any time the source JSON changes. The generator wipes
and rebuilds `wiki/talks`, `wiki/concepts`, `wiki/speakers`, and this README from scratch.
See [`../BUILD.md`](../BUILD.md) for how the corpus was built.
