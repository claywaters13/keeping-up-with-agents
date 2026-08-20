---
title: "reinforcement learning from verifiable rewards"
type: "concept"
slug: "reinforcement-learning-from-verifiable-rewards"
tier: "core"
maturity: "contested"
talk_count: 10
speaker_count: 12
---

# reinforcement learning from verifiable rewards

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **10** talk(s) by **12** speaker(s)

**Definition:** Post-training on tasks whose success can be checked programmatically (tests, compilers, solvers) rather than by a learned preference model.

*Also referred to as: reinforcement learning with verifiable rewards, rlvr, verifiable rewards, reinforcement learning from verifiable environments, reinforcement learning from verified outcomes, verifiable environments*

## State of Practice

The conference treated RLVR as proven in the places where a checker already exists — math answers, unit tests, database state, compilers — and treated everything else as the actual research problem. The dominant framing was that verifiability is a property of the domain rather than of the model: code is decomposable, executable and checkable, which is why models are good at it, so extending RLVR to design, biology, finance or computer use means manufacturing a checkable substrate rather than picking a better algorithm. Practitioners reported that task and environment design, not GRPO-vs-PPO, is where the difficulty lives: tasks must sit in a difficulty window where rollouts separate, graders must be durable across multiple valid solution paths, and end-to-end outcome reward is usually too sparse, so people decompose into intermediate nodes (analysis-DAG choke points in biology, codified brand elements in design, retrieval-plus-trajectory rewards in search). The stopgap for unverifiable domains — LLM-as-judge and rubrics-as-rewards — was openly distrusted: rubric scores were reported as only loosely correlated with verifiable outcomes, judges as reward-hackable, and human expert judgment as still substantially better. The other consistent claim was economic: environments and evals are the same artifact, and the scarce input is not model access but proprietary deployment traces and verified real-world outcomes that frontier labs cannot buy. Dissent came from speakers arguing the field is over-indexed on procedural single-answer tasks and that the next post-training objective is calibrated decision-making rather than either RLHF or RLVR.

## Consensus

### Verifiability is a property of the task domain, not of the model; RLVR works in code and math because answer keys exist there, so extending it to other fields requires first constructing a programmatically checkable substrate.

Support: **4** talk(s)

> "we treat for example the fact that code is verifiable and measurable as something that is a property about models and models are great at at coding um because we've made them great at coding but realistically it's actually a fact about code."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [1:57](https://www.youtube.com/watch?v=lCBf9slCanI&t=117s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

### Task and environment design — turning a fuzzy capability into a gradeable task at the right difficulty — is the hard part of RLVR, not the choice of training algorithm.

Support: **4** talk(s)

> "So in this case the task design itself is really kind of the hardest part of the problem of how do you turn something that appears very fuzzy into something that actually can be arled."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [5:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=344s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)

### End-to-end outcome-only reward is too sparse and too permissive; tasks must be decomposed into intermediate checkpoints and the trajectory itself scored, not just the final state.

Support: **4** talk(s)

> "the the grading of these end outcomes in biology uh is too sparse because the models are pretty bad. So, you have to break things up into manageable chunks to get some semblance of verifiability."
>
> — [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [7:50](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=470s)

Supporting talks: [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [From RL to IRL](../talks/from-rl-to-irl.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Ending AI Slop](../talks/ending-ai-slop.md)

### LLM-as-judge and rubric scores are not yet trustworthy as reward signal for subjective or expert domains — they are reward-hackable, only loosely correlated with verified outcomes, and behind human expert judgment.

Support: **3** talk(s)

> "LLM LLM as a judge might not necessarily always be the best method. We know that there's a lot of reward hacking."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [5:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=344s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### The scarce input for outcome-verified training is proprietary data from real deployment — production traces, failed experiments, verified business outcomes — not model access or scale.

Support: **4** talk(s)

> "the moat here is that it's not about the model access, it's about the data itself that you have."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From RL to IRL](../talks/from-rl-to-irl.md)

### RL post-training, not pre-training, is now the decisive stage: a state-of-the-art base model alone does not produce a useful product, and supervised learning's role is increasingly to build representations RL will later compose.

Support: **3** talk(s)

> "A good base model is not enough. So I took that lesson quite early on. So like I said, RLHF made LLMs products."
>
> — [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [3:03](https://www.youtube.com/watch?v=2bvtay8wGYI&t=183s)

Supporting talks: [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

## Disagreements

### Can LLM judges and rubrics serve as a legitimate reward signal where programmatic verification is unavailable?

| Position A | Position B |
|---|---|
| Yes — judges are already powerful general reasoners and are usable as reward if applied correctly: judge in hindsight after seeing the full trajectory or poll several models, and use rubric-based trajectory rewards alongside retrieval metrics. Simple hindsight review catches most reward hacks in practice.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* | No — judges produce plausible jargon without understanding the concepts, rubrics-as-rewards create an echo chamber where the model grades itself into agreement, and measured rubric scores correlate only loosely with verifiable outcomes, so they should not yet be used for RL. Human expert judgment remains substantially better.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* |

*Why it matters: If judges are admissible reward, RLVR generalizes to almost any domain via automated environment generation; if they are not, every new domain is gated on expensive expert-built graders and human grading throughput.*

### When a domain has no programmatic answer key, should you engineer a verifiable environment for it or fall back to expert-in-the-loop data and outcome grounding?

| Position A | Position B |
|---|---|
| Engineer verifiability: decompose the fuzzy goal into codified elements and deterministic graders, mine deployed traces into tasks, learn simulators of systems you cannot program, and work backwards from known-reachable end states so supervision comes for free.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Ending AI Slop](../talks/ending-ai-slop.md)* | Do not try to RL it. Models cannot verify themselves where there are no answer keys; hire the domain expert, run error analysis over observability logs before touching weights, and ground the model in observed real-world outcomes with selection-bias adjustment rather than in a constructed environment.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)* |

*Why it matters: This decides whether a vertical AI team invests in environment/grader infrastructure and a training loop, or in expert headcount and an outcome-labelled data asset — very different cost structures and time-to-value.*

### Does the verifiable-coding paradigm generalize to the rest of real work?

| Position A | Position B |
|---|---|
| Yes — code is the template: data analysis can be the verifiable substrate for biology exactly as code was for software, most real computer tasks are reachable through MCP/APIs/Playwright and can be represented as coding tasks, and code has become the dominant subset of pre-training data precisely because it carries this structure.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [From RL to IRL](../talks/from-rl-to-irl.md)* | No — the industry is over-indexed on coding and procedural tasks with one or two valid solutions, which leaves no room for creativity, ignores multi-agent environments with conflicting goals, and misses that in creative and open-ended domains the most likely output is not the optimal one. Benchmark success on verifiable tasks coexists with real-world failure on the tasks that matter.<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Ending AI Slop](../talks/ending-ai-slop.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: It determines whether the next capability jump comes from scaling verifiable-task RL into new domains, or from a different objective entirely — e.g. calibrated decision-making or preference-pluralism data — which implies a different API shape and different training investment.*

## Practical Guidance

**Do:**

- Decompose the fuzzy target into codified elements and grade outputs against that decomposed ground truth rather than against the original reference artifact, so novel-but-valid solutions are not penalized
- Ship tasks as a prompt + grader config + deterministic Python grader (SWE-bench-shaped), and make the grader durable — path-invariant across the multiple valid analysis routes an expert could take
- Keep task difficulty inside the window where rollouts separate; too-easy and too-hard tasks give no advantage signal, so search for and iterate on mid-difficulty tasks
- Score the trajectory as well as the outcome: reward query quality and exploration volume in search, penalize dangerous or unauthorized intermediate actions in computer use
- Mine traces from a deployed agent as the source material for new tasks when no labels exist, and run the loop online — generate, solve, synthesize, gate on pass rate
- Work backwards from an end state you know is reachable: plant the answer, throw away the solution, and train the model to re-find it
- Judge in hindsight after the full chain of events (or by polling several models) rather than instructing a judge up front not to allow a behavior
- Pass infrastructure errors to the model instead of resetting the environment, so recovery becomes a native model action and handoff to the user becomes an available optimal action
- Run small training runs as part of environment design — some failure modes only appear once RL is actually running
- Adjust for selection bias when deriving reward from observational outcome data; firms that took an action differ systematically from those that did not
- In subjective domains, attach preferences to per-rater preference vectors instead of averaging across unmodeled raters, and tie expert commentary to the specific code component that produced the visual
- Reserve RL for refining existing skills and use supervised data for dense new knowledge; ensure the base model has seen the atomic skills RL will compose
- Hire the domain expert before iterating, and do error analysis over observability logs before any weight-touching technique

**Avoid:**

- Prompting an LLM as a judge for a holistic verdict (e.g. 'is this on brand?') — decompose first or the signal is reward-hackable noise
- Outcome-only reward: a trajectory can reach 'done' having taken dangerous, irreversible, or unintended actions along the way
- Treating rubric scores as ready for RL or benchmarking when they are only loosely correlated numerically with verifiable outcomes
- Rubrics-as-rewards where the AI grades itself into agreement — an echo chamber, not a signal
- Building the training basis from a few hundred handcrafted expert tasks and expecting it to cover open-ended real-world work
- Giving agents tools that can search prior trajectories or archives — this teaches retrieval of previous answers instead of reasoning
- Resetting the environment on infrastructure errors, and assuming failure resets rather than persists
- Assuming more context substitutes for outcome grounding — a company's full financial data is still one group of data points
- Averaging preference data across raters you have not modeled, and treating expert disagreement on style or aesthetics as bad data
- Cranking up the MoE load-balancing coefficient during SFT to paper over pre/post-training distribution mismatch instead of fixing the early data mix
- Treating full autonomy as the objective by default; handoff to the user is sometimes the optimal action given calibrated confidence about risk and reversibility
- Treating adversarial or red-team tasks as a byproduct instead of mainstream training data

## Notable Outliers

- Environments and evals are the same object — one environment can serve RL, SFT data generation, on-policy distillation, and prompt optimization — and verifiable rewards are the easy special case, not the norm. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [4:38](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=278s))
- Learned simulators make better RL environments than real production systems, because full back-end controllability lets you plant the answer and guarantee solvability. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [12:24](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=744s))
- The next post-training paradigm is neither RLHF nor RLVR: RLHF optimizes human preference and RLVR optimizes log error rates of pure correctness, while the target should be calibrated decision-making with a different API shape. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [17:04](https://www.youtube.com/watch?v=cJ0EOzey--o&t=1024s))
- Given $100K to trade Premier League football matches over a one-year horizon, every frontier model lost money; in the Princeton 500-day business simulation a simple rules-based system outperformed almost all of them. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s))
- Value models beat GRPO for long-horizon RL — lower gradient variance, trajectory-level operation compatible with compaction, and bootstrapping — accepting the added bias and complexity; off-policy staleness up to about eight steps is tolerable in pipeline RL. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [11:31](https://www.youtube.com/watch?v=2bvtay8wGYI&t=691s))
- The base model only needs exposure to the atomic skills RL will later compose; RL extrapolates from there provided the environment is hard enough. ([The Base Model Is Dead](../talks/the-base-model-is-dead.md), [14:48](https://www.youtube.com/watch?v=xbPriQWXtWM&t=888s))
- Building evals exposed that many canonical numerical QC thresholds in bioinformatics are arbitrary — writing the grader forces more rigorous reasoning than doing the analysis yourself. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s))
- In creative domains quality lives at the tails of the distribution, so optimizing toward the most likely output is what produces slop; expert disagreement on style is signal, not noise. ([Ending AI Slop](../talks/ending-ai-slop.md), [8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s))
- Agents write keyword-stuffed 'caveman' queries because RL and benchmarks (BEIR/NanoBEIR) structurally favor BM25; instructing the model to write 'one concise sentence describing what it wants to find' bypasses the trained pattern. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [9:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=545s))
- Harness guardrails are a transitional scaffold — strong early, progressively thinner as model capability improves — and realistic training data only comes from deploying the product and letting it fail. ([From RL to IRL](../talks/from-rl-to-irl.md), [17:12](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=1032s))

## All Talks

- [Ending AI Slop](../talks/ending-ai-slop.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
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

