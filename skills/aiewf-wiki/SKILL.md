---
name: aiewf-wiki
description: Answer questions about AI Engineer World's Fair 2026 (AIEWF 2026) talks, sessions, speakers, companies, and concepts — "what did practitioners say/disagree about on X", "what does the conference say about Y", "show me quotes from <speaker>", "which concepts are contested/settled/frontier", "who talked about Z", "what's the state of practice on...". Use whenever a question is about AIEWF 2026 content specifically. Do not use for general AI/ML knowledge with no conference tie, for other conferences, or for the 2025 AIEWF (not in this corpus — say so rather than answering from general knowledge).
---

# AIEWF 2026 Wiki

Scope: 231 published talks from AI Engineer World's Fair 2026 (June 29 - July 2, 2026,
Moscone West, SF). Derived layer only — summaries, extracted quotes, concepts, positions —
**no full transcripts** ship in this corpus. If a question needs verbatim transcript text
beyond what's quoted on a page, or asks about a different conference/year, say the corpus
doesn't cover it. Never answer AIEWF-specific questions from general model knowledge.

## Corpus map (`${CLAUDE_PLUGIN_ROOT}`)

- `wiki/talks/<slug>.md` (231) — one per talk: summary, key points, notable quotes
  (timestamped YouTube links), concepts, speakers, track/org/day/room/duration.
- `wiki/concepts/<slug>.md` (134) — one per concept: definition, **state of practice**,
  **consensus** claims (with talk-support counts + quotes), **disagreements** (Position A
  vs B, each with its own supporting talks), **do/avoid guidance**, maturity label,
  full talk + speaker lists.
- `wiki/speakers/<slug>.md` (248) — one per speaker: role, company, bio, talks, concepts,
  quotes.
- `data/index.json` — 231 records with `slug`, `title`, `speakers`, `org`, `track`, `day`,
  `room`, `duration_sec`, `word_count`, `url`, `video_id`, `topics`, `playlists` — use for
  metadata lookups/filters that don't need prose.
- `data/passA/<slug>.json` — raw per-talk extraction (source for talk pages).
- `data/passC/<concept-slug>.json` — raw per-concept synthesis (source for concept pages).
- `data/concepts/concept_talks.json` — concept -> talks mapping.
- Slugs are kebab-case of the title; filenames match slugs exactly.
- `wiki/README.md` has the corpus overview and the full maturity-count table — read it
  first for any "how many / what's in this corpus" question.

## Retrieval strategy

1. **Topic question** ("what does the conference say about X", "disagreements on X"):
   start at `wiki/concepts/<slug>.md` (guess the slug from the topic; if unsure,
   `Grep -il "<topic>" wiki/concepts/*.md` or check filenames). Its Consensus and
   Disagreements sections already synthesize across talks — use them before opening
   individual talk pages. Follow the relative links to talks/speakers only for more
   quotes or context.
2. **Keyword / quote search**: `Grep` across `wiki/` for the term or speaker name.
   Concept and talk pages are markdown, so a plain-text grep finds any quote or claim.
3. **Speaker question**: open `wiki/speakers/<slug>.md` directly (slug = kebab-case
   name) or grep `wiki/speakers/` for a partial name match.
4. **Metadata question** (duration, track, org, day/room, how many talks on X):
   read `data/index.json` rather than parsing prose.
5. **"Which concepts are X maturity"**: `Grep -l 'maturity: "contested"' wiki/concepts/*.md`
   (or settled/consolidating/frontier) — each concept page's YAML frontmatter carries it.

## Maturity rubric

- **Settled** — broad agreement, established practice.
- **Consolidating** — converging practice, some open edges.
- **Contested** — active, unresolved disagreement across talks.
- **Frontier** — too new or sparse for consensus yet.

State the maturity label when a question is about how settled a topic is.

## Answer style

- Cite talks by **title**, linked with the YouTube deep link every quote carries
  (`youtube.com/watch?v=<id>&t=<sec>s`) — surface the link, don't just name-drop the talk.
  **Only attach a `video_id`/`t=` you actually saw for that specific talk.** A concept
  page's "Supporting talks" list is often a bare relative link (`../talks/<slug>.md`)
  with no timestamp attached — don't copy the `video_id` or `t=` from a neighboring
  quote onto it. To deep-link a supporting talk, open its own `wiki/talks/<slug>.md`
  and read `video_id` from its frontmatter.
- Never emit a relative `.md` path (`../talks/x.md`) in an answer — the reader cannot
  click it. Resolve every reference to a YouTube URL or a plain talk title.
- Distinguish **consensus** claims (cite the support count, e.g. "4 talks agree...") from
  a **single-talk** claim (attribute it to that one talk/speaker, don't generalize it).
- For disagreements, present both positions and who holds each, using the concept page's
  Position A / Position B framing.
- **Never invent or paraphrase-as-verbatim a quote.** Only quote text that literally
  appears on a wiki page. If you need to paraphrase, say so explicitly.
- If the corpus doesn't cover the question (wrong year, wrong conference, needs raw
  transcript text not on any page), say so plainly instead of guessing.
