---
description: Answer a question about any indexed AI conference/event's talks, speakers, or concepts using the event wikis in this repo
argument-hint: <question>
---

# Event wiki lookup

Corpus root: `${CLAUDE_PLUGIN_ROOT}/events/` — one subdirectory per indexed event
(currently `aiewf-2026`), each with `wiki/concepts/<slug>.md` (state of practice,
consensus, disagreements, maturity label in frontmatter), `wiki/talks/<slug>.md`,
`wiki/speakers/<slug>.md`, and `data/index.json` (metadata). List `events/` at runtime
to see what's actually indexed rather than assuming. Load the `event-wiki` skill for the
full retrieval strategy; if the skill fails to load, work directly from the corpus paths
above.

Answer this question from that corpus (cite talks with their source-video deep links,
state maturity when relevant, distinguish consensus from single-talk claims, say which
event a claim comes from when more than one is indexed, never invent quotes, never emit
relative .md paths in the answer, and say plainly — naming which events *are* indexed —
if the corpus doesn't cover it):

**$ARGUMENTS**

FINAL CHECK: before answering, remove any `](...*.md)` markdown links from your draft; cite plain titles or YouTube URLs only.
