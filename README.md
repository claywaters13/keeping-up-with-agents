# AI Engineer World's Fair 2026 — Wiki + Claude Code Plugin

A linked, graph-style wiki distilled from every session at the AI Engineer World's Fair
2026 (Moscone West, San Francisco, June 29 – July 2, 2026): 231 talks, 134 concepts,
248 speakers — plus a Claude Code plugin so an agent can answer questions from it directly.
No RAG server, no vector DB: the markdown link graph plus `grep` **is** the retrieval
structure. See [`wiki/README.md`](wiki/README.md) for the full corpus writeup (counts,
layout, quote-verification methodology, publishing posture).

**Headline finding:** of 134 concepts synthesized across all 231 talks, **zero** are
settled practice — 87 consolidating, 43 contested, 4 frontier.

## Claude Code plugin

Point an agent at this repo and ask it things like *"what do practitioners disagree about
on agent memory?"*, *"what does the conference say about reward hacking?"*, *"show me
quotes from Lance Martin"*, or *"which concepts are contested?"* — it answers from the
wiki, citing talks with their YouTube deep links.

> Note: this repo is currently private. `marketplace add` from GitHub works once Clay
> makes it public (or for anyone with repo access); the local-clone path works today.

### Install from GitHub (once public)

```
claude plugin marketplace add claywaters13/aiewf-2026-wiki
claude plugin install aiewf-wiki@aiewf-2026-wiki
```

Or from inside an interactive session: `/plugin marketplace add claywaters13/aiewf-2026-wiki`
then `/plugin install aiewf-wiki@aiewf-2026-wiki`.

### Install from a local clone

```
git clone https://github.com/claywaters13/aiewf-2026-wiki.git
cd aiewf-2026-wiki
claude plugin marketplace add .
claude plugin install aiewf-wiki@aiewf-2026-wiki
```

### Try it

```
claude
> /aiewf-wiki:aiewf what do practitioners disagree about on agent memory?
```

or headless:

```
claude -p "which concepts in the AIEWF 2026 wiki are labeled contested?"
```

The plugin ships one skill (`skills/aiewf-wiki`) that teaches the agent the corpus map,
retrieval strategy, citation style, and the maturity rubric (settled / consolidating /
contested / frontier), plus a `/aiewf-wiki:aiewf <question>` convenience command (plugin commands are namespaced).

## Two other ways to use this repo

- **Obsidian vault** — clone, open `wiki/` as a vault; the relative links build the
  graph view for free.
- **Quartz static site** — point a [Quartz](https://quartz.jzhao.xyz/) build at `wiki/`
  for a searchable site with backlinks, deployable to GitHub Pages.

## Layout

```
wiki/                    the published derived-layer wiki (see wiki/README.md)
data/                     machine-readable layer: index.json, passA/passC extractions,
                          speakers, concepts — source data the wiki is generated from
scripts/                  build pipeline (harvest, normalize, Pass A/B/C, wiki generator)
skills/aiewf-wiki/        Claude Code skill (corpus map, retrieval strategy, answer style)
commands/aiewf.md         /aiewf-wiki:aiewf slash command
.claude-plugin/           plugin.json + marketplace.json
```
