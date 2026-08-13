---
title: "Emulated: The Data for Fully Autonomous Software Engineers and Companies"
type: "talk"
slug: "emulated-the-data-for-fully-autonomous-software-engineers-and-companies"
track: "Posttraining & Midtraining"
org: "Emulated"
day: "Day 3 — Session Day 2"
room: "Track 9"
video_id: "zkX03APVj0M"
duration_sec: 992
word_count: 2563
speakers: ["Joseph Wang"]
---

# Emulated: The Data for Fully Autonomous Software Engineers and Companies

*Program title: Emulated: The data for fully autonomous software engineers and companies*

**Speakers:** [Joseph Wang](../speakers/joseph-wang.md)

**Org:** Emulated

**Track:** Posttraining & Midtraining &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 16m 32s

[Watch on YouTube](https://www.youtube.com/watch?v=zkX03APVj0M)

## Summary

Joseph Wang and co-founder Sid present Emulated, a data lab building environments that train AI agents on full-stack infrastructure work rather than isolated code changes. Their argument: frontier coding benchmarks like SWE-Bench Pro and Terminal Bench confine agents to a codebase, producing thousand-line PRs over 50–100 turns while skipping everything a real engineering org does — customer conversations, incident history, performance testing, rolling deployments, and years of ownership. They demo a containerized simulation of an etcd-style consensus cluster with flapping nodes, live traffic, and blast-radius constraints, then argue that single-node sandboxes structurally break down once you need real resource provisioning, front-end APIs, throttling/auth, deployment systems, DNS, and billing. Their proposed direction is multi-node sandboxes that provision real cloud infrastructure — a 'cloud in a box' — and the open problems that come with it (hours-long stack spin-up inside post-training rollouts, cost, a persistent sim-to-real gap). Worth watching if you care about RL environment design, agentic data generation, or why infra-domain agents lag application-layer ones.

## Key Points

- The speakers frame the model capability gap on infrastructure work as a data gap, not an architecture gap: models are only as good as the data, and capability has never regressed from adding more high-quality data.
- Current frontier coding benchmarks operate entirely inside the codebase, so agents never learn the PM work, approach exploration, performance testing, or multi-year infra ownership that human engineers do.
- Emulated packages whole software engineering companies into containerized environments including organizational context — projects, incidents, postmortems, and customer conversations — much of which is deliberately out of date, as in reality.
- Their example environment simulates a consensus cluster where the agent must handle network failures, data corruption, clock skew, failing and stale nodes, and hardware migration while live traffic keeps flowing and blast radius stays bounded.
- Single-node sandboxes hit a hard ceiling: you cannot meaningfully simulate EC2- or Cloud Run-style resource provisioning, VPCs, security groups, throttling, auth, DNS, cert management, telemetry, and billing inside one container.
- The proposed successor is a multi-node sandbox with access to real cloud resources — a 'cloud in a box' — which in turn destabilizes standard post-training pipelines built around homogeneous single-container rollouts.
- Open problems they name explicitly: spinning up an AWS Lambda-scale stack takes hours and doesn't fit a rollout budget, cost management is unsolved, and the sim-to-real gap persists even with real infrastructure because live customer traffic and scale-only failures are still missing.
- They start with infrastructure because it matches their own background (network infra, distributed databases, sandbox infra) and because infra companies have legible problem statements, unlike a pre-product-market-fit startup — while expecting vertical depth to transfer horizontally.

## Notable Quotes

> "Emulated is a data lab focused on increasing the reliability and autonomy of AI agents."
>
> — [0:14](https://www.youtube.com/watch?v=zkX03APVj0M&t=14s) &middot; *one-line statement of what the company is, useful for indexing*

> "we're headed towards a future where agents are able to perform useful work over longer and longer horizons with little to no supervision"
>
> — [0:14](https://www.youtube.com/watch?v=zkX03APVj0M&t=14s) &middot; *states the premise the whole talk builds on*

> "why is it that my model or my agent is so proficient at handling the application layer, but is struggles when it comes to reasoning through infrastructure complexities?"
>
> — [1:35](https://www.youtube.com/watch?v=zkX03APVj0M&t=95s) &middot; *the motivating question, and an empirical claim about where agents fail*

> "the gap in models is usually a gap in data. Models typically are only as good at as data is."
>
> — [2:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=140s) &middot; *the core thesis, stated as a general principle*

> "if you look at any of the frontier or recent benchmarks, like SweBench Pro, Terminal Bench, or something like Frontier Code and Deep Sweep, um the tasks only operate within the code base."
>
> — [2:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=140s) &middot; *names specific benchmarks and asserts a shared limitation*

> "the agent is given a pretty large uh task uh and over the course of 50 to 100 turns produces a couple thousand-line PR"
>
> — [3:08](https://www.youtube.com/watch?v=zkX03APVj0M&t=188s) &middot; *concrete numbers characterizing the current benchmark regime*

> "It doesn't do uh what a PM does with talking to customers, understanding their problems, what an engineer does with trying out different approaches, performing performance testing them, um and owning the underlying infra for the code base over the course of not just months, but years."
>
> — [3:08](https://www.youtube.com/watch?v=zkX03APVj0M&t=188s) &middot; *spells out exactly what current training data omits*

> "We've taken software engineering companies and we've put them into containerized environments."
>
> — [3:08](https://www.youtube.com/watch?v=zkX03APVj0M&t=188s) &middot; *the product claim in one sentence*

> "the agent also has to deal with issues that only appear at scale like network failures between distributed nodes, data corruption, and clock skew"
>
> — [3:59](https://www.youtube.com/watch?v=zkX03APVj0M&t=239s) &middot; *specifies the failure classes their environments inject*

> "environments are far more complex and long horizon than a simple code diff"
>
> — [3:59](https://www.youtube.com/watch?v=zkX03APVj0M&t=239s) &middot; *compact framing of the difficulty delta they are targeting*

> "you can make this pretty long horizon by just say doing multiple deployments instead of just one. But really what we're seeing is that this is not enough."
>
> — [6:21](https://www.youtube.com/watch?v=zkX03APVj0M&t=381s) &middot; *the pivot where they reject their own single-node approach*

> "even though you can use something like deterministic simulation to simulate network failures, it doesn't represent what you might run into if you're building an AWS-scale service"
>
> — [7:02](https://www.youtube.com/watch?v=zkX03APVj0M&t=422s) &middot; *takes a contestable side against deterministic simulation as a sufficient technique*

> "this is already where the single node sandbox starts breaking down. How do you provision resources within a single sandbox? You can't exactly simulate something like EC2 or Cloud Run, right?"
>
> — [7:55](https://www.youtube.com/watch?v=zkX03APVj0M&t=475s) &middot; *names the precise point at which the standard sandbox abstraction fails*

> "Beyond beyond a certain threshold, there is a critical mass at which sandboxing on a single node uh can only get you so far."
>
> — [10:01](https://www.youtube.com/watch?v=zkX03APVj0M&t=601s) &middot; *the talk's central architectural conclusion*

> "what this is is um a multi-node sandbox with access to real infra, real cloud resources. Uh we kind of put a cloud in box, so cloud box could be another name for this."
>
> — [10:46](https://www.youtube.com/watch?v=zkX03APVj0M&t=646s) &middot; *describes the proposed replacement architecture*

> "spinning up the entire stack for something like AWS Lambda takes hours. Um how do you fit that into a post training rollout?"
>
> — [12:13](https://www.youtube.com/watch?v=zkX03APVj0M&t=733s) &middot; *names a hard, quantified open problem in RL environment engineering*

> "the real world is very, very complex, um, and how we as a industry emulate the real world is incredibly contrived and low fidelity."
>
> — [12:56](https://www.youtube.com/watch?v=zkX03APVj0M&t=776s) &middot; *a blunt criticism of current industry practice in environment design*

> "emulated goal is really how do you make these agents own systems like this, uh, maybe beyond systems, entire companies, by emulating the real world with full fidelity."
>
> — [13:40](https://www.youtube.com/watch?v=zkX03APVj0M&t=820s) &middot; *states the company's end goal, including the leap from systems to companies*

> "We think that domain expertise is something that informs how high quality your data can be."
>
> — [14:29](https://www.youtube.com/watch?v=zkX03APVj0M&t=869s) &middot; *a position on what determines data quality in the current 'boutique' data market*

> "there's also lessons learned that going really vertical on a single domain like infrastructure do translate into other horizontal domains"
>
> — [15:56](https://www.youtube.com/watch?v=zkX03APVj0M&t=956s) &middot; *the transferability bet underlying their go-to-market sequencing*

## Positions

- Model weakness on infrastructure work is fundamentally a data gap rather than an architecture or capability-ceiling problem. ([2:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=140s), confidence: stated)
- Model capability has never regressed when more high-quality data is introduced. ([2:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=140s), confidence: stated)
- Frontier coding benchmarks such as SWE-Bench Pro, Terminal Bench, and Frontier Code operate only within the codebase and therefore cannot train or measure organizational and infrastructure ownership work. ([2:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=140s), confidence: stated)
- Single-node containerized sandboxes cannot represent real infrastructure work past a certain threshold, because resource provisioning like EC2 or Cloud Run cannot be simulated inside one node. ([7:55](https://www.youtube.com/watch?v=zkX03APVj0M&t=475s), confidence: stated)
- Deterministic simulation of network failures is insufficient to represent what an AWS-scale service actually encounters. ([7:02](https://www.youtube.com/watch?v=zkX03APVj0M&t=422s), confidence: stated)
- The future of agent training environments is environments that provision real infrastructure across multiple nodes. ([10:46](https://www.youtube.com/watch?v=zkX03APVj0M&t=646s), confidence: stated)
- Standard post-training pipelines are homogeneous — single containerized sandbox per rollout — and multi-node real-infra environments require rethinking that infrastructure. ([7:02](https://www.youtube.com/watch?v=zkX03APVj0M&t=422s), confidence: stated)
- A sim-to-real gap persists even when environments use real cloud resources, because live customer traffic and scale-dependent failures are still absent. ([12:13](https://www.youtube.com/watch?v=zkX03APVj0M&t=733s), confidence: stated)
- Founder domain expertise directly determines how high-quality generated training data can be, especially given the boutique nature of data today. ([14:29](https://www.youtube.com/watch?v=zkX03APVj0M&t=869s), confidence: stated)
- Infrastructure is the easiest domain in which to simulate an entire company because infra and dev-tools companies have clear, well-understood problem statements, unlike early-stage startups still seeking product-market fit. ([15:11](https://www.youtube.com/watch?v=zkX03APVj0M&t=911s), confidence: stated)
- Lessons from going vertically deep on infrastructure will transfer to other horizontal domains, justifying a depth-first then scale-out strategy. ([15:56](https://www.youtube.com/watch?v=zkX03APVj0M&t=956s), confidence: stated)
- Publicly sharing the architecture of their environments costs them little relative to the recruiting and community value of doing so. ([11:37](https://www.youtube.com/watch?v=zkX03APVj0M&t=697s), confidence: implied)
- Fully autonomous software engineering requires agents trained on organizational artifacts — tickets, postmortems, customer sentiment — that are often stale or inconsistent, not just clean code. ([4:47](https://www.youtube.com/watch?v=zkX03APVj0M&t=287s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [benchmark saturation](../concepts/benchmark-saturation.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [ontology design](../concepts/ontology-design.md)
- [post-training](../concepts/post-training.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [simulation environments](../concepts/simulation-environments.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)

