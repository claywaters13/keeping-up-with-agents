---
description: Answer a question about AI Engineer World's Fair 2026 talks, speakers, or concepts using the wiki corpus in this repo
argument-hint: <question>
---

# AIEWF 2026 wiki lookup

Corpus root: `${CLAUDE_PLUGIN_ROOT}` — key paths: `wiki/concepts/<slug>.md` (134
syntheses: state of practice, consensus, disagreements, maturity label in frontmatter),
`wiki/talks/<slug>.md` (231), `wiki/speakers/<slug>.md` (248), `data/index.json`
(metadata). Load the `aiewf-wiki` skill for the full retrieval strategy; if the skill
fails to load, work directly from the corpus paths above.

Answer this question from that corpus (cite talks with their YouTube deep links, state
maturity when relevant, distinguish consensus from single-talk claims, never invent
quotes, never emit relative .md paths in the answer, and say plainly if the corpus
doesn't cover it):

**$ARGUMENTS**
