---
title: "WTF Is the Context Layer? The Missing Infrastructure for Production Agents"
type: "talk"
slug: "wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents"
track: "Context Engineering"
org: "Atlan"
day: "Day 3 — Session Day 2"
room: "Track 8"
video_id: "8G_1-3IO4ZQ"
duration_sec: 1253
word_count: 3374
speakers: ["Prukalpa Sankar"]
---

# WTF Is the Context Layer? The Missing Infrastructure for Production Agents

**Speakers:** [Prukalpa Sankar](../speakers/prukalpa-sankar.md)

**Org:** Atlan

**Track:** Context Engineering &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 20m 53s

[Watch on YouTube](https://www.youtube.com/watch?v=8G_1-3IO4ZQ)

## Summary

Prukalpa Sankar, founder of Atlan, argues that model intelligence has 1,000x'd over the last decade while 'context' — the situated knowledge of a business — has barely moved, and that this gap explains why so few AI use cases reach production. She uses an analogy of a human analyst (Maya) to decompose business context into knowledge, expertise/playbooks, and norms, then walks through two eras of Atlan's own internal agent buildout: bootstrapping single-purpose agents (which hit context-engineering cost, siloed memory, and untraceable failures) and then a shared 'company brain' context layer feeding general-purpose agents (which hit skill dependency drift, unclear ownership, and security problems). Her core proposal is that context needs to be managed like code — versioning, dependency management, ownership, quality and security posture — essentially a 'GitHub for context.' She also argues traces should be mined by a specialized harness to build compounding learning loops, and that context can be reverse-constructed from existing business systems as a starting point. The closing claim: in a world where competitors share the same models, context is the differentiating IP.

## Key Points

- Model intelligence has improved roughly 1,000x in a decade (2x in the last six months), but real-world usefulness has not followed — only 1 in 5 AI use cases reaches production and 56% of CEOs report zero financial benefit from AI.
- Performance is a function of intelligence plus context, mirroring the human world where only 10% of job performance variance is explained by IQ.
- Business context decomposes into three parts: knowledge (definitions, metric semantics, time windows), expertise (diagnostic playbooks learned on the job), and norms (persona scoping, who's allowed to decide what).
- Atlan's first era of bootstrapped single-purpose agents failed at scale: building an agent took five minutes but giving it accurate business context took forever, agents lived on isolated islands with separate memory systems, and failures were hard to trace back to model vs. agent vs. context.
- Frequent agent-framework churn (Relevance → Google ADK → Glean → Claude Code → 50/50 Claude and Codex) trapped context inside each successive system, making context portability a first-class requirement.
- The second era used a shared context layer — a 'company brain' of data graph, skills library, semantics/metrics, and org entities — with domain experts authoring skills; the marketing team alone produced ~300 skills and 40 agents in six months.
- Shared context introduced code-like problems: skill dependency chains (competitive intel → category positioning → sales battle cards) break downstream when upstream skills self-improve, ownership of skill quality is unclear, and security was poor with hardcoded secrets in .env files and downloaded public skill repos.
- Sankar proposes a 'GitHub for context' with lifecycle management, versioning, approvers/maintainers/contributors, quality and security posture management, plus a trace-reading harness that feeds approve/reject decisions back into a compounding learning loop.
- As a starting point for disparate businesses, connect systems like Salesforce, HubSpot, the data warehouse, and the application layer and reverse-construct how they relate, since context is lost at every hop between them.

## Notable Quotes

> "There is no doubt that the models are getting exponentially smarter by the day. 2 years ago they couldn't pass the bar. Today, if they were to take the bar, it was they're the top 1% of test scorers. On the other hand, they're not exponentially more useful by any benchmark."
>
> — [1:57](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=117s) &middot; *States the central gap the talk is built around, with a concrete benchmark contrast.*

> "1 out of 5, you know, AI use cases actually make it to production. You know, 56% of CEOs say that there's zero financial benefit from AI today."
>
> — [1:57](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=117s) &middot; *The hard numbers behind the claim that intelligence gains aren't converting to value.*

> "Cognitive intelligence doesn't really determine real-world effectiveness. In fact, only 10% of job performance variance is explained by IQ."
>
> — [2:32](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=152s) &middot; *The human-performance analogy that grounds her intelligence-vs-context framing.*

> "Intelligence has 1,000x'd in the last decade. Just in the last 6 months, we have 2x'd on that axis. On the other hand, context, the situated knowledge of your business, that's barely moved."
>
> — [3:17](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=197s) &middot; *The thesis in one line, with the asymmetry quantified.*

> "We've moved some data to the cloud, uh but that's about it. It's otherwise logged in dashboards and Slack threads and uh the head of that analyst who might be leaving next week."
>
> — [3:17](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=197s) &middot; *Names concretely where business context actually lives today.*

> "we got to the point by middle of last year where building an agent was really easy. Took like 5 minutes. Uh but giving it the business context that it took to actually get it to be accurate took forever."
>
> — [8:38](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=518s) &middot; *Reports the cost asymmetry between agent scaffolding and context engineering.*

> "our marketing team had these agents and they started making changes to that and then our SDR agent on our website was still pitching the old version. Uh we had no idea how any of these things were even connected."
>
> — [9:18](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=558s) &middot; *Concrete failure mode of per-agent siloed context in production.*

> "when an agent gets something wrong, this is hard. Uh it was really hard to like trace back what happened. Was it the model? The agent? Was it the context?"
>
> — [9:53](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=593s) &middot; *Names the attribution problem in multi-agent debugging.*

> "agents all had their own memory systems to a certain extent. So, they were learning They were all learning separately and they were learning differently."
>
> — [9:53](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=593s) &middot; *Explains why per-agent memory produces context sprawl rather than compounding learning.*

> "About 12 months ago we were using one of these no-code type builders uh called Relevance. We went from there into Google ADK, then we tried Glean. Uh start of this year we moved to Claude Code. Now we are kind of like 50/50 Claude and Codex."
>
> — [10:38](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=638s) &middot; *Rare candid account of framework churn, which motivates the portability argument.*

> "every single time as these changes happened, uh our context got trapped in each of these individual systems."
>
> — [10:38](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=638s) &middot; *The lock-in cost that makes a separate context layer necessary.*

> "often these dream teams are built on shared context, right? They have a shared language. They have a shared picture of what's true today. They have shared playbooks. They have shared norms, who's allowed to make what decision."
>
> — [11:20](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=680s) &middot; *Defines the components of shared context by analogy to human teams.*

> "Over the last 6 months, we ended up creating about 300 skills and 40 agents in this team"
>
> — [13:59](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=839s) &middot; *A concrete scale number for what a single team's context layer looks like in practice.*

> "each of these skills is learning and evolving, uh but every time they learn and evolve, it breaks something downstream."
>
> — [14:47](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=887s) &middot; *The core tension between self-improving skills and dependency stability.*

> "Security and governance was a nightmare. Uh we had secrets hardcoded in .env files. Uh it was People were downloading these public skill repos, this the whole thing was like a nightmare."
>
> — [14:47](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=887s) &middot; *Honest report of the security posture of a fast-growing skills repo.*

> "Company context needs life cycle management and collaboration and versioning just like code does."
>
> — [15:33](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=933s) &middot; *The central prescription of the talk, stated plainly.*

> "every AI interaction creates more context and harnessing this is gold."
>
> — [16:27](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=987s) &middot; *Frames traces as the raw material for compounding learning loops.*

> "if you're able to connect your Salesforce and your HubSpot to your data warehouse, to your application layer, and then you're able to reverse construct how these things are actually connected one to another, context today gets lost in every one of those hops."
>
> — [17:09](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=1029s) &middot; *Actionable answer to the 'how do I start' question.*

> "Today, we're largely building agents by hardcoding context. The scale of this problem I truly believe is underhyped, because with scale this can become really unsustainable."
>
> — [17:48](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=1068s) &middot; *Her sharpest contrarian claim against the current default practice.*

> "in a world where you and your competitor have access to the same models and the same intelligence, what differentiates a company?"
>
> — [19:21](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=1161s) &middot; *The strategic framing behind 'context is IP.'*

## Positions

- The bottleneck on useful AI is business context, not model intelligence; intelligence has 1,000x'd in a decade while context has barely moved. ([3:17](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=197s), confidence: stated)
- Only about 1 in 5 AI use cases makes it to production, and 56% of CEOs report zero financial benefit from AI today. ([1:57](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=117s), confidence: stated)
- Only 10% of job performance variance is explained by IQ, so cognitive intelligence alone is a poor predictor of real-world effectiveness for agents too. ([2:32](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=152s), confidence: stated)
- Building an agent is trivial (~5 minutes); supplying accurate business context is the expensive part. ([8:38](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=518s), confidence: stated)
- Per-agent memory systems are the wrong architecture — they cause context sprawl and prevent a single version of truth. ([9:53](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=593s), confidence: stated)
- Context should live outside any specific agent framework, because agent tooling churns roughly annually and trapped context is lost on each migration. ([10:38](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=638s), confidence: stated)
- Context must be managed like code, with versioning, dependency management, approvers/maintainers/contributors, quality management, and security posture management. ([15:33](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=933s), confidence: stated)
- Self-improving skills break downstream dependents, so autonomous skill evolution requires explicit dependency and impact tracking. ([14:47](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=887s), confidence: stated)
- Self-improvement should run through a specialized harness that reverse-constructs learnings from traces and routes them to a human maintainer for approve/reject. ([16:27](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=987s), confidence: stated)
- A usable first version of a company brain can be reverse-constructed with high accuracy by connecting existing business systems and inferring how they link. ([17:09](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=1029s), confidence: stated)
- Hardcoding context into agents is the dominant practice today and it will not scale. ([17:48](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=1068s), confidence: stated)
- Inconsistent context across autonomous agents will reproduce the classic sales-vs-finance revenue discrepancy at machine scale, which is dangerous. ([18:33](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=1113s), confidence: stated)
- Context, not models, is a company's durable competitive IP once everyone has access to the same intelligence. ([19:21](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=1161s), confidence: stated)
- The jobs-to-be-done framing that some tasks (relationship management) are safe from AI while others (documentation) are automatable was itself a flawed early hypothesis. ([8:00](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=480s), confidence: implied)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent skills](../concepts/agent-skills.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [context engineering](../concepts/context-engineering.md)
- [continual learning](../concepts/continual-learning.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [semantic layer](../concepts/semantic-layer.md)
- [session management](../concepts/session-management.md)

