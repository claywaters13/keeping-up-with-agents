# Keeping up with Agents

**AI moves fast. Keep up.**

An AI-narrated podcast navigating the field's live arguments, built from verified wikis
of major AI events' talks: who is on each side of every real disagreement, the variable
that explains the split, and what a technical product manager would do about it. By
[Clay Waters](https://www.linkedin.com/in/claywaters).

This repo is the single home for the show: the podcast feed itself, and the per-event
wiki + Claude Code plugin each season is built from.

## Podcast

**Feed:** https://claywaters13.github.io/keeping-up-with-agents/feed.xml

Listen on Spotify / Apple Podcasts: links coming after directory approval.

Hosts are AI-generated (Google NotebookLM); every episode discloses this. Episodes ship
from [`episodes/`](episodes/) with cover art at [`cover.png`](cover.png).

New episode:

```
python3 scripts/add_episode.py <audio> --slug episode-NNN --title "..." --description "..."
```

then `git push` — `scripts/add_episode.py` regenerates `feed.xml` idempotently.

## Events

Each season draws on a linked, graph-style wiki built from one AI event's talks — no
vector database, the link graph plus grep is the index — and a Claude Code plugin so an
agent (or this show's writers) can query it directly.

### [AI Engineer World's Fair 2026](events/aiewf-2026/) — Season 1

231 talks, 134 concepts, 248 speakers, almost a million words, every quote verified
verbatim against the source video. Headline finding: of 134 concepts synthesized across
those talks, zero came back settled practice. See
[`events/aiewf-2026/README.md`](events/aiewf-2026/README.md) for the full corpus writeup,
scope caveats, and how it was built.

More events get their own `events/<slug>/` section as future seasons are built.

## Claude Code plugin

One marketplace, one **event-agnostic** plugin: `keeping-up-with-agents`. Install once
and every event indexed under `events/` becomes queryable automatically, including ones
added after you install — no per-event plugin, no reinstall when a new season ships. It
answers questions like *"what do practitioners disagree about on agent memory?"* or
*"which concepts are contested at AIEWF 2026?"*, citing talks with their source-video
deep links and naming which event each claim comes from. Currently indexed: AI Engineer
World's Fair 2026 (231 talks).

### Install from GitHub

```
claude plugin marketplace add claywaters13/keeping-up-with-agents
claude plugin install keeping-up-with-agents@keeping-up-with-agents
```

Or from inside an interactive session:
`/plugin marketplace add claywaters13/keeping-up-with-agents` then
`/plugin install keeping-up-with-agents@keeping-up-with-agents`.

### Try it

```
claude
> /keeping-up-with-agents:ask what do practitioners disagree about on agent memory?
```

or headless:

```
claude -p "which concepts in the AIEWF 2026 wiki are labeled contested?"
claude -p "what do the indexed events say about reward hacking?"
```

Plugin internals — `skills/event-wiki/` (event-agnostic corpus map, retrieval strategy,
answer style), `commands/ask.md` (the `/keeping-up-with-agents:ask` command), `evals/`
(10-case eval suite, run against the AIEWF 2026 corpus), `.claude-plugin/` (plugin +
marketplace manifests) — live at this repo's root and discover corpora by listing
`events/*/wiki/` and `events/*/data/` at runtime.

## Layout

```
feed.xml, cover.png, episodes/   the podcast (do not restructure — feed URLs are live)
scripts/add_episode.py           publishes a new episode into feed.xml, idempotent
.claude-plugin/                  plugin.json + marketplace.json (repo-wide marketplace)
skills/event-wiki/               event-agnostic Claude Code skill
commands/ask.md                  /keeping-up-with-agents:ask slash command
evals/                           10-case eval suite (exercises the AIEWF 2026 corpus)
events/aiewf-2026/               Season 1: the full AIEWF 2026 wiki project
  wiki/                            published derived-layer wiki
  data/                            machine-readable layer the wiki is generated from
  scripts/                         corpus build pipeline (harvest, Pass A/B/C, wiki gen)
  viz/                             concept graph explorer + static visualizations
```

## History note

This repo consolidates what used to be two public repos: the podcast (previously its own
repo) and [`aiewf-2026-wiki`](https://github.com/claywaters13/aiewf-2026-wiki) (now
archived, its full history preserved here under `events/aiewf-2026/`).
