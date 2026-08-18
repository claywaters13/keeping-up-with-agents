# AI Engineer World's Fair 2026 Wiki

A linked, graph-style wiki built from 231 talks at the AI Engineer World's Fair
2026 (Moscone West, San Francisco, June 29 to July 2, 2026), transcribed from the
conference's own YouTube channel and distilled into summaries, extracted quotes, concepts,
and cross-talk syntheses. Every claim links back to the source video at the exact
timestamp.

## Scope

The fair's official schedule listed 561 sessions across talks, keynotes, workshops, and
sponsor slots. This corpus covers the 231 that had been published to the
conference's YouTube channel when it was built, and more were still premiering at the
time. It is a large sample of the fair, not a complete record of it. Every count below
describes that sample.

## What this is

- **231 talks** (229 individual talks plus 2 full-day livestream compilations)
- **933,897 deduplicated words**, **93.9 hours** of source material.
  Raw totals across all 231 entries are 1,011,341 words and
  101.7 hours. The difference is roughly 77,444 words of
  livestream-compilation content that duplicates individual talks already covered
  separately, kept as its own entry but not double-counted above.
- **248 speakers**
- **134 concepts**, each with a cross-talk synthesis: state of practice,
  consensus, open disagreements, and do/avoid guidance
- **4,633 verified quotes**, every one checked verbatim against the raw YouTube
  captions before publication (see Quote verification below)

### Concept maturity

| Maturity | Count | Meaning |
|---|---|---|
| Settled | 0 | Broad agreement, established practice |
| Consolidating | 87 | Converging practice, some open edges |
| Contested | 43 | Active, unresolved disagreement across talks |
| Frontier | 4 | Too new or sparse for consensus yet |

The empty settled bucket needs a caveat before it gets quoted. The synthesis prompt that
assigns these labels is deliberately instructed to hunt for disagreement, which almost
certainly biases the distribution. See "On the headline finding" in the repository README.

## Publishing posture

This repo ships the derived layer only: summaries, extracted quotes with timestamps,
concepts, positions, speakers, companies, and links back to YouTube. It does not contain
full verbatim transcripts of any talk. Those stay local as build substrate. Every notable
quote and consensus claim deep-links to `youtube.com/watch?v=<id>&t=<sec>s` on the
conference's own channel, so reading this wiki drives traffic back to the original talks
rather than replacing them.

**Not included:** `data/livestream_segments/` (incomplete segmentation, low-confidence
speaker attribution, excluded from this wiki entirely rather than just de-duplicated).

**Speaker attribution:** 30 talks have multiple speakers. Where the
extraction cannot tell which co-presenter said which line, quotes and positions are kept
at talk level and are rendered on speaker pages under a clearly labeled "From Talks This
Speaker Co-Presented" heading. They are never attributed to one individual as their own
words.

## Layout

```
wiki/
  README.md            this file
  talks/<slug>.md       231 talk pages: summary, key points, quotes, positions, concepts
  concepts/<slug>.md    134 concept pages: definition, state of practice, consensus,
                        disagreements, do/avoid guidance, full talk list, speakers
  speakers/<slug>.md    248 speaker pages: role, company, bio, talks, sessions,
                        concepts, quotes
```

Every page carries YAML frontmatter (`title`, `type`, plus type-appropriate fields like
`track`, `org`, `maturity`, `company`) so Obsidian and Quartz can filter and query on it.

## Three ways to use this repo

1. **Obsidian vault.** Clone the repo, open `wiki/` as a vault. The relative markdown links
   between talks, concepts, and speakers build Obsidian's graph view for free, with no
   plugin configuration needed.
2. **Quartz static site.** Point a [Quartz](https://quartz.jzhao.xyz/) build at `wiki/` for a
   searchable site with backlinks and a graph view, deployable to GitHub Pages.
3. **Claude Code / agent access.** Point an agent at this repo and let it `Grep`, `Glob`,
   and `Read` the markdown directly. No RAG server, no vector DB, no hosted API. The link
   graph plus the YAML frontmatter is the retrieval structure: grep concept pages for a
   topic, follow links to the talks and speakers that cover it. It works offline, never
   goes down, and costs nothing to run.

## Quote verification

Every quote in this wiki passed a deterministic verification pass against the raw YouTube
caption files (`raw/caps/<video_id>.en.json3`) before publication, using normalized
word-sequence matching rather than a model judgment call. Quotes that failed verbatim
verification were dropped, not edited (see `data/passA/_dropped_quotes.json` for the list).
4,633 quotes passed and are rendered across the 231 talk pages:
3,913 individually speaker-attributed, and 720
talk-level from multi-speaker sessions.

## Source data

Generated deterministically (no model calls) by `scripts/build_wiki.py` from:

- `data/index.json`, the corpus index (231 entries)
- `data/passA/<slug>.json`, per-talk extraction (summary, quotes, concepts, positions)
- `data/passC/<concept-slug>.json`, per-concept cross-talk synthesis
- `data/concepts/canonical.json` and `data/concepts/concept_talks.json`, concept vocabulary
- `data/speakers/<slug>.json` and `data/speakers/concept_speakers.json`, speaker profiles

Re-run `python3 scripts/build_wiki.py` any time the source JSON changes. The generator wipes
and rebuilds `wiki/talks`, `wiki/concepts`, `wiki/speakers`, and this README from scratch.
