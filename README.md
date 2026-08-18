# AI Engineer World's Fair 2026 Wiki + Claude Code Plugin

A linked, graph-style wiki built from 231 talks at the AI Engineer World's Fair 2026
(Moscone West, San Francisco, June 29 to July 2, 2026): 134 concepts, 248 speakers, and a
Claude Code plugin so an agent can answer questions from it directly.

There is no vector database here. The link graph is the index.

**Scope, stated up front:** the fair's official schedule listed 561 sessions across talks,
keynotes, workshops, and sponsor slots. This corpus covers the 231 that had been published
to the conference's YouTube channel when it was built. It is a large sample of the fair,
not a complete record of it. See [`wiki/README.md`](wiki/README.md) for the full corpus
writeup.

**Headline finding:** of the 134 concepts synthesized across those 231 talks, zero are
settled practice. 87 are consolidating, 43 contested, 4 frontier. That number needs a
caveat, which is [below](#on-the-headline-finding) rather than buried.

**Publishing posture:** this repo ships the derived layer only, meaning summaries,
excerpted quotes with timestamps, concepts, and speaker pages. It contains no full
transcripts. Every quote deep-links to the conference's own video at the exact second, so
the wiki points at the talks instead of replacing them. See
[License and sources](#license-and-sources).

## Claude Code plugin

Point an agent at this repo and ask it things like *"what do practitioners disagree about
on agent memory?"*, *"what does the conference say about reward hacking?"*, *"show me
quotes from Lance Martin"*, or *"which concepts are contested?"* It answers from the wiki
and cites talks with their YouTube deep links.

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
retrieval strategy, citation style, and the maturity rubric (settled, consolidating,
contested, frontier), plus a `/aiewf-wiki:aiewf <question>` convenience command. Plugin
commands are namespaced.

## Two other ways to use this repo

- **Obsidian vault.** Clone, open `wiki/` as a vault. The relative links build the graph
  view for free.
- **Quartz static site.** Point a [Quartz](https://quartz.jzhao.xyz/) build at `wiki/` for
  a searchable site with backlinks, deployable to GitHub Pages.

## Podcast

**Keeping up with Agents** is an AI-narrated companion podcast built from this wiki. Each
episode takes one fault line from the 231 talks and works it — what practitioners actually
disagree on, and why. Hosts are AI-generated (NotebookLM); every episode's description links
back to the sources here.

- Feed: [`podcast/feed.xml`](podcast/feed.xml) —
  `https://claywaters13.github.io/aiewf-2026-wiki/podcast/feed.xml`
- Listen on Spotify: *(link pending directory approval)*
- Listen on Apple Podcasts: *(link pending directory approval)*
- New episodes: `python3 scripts/add_episode.py <audio> --slug episode-00N --title "..." --description "..."`, then commit and push.

## Layout

```
wiki/               the published derived-layer wiki (see wiki/README.md)
data/               machine-readable layer: index.json, passA/passC extractions,
                    speakers, concepts. The source data the wiki is generated from
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
refusal cases (a speaker who is not in the corpus, and a question about AIEWF 2025, which
this corpus does not cover). Graders are a mix of deterministic regex checks and
LLM-judged rubrics.

```
python3 evals/run.py            # run all cases
python3 evals/run.py --case refusal-nonexistent-speaker
```

Latest committed run: [`evals/RESULTS.md`](evals/RESULTS.md).

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

- **Code** (`scripts/`, `evals/`, `skills/`, `commands/`): [MIT](LICENSE).
- **Derived wiki** (`wiki/`, `data/`): [CC BY 4.0](wiki/LICENSE).

The underlying talks are the work of their speakers and of the AI Engineer World's Fair.
Copyright in them is unchanged and is not claimed here. This repo contains excerpted
quotes and derived summaries, not transcripts, and every quote links back to the
conference's own YouTube channel at its source timestamp. If you are a speaker or an
organizer and want something changed or removed, open an issue and I will handle it.
