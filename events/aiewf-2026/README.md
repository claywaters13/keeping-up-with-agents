# AI Engineer World's Fair 2026 Wiki

*Part of [Keeping up with Agents](../../README.md) — this is the Season 1 event
section. The Claude Code plugin that answers questions from this (and any future) event
corpus is event-agnostic and lives at the
[repo root](../../README.md#claude-code-plugin) (`skills/event-wiki/`,
`commands/ask.md`, `evals/`, `.claude-plugin/`).*

A linked, graph-style wiki built from 256 talks at the AI Engineer World's Fair 2026
(Moscone West, San Francisco, June 29 to July 2, 2026): 134 concepts, 276 speakers, and a
Claude Code plugin so an agent can answer questions from it directly.

There is no vector database here. The link graph is the index.

**Scope, stated up front:** the fair's official schedule listed 561 sessions across talks,
keynotes, workshops, and sponsor slots. This corpus covers the 256 that had been published
to the conference's YouTube channel when it was built. It is a large sample of the fair,
not a complete record of it. A refresh on 2026-08-19 re-fetched the conference playlists
and added 15 newly published talks, including the whole new Generative Media track. See
[`wiki/README.md`](wiki/README.md) for the full corpus writeup.

**Headline finding:** of the 134 concepts synthesized across those 256 talks, zero are
settled practice. 79 are consolidating, 51 contested, 4 frontier. That number needs a
caveat, which is [below](#on-the-headline-finding) rather than buried.

**Publishing posture:** this repo ships the derived layer only, meaning summaries,
excerpted quotes with timestamps, concepts, and speaker pages. It contains no full
transcripts. Every quote deep-links to the conference's own video at the exact second, so
the wiki points at the talks instead of replacing them. See
[License and sources](#license-and-sources).

## Claude Code plugin

Point an agent at the [`keeping-up-with-agents`](https://github.com/claywaters13/keeping-up-with-agents)
repo and ask it things like *"what do practitioners disagree about on agent memory?"*,
*"what does the conference say about reward hacking?"*, *"show me quotes from Lance
Martin"*, or *"which concepts are contested?"* It answers from this wiki and cites talks
with their YouTube deep links. The plugin is event-agnostic — it's not specific to this
event, it just happens to be the first one indexed.

### Install from GitHub

```
claude plugin marketplace add claywaters13/keeping-up-with-agents
claude plugin install keeping-up-with-agents@keeping-up-with-agents
```

Or from inside an interactive session:
`/plugin marketplace add claywaters13/keeping-up-with-agents` then
`/plugin install keeping-up-with-agents@keeping-up-with-agents`.

### Install from a local clone

```
git clone https://github.com/claywaters13/keeping-up-with-agents.git
cd keeping-up-with-agents
claude plugin marketplace add .
claude plugin install keeping-up-with-agents@keeping-up-with-agents
```

### Try it

```
claude
> /keeping-up-with-agents:ask what do practitioners disagree about on agent memory?
```

or headless:

```
claude -p "which concepts in the AIEWF 2026 wiki are labeled contested?"
```

The plugin ships one skill (`skills/event-wiki` at the repo root) that teaches the agent
the corpus map, retrieval strategy, citation style, and the maturity rubric (settled,
consolidating, contested, frontier), plus a `/keeping-up-with-agents:ask <question>`
convenience command. It discovers this event (and any others) by listing `events/*` at
runtime rather than hardcoding AIEWF 2026.

## Two other ways to use this wiki

- **Obsidian vault.** Clone, open `events/aiewf-2026/wiki/` as a vault. The relative
  links build the graph view for free.
- **Quartz static site.** Point a [Quartz](https://quartz.jzhao.xyz/) build at
  `events/aiewf-2026/wiki/` for a searchable site with backlinks, deployable to GitHub
  Pages.

## Podcast

This corpus powers season 1 of **Keeping up with Agents** ("AI moves fast. Keep up.") —
an AI-narrated podcast navigating the field's live arguments. Feed and episodes:
[repo root](../../README.md).

## Layout

```
wiki/               the published derived-layer wiki (see wiki/README.md)
data/               machine-readable layer: index.json, passA/passC extractions,
                    speakers, concepts. The source data the wiki is generated from
scripts/            build pipeline (harvest, normalize, Pass A/B/C, wiki generator)
viz/                concept graph explorer + static visualizations
```

The plugin itself — `skills/event-wiki/`, `commands/ask.md`, `evals/`,
`.claude-plugin/` — lives at the [repo root](../../), since one event-agnostic plugin
now serves the whole `keeping-up-with-agents` repo (and any events added after this
one).

## How this was built

[`BUILD.md`](BUILD.md) is the engineering writeup: the pipeline design, the constraints
that shaped it, the measured cost and throughput, the bug that corrupted 18% of word
boundaries across all 231 transcripts before it was caught, and the verification gotcha
that produced a false 0/19 quote failure. It also states plainly which parts were
model-generated and which were human decisions.

## Evals

The plugin ships a 10-case eval suite in [`evals/`](../../evals/) at the repo root,
covering metadata lookup, topic synthesis, quote fidelity, ambiguous-topic routing,
prompt injection, and two refusal cases (a speaker who is not in the corpus, and a
question about AIEWF 2025, which this corpus does not cover). Graders are a mix of
deterministic regex checks and LLM-judged rubrics.

```
python3 ../../evals/run.py            # run all cases, from this directory
python3 ../../evals/run.py --case refusal-nonexistent-speaker
```

Latest committed run: [`evals/RESULTS.md`](../../evals/RESULTS.md).

## On the headline finding

"Zero settled" is a real output of the pipeline, not a rhetorical flourish. It deserves two
caveats, and they matter more than the number does.

First, the label is applied per concept by a model during cross-talk synthesis (Pass C),
against a fixed four-level rubric. Settled means the debate is over. Consolidating means
converging, with edges still argued. Contested means credible people actively disagree on
fundamentals. Frontier means too new for consensus. Each label carries a written
`maturity_rationale` in the underlying `data/passC/<concept>.json`.

Second, and this is the part worth knowing before you quote the number: the Pass C prompt
explicitly instructs the model to look hard for disagreement, and warns it that finding
unanimous agreement across 20 or more talks usually means it did not read closely enough.
That instruction exists because vague both-sides synthesis is useless, but it almost
certainly biases the distribution away from settled. So the honest reading of "zero
settled" is narrower than it first sounds: on no topic did this corpus produce agreement
strong enough to survive a reviewer actively hunting for dissent. That is a real result.
It is not the same claim as "the field agrees on nothing." Treat the consolidating and
contested split as the useful signal, and the empty settled bucket as a property of a
deliberately adversarial rubric.

## License and sources

- **Code in this section** (`scripts/`): [MIT](LICENSE). The plugin code that moved to
  the repo root (`skills/`, `commands/`, `evals/`) carries the same MIT terms.
- **Derived wiki** (`wiki/`, `data/`): [CC BY 4.0](wiki/LICENSE).

The underlying talks are the work of their speakers and of the AI Engineer World's Fair.
Copyright in them is unchanged and is not claimed here. This repo contains excerpted
quotes and derived summaries, not transcripts, and every quote links back to the
conference's own YouTube channel at its source timestamp. If you are a speaker or an
organizer and want something changed or removed, open an issue and I will handle it.
