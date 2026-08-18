---
title: "Research to Reality: Bringing Frontier ML Research to Production"
type: "talk"
slug: "research-to-reality-bringing-frontier-ml-research-to-production"
track: "Robotics & World Models"
org: "Higharc"
day: "Day 3 — Session Day 2"
room: "Track 2"
video_id: "OXMMN-XbxwA"
duration_sec: 897
word_count: 2284
speakers: ["Deepak Pathak"]
---

# Research to Reality: Bringing Frontier ML Research to Production

*Program title: Frontier Robotics Research*

**Speakers:** [Deepak Pathak](../speakers/deepak-pathak.md)

**Org:** Higharc

**Track:** Robotics & World Models &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 2 &nbsp;|&nbsp; **Duration:** 14m 57s

[Watch on YouTube](https://www.youtube.com/watch?v=OXMMN-XbxwA)

## Summary

Vaidas Razgaitis, a senior research engineer on Higharc's labs team, treats the research-to-production handoff as a systems and process problem rather than a modeling problem. He argues that the core friction is bidirectional: software engineers who build production-grade systems don't know ML methodology, and ML researchers who track the latest papers have never owned production APIs. He proposes three levers — a 'research prototype taxonomy' document that makes a prototype legible to non-researchers, a Python mono repo of fully decoupled microservices (roughly one per researcher) behind a gateway, and a deliberate PR decomposition plan using stacked diffs for asynchronous review. He closes with diagnostic questions for each lever, so teams can locate where their own handoff is breaking down. Worth watching if you run an applied research team and want a concrete organizational template rather than modeling techniques.

## Key Points

- Higharc's labs team applies a wide range of ML — computer vision to parse hand-sketched floor plans, reasoning agents, custom transformers, and diffusion models for image generation — because the home-building and spatial-reasoning product domain is inherently multidisciplinary.
- The research-to-production gap is symmetric: platform and backend engineers lack familiarity with CV and LLM training methodology, while ML researchers have typically never been responsible for production-grade APIs.
- Higharc requires a 'research prototype taxonomy' document from every research prototype — essentially a technical design doc adapted for ML, covering domain context and data representations, business goal, type safety, persistence, system architecture, and the merge/decomposition plan.
- The domain-context section is written for a hypothetical engineer just hired from JP Morgan, forcing researchers to spell out domain-specific representations like party diagrams, circulation graphs, and latent space embeddings.
- Researchers are deliberately kept out of deep persistence-layer work; they document how far they got, and the database layer becomes the natural first entry point for software engineering help.
- The ML code lives in a separate Python mono repo of cleanly isolated, fully decoupled microservices at roughly a one-to-one researcher-to-microservice ratio, fronted by a gateway on a Docker bridge network that routes client API calls.
- Each microservice follows the same layered architecture — services holding business logic, wrapped in controllers, wrapped in API routers exposed as standalone FastAPI apps — with well-documented specs so coding agents can navigate the repo and accelerate researchers.
- Large monolithic prototypes are decomposed into stacked PRs via Graphite, which enables asynchronous review and lets specific subject matter experts be tapped for the slices relevant to them.
- The taxonomy document's architecture and type mapping directly informs the decomposition strategy, so the three levers are coupled rather than independent.
- The proposed diagnostics: unclear where staff should concentrate effort signals a legibility problem; fighting old abstractions when adding research code signals you've outgrown the repo; inability to estimate delivery timelines points upstream to either coordination or the codebase.

## Notable Quotes

> "we need to start working with software engineers, let's say platform engineers, infrastructure engineers, back-end engineers who are very familiar with building robust and production-grade code, but are likely not familiar with the methodology and research in computer vision, in training your own LLMs"
>
> — [1:03](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=63s) &middot; *States one half of the two-sided skills gap that motivates the entire talk.*

> "you kind of have the flip side problem with our uh ML researchers who are very up-to-date with the latest papers and can uh pull together these concepts in novel and creative ways to develop new features, but they have not really worked as software engineers typically where they've been responsible for production grade APIs"
>
> — [1:03](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=63s) &middot; *Completes the symmetry — the researchers are the other half of the handoff problem.*

> "we look at this basically as a systems and process problem and I want to kind of zero in on three main focus areas that you can use to improve this the velocity of teams that that are bringing research into production"
>
> — [2:10](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=130s) &middot; *The talk's central framing claim: this is org design, not modeling.*

> "we have a very analogous document um that we require from all research prototypes that we call the research prototype taxonomy document"
>
> — [4:02](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=242s) &middot; *Names the concrete artifact and states it is mandatory, not optional.*

> "I like to say kind of picture a software engineer who just we just hired from JP Morgan. What are the kind of uh specific lingos and and data representations that they might need to know before jumping into this project"
>
> — [4:47](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=287s) &middot; *A memorable, reusable heuristic for calibrating how much domain context to write down.*

> "what is the type contract between our core product repository and this machine learning repo? How are those types shared and how do they stay in sync?"
>
> — [5:31](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=331s) &middot; *Identifies the specific cross-repo interface that the design doc must pin down.*

> "this is an area where uh we think it's probably best not to have our researcher spend too much time in the persistence layer and just map out how far they got and this is a great first entry point once we start bringing in software engineering help on the project"
>
> — [5:31](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=331s) &middot; *A specific, contestable division of labor — researchers should stop short of the database.*

> "It's all AI ML stuff and it's basically a mono repo of uh cleanly isolated and fully decoupled microservices."
>
> — [7:06](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=426s) &middot; *The core architectural decision: mono repo containing decoupled services, separate from the product repo.*

> "it's pretty much a one-to-one researcher to microservice ratio. So, we find that works really well."
>
> — [7:06](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=426s) &middot; *A concrete, unusual staffing-to-architecture ratio others can compare against.*

> "we have a kind of gateway that that guards requests um and it's all in one Docker Bridge network"
>
> — [7:06](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=426s) &middot; *Describes the routing and isolation boundary in front of the microservices.*

> "we tend to have like some really um really cleanly documented specs uh so that agents can navigate these repositories and help accelerate our ML researchers as much as possible"
>
> — [7:55](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=475s) &middot; *Ties documentation quality directly to coding-agent effectiveness, a design goal beyond human readers.*

> "Then we wrap that business logic with controllers. Um then we put API routers around those and expose them in FastAPI applications. And each of those microservices is a standalone application."
>
> — [8:42](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=522s) &middot; *The concrete layered template every service repeats.*

> "we use Graphite um for kind of stack diffs to then uh decompose these large monolithic prototypes that have been proven out um and then get the right eyes on on review to make sure that these are ready for production"
>
> — [10:51](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=651s) &middot; *Names the specific tooling and the reason for it — routing review to the right experts.*

> "We really like Graphite because it allows for asynchronous review, right? I could be working on a PR all the way up here while a domain specialist is still reviewing a different PR."
>
> — [11:38](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=698s) &middot; *States the concrete throughput tradeoff that justifies stacked diffs.*

> "once we've mapped out these layers, these the architecture, what kind of persistence there is in the types, that tends to inform uh your decomposition strategy on how to bring it into the into the mono repo"
>
> — [11:38](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=698s) &middot; *Explains why the design doc and the PR plan are coupled rather than separate exercises.*

> "is it possible that maybe you've started to outgrow that code base and that system architecture, and every time you bring in new research concepts, you're fighting these old abstractions and having headaches from limitations of your repository"
>
> — [13:15](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=795s) &middot; *The clearest diagnostic signal offered for when the repo itself is the bottleneck.*

> "are you able to consistently estimate the timelines and delivery dates for moving research concepts into your repository?"
>
> — [13:15](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=795s) &middot; *Proposes predictability of delivery as the measurable output metric of the whole process.*

> "if you're having issues here, it probably points to the stream issues, either in uh how this research is being coordinated and handing off, or perhaps the code base that's hosting it"
>
> — [14:09](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=849s) &middot; *Argues decomposition failures are downstream symptoms, not root causes.*

## Positions

- Getting frontier research into production is fundamentally a systems and process problem, not a modeling or research problem. ([2:10](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=130s), confidence: stated)
- Every research prototype should be required to produce a written taxonomy/design document before software engineers are brought onto the project. ([4:02](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=242s), confidence: stated)
- A research design document needs ML-specific sections beyond a standard TDD — namely domain context and data representations, plus the business rationale for the ML tool. ([4:02](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=242s), confidence: stated)
- ML researchers should not spend much time on the persistence layer; they should document how far they got and hand it off as the first task for software engineers. ([5:31](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=331s), confidence: stated)
- ML/research code belongs in a separate repository from the core product repo, with an explicit type contract keeping the two in sync. ([5:31](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=331s), confidence: stated)
- A one-to-one researcher-to-microservice ratio with fully decoupled services works well because it lets each research initiative iterate independently. ([7:06](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=426s), confidence: stated)
- Clients should not call ML microservices directly; requests should route through a gateway. ([8:42](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=522s), confidence: stated)
- Cleanly documented specs are worth writing partly so coding agents can navigate the repo and accelerate ML researchers. ([7:55](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=475s), confidence: stated)
- Stacked diffs are superior to a single large PR for research productionization because they enable asynchronous review and let you tap specific subject matter experts per slice. ([11:38](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=698s), confidence: stated)
- Consistent skeletal structure across microservices makes it easy to verify projects are growing along software engineering best practices. ([9:25](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=565s), confidence: stated)
- If a team cannot reliably estimate delivery dates for moving research into the repo, the root cause lies upstream in research coordination or in the codebase, not in the decomposition step itself. ([14:09](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=849s), confidence: stated)
- Repeatedly fighting existing abstractions when landing new research concepts is a signal that the team has outgrown its codebase and system architecture. ([13:15](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=795s), confidence: implied)

## Concepts

- [agent-readable codebases](../concepts/agent-readable-codebases.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [spec-driven development](../concepts/spec-driven-development.md)
- [task decomposition](../concepts/task-decomposition.md)

