---
title: "world models"
type: "concept"
slug: "world-models"
tier: "supporting"
maturity: "frontier"
talk_count: 8
speaker_count: 10
---

# world models

**Maturity: FRONTIER** — Frontier — too new or sparse for consensus yet

*Supporting concept* &middot; discussed across **8** talk(s) by **10** speaker(s)

**Definition:** Learned internal or simulated models of an environment that a system can plan or generate against.

*Also referred to as: world model, world model evaluation, world simulators, codebase world models, generative text-based games, spatial reasoning in llms, microworlds*

## State of Practice

"World model" at this conference means an explicit, queryable representation of a bounded environment that a system reasons or plans against — and the striking thing is how many independent teams built one out-of-band rather than expecting it to emerge from the weights. Concrete instances presented: a machine-readable graph of 25,000 repos and their service dependencies (Agentic AI Foundation), a per-user context model computed by a slow engine that learns durable patterns plus a fast engine that recomputes live urgency (monday.com), learned simulators of tools that cannot be programmed, built so answers can be planted and solvability guaranteed (Prime Intellect), and an agent's own predicted next state of the machine, made measurable by forking a recorded trajectory and asking it what the computer looks like (Cua). The shared diagnosis is that frontier model capability is no longer the binding constraint — Yu Su argues that past an intelligence threshold the continual-learning algorithm sets the slope, monday.com says the most capable agent in the world still does not understand you, and Cua shows pass rate moving 62%→80% purely by scoping the agent's view to a window. The repeated failure mode is substitution: a longer context window, more memory, or a bigger prompt offered in place of a precomputed structure, all of which speakers report do not work. Where the field is genuinely split is on whether that structure should be hand-engineered outside the model and served at query time, or learned into the model in situ from environment interaction — and, relatedly, whether humans still need their own model of a system once the agent has a good one.

## Consensus

### A usable world model must be computed ahead of time as an explicit structure; a longer context window, a bigger prompt, or bolted-on memory is not a substitute.

Support: **4** talk(s)

> "You need to build it much before someone asks the question."
>
> — [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [6:37](https://www.youtube.com/watch?v=Btk8wDUVs74&t=397s)

Supporting talks: [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)

### The relevant world is not one environment but many idiosyncratic micro-worlds (per repo, per user, per application), so world models must be built per-environment rather than as a single global representation.

Support: **3** talk(s)

> "It's just like too heterogeneous and dynamic for any monolithic model to try to compress it into one static representation"
>
> — [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [5:27](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=327s)

Supporting talks: [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)

### Frontier model capability is not the limiting factor for agents operating in a specific environment; the environment representation given to the model is.

Support: **4** talk(s)

> "If you ask me, it's not the model, it's the medium."
>
> — [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [2:20](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=140s)

Supporting talks: [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)

### Whether an agent (or a human) actually models the environment must be probed with an explicit test, because successful task completion or a fluent explanation is not evidence of understanding.

Support: **3** talk(s)

> "to measure the intelligence of an agent, you can't just measure its ability to successfully perform actions."
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s)

Supporting talks: [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)

## Disagreements

### Should the world model live outside the model as a precomputed artifact served into context, or inside the model as learned parameters?

| Position A | Position B |
|---|---|
| Build the world model as an external, hand-designed structure — a machine-readable service graph, a per-user profile computed offline by slow and fast engines — and serve it to an unmodified frontier model at query time; per-user/per-repo preprocessing, not training, is the missing layer.<br>*[From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* | External context is insufficient: the model must internalize the environment. Weak in-context approaches yield only marginal gains, both parametric and non-parametric learning are required, and supervised signal from environment tokens gives the model a native likelihood model of the environment that RL alone would not produce.<br>*[Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* |

*Why it matters: It decides whether the investment is a data/context-engineering pipeline you own or an RL-and-environments training stack, and whether a world model built for one deployment can compound across users or must be retrained per environment.*

### Once agents can model a system well enough to act on it, do humans still need to maintain their own understanding of it?

| Position A | Position B |
|---|---|
| Human understanding remains a hard requirement and needs an explicit speed regulator — don't send agent-written code for team review until you can pass a quiz on it, don't delegate every bug fix because you forfeit the peripheral feel for the machine, and keep agent plans in shared commentable spaces because understanding is a team property.<br>*[Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* | Push humans up the abstraction ladder: the end state is agents producing shippable results without human guidance, anyone filing work from Slack without touching GitHub, humans reserved for the highest-level judgments about goals and quality, and agents doing the grunt work while people focus on vision and story.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)* |

*Why it matters: It sets whether you build throughput gates that deliberately slow delegation to the speed of human comprehension, or infrastructure that removes humans from the loop — and Bouffard's talk ends by asking whether the second path ends in laying off the people who built it.*

### At serve time, should an agent receive the full modeled world or a deliberately narrowed slice of it?

| Position A | Position B |
|---|---|
| Maximize coverage: ingest everything, make each new data source cheap and purely additive, model the entire 25,000-repo codebase, and serve the whole precomputed context to the agent — the more it sees, the more it understands, and the model compounds over time.<br>*[From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* | Narrow the view: scoping the agent to a single window instead of the full desktop raised pass rate from 62% to 80% while using 34% fewer tokens, and lead with intuition before details rather than dumping the full structure.<br>*[Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* |

*Why it matters: The two prescriptions produce opposite engineering roadmaps — one spends on ingestion breadth and offline precomputation, the other on attention-scoping and retrieval discipline — and they give contradictory advice about whether adding a data source is free or actively harmful.*

## Practical Guidance

**Do:**

- Build a machine-readable model of every service and how they connect before attempting multi-agent autonomous work — Bouffard's team did this across 25,000 repos as the prerequisite for delegation from Slack.
- Split environment modeling into two engines on different schedules: a slow one over a long window that learns durable patterns, and a fast one over a short recent window that recomputes live signals; precompute both offline and recompute only a thin recent slice at request time.
- Scope a computer-use agent's observation to a single window rather than the full desktop — Cua measured 62%→80% pass rate at 34% fewer tokens.
- Measure the agent's world model directly: fork a recorded run at any point in its trajectory and ask the agent to predict the state of the computer at that moment.
- Adversarially attack your own environment for reward hacks before any task enters the dataset; only tasks that survive get admitted.
- When no labels exist, work backwards from a known-reachable end state — verify the easy problem, throw away the solution, and train the model to find it again.
- Simulate tools you cannot instrument. Full back-end controllability lets you plant the answer and guarantee the task is solvable, which real production systems cannot.
- Calibrate generated tasks to intermediate difficulty and gate on pass rate, because the RL advantage signal depends on separation across rollouts.
- Judge agent behavior in hindsight, after the full chain of events, rather than instructing a judge in advance about what to disallow.
- Run small training runs as part of environment design — some environment defects only appear once RL is actually running.
- Give agents a language-native authoring medium (HTML, structure, tokens) instead of coordinate/canvas interfaces, so the model never has to place a coordinate.
- Gate sending agent-written code to team review on being able to pass a quiz about what the agent wrote.
- Spend nearly-free generated code on throwaway micro-worlds built solely to understand an existing system.
- Isolate data sources so a bad feed degrades the model gracefully instead of breaking it, with fallback to last-verified context.
- Over-provision a warm sandbox pool with demand-based autoscaling — sandbox compute is 2–4x cheaper than GPU time, so redundancy still saves money.

**Avoid:**

- Do not treat a longer context window, a bigger prompt, or an added memory layer as a substitute for a structured model of the user or environment — none of them tell the agent what to prioritize.
- Do not expect a single monolithic model to compress heterogeneous, dynamic micro-worlds into one static representation.
- Do not report task success rate as your only measure of agent competence in an environment.
- Do not rely on telling a judge model not to permit a behavior; it does not prevent the behavior in the rollout.
- Do not build a training basis from a few hundred handcrafted expert tasks and expect it to cover open-ended real work.
- Do not hand agents tools designed for human hands and human eyes — Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops — or expect them to imitate human interaction patterns.
- Do not ship a history-derived context model to cold-start users; there is no reliable data to reason from, and the model always trails the live world.
- Do not delegate every bug fix to an agent — you lose the peripheral vision you get from debugging the system yourself.
- Do not add interactive figures by default when explaining a system; used untastefully they are slop and a crutch.
- Do not expect a computer-use agent to create artifacts from scratch yet — Cua's top model passed 6/25 tasks, all of them edits, and 0% starting from a blank schematic.
- Do not run multi-agent parallelism on local developer machines; give each agent an isolated cloud workspace.
- Do not leave GPUs idle waiting on sandbox spin-up or reset during RL for computer use — pay the startup cost on the infrastructure side.

## Notable Outliers

- Supervised signal from the environment gives the model a likelihood model of environment tokens — a native world model — which RL alone would not produce. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [17:35](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1055s))
- Computer-use agents pass only when editing an existing artifact; starting from a blank schematic, success drops to exactly 0%, and no tested model exceeds 30% reward. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s))
- Past a threshold of raw intelligence, more intelligence is unnecessary — current frontier models may already be smart enough, and the continual-learning algorithm becomes the binding constraint ('unbounded expertise from bounded intelligence'). ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))
- The fast/slow split was not invented for this product — neuroscience calls it complementary learning systems and data engineering calls it lambda architecture, and two unrelated fields converging on it is the argument for adopting it. ([From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [10:29](https://www.youtube.com/watch?v=Btk8wDUVs74&t=629s))
- The company world model over 25,000 repos let anyone ship a fix or feature from Slack without touching GitHub — and the speaker asks openly whether building it contributed to the layoffs of the people who built it. ([Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [16:49](https://www.youtube.com/watch?v=whue9_YquGA&t=1009s))

## All Talks

- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [OpenClaw in Your Hand: Building a Physical AI Terminal](../talks/openclaw-in-your-hand-building-a-physical-ai-terminal.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)

## Speakers

- [Dillon DuPont](../speakers/dillon-dupont.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Francesco Bonacci](../speakers/francesco-bonacci.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [George Cameron](../speakers/george-cameron.md)
- [James Russo](../speakers/james-russo.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Will Brown](../speakers/will-brown.md)
- [Yu Su](../speakers/yu-su.md)

