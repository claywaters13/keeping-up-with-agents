# Y Combinator Startup School 2026

A linked markdown wiki distilled from the talks and firesides at Y Combinator's
**Startup School 2026** — Chase Center, San Francisco, July 25–26, 2026.

Fourteen sessions, 111,887 words, 10.6 hours of stage time, turned into talk pages,
concept pages, and speaker pages where every quote and every synthesized claim deep-links
back to Y Combinator's own video at the exact second it was said.

**Start here: [`wiki/README.md`](wiki/README.md).**

## Scope, and the snapshot caveat

This is a **snapshot of a corpus that is still growing.** Membership comes from YC's
official [Startup School 2026 playlist](https://www.youtube.com/playlist?list=PLEb7ftOB0yf0),
which held 14 videos when this was built on **2026-08-19**. Those 14 were uploaded between
2026-07-26 and 2026-08-18 — YC published one the day before the build and has not
obviously finished. More sessions from the same event will almost certainly appear on that
playlist later and are not in here. **No recurring refresh has been built yet.**

Read every number below as describing the 14 published talks, not the event's full
program.

**Exclusions: none.** All 14 playlist members were vetted one at a time against their own
video metadata — description, chapters, duration, upload date — and all 14 are talks or
on-stage firesides recorded at this event, each with English auto-captions. Nothing was
dropped as repackaged podcast content, channel evergreen, or caption-less. The per-video
verdicts and their evidence are in `raw/vetting_20260819.md` (local; `raw/` is not
published).

## Stats

| | |
|---|---|
| Talks | 14 (14 included, 0 excluded) |
| Words | 111,887 |
| Hours | 10.6 |
| Speakers | 14 |
| Concepts | 36 — 11 reused from the AIEWF 2026 vocabulary, 25 new |
| Concepts with cross-talk synthesis | 18 (those tagged by 3+ talks) |
| Verified quotes | 328, 100% verbatim, 0 dropped |

Concept maturity across the 18 synthesized concepts: 0 settled, 13 consolidating,
4 contested, 1 frontier.

## Speakers

Jensen Huang (NVIDIA) · Sam Altman (OpenAI) · Boris Cherny (Anthropic) ·
Jeff Dean (Google) · Alexandr Wang (Meta) · Patrick Collison (Stripe) ·
Garry Tan (Y Combinator) · Dmitri Dolgov (Waymo) · Chelsea Finn (Physical Intelligence) ·
Max Hodak (Science) · Peter Steinberger (OpenClaw) · Susan Kare ·
Blake Scholl (Boom Supersonic) · Michael Kratsios (White House OSTP)

## Publishing posture

This directory ships the **derived layer only**: summaries, extracted quotes with
timestamps, concepts, positions, speakers, and links back to YouTube. It contains no full
verbatim transcripts. Raw captions (`raw/`) and rendered transcripts
(`data/transcripts/`) stay local as build substrate and are gitignored. Every quote and
consensus claim deep-links to `youtube.com/watch?v=<id>&t=<sec>s` on Y Combinator's own
channel, so reading this wiki sends people to the original talks rather than replacing
them.

Quote verification is a deterministic hard gate, not a review step: every quote is
string-matched against the raw caption files before it can be published, and failures are
dropped rather than repaired. This build dropped none — 328 of 328 were verbatim on the
first pass.

## Layout

```
README.md      this file
BUILD.md       how it was built, what was reused from AIEWF 2026, what differed
LICENSE        MIT — covers scripts/
wiki/          the published wiki (talks, concepts, speakers) + CC BY 4.0 LICENSE
data/          derived JSON: index, Pass A extractions, Pass C syntheses, concepts, speakers
scripts/       the pipeline (harvest, normalize, three model passes, verifiers, builders)
raw/           local only: YouTube captions, video metadata, playlist manifest, vetting record
```

## Links

- [Wiki entry point](wiki/README.md)
- [Build notes](BUILD.md)
- [Startup School 2026 playlist on YouTube](https://www.youtube.com/playlist?list=PLEb7ftOB0yf0)
- [Sibling corpus: AI Engineer World's Fair 2026](../aiewf-2026/README.md)
