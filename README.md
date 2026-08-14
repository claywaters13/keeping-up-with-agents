# AI Engineer World's Fair 2026 — Wiki + Claude Code Plugin

A linked, graph-style wiki distilled from every session at the AI Engineer World's Fair
2026 (Moscone West, San Francisco, June 29 – July 2, 2026): 231 talks, 134 concepts,
248 speakers — plus a Claude Code plugin so an agent can answer questions from it directly.
No RAG server, no vector DB: the markdown link graph plus `grep` **is** the retrieval
structure. See [`wiki/README.md`](wiki/README.md) for the full corpus writeup (counts,
layout, quote-verification methodology, publishing posture).

**Headline finding:** of 134 concepts synthesized across all 231 talks, **zero** are
settled practice — 87 consolidating, 43 contested, 4 frontier. ([How that label was
assigned, and how much weight it holds](#on-the-headline-finding).)

**Publishing posture:** this repo ships the derived layer only — summaries, excerpted
quotes with timestamps, concepts, and speaker pages. It contains **no full transcripts**.
Every quote deep-links to the conference's own YouTube video at the exact second, so the
wiki points at the talks rather than replacing them. See [License and sources](#license-and-sources).

## Claude Code plugin

Point an agent at this repo and ask it things like *"what do practitioners disagree about
on agent memory?"*, *"what does the conference say about reward hacking?"*, *"show me
quotes from Lance Martin"*, or *"which concepts are contested?"* — it answers from the
wiki, citing talks with their YouTube deep links.

### Install from GitHub

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
wiki/               the published derived-layer wiki (see wiki/README.md)
data/               machine-readable layer: index.json, passA/passC extractions,
                    speakers, concepts — the source data the wiki is generated from
scripts/            build pipeline (harvest, normalize, Pass A/B/C, wiki generator)
evals/              10-case eval suite for the plugin, with a runner (see below)
skills/aiewf-wiki/  Claude Code skill (corpus map, retrieval strategy, answer style)
commands/aiewf.md   /aiewf-wiki:aiewf slash command
.claude-plugin/     plugin.json + marketplace.json
```

## How this was built

[`BUILD.md`](BUILD.md) is the engineering writeup: the pipeline design, the constraints
that shaped it, the measured cost and throughput, the bug that corrupted 18% of word
boundaries across all 231 transcripts before it was caught, and the verification gotcha
that produced a false 0/19 quote failure. It also states plainly which parts were
model-generated and which were human decisions.

## Evals

The plugin ships a 10-case eval suite in [`evals/`](evals/) covering metadata lookup,
topic synthesis, quote fidelity, ambiguous-topic routing, prompt injection, and two
refusal cases (a speaker who isn't in the corpus, and a question about AIEWF 2025, which
this corpus does not cover). Graders are a mix of deterministic regex checks and
LLM-judged rubrics.

```
python3 evals/run.py            # run all cases
python3 evals/run.py --case refusal-nonexistent-speaker
```

Latest committed run: [`evals/RESULTS.md`](evals/RESULTS.md).

## On the headline finding

"Zero settled" is a real output of the pipeline, not a rhetorical flourish — but it
deserves two caveats, and they matter more than the number does.

First, the label is applied per concept by a model during cross-talk synthesis (Pass C),
against a fixed four-level rubric: `settled` = the debate is over; `consolidating` =
converging, edges still argued; `contested` = credible people actively disagree on
fundamentals; `frontier` = too new for consensus. Each label carries a written
`maturity_rationale` in the underlying `data/passC/<concept>.json`.

Second — and this is the honest part — the Pass C prompt explicitly instructs the model to
look hard for disagreement and warns it that finding unanimous agreement across 20+ talks
usually means it did not read closely enough. That instruction exists because vague
both-sides synthesis is useless, but it does bias the distribution away from `settled`.
The correct reading of "zero settled" is therefore *"on no topic did this corpus produce
agreement strong enough to survive a reviewer actively hunting for dissent"* — which is a
narrower and more defensible claim than "the field agrees on nothing." Treat the
consolidating/contested split as the useful signal and the empty `settled` bucket as a
property of a deliberately adversarial rubric.

## License and sources

- **Code** (`scripts/`, `evals/`, `skills/`, `commands/`) — [MIT](LICENSE).
- **Derived wiki** (`wiki/`, `data/`) — [CC BY 4.0](wiki/LICENSE).

The underlying talks are the work of their speakers and of the AI Engineer World's Fair;
copyright in them is unchanged and is not claimed here. This repo contains excerpted
quotes and derived summaries, not transcripts, and every quote links back to the
conference's own YouTube channel at its source timestamp. If you are a speaker or an
organizer and want something changed or removed, open an issue and it will be handled.
