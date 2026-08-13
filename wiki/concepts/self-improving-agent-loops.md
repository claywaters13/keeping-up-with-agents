---
title: "self-improving agent loops"
type: "concept"
slug: "self-improving-agent-loops"
tier: "core"
maturity: "consolidating"
talk_count: 20
speaker_count: 21
---

# self-improving agent loops

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **20** talk(s) by **21** speaker(s)

**Definition:** Agents that modify their own prompts, skills, tools, or harness based on their results, closing a loop from outcome back to configuration.

*Also referred to as: self-improving systems, recursive self-improvement, agent self-improvement, self-improvement loops, multi-agent self-improving systems, automatic skill generation, agent self-modification*

## State of Practice

The field has converged on a concrete recipe: an agent proposes a change to another agent's prompt, tools, or codebase; the change is measured against a held-out eval suite; and it is kept or rolled back based on the delta. Multiple teams independently reported working numbers from this loop — 18%→83% pass rate in ~10 iterations (Nearform), 68%→83% with 80.2% on unseen test data (Langfuse), NanoChat bits-per-byte 0.93→0.91 and CUDA kernels beating NVIDIA's leaderboard (Recursive), top 12% on an NVIDIA Kaggle competition in 10 iterations (Morgan Stanley), and seven leaderboard records versus the best human's three (Weco). The load-bearing component is universally agreed to be the eval, not the optimizer: speakers repeatedly said that optimizing against a bad target function collapses the whole system, and that the optimizer must be structurally prevented from touching its own scorers or leaking test data into training. Control structures have standardized around per-hypothesis git branches with rollback on regression, and acceptance rates are low by design — BabyAGI 4 accepted 4-5 of 8-13 proposed patches, Weco landed 28% of submissions. What remains unsettled is scope: whether the loop's durable home is the harness or the weights, whether it can ship without a human gate, whether eval data should come from production or simulation, and whether iteration compounds or whether nearly all the gain arrives in the first pass.

## Consensus

### The eval / target function is the load-bearing component of a self-improvement loop; a bad eval makes the entire loop optimize toward the wrong optimum regardless of how good the optimizer is.

Support: **7** talk(s)

> "of course the evaluation is the most important piece and LLMs aren't malicious, but they can make, you know, very silly mistakes and if you're optimizing against a bad a bad eval, the whole thing kind of falls apart."
>
> — [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [9:18](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=558s)

Supporting talks: [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Agents Building Agents](../talks/agents-building-agents.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)

### The binding constraint on agent quality is the harness and the improvement loop around the model, not model capability — reaching for a bigger model, longer context, or more MCP servers is the wrong reflex.

Support: **6** talk(s)

> "there is a massive capabilities overhang in computer use. The models are good enough, but we haven't done the engineering work to solve it."
>
> — [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [5:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=346s)

Supporting talks: [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)

### The optimizing agent must be structurally prevented from reaching its own scoring surface — forbidden from editing golden datasets and scorers, and constrained by an API that makes test-data leakage impossible rather than merely discouraged.

Support: **4** talk(s)

> "updating the golden data sets or the scorers just to let the evals pass is not a good idea, so we want to enforce we want to tell the we want to tell the AI agent to not do that"
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [11:55](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=715s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)

### The loop works by proposing many candidate changes and accepting only a minority, gated on a measured metric delta with rollback on regression — low acceptance rates are normal, not a sign of failure.

Support: **3** talk(s)

> "for these loops, it would loop like eight or 13 times, but only accept four or five of those patches. And it actually did have, you know, modest, but like statistically significant improvement on long mem eval scores."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [11:47](https://www.youtube.com/watch?v=khVX_BUnEwU&t=707s)

Supporting talks: [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Agents Building Agents](../talks/agents-building-agents.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### Gains track the specificity of the failure signal: unambiguous, causal, binary feedback drives improvement, while scalar quality scores and bare pass/fail results do not tell the agent what to change.

Support: **4** talk(s)

> "Agents thrive on feedback. Immediate unambiguous feedback. Not just feedback that shows this went wrong. Feedback that shows why and how this went wrong."
>
> — [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [11:57](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=717s)

Supporting talks: [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)

### Runtime telemetry — traces, execution logs, correction events — is a prerequisite input to the loop, and instrumentation volume should increase sharply now that agents rather than humans are the consumers.

Support: **5** talk(s)

> "Now, you're going to trace 10 times more. You're going to log 10 times more because that helps you know what path your software took."
>
> — [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [9:12](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=552s)

Supporting talks: [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Agents Building Agents](../talks/agents-building-agents.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)

### The human role in a working loop shifts from executing the fix to designing the loop and reviewing its output — the human moves up the stack rather than out of it.

Support: **6** talk(s)

> "So the search is automated. the human would just move up the stack not out of it."
>
> — [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [15:04](https://www.youtube.com/watch?v=iCj_ATyThvc&t=904s)

Supporting talks: [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)

## Disagreements

### As models improve, does the self-improvement loop belong in the harness/scaffolding layer, or does it collapse into the model weights?

| Position A | Position B |
|---|---|
| The harness is durable and is where the loop lives. Long-running agents need an experiential world model built from their own log; a domain-optimized harness produces above-baseline results from the same model; codebase and setup work is a permanent standing investment.<br>*[Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | Real self-improvement is weight-level. True RSI requires an AI with access from pre-training through RL and harnesses to update its own next version; the whole system is bottlenecked on the intelligence of its smartest model since every judge and reward model is distilled from it; and scale, not scaffolding, is what drives progress.<br>*[First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md)* |

*Why it matters: If the harness is transient, every hour spent on prompt/skill/tool optimization is depreciating work that the next model release erases. If it is durable, harness engineering is the permanent locus of differentiation and should be staffed accordingly.*

### For an enterprise, where does durable value from auto-improvement accumulate — in the custom harness, or in the environments, evals, and specifications it optimizes against?

| Position A | Position B |
|---|---|
| Build and own the harness. A harness tuned to your domain achieves above-model results, building one is an ordinary engineering problem rather than a frontier-lab capability, and writing it from scratch rather than using an off-the-shelf framework gives maximum freedom to tweak.<br>*[Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)* | General auto-research capability becomes a commodity, so whatever lives in the middle stops mattering. Value migrates to environments and proprietary evaluation data, to codebase abstraction (currently underrated relative to evals), and for infrastructure vendors to the specification itself rather than the implementation.<br>*[Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)* |

*Why it matters: This determines whether an org's scarce senior engineering time goes into scaffolding code or into curating evaluation environments and proprietary measurement data — and whether the harness is treated as an asset or as a disposable middle layer.*

### Should a self-improved agent variant ship to production automatically once it clears its eval targets, or does a human gate remain mandatory?

| Position A | Position B |
|---|---|
| Auto-ship on eval targets. If an optimized variant meets its scores it goes to production without human review, and being bottlenecked on humans launching, reviewing, and babysitting runs is a state to be engineered away.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)* | A human gate is still required. Clustered failure reports must be triaged by domain experts because clusters can be false positives or intended behavior; production data must be reviewed by a human and not only by coding agents; larger fixes still need a human to spearhead them; and in regulated domains agent-to-agent code review fails because accountability cannot be assigned to the model.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* |

*Why it matters: Full autonomy is what converts the loop from a productivity multiplier into a genuinely self-improving system; keeping the human gate caps throughput at human review capacity but is the only current answer to accountability and to evals that are themselves incomplete.*

### Should the eval data that drives the loop be generated in simulation, or discovered from production traffic?

| Position A | Position B |
|---|---|
| Generate it in simulation. Waiting on production data is the bottleneck, A/B testing means experimenting on live users, and simulated evals correlate highly enough with real data (80% of domain-expert labels confirming usability) to cut the iteration cycle from weeks to under a day. Deterministic simulation can even expose information the real system hides, which is exactly the signal the agent needs.<br>*[SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)* | The complete eval suite is a product of discovery from production. It cannot be pre-guessed upfront by domain experts; failure modes found in live traces become new golden-dataset entries, and LLM-as-a-judge evals are inherently backward-looking because you build them for failures you have already seen.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Agents Building Agents](../talks/agents-building-agents.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)* |

*Why it matters: It sets whether a team can run the loop pre-launch on a greenfield agent at all, or must first ship, accumulate traffic, and pay the sim-to-real gap in review effort — a difference of weeks per iteration and, on the sim side, a mandatory investment in measuring that gap.*

### Does the self-improvement loop compound across iterations, or does nearly all of the gain arrive in the first pass?

| Position A | Position B |
|---|---|
| Iteration count is the lever. Systems work best the more iterations they can explore; ~10 iterations moved a naive agent 18%→83% and a human-optimized production agent up another 10%; 1,300 experiments over 22 days beat the best human contributor through tireless iteration rather than parallelism.<br>*[Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [Agents Building Agents](../talks/agents-building-agents.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)* | Returns collapse fast. The first iteration captured a 10-point gain and everything after was marginal before plateauing — you could have stopped there — and label noise in the ground truth itself caps the ceiling, so the loop needs an explicit escape hatch rather than being left to burn tokens against a wall.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)* |

*Why it matters: It decides the budget: whether to fund long autonomous runs and treat compute as the input, or to run one high-signal pass, take the cheap gain, and spend the remaining effort on sharpening the evaluator instead.*

## Practical Guidance

**Do:**

- Run each optimization hypothesis on its own git branch; continue from that branch if metrics improve, roll back if there is a regression.
- Explicitly instruct the optimizing agent that it may not modify golden datasets or scorers, and tighten the codebase API so test data physically cannot reach training (this dropped one fraud-detection pipeline's leakage rate to zero).
- Replace scalar 0-1 / 1-5 quality scores with binary domain-specific checks — 'is the answer grounded in the retrieved context, yes/no', brand-name correctness, categorization into known failure modes.
- Calibrate LLM judges before using them to compare agent versions, since the same judge scores the same problem differently run to run.
- Split into fit/validate and a held-out unseen test set (~300 items) and confirm the optimized prompt generalizes; a few hundred labeled examples was enough to produce high-signal feedback.
- Give the loop an explicit escape hatch so it stops instead of grinding against a plateau.
- Deliver the production data the coding agent needs as files written into the repo — harnesses work well with files, even ~10MB ones — rather than just pointing the agent at a data source.
- Measure every agent against the raw baseline model to confirm the harness is actually adding value.
- Feed every newly discovered production failure mode back into the golden dataset so the eval suite catches that regression thereafter; generate a live-data failure report roughly once per sprint.
- Retire any eval where all models score ~90%, and when running evals delete git history and apply network allowlists so models cannot mine the answer.
- Cap skill.md at ~100 lines (a skill is a folder) and treat a first prompt exceeding 40-50K tokens of baseline context as a progressive-disclosure failure; ~20-25K is the target.
- Source agent context from live systems (GitHub, CRM, Tableau, dbt) and log correction events back into it, rather than relying on hand-maintained markdown.
- If you adopt simulation, explicitly measure and close the sim-to-real gap first — the gains are unavailable until the results can be trusted.

**Avoid:**

- Responding to bad agent answers by upgrading the model, extending the context window, or bolting on more knowledge bases and MCP servers.
- Letting the optimizer touch its own scoring surface — it will make the evals pass by cheating rather than by fixing the agent.
- Generic evaluators (correctness, helpfulness, hallucination) scored on an undefined 0-1 or 1-5 scale; the levels are almost never defined, so the signal is both low and inconsistent across runs.
- Pointing a coding agent at raw production data and expecting results without a skill that selects the right data and lands it in the repo.
- Reviewing production data only with coding agents — a human must look at it, because failure modes and usage shift over time.
- Hand-maintained .md files and skills as the context substrate for enterprise definitions and KPIs, which change faster than anyone can update them.
- Babysitting agents: if engineers on your team are doing it, the codebase and harness setup is wrong, and it silently burns context and money.
- Mandating agent adoption across a company; uneven adoption is actively harmful because low-adoption engineers inherit the review burden for high-adoption engineers' PRs.
- Plain next-token-prediction finetuning on your own corpus to make an agent learn from its data — loss goes to near zero, generation collapses, and nothing generalizes.
- Shipping agents to production without observability; without traces you are guessing among a million possible code paths.
- Serving production browser agents from self-hosted Mac Minis, and letting rendering vary (mobile vs desktop layout) between runs.
- Assuming a complete eval suite can be written upfront by domain experts before any production failures exist.

## Notable Outliers

- The choice of harness architecture itself — number of strategist agents, agent roles — is arbitrary when humans pick it, and should be handed to an LLM as a verifiable meta-optimization loop. ([Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [15:00](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=900s))
- Almost every record-setting idea the auto-research agent produced originated from humans (papers, other participants, adjacent communities); the tiny fraction of genuinely original ideas emerged from the agent working around a 16MB file-size constraint. ([How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [5:38](https://www.youtube.com/watch?v=iCj_ATyThvc&t=338s))
- Models write shared-state/blackboard-style agent code better than LLM-agent-style code, because decades of blackboard-architecture discussion sit in the training data while LLM agent patterns are only ~3 years old. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [14:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=894s))
- Any loop that fixes a dataset and trains on it saturates unless the model is underparameterized; real self-improvement requires the system to make its own training data harder as it improves, which is the actual mechanism behind AlphaGo. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [17:30](https://www.youtube.com/watch?v=WiqDvX6isc4&t=1050s))
- NanoChat-style auto-research is not true recursive self-improvement — RSI requires an AI with self-awareness of its own shortcomings and access from pre-training through RL and harnesses to update its next version. ([First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [14:13](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=853s))
- The entire training system is capped by the intelligence of its single smartest model, because every judge, reward model, and research agent in the loop is distilled from it. ([Recursive Model Improvement](../talks/recursive-model-improvement.md), [19:19](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=1159s))
- LLM-generated skills measurably degrade LLM performance relative to human-written ones by consuming more tokens and more reasoning time — a skill is only as good as the human who wrote it. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [24:09](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1449s))
- Let the agent 'dream' in the background — compacting recurring customer session patterns into reusable data points — as a self-upgrade mechanism. ([Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [11:40](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=700s))

## All Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Agents Building Agents](../talks/agents-building-agents.md)
- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Recursive Model Improvement](../talks/recursive-model-improvement.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Aman Gupta](../speakers/aman-gupta.md)
- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Bennet Fenner](../speakers/bennet-fenner.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [Dominik Tornow](../speakers/dominik-tornow.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Jack Morris](../speakers/jack-morris.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Richard Socher](../speakers/richard-socher.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Shreya Rajpal](../speakers/shreya-rajpal.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)
- [Zubin Aysola](../speakers/zubin-aysola.md)

