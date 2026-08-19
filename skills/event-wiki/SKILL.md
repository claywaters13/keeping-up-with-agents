---
name: event-wiki
description: Answer questions about AI conference/event talks, sessions, speakers, companies, and concepts from this repo's event-indexed wikis — "what did practitioners say/disagree about on X", "what does <event> say about Y", "show me quotes from <speaker>", "which concepts are contested/settled/frontier", "who talked about Z", "what's the state of practice on...". Currently indexed events: AI Engineer World's Fair 2026 (AIEWF 2026, 246 talks). Use whenever a question is about content from an indexed event. Do not use for general AI/ML knowledge with no event tie, or for an event/year not in the indexed list (say so rather than answering from general knowledge) — list events/ at runtime to check what's actually indexed rather than trusting this description as the corpus ages.
---

# Event Wiki

Event-agnostic: this skill answers from every event corpus indexed under `events/` in
this repo, not one hardcoded conference. New events get added as new `events/<slug>/`
directories over time — **discover what's indexed by listing `events/` at runtime**
(`Glob ${CLAUDE_PLUGIN_ROOT}/events/*/` or `Glob ${CLAUDE_PLUGIN_ROOT}/events/*/wiki/README.md`)
rather than assuming only the event named in this file exists.

Currently indexed: **AI Engineer World's Fair 2026** (`events/aiewf-2026/`) — 246
published talks (June 29 - July 2, 2026, Moscone West, SF).

Derived layer only — summaries, extracted quotes, concepts, positions — **no full
transcripts** ship in any event's corpus. If a question needs verbatim transcript text
beyond what's quoted on a page, or asks about an event/year that isn't one of the
indexed `events/*` directories, say the corpus doesn't cover it. Never answer
event-specific questions from general model knowledge.

## Corpus map (`${CLAUDE_PLUGIN_ROOT}/events/<event-slug>/`)

Every indexed event follows the same layout under its own `events/<event-slug>/`
directory. All paths below are relative to that per-event directory inside the plugin
root and usually resolve directly (your working directory is normally inside or near
the repo). **If a Glob/Read/Grep at a bare relative path (e.g.
`events/aiewf-2026/wiki/talks/`) comes back empty**, don't conclude the corpus is
missing — resolve the actual value of the `CLAUDE_PLUGIN_ROOT` environment variable
from your context and retry with `${CLAUDE_PLUGIN_ROOT}/events/<event-slug>/wiki/talks/`
etc. (substitute the real path string; tools don't shell-expand `$VARS` themselves).
Only report "corpus not available" after that retry also comes up empty, and after
confirming via `Glob events/*/` that the event genuinely isn't indexed.

Per event (substitute the event's own slug, e.g. `aiewf-2026`):

- `events/<event-slug>/wiki/talks/<slug>.md` — one per talk: summary, key points,
  notable quotes (timestamped source-video links), concepts, speakers,
  track/org/day/room/duration. (246 for aiewf-2026.)
- `events/<event-slug>/wiki/concepts/<slug>.md` — one per concept: definition,
  **state of practice**, **consensus** claims (with talk-support counts + quotes),
  **disagreements** (Position A vs B, each with its own supporting talks), **do/avoid
  guidance**, maturity label, full talk + speaker lists. (134 for aiewf-2026.)
- `events/<event-slug>/wiki/speakers/<slug>.md` — one per speaker: role, company, bio,
  talks, concepts, quotes. (264 for aiewf-2026.)
- `events/<event-slug>/data/index.json` — one record per talk with `slug`, `title`,
  `speakers`, `org`, `track`, `day`, `room`, `duration_sec`, `word_count`, `url`,
  `video_id`, `topics`, `playlists` — use for metadata lookups/filters that don't need
  prose.
- `events/<event-slug>/data/passA/<slug>.json` — raw per-talk extraction (source for
  talk pages).
- `events/<event-slug>/data/passC/<concept-slug>.json` — raw per-concept synthesis
  (source for concept pages).
- `events/<event-slug>/data/concepts/concept_talks.json` — concept -> talks mapping.
- Slugs are kebab-case of the title; filenames match slugs exactly.
- `events/<event-slug>/wiki/README.md` has that event's corpus overview and full
  maturity-count table — read it first for any "how many / what's in this corpus"
  question about that event.

## Retrieval strategy

1. **Figure out which event(s) the question is about.** If the user names an event, map
   it to its `events/<slug>/`. If they don't name one and only one event is indexed,
   use that one. If several events are indexed and the question is ambiguous, either
   ask or (for broad questions like "what do the indexed events say about X") search
   across all of them and attribute each claim to its event.
2. **Topic question** ("what does <event> say about X", "disagreements on X"): start at
   `events/<event-slug>/wiki/concepts/<slug>.md` (guess the slug from the topic; if
   unsure, `Grep -il "<topic>" events/<event-slug>/wiki/concepts/*.md` or check
   filenames). Its Consensus and Disagreements sections already synthesize across talks
   — use them before opening individual talk pages. WARNING: concept pages contain
   relative `.md` links (e.g. "Supporting talks" lists); NEVER copy those links into
   your answer — they are unclickable outside the repo. Cite the talk by plain title,
   or open its page and use its YouTube URL. Follow the relative links to
   talks/speakers only for more quotes or context.
3. **Keyword / quote search**: `Grep` across `events/<event-slug>/wiki/` (or all
   `events/*/wiki/` for a cross-event search) for the term or speaker name. Concept and
   talk pages are markdown, so a plain-text grep finds any quote or claim.
4. **Speaker question**: open `events/<event-slug>/wiki/speakers/<slug>.md` directly
   (slug = kebab-case name) or grep `events/<event-slug>/wiki/speakers/` for a partial
   name match. If the event isn't known, grep `events/*/wiki/speakers/` for the name.
5. **Metadata question** (duration, track, org, day/room, how many talks on X): read
   `events/<event-slug>/data/index.json` rather than parsing prose.
6. **"Which concepts are X maturity"**:
   `Grep -l 'maturity: "contested"' events/<event-slug>/wiki/concepts/*.md` (or
   settled/consolidating/frontier) — each concept page's YAML frontmatter carries it.

## Maturity rubric

- **Settled** — broad agreement, established practice.
- **Consolidating** — converging practice, some open edges.
- **Contested** — active, unresolved disagreement across talks.
- **Frontier** — too new or sparse for consensus yet.

State the maturity label when a question is about how settled a topic is.

## Answer style

FINAL CHECK before sending any answer: scan your draft for the pattern `](...` ending
in `.md)`. If found, replace each with the talk/concept plain title (no link) or its
YouTube URL. An answer containing any `.md` link is defective, full stop.

- Cite talks by **title**, linked with the source-video deep link every quote carries
  (e.g. `youtube.com/watch?v=<id>&t=<sec>s`) — surface the link, don't just name-drop
  the talk. **Only attach a `video_id`/`t=` you actually saw for that specific talk.**
  A concept page's "Supporting talks" list is often a bare relative link
  (`../talks/<slug>.md`) with no timestamp attached — don't copy the `video_id` or `t=`
  from a neighboring quote onto it. To deep-link a supporting talk, open its own
  `events/<event-slug>/wiki/talks/<slug>.md` and read `video_id` from its frontmatter.
- **Never resolve that tension by dropping links entirely.** A synthesis answer that
  names ten talks in italics and links none of them has failed the citation bar. When an
  answer cites many talks at once, get their ids in **one** lookup instead of opening
  ten pages: `events/<event-slug>/data/index.json` carries `slug`, `title`, and
  `video_id` for every talk — grep or read it once and link from that. A talk
  deep-linked from `index.json` with no `&t=` is fine; a bare title with no link is not.
  At minimum, every answer that cites talks must surface at least one working video
  link, and every quote must carry its own.
- **When citing across more than one event**, say plainly which event each claim comes
  from (e.g. "at AIEWF 2026, ..."). Cross-event comparisons are welcome when the user
  asks for them, but never blur which event a quote or claim is attributed to.
- Never emit *any* relative `.md` path in an answer — not `../talks/x.md`, not
  `events/<event-slug>/wiki/concepts/x.md`, not a "full writeup at ..." pointer to the
  concept page you're summarizing, not a closing list of "raw wiki pages" for the
  topics touched. The reader is in a chat, not a file browser, and cannot click any of
  these. Resolve every reference to a video URL or a plain concept/talk/speaker name
  instead.
- `events/<event-slug>/data/transcripts/` and `events/<event-slug>/raw/` are gitignored
  local build substrate — they are **not part of the published wiki** a stranger's
  clone contains. Never point a user there; everything that actually ships is in the
  corpus map above.
- Distinguish **consensus** claims (cite the support count, e.g. "4 talks agree...")
  from a **single-talk** claim (attribute it to that one talk/speaker, don't generalize
  it).
- For disagreements, present both positions and who holds each, using the concept
  page's Position A / Position B framing.
- **Never invent or paraphrase-as-verbatim a quote.** Only quote text that literally
  appears on a wiki page. If you need to paraphrase, say so explicitly.
- If the corpus doesn't cover the question (event/year not indexed under `events/*`,
  needs raw transcript text not on any page), say so plainly instead of guessing. Name
  which events *are* indexed so the user knows what you can actually answer.
