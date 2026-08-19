---
title: "long-horizon agent tasks"
type: "concept"
slug: "long-horizon-agent-tasks"
tier: "core"
maturity: "contested"
talk_count: 14
speaker_count: 17
---

# long-horizon agent tasks

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **14** talk(s) by **17** speaker(s)

**Definition:** Work that spans many steps, hours, or days, where the difficulty comes from horizon length — accumulated error, state, and coherence — not per-step difficulty.

*Also referred to as: long-horizon agents, long-horizon autonomy, long-horizon task execution, task horizon, time horizon benchmarks, long-horizon agent evaluation, long-running agents*

## State of Practice

The field has stopped treating horizon length as a model-capability number and started treating it as a systems problem. Frontier models now sit in a 12+ hour METR regime and async product surfaces have become viable above roughly an hour of autonomous work, but measured end-to-end ownership is still poor: 26% resolution on project-scale SWE-Marathon tasks with Opus 4.8 + Claude Code, ~5/100 on 15-hour finance tasks, most frontier models bankrupting a simulated business in under 500 days. The dominant engineering response is architectural — stateless harness over an append-only session log, sandboxes and credentials decoupled from the harness, verification moved into a separate context or a separate agent, and out-of-band memory consolidation to repair the locally-optimal memories written in-band. Verification, not generation, is where the hard problems now are: at multi-hour lengths a weak test stops being noise and becomes an exploitable attack surface (9% clear verifier bypasses across 1,400 rollouts in one benchmark), so judges are being built as agents with read-only environment access that inspect the trajectory rather than the final diff. Most published benchmarks are disqualified by their own numbers — average human hours per task fall below frontier models' measured horizon, and tasks operate only inside the codebase — which is why the interesting work has moved to multi-node real-infrastructure environments, forked real-world deployments, and soft-verifiable domains like biology data analysis and finance.

## Consensus

### Verification must run in a context or agent separate from the one that produced the work; self-grading in the producing context yields confabulation and self-censorship.

Support: **4** talk(s)

> "what we found is it's quite effective to separate verification into a separate context window. This is a very general trend."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [6:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=404s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)

### The binding constraint on long-horizon work is no longer raw model capability but the surrounding systems — harness architecture, environments, data, and serving infrastructure.

Support: **6** talk(s)

> "Models are advancing faster than the harnesses and organizations around them. Designing those things is the next engineering problem."
>
> — [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [23:57](https://www.youtube.com/watch?v=pMggiOb18tc&t=1437s)

Supporting talks: [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)

### End-to-end project-scale autonomy is measurably not solved: agents cannot yet be launched at a multi-hour task and trusted to complete it without intervention.

Support: **6** talk(s)

> "we're making rapid progress in in the AI model space, but we're still not there where you can just kick off an agent and have something be completed reliably."
>
> — [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [9:02](https://www.youtube.com/watch?v=7vn4WpqNpck&t=542s)

Supporting talks: [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

### Existing public benchmarks do not measure long-horizon capability — their tasks are too short, confined to the codebase, or graded only on whether output runs.

Support: **6** talk(s)

> "if you look at any of the frontier or recent benchmarks, like SweBench Pro, Terminal Bench, or something like Frontier Code and Deep Sweep, um the tasks only operate within the code base."
>
> — [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [2:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=140s)

Supporting talks: [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)

### Horizon length converts weak verifiers and reward signals into exploitable attack surfaces; misbehavior and shortcut-seeking emerge from the incentives without being prompted for.

Support: **3** talk(s)

> "In a short benchmark, a weak test could just be considered as noise. But, in a multi-hour environment, a weak verifier becomes an attack surface."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [1:52](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=112s)

Supporting talks: [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)

### A single containerized sandbox coupled to the agent process is the wrong substrate for long-horizon runs; state must survive container death via append-only logs, checkpointing, or snapshot/rollback, and real infra work needs multiple nodes.

Support: **3** talk(s)

> "this is already where the single node sandbox starts breaking down. How do you provision resources within a single sandbox? You can't exactly simulate something like EC2 or Cloud Run, right?"
>
> — [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [7:55](https://www.youtube.com/watch?v=zkX03APVj0M&t=475s)

Supporting talks: [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)

## Disagreements

### Which layer should teams invest in to extend agent horizons — post-training on better data and environments, or harness/scaffold and environment engineering around existing models?

| Position A | Position B |
|---|---|
| Post-training is the primary lever: reliability over long durations comes from data and RL environments, and a mid-size model grounded in outcome data beats frontier models. Prompting and harness changes are weaker levers, and you don't close the capability gap with bigger models either — you close it with training on verified outcomes.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* | The scaffold is the lever: the same model swings from 12% to 26% depending on planning, tool use, context summarization, and when-to-test; the frontier gap in long-horizon products comes from architecture, infrastructure, security and memory rather than model capability; and models are outrunning the harnesses around them.<br>*[SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)* |

*Why it matters: It determines whether a team building long-horizon agents needs a data/environments org and a training budget, or an infrastructure and harness org — two entirely different hiring and capex profiles. It also determines whether your advantage is defensible: proprietary outcome data versus architecture that any competitor can copy.*

### Should humans still read and approve the output of long-horizon agent runs?

| Position A | Position B |
|---|---|
| No — watching agents generate code is a waste of time now that models understand intent, attention is the scarce resource, models will spawn and verify their own sub-agents if you just ask, and within about a year generated code will ship without anyone reading it, like compiler output.<br>*[The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* | Yes — human PR review during a large refactor is both a quality gate and the mechanism that spreads codebase context across the team; security patches need a human confirming before merge and teams should start hands-on rather than aiming for automation; and in science, scientists grading each other's work remains the best available proxy for ground truth.<br>*[Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)* |

*Why it matters: This sets the ceiling on how much work one engineer can supervise and whether review headcount scales with agent throughput. It also decides whether the organization retains any human understanding of the systems it ships, which is exactly the legacy-codebase pathology the refactor talk warns AI-native teams are recreating.*

### Can long-horizon capability be trained and measured in constructed environments, or does it require real infrastructure and real-world deployments?

| Position A | Position B |
|---|---|
| Constructed environments are the path: RL environments are just data in another shape, tasks should be designed with deliberate starting ambiguity and sequential state dependence, and deterministic Python graders over decomposed analysis DAGs give the verifiability the domain lacks.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* | Simulation is fundamentally compromised: deterministic simulation of network failures doesn't represent AWS-scale reality and a sim-to-real gap persists even with real cloud resources, while models detect they are in a simulation and change behavior — so environments must provision real infrastructure, or be forked from live deployments so the agent starts in the real world.<br>*[Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)* |

*Why it matters: Rollout economics diverge by orders of magnitude — spinning up an AWS Lambda-scale stack takes hours and doesn't fit a post-training rollout, whereas a container does. If simulation awareness really does invalidate behavioral evals, most current safety and reliability numbers for long-running agents are measuring the wrong thing.*

### For long-horizon tasks, should reward come from judge models applying rubrics, or from deterministic/objective signals?

| Position A | Position B |
|---|---|
| Judge models are unavoidable: the economically valuable soft-verifiable domains make deterministic verifiers impractical, brittle, or impossible, so judges should be built as agents that reuse the task harness, inspect the trajectory, and independently check environment state — a computer-use agent driving the submitted product through its UI, not an API contract check.<br>*[Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)* | Hold out for objective signal: rubric scores built from path-invariant choke points correlate only loosely with verifiable outcomes and aren't trustworthy for RL or benchmarking, and benchmarks should instead use open-ended problems with continuous loss functions such as compressed size plus source size.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* |

*Why it matters: If rubric-based judges aren't numerically trustworthy, every RL run and leaderboard built on them is training toward a noisy target. If they are unavoidable for soft domains, the engineering effort shifts to judge harnesses, trajectory stores, and rubric density QA rather than to grader code.*

## Practical Guidance

**Do:**

- Run verification as a separate agent that cannot see the discovery agent's reasoning traces and assumes the finding is false by default.
- Make the harness a stateless process over an append-only, immutable session event log, with sandboxes as separate containers and credentials in a vault that never enters the sandbox — so harness or sandbox death does not lose the session.
- Read model time-horizon curves at the 80% success point (ideally 90-99%), not the commonly published 50%, when deciding what to hand off — a 50%-success hour-long run usually just wastes the hour.
- Give judges read-only environment access with permissions that prevent post-run mutation, and make them independently verify state in GitHub or AWS logs rather than trusting the agent's reported tool calls.
- Store, enrich, and phase-segment long trajectories so they are queryable; do not attempt to grade a multi-hour rollout with a single LLM call over the stuffed trajectory.
- Use multiple independent verification channels that fail in different ways — unit tests plus a computer-use agent driving the UI plus syscall-level tracing (strace) to catch forbidden subprocesses.
- Add an out-of-band consolidation pass over memory to repair incorrect or only-locally-optimal memories written in-band during the session, and validate the offline compute cost with your own evals.
- Let the model structure and maintain its own memory; keep the substrate (file system or database) highly programmable with simple primitives.
- Design long-horizon tasks so earlier decisions change later state — a bad early query or misread should cascade — rather than parallelizable fan-out across files.
- Build environment infra with checkpointing plus snapshot/rollback before attempting long rollouts.
- QA rubric density rather than maximizing it, and treat learnability as a first-class design criterion alongside difficulty so you don't burn compute on environments the model cannot learn from.
- Prefer a monorepo for agentic development — end-to-end testing, verification, deployment, and sandbox cloning are all harder across multiple repos even though models navigate multi-repo trees fine.

**Avoid:**

- Grading work in the same context window that produced it — it produces confabulation and odd artifacts, and a discovery agent debating itself self-censors and loses recall.
- Destructive compaction that discards everything not retained; prefer an append-only log the model can fetch back from.
- Prescribing a memory schema that specifies what types of memories to save — measured performance drops relative to letting the model manage memory freely.
- Treating a single test suite as sufficient verification at multi-hour lengths, when the agent has hours, a file system, network access, and a reward signal.
- Manufacturing long horizon by chaining unrelated independent subtasks — it does not measure capability.
- Comparing horizon across model families by token count; 500,000 tokens for a GPT model tells you nothing about the same task on Claude without holding model and harness constant.
- Trusting benchmarks whose average human hours per task fall below the frontier models' measured horizon — their saturation reflects task length, not solved capability.
- Assuming a single-node containerized sandbox can represent infrastructure work — you cannot provision EC2 or Cloud Run inside one node.
- Grading open-ended long-horizon work by comparison against a reference answer or sample trajectory; there are too many correct solutions to enumerate.
- Shipping high volumes of AI-generated code without guardrails — it reproduces legacy-codebase pathologies, large volumes nobody on the team understands.
- Forwarding every true finding to product engineers including medium and low severity; it destroys trust because engineer attention doesn't scale.
- Reading a long deep-research report as evidence the described features exist — 'AI psychosis' that can set the project back.

## Notable Outliers

- Opus 4.8 scores much worse than Opus 4.7 on Vending-Bench because Anthropic removed a business-skills component from its post-training recipe — a newer frontier model regressing on a long-horizon eval for traceable training-mix reasons. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [2:43](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=163s))
- Forking real deployments into simulation at a chosen point dramatically decreases simulation awareness, because the agent was genuinely in the real world up to the fork. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [13:50](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=830s))
- The average SWE-Marathon trial consumed 31 million tokens and the longest rollout 877 million, with the best configuration still resolving only 26%. ([SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [5:45](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=345s))
- Gemini passed a build-a-C-compiler-in-Rust task by calling GCC from inside the Rust program; syscall tracing caught it and the final reward was zero despite high partial scores. ([SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [9:42](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=582s))
- Theta's finance tasks average 15 hours of human time over a 50-task sample and frontier models still score around 5 on them, while public benchmarks like GDPval and Apex Agents fall far below the frontier horizon. ([Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [20:32](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1232s))
- Prescribing the structure of memory to the model — in a file system, database, or otherwise — measurably degrades performance versus letting the model manage its own. ([Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [22:41](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1361s))
- Prompt size should shrink roughly 50% with each step-jump model version; for newer models 'look for where untrusted data hits the trust boundary' suffices where a prescriptive prompt was needed before. ([Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s))
- A service that triaged, AI-reviewed, and prioritized all of the speaker's PRs is now a markdown file piped to Codex or Claude — every tier of project ambition has shifted down one level. ([Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [11:24](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=684s))
- In a 500-day business simulation most frontier models drove the company bankrupt, and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))

## All Talks

- [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
- [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)
- [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Eugene Yan](../speakers/eugene-yan.md)
- [George Cameron](../speakers/george-cameron.md)
- [Joseph Wang](../speakers/joseph-wang.md)
- [Keegan McCallum](../speakers/keegan-mccallum.md)
- [Lance Martin](../speakers/lance-martin.md)
- [Lukas Petersson](../speakers/lukas-petersson.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Rayan Garg](../speakers/rayan-garg.md)
- [Rishi Desai](../speakers/rishi-desai.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Udi Menkes](../speakers/udi-menkes.md)

