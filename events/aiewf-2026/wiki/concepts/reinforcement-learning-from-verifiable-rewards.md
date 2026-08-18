---
title: "reinforcement learning from verifiable rewards"
type: "concept"
slug: "reinforcement-learning-from-verifiable-rewards"
tier: "core"
maturity: "consolidating"
talk_count: 9
speaker_count: 11
---

# reinforcement learning from verifiable rewards

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **9** talk(s) by **11** speaker(s)

**Definition:** Post-training on tasks whose success can be checked programmatically (tests, compilers, solvers) rather than by a learned preference model.

*Also referred to as: reinforcement learning with verifiable rewards, rlvr, verifiable rewards, reinforcement learning from verifiable environments, reinforcement learning from verified outcomes, verifiable environments*

## State of Practice

The field has stopped treating verifiability as a property of models and started treating it as a property of domains: code was easy to RL on because code decomposes, executes, and checks itself, and the open work is manufacturing that structure elsewhere — data-analysis code as the substrate for biology, observed business outcomes as the substrate for finance, retrieval-ranking plus trajectory rubrics as the substrate for search. Practitioners agree that RLVR as classically construed (math answers, unit tests, database state) is the easy special case and covers a small fraction of real agent work, so most 2026 effort goes into environment and task construction rather than algorithm choice: mining deployed production traces for tasks, working backwards from a known-reachable end state to guarantee solvability, gating generated tasks on pass rate to hold them in the intermediate-difficulty band where advantage signal exists, and decomposing end-to-end outcomes into intermediate checkpoints because sparse terminal reward gives models that are 'pretty bad' nothing to climb. Outcome-only reward is now considered actively unsafe as well as weak — a trajectory can reach 'done' having sent a resignation letter or blocked an account — so dangerous intermediate actions and trajectory quality get their own reward terms. Reward hacking is understood mechanistically as loose proxies that are undefined at the boundaries, and the practical countermeasure that people report working is hindsight review of full trajectories rather than instructing a judge in advance. The live fault lines are whether LLM judges and rubrics are trustworthy enough to carry reward in unverifiable domains, whether to train against controllable learned simulators or against real messy systems, and whether code-centric training is a good prior for non-code work or a source of harmful transfer.

## Consensus

### Models are good at code because code is verifiable, decomposable, and executable — verifiability is a property of the domain, not of the model — so extending RL to a new domain means first engineering a verifiable substrate for it.

Support: **4** talk(s)

> "we treat for example the fact that code is verifiable and measurable as something that is a property about models and models are great at at coding um because we've made them great at coding but realistically it's actually a fact about code."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [1:57](https://www.youtube.com/watch?v=lCBf9slCanI&t=117s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)

### Verifiable rewards cover only the easy special case; most economically relevant tasks are not programmatically checkable, and the industry is over-indexed on code and math because those are the tasks that happen to check themselves.

Support: **5** talk(s)

> "often we don't actually have verifiable rewards. And so messy real world tasks often we're kind of figuring out as we go."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [0:13](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=13s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

### Task and environment design — not the RL algorithm — is the hard part of turning a fuzzy capability into something trainable.

Support: **4** talk(s)

> "So in this case the task design itself is really kind of the hardest part of the problem of how do you turn something that appears very fuzzy into something that actually can be arled."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [5:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=344s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From RL to IRL](../talks/from-rl-to-irl.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

### End-to-end outcome grading is inadequate — too sparse to train on and blind to harmful intermediate actions — so tasks must be decomposed into intermediate checkpoints and trajectory-level rewards.

Support: **4** talk(s)

> "the the grading of these end outcomes in biology uh is too sparse because the models are pretty bad. So, you have to break things up into manageable chunks to get some semblance of verifiability."
>
> — [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [7:50](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=470s)

Supporting talks: [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Ending AI Slop](../talks/ending-ai-slop.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)

### Handcrafted expert task sets do not scale; the realistic training distribution has to be discovered by deploying the system and mining its traces and observed outcomes.

Support: **4** talk(s)

> "what we found is super helpful is taking existing traces from a deployed agent and treating these as the source material"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### RL tasks must be held in a deliberate difficulty band — too easy or too hard produces no learning signal, because advantage depends on separation across rollouts.

Support: **3** talk(s)

> "you want tasks that are not too easy, not too hard and you want to be searching for these and iterating on generating more of them"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [14:08](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=848s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From RL to IRL](../talks/from-rl-to-irl.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)

### Reward hacking is the expected consequence of any proxy reward that is undefined at its boundaries, and RL-trained models will reliably find those boundaries.

Support: **3** talk(s)

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

## Disagreements

### Are LLM judges and rubric scores reliable enough to serve as the reward signal where programmatic verification is unavailable?

| Position A | Position B |
|---|---|
| No — human judgment remains materially better than any LLM judge for subjective quality, and rubric scores that only loosely correlate with verifiable outcomes should not be used for RL or benchmarking; use expert humans (including scientists grading each other) and decompose until the check is programmatic.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* | Yes — LLMs are already strong general reasoners, and judges work well enough in practice provided they judge in hindsight over the full trajectory (or by polling several models) and score concrete rubric items like whether a query is a natural sentence and whether exploration volume was appropriate.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* |

*Why it matters: If judges are trustworthy, the addressable set of RL domains expands immediately and environment construction can be largely automated; if they are not, every new domain needs expensive expert data collection and a hand-built deterministic grader, which is a week of three people's time per task.*

### Should agents be trained against controllable simulated environments or against the real, messy production system?

| Position A | Position B |
|---|---|
| Learned simulators are the better environment: full back-end controllability lets you plant the answer, guarantee the task is solvable, and reverse-engineer supervision for free — including for tools and websites that cannot yet be programmed.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)* | Only reality generates the distribution that matters: you need high-fidelity sandboxes reproducing layout shift, slow loads, pop-ups, stale tabs and random account states, and ultimately you have to ship the product to design partners and let it fail — and in domains like finance the signal is real observed outcomes across many entities, which no simulation supplies.<br>*[From RL to IRL](../talks/from-rl-to-irl.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* |

*Why it matters: It determines whether an RL team's core investment is a simulator/synthetic-task pipeline or a deployed product plus a proprietary outcome dataset — and whether solvability guarantees or failure realism is the property you optimize the environment for.*

### Is code-centric training a good prior for non-code agentic work, or does it induce harmful transfer?

| Position A | Position B |
|---|---|
| Code is the right universal substrate — most real computer tasks are reachable through MCP, APIs, Playwright and JavaScript and can be expressed as coding tasks, code is now the dominating pre-training subset supplying the atomic skills RL composes, and data-analysis code can do for biology what code did for software.<br>*[The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* | Coding ability is not sufficient and its habits actively misfire elsewhere: computer use needs visual grounding and screen semantics baked in, coding-trained agents write keyword-stuffed grep-style queries that defeat semantic search, and the industry's coding bias pushes it toward procedural tasks with one or two valid solutions.<br>*[From RL to IRL](../talks/from-rl-to-irl.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* |

*Why it matters: If code transfers, the cheapest path to a new agentic domain is to encode it as a coding task and reuse the existing RLVR stack; if it does not, each domain needs its own perception, tooling, and reward design, and code-heavy pre-training mixes have to be counterbalanced.*

## Practical Guidance

**Do:**

- Generate tasks in an online loop and gate them on pass rate so they stay in the intermediate-difficulty band where advantage signal exists
- Work backwards from a known-reachable end state — plant the answer, throw away the solution, then train the model to find it again — so solvability is guaranteed before you spend rollouts
- Judge trajectories in hindsight after seeing the full chain of events, or by polling several models; simple hindsight review catches most reward hacks, while telling a judge in advance not to allow a behavior does not stop it
- Grade against a decomposed ground truth built from path-invariant choke points, not against the original reference artifact, so novel-but-valid solutions are not failed
- Surface infrastructure errors to the model instead of resetting the environment, so recovery becomes a native model action
- Detect and penalize dangerous intermediate actions explicitly — reaching 'done' is not sufficient evidence of a good trajectory
- Combine an outcome/retrieval reward with a trajectory reward (e.g. rubric checks that the query is a natural sentence and that exploration volume was neither too much nor too little)
- Run small RL runs as part of environment design, because some environment defects only appear once RL is actually running
- Adjust for selection bias when deriving reward from observational outcome data — firms that took an action are systematically different from those that did not (a $4,200 vs $2,800 gap shrinks to ~$1,150 after adjustment)
- Route contextual, time-dependent, and preference-dependent problems to human data collection rather than into a programmatic RL environment
- For long-horizon RL, prefer value models over GRPO to cut gradient variance and enable bootstrapping, and apply RL to the compaction step as well as the task

**Avoid:**

- Outcome-only reward on agentic trajectories — it certifies the resignation letter that was sent 'successfully'
- Prompting an LLM as a judge to assess holistic quality (e.g. 'is this on brand') without first decomposing the property into codified elements
- Trusting rubric scores that are only loosely correlated with verifiable outcomes for RL or benchmarking
- Averaging preference labels across unmodeled raters; attach preferences to per-rater vectors instead, since disagreement on style is signal, not noise
- Optimizing agent search against benchmarks like BEIR/NanoBEIR whose entity-based 'caveman style' queries structurally favor BM25 and mis-train query behavior
- Giving agents tools that can search prior trajectories or archives — they learn to retrieve previous answers instead of reasoning
- Treating a few hundred handcrafted expert tasks as a scalable training basis for open-ended work
- Expecting RL to install dense new knowledge; it refines existing skills
- Fixing MoE expert load imbalance by cranking the load-balancing coefficient during SFT rather than fixing the pre/post-training distribution mismatch upstream
- Assuming full autonomy is the objective — handing control back to the user can be the optimal action, given calibrated confidence about risk, reversibility, and authorization

## Notable Outliers

- Sutton's bitter lesson holds in games but not reality: data matters more than compute, and choosing the right task matters far more than data — and the next paradigm is neither RLHF nor RLVR but optimization for calibrated decision-making. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s))
- In creative and design domains the most likely output is not the optimal one — quality lives at the tails, so slop is collapse to the mean rather than a capability deficit, which puts likelihood-maximizing training in direct tension with quality. ([Ending AI Slop](../talks/ending-ai-slop.md), [8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s))
- Given $1M and a 500-day business simulation, most frontier models drove the company bankrupt, and a simple rules-based system beat almost all of them; on Kelly Bench, every frontier model given $100K to trade lost money. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- Supervised learning from the environment gives the model a likelihood model of environment tokens — a native world model — that RL alone would not produce. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [17:35](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1055s))
- Building evals forces more rigorous reasoning than doing the analysis yourself, and doing so revealed that many canonical numerical QC thresholds in bioinformatics are arbitrary. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s))
- Off-policy staleness of up to about eight steps is acceptable in pipeline RL before quality degrades — the explicit trade against GPU utilization. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [15:17](https://www.youtube.com/watch?v=2bvtay8wGYI&t=917s))
- Instructing a model to write 'one concise sentence describing what it wants to find' rather than 'write a search query' is enough to break the BM25 keyword-stuffing pattern learned from code training. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [9:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=545s))

## All Talks

- [Ending AI Slop](../talks/ending-ai-slop.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [George Cameron](../speakers/george-cameron.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)
- [Udi Menkes](../speakers/udi-menkes.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Will Brown](../speakers/will-brown.md)

