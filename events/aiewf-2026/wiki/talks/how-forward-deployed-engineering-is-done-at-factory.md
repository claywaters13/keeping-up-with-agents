---
title: "How Forward Deployed Engineering is done at Factory"
type: "talk"
slug: "how-forward-deployed-engineering-is-done-at-factory"
track: "Forward Deployed Engineering"
org: "Factory"
day: "Day 2 — Session Day 1"
room: "Track 8"
video_id: "wpOA-UXynoM"
duration_sec: 1281
word_count: 3825
speakers: ["Eno Reyes"]
---

# How Forward Deployed Engineering is done at Factory

**Speakers:** [Eno Reyes](../speakers/eno-reyes.md)

**Org:** Factory

**Track:** Forward Deployed Engineering &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 21m 21s

[Watch on YouTube](https://www.youtube.com/watch?v=wpOA-UXynoM)

## Summary

Eno Reyes, co-founder and CTO of Factory, describes how his company structures forward deployed engineering ('deployed engineers') differently from the Palantir-era playbook. He argues against doing professional-services work on a customer's behalf, positioning deployed engineers instead as the 'tip of the spear' — an information stream from large enterprise customers back into the product. The core technical thesis is the 'software factory': an instrumented pipeline from external signals through planning, code changes, validation, and deploy, where the goal is flow from signal to deploy uninterrupted by humans while humans engineer and maintain the system itself. He makes agent readiness — the density of deterministic validation loops in a codebase — the gating variable for autonomy, drawing an explicit analogy to dense reward in model post-training. Useful for anyone building enterprise AI deployment teams or trying to understand why agent rollouts stall on verification infrastructure rather than model capability.

## Key Points

- Factory deliberately refuses professional-services engagements (e.g. doing a customer's codebase migration for them) because it generates revenue without making the product better or scaling the business.
- Deployed engineers are positioned as the 'tip of the spear': their job is to route ground-truth information from the largest customers' engineering leadership and tactical engineers back into the product for rapid adjustment.
- The 'software factory' is a feedback loop where outside signals (bug reports, Slack threads, exec mandates) are triaged into plans, converted into code changes, passed through validation, deployed, and then generate new signals — a loop most organizations instrument very poorly.
- Model independence and ownership of traces and data are presented as prerequisites for a software factory; building it inside a vendor-locked, single-model solution creates cost and control risk.
- 'Agent readiness' is defined as a measure of how many deterministic validation loops (linters, type checkers, security scans, end-to-end tests) exist in a codebase, and it directly gates how long agents can run unattended.
- The quality of long-running agent harnesses is directly proportional to how well work can be validated, which mirrors how models receive dense reward during post-training.
- Humans move from directly manipulating software to maintaining the system that builds software — an abstraction shift Reyes says most engineers, even thoughtful ones, will struggle with; DevEx people and rapidly-technical PMs adapt best.
- Factory's own codebase runs at roughly 15–20% autonomy with an autonomy ratio in the upper 80s, and some customer codebases are more autonomous because they operate under more constrained conditions.
- Reyes uses Disney's Epcot as a cautionary analogy: the demonstration deployment must be advanced enough to inspire imitation but not so advanced that the org dismisses it as a theme park irrelevant to their reality.

## Notable Quotes

> "at least at Factory, we definitely do not want to be doing professional services work on behalf of a customer"
>
> — [2:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=177s) &middot; *States the central strategic boundary that distinguishes Factory's model from the Palantir-era playbook.*

> "that is a great way way get I'd say a decent amount of revenue, but I don't think that that's the way that you can scale a business out enormously"
>
> — [3:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=221s) &middot; *Gives the business rationale for refusing services work, not just a philosophical preference.*

> "we need deployed engineers to be the tip of the spear of the product"
>
> — [3:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=221s) &middot; *The talk's one-line definition of the role.*

> "there's this implicit process that every organization in the world sits on top of, where signals from the outside world flow in on one side"
>
> — [5:04](https://www.youtube.com/watch?v=wpOA-UXynoM&t=304s) &middot; *Sets up the software factory framing that structures the rest of the talk.*

> "this implicit feedback loop is instrumented very poorly, to be honest, at most organizations"
>
> — [5:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=341s) &middot; *The diagnosis that motivates the entire product thesis.*

> "that does not mean that humans are not a part of engineering this system, right? But it is that the flow of signal to deploy is uninterrupted by a human"
>
> — [6:40](https://www.youtube.com/watch?v=wpOA-UXynoM&t=400s) &middot; *Precise definition of the autonomy target, distinguishing it from human replacement.*

> "if you also don't own the traces, the data, everything that flows through your software factory, um then you're probably going to be in trouble as you start to want to evolve your software factory"
>
> — [7:32](https://www.youtube.com/watch?v=wpOA-UXynoM&t=452s) &middot; *States the data-ownership position that others building on closed platforms would dispute.*

> "One of our deployed engineers jokes that you could run Droid in a submarine if you wanted to. And that's that's honestly true."
>
> — [8:13](https://www.youtube.com/watch?v=wpOA-UXynoM&t=493s) &middot; *Memorable framing of the air-gapped deployment requirement in regulated industries.*

> "there needs to be an ROI or an outcome story that is extremely clear from the beginning"
>
> — [8:59](https://www.youtube.com/watch?v=wpOA-UXynoM&t=539s) &middot; *Names what the deployed engineer is accountable for beyond technical installation.*

> "most organizations do not have an autonomy maturity model. They do not have a road map, they don't have a conception of what it means to truly build an autonomous software organization"
>
> — [9:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=581s) &middot; *Identifies the gap deployed engineers are meant to fill.*

> "the engineers at a company go from directly manipulating software to directly maintaining and managing a system that builds software"
>
> — [10:20](https://www.youtube.com/watch?v=wpOA-UXynoM&t=620s) &middot; *The clearest statement of what happens to human engineering roles.*

> "I would argue that in fact most people, even very thoughtful software engineers, will have a learning curve in trying to shift"
>
> — [10:20](https://www.youtube.com/watch?v=wpOA-UXynoM&t=620s) &middot; *A contestable claim about who adapts to agent-era engineering.*

> "What agent readiness really is is it's a measure of how many of these deterministic validation loops are present inside of your code base"
>
> — [12:23](https://www.youtube.com/watch?v=wpOA-UXynoM&t=743s) &middot; *Defines the talk's key operational metric.*

> "the quality of the output of these very long-running harnesses of advanced agents is directly proportional to the degree to which you can validate their work"
>
> — [12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s) &middot; *The central causal claim linking verification infrastructure to agent performance.*

> "for I'd say maybe 30 to 40% of the low-hanging fruit, you click droid, please fix all of this and it'll go in and it'll fix it"
>
> — [12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s) &middot; *A concrete number on how much agent-readiness work is automatable.*

> "if you can frame any problem as the set of verification uh systems that need to validate it, then you can solve that problem with AI today"
>
> — [14:15](https://www.youtube.com/watch?v=wpOA-UXynoM&t=855s) &middot; *The strongest and most falsifiable claim in the talk.*

> "if your code base isn't agent ready, you won't see any of the success of the most capable AI systems in the world today"
>
> — [15:21](https://www.youtube.com/watch?v=wpOA-UXynoM&t=921s) &middot; *Shifts blame for failed agent rollouts from model capability to environment preparation.*

> "Less so solving the problem, more so preparing the environment for verification of the problem."
>
> — [15:21](https://www.youtube.com/watch?v=wpOA-UXynoM&t=921s) &middot; *Compresses the talk's advice on where enterprises should invest.*

> "Models need dense reward. These verification signals form the basis of that reward that they use to keep them on track over a long-term goal-directed problem."
>
> — [16:01](https://www.youtube.com/watch?v=wpOA-UXynoM&t=961s) &middot; *Connects the practical validation argument to model training mechanics.*

> "if you build too much of an advanced example, then people will say, "That's a theme park. That is not at all how the rest of the world works.""
>
> — [17:23](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1043s) &middot; *The Epcot analogy's punchline — a real tradeoff in deployment strategy.*

> "we ourselves have roughly 15 to 20% of what we call like autonomy, and our autonomy ratio is like in the upper 80%, which means the ratio of actions done by humans to AI systems before interruption"
>
> — [18:13](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1093s) &middot; *The only hard self-reported metrics in the talk.*

> "we do not yet have validators that can validate some of the hard visual problems of a like terminal based harness"
>
> — [18:52](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1132s) &middot; *An honest limit case showing where the verification thesis currently breaks down.*

> "each like stage of the SDLC that Droid has, we think is a billion-dollar business. Like just code review, just incident response, just QA, just testing."
>
> — [19:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1181s) &middot; *A strong market claim about SDLC-stage unbundling.*

## Positions

- Deployed engineers should not perform professional-services work on a customer's behalf, because it does not improve the product and does not scale as a business. ([2:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=177s), confidence: stated)
- The correct role of a deployed engineer is to act as an information conduit from the customer's engineering org back into the product ('tip of the spear'). ([3:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=221s), confidence: stated)
- A software factory must be built by the organization, not bought off the shelf. ([6:40](https://www.youtube.com/watch?v=wpOA-UXynoM&t=400s), confidence: stated)
- Building a software factory on a vendor-locked, single-model platform is both expensive and strategically risky because the model provider dictates what you can build. ([6:40](https://www.youtube.com/watch?v=wpOA-UXynoM&t=400s), confidence: stated)
- Agent autonomy is gated by the density of deterministic validation loops in a codebase, not by model capability. ([12:23](https://www.youtube.com/watch?v=wpOA-UXynoM&t=743s), confidence: stated)
- Output quality of long-running agents is directly proportional to how well their work can be validated. ([12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s), confidence: stated)
- Any problem that can be framed as a set of verification systems can be solved with AI today. ([14:15](https://www.youtube.com/watch?v=wpOA-UXynoM&t=855s), confidence: stated)
- Roughly 30-40% of agent-readiness fixes are low-hanging fruit an agent can do automatically; the remaining ~60% require human workflow changes. ([12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s), confidence: stated)
- Most software engineers, including strong ones, will face a significant learning curve moving from writing software to managing systems that write software. ([10:20](https://www.youtube.com/watch?v=wpOA-UXynoM&t=620s), confidence: stated)
- DevEx engineers, technically-inclined product managers, and people from high-quality dev-environment teams are best suited to deployed engineering roles. ([11:00](https://www.youtube.com/watch?v=wpOA-UXynoM&t=660s), confidence: stated)
- Highly constrained internal tools will reach 100% autonomy before general product codebases. ([18:52](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1132s), confidence: stated)
- A demonstration deployment that is too far ahead of the org's current practice will be dismissed as irrelevant rather than copied. ([17:23](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1043s), confidence: stated)
- Each individual stage of the SDLC (code review, incident response, QA, testing) is independently a billion-dollar market. ([19:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1181s), confidence: stated)
- Human advantages in visual perception and outside-world context will remain the source of work in building autonomous systems. ([18:52](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1132s), confidence: implied)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent-readable codebases](../concepts/agent-readable-codebases.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [forward deployed engineering](../concepts/forward-deployed-engineering.md)
- [model portability](../concepts/model-portability.md)
- [reward design](../concepts/reward-design.md)
- [sovereign and air-gapped deployment](../concepts/sovereign-and-air-gapped-deployment.md)

