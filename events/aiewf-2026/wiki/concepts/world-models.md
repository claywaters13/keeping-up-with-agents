---
title: "world models"
type: "concept"
slug: "world-models"
tier: "supporting"
maturity: "contested"
talk_count: 12
speaker_count: 14
---

# world models

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **12** talk(s) by **14** speaker(s)

**Definition:** Learned internal or simulated models of an environment that a system can plan or generate against.

*Also referred to as: world model, world model evaluation, world simulators, codebase world models, generative text-based games, spatial reasoning in llms, microworlds*

## State of Practice

The conference used "world models" for two barely-overlapping things, and neither camp cited the other. In generative media, a world model means a real-time interactive video model — pixels generated causally under user control — where the frontier has moved off per-frame quality onto serving (sub-100ms routing to geographically local GPUs, one-step distillation of ~30 denoising steps, drift-free multi-hour streams) and where consistency evaluation is admitted to be unsolved even at DeepMind. In agent infrastructure, a world model means an explicit, precomputed, machine-readable representation of a specific environment — a 25,000-repo service graph, a per-user entity graph computed offline on slow and fast clocks, an ECS-style asset-tag description of a game, a learned simulator of an un-programmable API — built precisely because no frontier model, however capable, contains the local physics of your microworld. The shared technical claim across the agent camp is that the representation must live in the model's native medium (code, HTML, tags, symbols, accessibility trees), not in pixels or human GUI affordances, and that it must be constructed ahead of query time rather than stuffed into a longer prompt. Measurement is the weak joint everywhere: computer-use leaderboards are flat below 30% reward, agents score 0% starting from a blank artifact, and the only proposal for measuring a world model directly — asking the agent to predict the next environment state and scoring that prediction — was made by exactly one talk.

## Consensus

### A frontier model does not arrive with a usable model of your specific environment; the environment model must be constructed and computed ahead of query time, outside the weights and outside the prompt.

Support: **4** talk(s)

> "the most capable agent in the world whether it's like a cloud and Gemini, it doesn't understand you. He need to process it beforehand."
>
> — [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [14:55](https://www.youtube.com/watch?v=Btk8wDUVs74&t=895s)

Supporting talks: [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)

### The environment should be represented in the symbolic medium models natively predict over — code, HTML, tags, entity graphs, accessibility trees — rather than in pixels or in human-facing GUI surfaces.

Support: **5** talk(s)

> "You need to give the AI tools based on how it thinks, not in pixels, in language. Words, tokens, structure, that is its native medium."
>
> — [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [2:57](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=177s)

Supporting talks: [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)

### For generative (pixel-space) world models the binding constraint is no longer output quality but serving infrastructure — streaming, global GPU placement, and CPU/GPU orchestration.

Support: **3** talk(s)

> "And so the models are here and the frontier is really in how we serve them."
>
> — [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [7:07](https://www.youtube.com/watch?v=Xln-On3syJk&t=427s)

Supporting talks: [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)

### The defining failure mode of live generative world models is long-horizon state retention — memory loss and compounding error over a session — not per-frame fidelity.

Support: **3** talk(s)

> "one of the things that live live real-time models struggle with is memory. If you've seen demos from Genie 3, for example, we've all seen that the character can look back and then will not remember what what's going on."
>
> — [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [12:20](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=740s)

Supporting talks: [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)

### Task success rate is not a sufficient measure of whether a system has a world model; environments and rewards must be probed adversarially and judged on state understanding, and no one has a solved evaluation.

Support: **3** talk(s)

> "to measure the intelligence of an agent, you can't just measure its ability to successfully perform actions."
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s)

Supporting talks: [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)

## Disagreements

### Is a world model a generative simulator of pixels, or a structured symbolic representation of an environment?

| Position A | Position B |
|---|---|
| A world model is real-time interactive video: pixels generated causally under user control. Anything offline or non-interactive (Gaussian splatting, batch video) does not qualify, and the value comes from steering the generated stream in under a second.<br>*[The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)* | A world model is a machine-readable map of an environment's entities and their relations — a service dependency graph over 25,000 repos, a per-user entity/priority graph, an asset-tag system describing a game, the symbolic 'local physics' of a microworld — queried by an agent, never rendered.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)* |

*Why it matters: The two definitions send budget in opposite directions: distributed GPU capacity, WebRTC and one-step distillation versus offline batch pipelines, graph construction and tag ontologies. A team that adopts the wrong definition of the term buys infrastructure that cannot serve its actual use case.*

### Should an environment's world model live in the model weights, or in an external artifact the agent reads at inference time?

| Position A | Position B |
|---|---|
| Train it in. A general video/world model focused on a domain yields hands, physics and micro-expressions as emergent properties rather than built features, and supervised learning over environment tokens gives the model a likelihood model of the environment — a native world model that RL alone would not produce.<br>*[Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | Compute it outside. Contextual understanding must be built before anyone asks the question, served as structured context; the codebase model is a separate machine-readable artifact; the game's world is an asset-tag system the LLM queries rather than re-derives.<br>*[From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)* |

*Why it matters: It decides whether improving an agent's grasp of your domain is a training problem (data, RL, environments, GPU) or a data-engineering problem (pipelines, graphs, offline recomputation). One talk splits the difference — intelligence-continual-learning-expertise argues both parametric and non-parametric learning are required and neither alone suffices — which is itself a rebuke to both pure positions.*

### For training and evaluating agents, should you learn a simulator of the environment or invest in running the real one?

| Position A | Position B |
|---|---|
| Learn to simulate it. Full back-end controllability lets you plant the answer, guarantee solvability, and work backwards from a known-reachable end state; for MCP tools, CLIs and sites you cannot program, a learned simulator is strictly better than the real system, and a controllable environment generates infinite robotics data.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md)* | Run the real thing. Ship real containerized GUI environments — 40GB images, warm pools autoscaled on GPU demand — and admit a task only after you have personally tried to break its evaluator, because reward-hackable environments make results untrustworthy.<br>*[Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* |

*Why it matters: Simulated environments are cheap and perfectly labeled but inherit the simulator's blind spots; real environments cost GPU idle time and heavy infrastructure but are the only place a genuine capability gap shows up. The choice determines whether your eval numbers survive contact with production.*

### Is pixel-generated world modeling ready to serve as the substrate for interactive experiences today?

| Position A | Position B |
|---|---|
| Yes. Real-time samples already beat batch samples on motion at roughly 1/100th the cost, avatar streams run 8-16 hours without drift at voice-model prices, and going from 16 to 30 FPS is a prioritization question, not a research one.<br>*[Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md)* | No — and it is a different medium regardless. Real-time 4K at 60 FPS with physics simulation is far off for world models, so interactive software should be built from deterministic systems over tagged assets with the LLM confined to authoring, not to rendering the world.<br>*[The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)* |

*Why it matters: It determines whether an interactive product is architected as a generated stream with an LLM in the loop or as a conventional deterministic runtime that an LLM configures — a decision that is extremely expensive to reverse.*

## Practical Guidance

**Do:**

- Scope a computer-use agent's observation to a single window rather than the full desktop — measured pass rate went 62% to 80% with 34% fewer tokens.
- Attempt accessibility-tree execution first and fall back to pixel-level background clicks only when it fails.
- Split the environment model across two clocks: a slow engine over a long window that learns durable structure, and a fast engine over a short recent window that recomputes live signals, with a thin slice recomputed at request time.
- Isolate each data source so one bad feed cannot poison the model, and fall back to last-verified context so the system degrades instead of failing.
- Build a machine-readable view of every service and how they connect before attempting multi-agent autonomous work on a large codebase.
- Grade context by proximity and editing focus the way rendering grades level-of-detail, instead of feeding the whole scene to the model.
- Try to break your own environment and its evaluator before admitting any task to the dataset; admit only tasks that survive.
- Score the agent's predicted next environment state, not just task completion, and keep forkable trajectories so any moment of the run can be replayed.
- Work backwards from a known-reachable end state, throw away the solution, and make the model rediscover it — supervision for free.
- Judge in hindsight after the full chain of events, or by polling several models, rather than instructing a judge in advance about what to disallow.
- Over-provision a warm sandbox pool with demand-based autoscaling: sandbox compute is 2-4x cheaper than the GPU time it keeps busy.
- For real-time video, train with a past-only attention mask, distill ~30 denoising steps to one, and route users to GPUs in their region for sub-100ms latency.

**Avoid:**

- Assuming a longer context window or a bigger prompt substitutes for a structured model of the user or environment.
- Waiting for a stronger frontier model to supply the missing environment model — capability was repeatedly identified as not the limiting factor.
- Handing agents human canvases (Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops) that force them to imitate human interaction patterns.
- Treating a flat leaderboard as a model problem: no model exceeded 30% reward on the CAD set and every full pass involved editing an existing artifact, with 0% from a blank one.
- Basing training for open-ended work on a handcrafted benchmark of a few hundred expert-built tasks.
- Building tasks that are too easy or too hard — RL's advantage signal needs separation across rollouts, so tasks must be calibrated to intermediate difficulty.
- Designing an environment without running a small RL job against it; some failures only appear once training starts.
- Reusing batch inference infrastructure for real-time serving — streaming, live-session memory and worldwide compute are new requirements, not tuning.
- Shipping a per-user world model as the primary experience for new users; the approach has a hard cold-start floor with no reliable history to reason from.
- Trusting human eyeballing as your consistency evaluation and calling the problem solved — nobody, including DeepMind, has a better answer yet.

## Notable Outliers

- Computer-use agents can edit an existing artifact but cannot construct one: 100% of the top agent's successes involved editing an existing schematic, and success from a blank schematic drops to 0%. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s))
- The agent's world model becomes measurable by asking it to predict the state of the computer at a forked point in its own trajectory. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [10:15](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=615s))
- Once raw intelligence crosses a threshold, more intelligence is unnecessary and the continual-learning algorithm becomes the binding constraint — current frontier models may already be past that threshold. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))
- A learned simulator is a better RL environment than the real production system, because full back-end controllability lets you plant the answer and guarantee the task is solvable. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [12:24](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=744s))
- The fast/slow two-engine design was not invented for this product — neuroscience calls it complementary learning systems and data infrastructure calls it lambda architecture. ([From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [10:29](https://www.youtube.com/watch?v=Btk8wDUVs74&t=629s))
- A human-focused world model generates continuously frame-by-frame for 8 hours with no reset and no noticeable drift, with a 16-hour run underway. ([Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [12:36](https://www.youtube.com/watch?v=z1dqv74SpUs&t=756s))
- Because generating code is nearly free, agents should build disposable micro worlds whose only purpose is to give a human a world model of their own system. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [14:49](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=889s))

## All Talks

- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [OpenClaw in Your Hand: Building a Physical AI Terminal](../talks/openclaw-in-your-hand-building-a-physical-ai-terminal.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)
- [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)

## Speakers

- [Ahmed Ahres](../speakers/ahmed-ahres.md)
- [Arturo Nunez](../speakers/arturo-nunez.md)
- [Dillon DuPont](../speakers/dillon-dupont.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Francesco Bonacci](../speakers/francesco-bonacci.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [George Cameron](../speakers/george-cameron.md)
- [James Russo](../speakers/james-russo.md)
- [Keegan McCallum](../speakers/keegan-mccallum.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Will Brown](../speakers/will-brown.md)
- [Yu Su](../speakers/yu-su.md)

