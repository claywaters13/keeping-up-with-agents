---
title: "agentic science"
type: "concept"
slug: "agentic-science"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 10
---

# agentic science

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **10** speaker(s)

**Definition:** Agents running the scientific loop — hypothesis generation, experiment design, analysis — in research and biomedical domains.

*Also referred to as: automated scientific discovery, auto-research agents, autonomous research agents, automated research agents, hypothesis generation, scientific workflow reproducibility, virtual cell modeling*

## State of Practice

Auto-research crossed from demo to deliverable in the last two quarters: multiple teams report agents setting real leaderboard records (seven Parameter Golf records in 22 days vs. three for the best human; NanoChat bits-per-byte 0.93→0.91; CUDA kernels beating NVIDIA's leaderboard bests), and practitioners date the inflection precisely to long-horizon coding ability arriving around Opus 4.5 / Claude Code / Codex in late 2025. The dominant methodological claim is that the eval or environment — not the harness, not model access — is the object of real engineering: your eval is the loss function, your codebase abstraction is the architecture, and the harness in the middle is on a path to commodity. That framing exports out of ML into wet-lab-adjacent domains: LatchBio treats data-analysis code as biology's verifiable substrate the way code was for SWE-bench, but has to decompose tasks into intermediate analysis-DAG nodes with deterministic graders because end-to-end outcome grading is too sparse a signal for current models. Outside of code-verifiable loops the picture is much worse — frontier models produce a 'fluent bluff' in finance (40% of advice across ~100k business situations reduced to 'acquire new customers'), single-cell transformer foundation models are matched by linear baselines, and no model reliably spots a lung nodule. The commercial consensus that follows is that proprietary outcome data and carefully built environments are the moat, and the live arguments are about ceilings: whether agents can originate hypotheses at all, and whether scaffolding like hierarchical decomposition is a durable lever or a chain-of-thought-style crutch that post-training will absorb.

## Consensus

### The evaluation/environment is the highest-leverage component of an auto-research system; a bad eval silently invalidates everything built on it, so eval construction deserves adversarial scrutiny and continuous reinvestment.

Support: **4** talk(s)

> "of course the evaluation is the most important piece and LLMs aren't malicious, but they can make, you know, very silly mistakes and if you're optimizing against a bad a bad eval, the whole thing kind of falls apart."
>
> — [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [9:18](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=558s)

Supporting talks: [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)

### Frontier models cannot be trusted to do real domain work out of the box — they know the literature but fail at extracting conclusions from real experimental or operational data, producing confident output that is wrong.

Support: **4** talk(s)

> "frontier models cannot be trusted to do real work. They're missing some capability between knowing biology and writing code. And this is exactly extracting scientific insight from real-world data."
>
> — [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [5:23](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=323s)

Supporting talks: [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [From Tokens to Cells: Foundation Models for Single-Cell Biology](../talks/from-tokens-to-cells-foundation-models-for-single-cell-biology.md)

### Durable competitive advantage comes from proprietary outcome data and hand-built environments, not from model size or model access, because general auto-research capability is heading toward commodity.

Support: **3** talk(s)

> "the moat here is that it's not about the model access, it's about the data itself that you have."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### Reward hacking and data leakage are the default failure mode of research agents and must be blocked structurally — by tightening interfaces and removing the shortcut from the environment — rather than by trusting the agent's intent.

Support: **4** talk(s)

> "We then tighten the obstruction to a more strict API where the test data couldn't reach the training and the data leakage rate just dropped to zero."
>
> — [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s)

Supporting talks: [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)

### Research agents now beat strong human efforts on narrow, well-instrumented benchmark tasks — leaderboard records, kernel optimization, competition submissions — within days of wall-clock time.

Support: **3** talk(s)

> "after very short amount of time it got better than people working often together with the AI for over a year on on this very on this benchmark and made the whole thing another two seconds over two seconds faster at 70 seconds."
>
> — [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [16:42](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1002s)

Supporting talks: [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)

### The human role shifts up the stack — from running experiments to designing environments, evals, and abstractions and supervising fleets of agents — rather than being eliminated.

Support: **4** talk(s)

> "So the search is automated. the human would just move up the stack not out of it."
>
> — [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [15:04](https://www.youtube.com/watch?v=iCj_ATyThvc&t=904s)

Supporting talks: [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)

## Disagreements

### Will scaling general frontier models close the gap to real scientific and domain work, or does that gap require domain-specific grounding, measurement, and verifiable structure?

| Position A | Position B |
|---|---|
| Capability will carry it: replacing manual processes with learned systems reliably produces improvements, recursive self-improvement is now feasible, and we are astronomically far from any intelligence ceiling — so the exponential does the work.<br>*[First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)* | Bigger models do not close it. The gap is experience and observation quality: outcome-verified data beats model size (a mid-size grounded model outperformed frontier models on business advice), scaling low-quality single-cell data will not generalize, current multimodal models cannot reliably observe scientific images, and verifiability structure rather than scale is what drives further gains.<br>*[Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [From Tokens to Cells: Foundation Models for Single-Cell Biology](../talks/from-tokens-to-cells-foundation-models-for-single-cell-biology.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)* |

*Why it matters: It decides whether a science-AI team should spend its next year buying compute and waiting for the next model, or spend it building instrumentation, outcome datasets, and graded environments. The two roadmaps share almost no work.*

### Do current research agents generate genuinely novel hypotheses, or do they mainly execute ideas that humans originated?

| Position A | Position B |
|---|---|
| Ideas remain human. Tracing every record-setting PR showed almost all ideas came from human papers, other participants, or adjacent communities, with only a very small fraction original to the agent; and without explicit scaffolding agents propose hyperparameter tweaks rather than radical changes like moving from 2.5D to 3D convolutions, saturating once they run out of research taste.<br>*[How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)* | Agents already originate real architectural novelty — hash bi-gram/tri-gram embedding tables mixed into attention value paths through learned gates — not hyperparameter tuning, and beat a benchmark humans-plus-AI had pushed on for over a year.<br>*[First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)* |

*Why it matters: If ideas are the human contribution, you staff for research taste and build agents as tireless executors; if agents originate ideas, the constraint becomes verification throughput and you staff for environment building instead.*

### Is hand-designed scaffolding — decomposition prompts, harness topology, codebase abstraction — a durable engineering lever or a temporary crutch that model progress will absorb?

| Position A | Position B |
|---|---|
| Temporary. Hierarchical decomposition prompting is analogous to chain-of-thought on GPT-4-era models and will be needed less as models are post-trained to decompose problems themselves; harness design choices (how many strategists, which agent roles) are arbitrary human guesses that an LLM should meta-optimize, and the harness in the middle is heading toward commodity.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)* | Durable and underrated. Codebase abstraction is the architecture — it sets what the agent can explore, and tightening it drove data leakage to zero — while in biology the decomposition into intermediate analysis-DAG nodes is what makes any verifiability possible at all given how sparse end-to-end grading is.<br>*[How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* |

*Why it matters: It determines whether scaffolding work is throwaway tooling to be minimized or the core artifact worth a week of three scientists' time per task.*

## Practical Guidance

**Do:**

- Start every auto-research project from the eval, and run two adversarial checker agents over it before trusting a score: one high-level, looking for conceptual errors and forward leakage of information, and one programmatic, writing unit and integration tests.
- Delete git history at the start of a coding eval run (restore it at the end) and use network allowlists, so the model cannot mine the fix from history or the web.
- Retire any eval where all models score around 90%, and treat eval creation as continuous investment since eval half-life shrinks as models improve.
- Constrain reward hacking through the interface: tighten the codebase API so test data physically cannot reach training rather than relying on the agent's intent.
- Make problem decomposition an explicit, separate action — have the agent generate a linked hierarchy of component documents over the codebase, then reason about improvements per component; this measurably widens the space of proposed changes versus a single 'optimize this' prompt.
- Route hypothesis generation and post-implementation critique to a stronger reasoning model than the executor (e.g. packaging code and data out to a GPT-5.x Pro-class model), and call a stronger multimodal model as a metric reviewer for image outputs.
- In biology, break tasks into intermediate analysis-DAG nodes with deterministic Python graders — task prompt, grader config, grader function, SWE-bench-shaped — because end-to-end outcome grading is too sparse for current models.
- Test eval durability against path invariance: confirm that alternative valid analysis paths still pass, and use panels of scientists grading each other's work as the ground-truth proxy to surface badly specified tasks.
- Adjust for selection bias when mining outcome data for advice (the naive $4,200/day vs $2,800/day price-raise gap shrinks to roughly $1,150 once you account for which firms can raise prices).
- Split roles: use frontier models as hypothesis-candidate generators and a separately trained RL selector to decide which candidates are actually right.
- Manufacture hard verifiable RL problems cheaply by deleting features or files from generated applications until tests fail, then asking the model to re-implement.
- Log every cross-organization step as a signed, chained receipt so results can be trusted and repeated across institutional boundaries.

**Avoid:**

- Answering agent plateau with more tools — adding tools does not fix a coordination or hypothesis-quality constraint.
- The Karpathy-style 'here's the codebase, here's the objective, optimize' prompt for long-horizon research; it saturates after a while and was beaten by an explicitly decomposed multi-agent loop.
- Trusting public benchmark scores as capability estimates — models go back through git history and the open web for answers, and controlling for that visibly changes the numbers.
- Treating more context as a substitute for outcome grounding: a company's entire financial dataset is still one group of data points, which is the difference between sounding right and being right.
- Using rubric or LLM-judge scores as an RL signal or benchmark in science — they are associated with verifiable outcomes but only loosely correlated numerically.
- Scaling existing low-quality measurement data and expecting generalization to unseen data instead of also improving how the data is measured.
- Assuming a compressed latent representation preserves the signal — check simple linear baselines, which sometimes match or beat expensive transformer foundation models on single-cell data.
- Expecting today's multimodal models to make reliable scientific observations; none reliably identify features like a lung nodule because they are not trained on scientific images.
- Confining AI gains to the R&D stage of a drug pipeline and expecting the 10-year, multi-billion-dollar timeline to move.
- Hand-designing harness topology and treating those arbitrary choices as settled rather than as another verifiable loop to optimize.

## Notable Outliers

- In a Princeton 500-day business simulation with $1M starting capital, most frontier models drove the company bankrupt in under 500 days, and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- The winning research agent used at most 4% of the competition's total compute while producing ~15% of the records, with a 28% leaderboard hit rate — roughly six times the community average. It did not win through parallelization. ([How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [4:30](https://www.youtube.com/watch?v=iCj_ATyThvc&t=270s))
- Within a couple of days and with no dedicated kernel experts on the team, the system discovered CUDA kernels beating NVIDIA's own leaderboard bests across all categories — and many MoE models still run billion-dollar clusters at ~30% utilization. ([First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [17:33](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1053s))
- Models refused disguised harmful biology requests far less often than they answered routine ones, and the right framing for that safety gap is as an evaluation problem. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [16:29](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=989s))
- Building evals exposed that many canonical numerical QC thresholds in bioinformatics are arbitrary — how to normalize, what counts as an inflammatory gene, what radius is appropriate — because evaluation forces more rigorous reasoning than doing the analysis yourself. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s))
- The number of new drugs developed per year is declining despite all advances in technology and AI — the inverse of Moore's law. ([From Tokens to Cells: Foundation Models for Single-Cell Biology](../talks/from-tokens-to-cells-foundation-models-for-single-cell-biology.md), [4:34](https://www.youtube.com/watch?v=-561cZmir5Q&t=274s))
- As automation matures, organizations will give agents budgets rather than just tools — so agents can discover services, negotiate terms, and pay peer-to-peer across organizational boundaries with no third party mediating quote, deal, execution, or receipt. ([Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [3:23](https://www.youtube.com/watch?v=Fu45geO3zX8&t=203s))
- The entire training system is bottlenecked on the intelligence of its smartest model, because every judge, reward model, and research agent is distilled from it — so improving the top-level model raises the floor of every loop at once. ([Recursive Model Improvement](../talks/recursive-model-improvement.md), [19:19](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1159s))
- Hierarchical decomposition prompting is a temporary scaffold analogous to chain-of-thought on GPT-4-era models, valuable mainly as a structured way to scale test-time compute, and will be needed less as models are post-trained to decompose problems themselves. ([Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s))

## All Talks

- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)
- [From Tokens to Cells: Foundation Models for Single-Cell Biology](../talks/from-tokens-to-cells-foundation-models-for-single-cell-biology.md)
- [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Recursive Model Improvement](../talks/recursive-model-improvement.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Akram Baharlouei](../speakers/akram-baharlouei.md)
- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [George Cameron](../speakers/george-cameron.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Richard Socher](../speakers/richard-socher.md)
- [Sina Shahandeh](../speakers/sina-shahandeh.md)
- [Udi Menkes](../speakers/udi-menkes.md)
- [Zubin Aysola](../speakers/zubin-aysola.md)

