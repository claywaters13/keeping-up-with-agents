---
title: "The Factory That Dreams: 39 AI Agents, No Framework"
type: "talk"
slug: "the-factory-that-dreams-39-ai-agents-no-framework"
org: "Machinecraft"
day: "Day 4 — Session Day 3"
room: "Expo Stage 4 SE"
video_id: "jtzh-GBXBWc"
duration_sec: 598
word_count: 1395
speakers: ["Rushabh Doshi"]
---

# The Factory That Dreams: 39 AI Agents, No Framework

*Program title: The Software Factory*

**Speakers:** [Rushabh Doshi](../speakers/rushabh-doshi.md)

**Org:** Machinecraft

**Day/Room:** Day 4 — Session Day 3 &middot; Expo Stage 4 SE &nbsp;|&nbsp; **Duration:** 9m 58s

[Watch on YouTube](https://www.youtube.com/watch?v=jtzh-GBXBWc)

## Summary

Rushabh Doshi describes how Machinecraft, a 100-person thermoforming machine factory in India with no data science team and no ML budget, built a multi-agent system called Eira that runs its entire go-to-market function. The core argument is that the valuable asset was never a model but institutional memory: three generations of quotes, drawings, and email threads that lived in two or three people's heads and leaked out every time an employee left. Rather than fine-tuning anything, they chunked hundreds of gigabytes of private history into vectors and a relationship graph, then split the work across ~36 single-purpose agents that deliberate with each other, backed by layered memory, a nightly consolidation 'dream cycle', and a values 'soul file' derived from Jain family-business principles. The economic claim is the sharpest part: zero training cost, roughly $30K to build against a $230K agency quote, and a couple thousand dollars a month to run. Worth watching if you want a concrete, non-framework, small-company blueprint for agentic memory architecture — and the open-sourced 'Brain OS' shell that ships with it.

## Key Points

- The company's real asset was tacit institutional knowledge held in two or three brains across three generations, and employee turnover was steadily draining it — the motivating fear was forgetting, not competition.
- No model was trained or fine-tuned; the entire system runs on off-the-shelf models reading chunked private history stored as vectors plus a relationship graph, making the differentiator organized memory rather than model quality.
- The architecture deliberately rejects a single mega-prompt in favor of ~36 named single-purpose agents (Athena for orchestration, Plutus for pricing, Hephaestus for machine specs, Vera for fact-checking, Memnon for guarding human corrections) that convene and argue before producing one answer.
- The system is modeled on biology — senses, gut, memory, immune system, dream cycle — on the reasoning that evolution already solved staying coherent over time.
- Memory is engineered in explicit layers: working memory, pinned facts, episodes, relationships with accumulating warmth, and a salience gate that filters what is worth storing at all; on conflict, human corrections always win.
- A nightly sleep cycle replays the day, resolves contradictions, forgets stale data, and distills work into reusable skills, producing a morning dream report for the operator.
- Agent values are encoded in a 'soul file' drawn from Jain family-business principles rather than generic helpful/harmless framing, yielding concrete production guardrails like cross-checking sources, citing document and date, and never speaking absolutely.
- Costs invert the usual assumption: zero training spend, ~$30K build versus a $230K agency quote, and low thousands per month to operate, with 213 tools exposed over one protocol and a hard 'Eira drafts, human sends' rule.
- The architecture was extracted as an empty, forkable shell called Brain OS at forkmybrain.org, on the premise that no vendor can build your company's brain for you.

## Notable Quotes

> "We weren't scared of the competitors, we were scared of forgetting."
>
> — [0:45](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=45s) &middot; *States the animating problem in one line — knowledge attrition, not market pressure.*

> "what if instead of writing the knowledge down in some document nobody ever reads, what if we grew a brain that just held it?"
>
> — [0:45](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=45s) &middot; *The founding premise, framed as an alternative to documentation.*

> "We never trained a model. No GPUs humming in the basement, no fine-tuning."
>
> — [2:37](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=157s) &middot; *The central counterintuitive technical claim of the talk.*

> "The brain isn't a smarter model. It's actually a really, really well-organized memory."
>
> — [2:37](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=157s) &middot; *Compresses the whole architectural thesis into one sentence.*

> "one prompt that's supposed to do everything ends up doing everything badly"
>
> — [3:25](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=205s) &middot; *The justification for multi-agent decomposition over a single mega-prompt.*

> "One agent, one job. It's a team, not a hero."
>
> — [4:11](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=251s) &middot; *Memorable statement of the single-responsibility principle applied to agents.*

> "It's like having a board room that never sleeps, never gets tired, and somehow has no ego."
>
> — [4:11](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=251s) &middot; *Describes the multi-agent deliberation pattern and its claimed advantage over humans.*

> "Where does all this live? One cursor tab. That's genuinely it."
>
> — [5:09](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=309s) &middot; *Reports the surprisingly minimal interface surface for a 36-agent system.*

> "All of it, every capability exposed as 213 tools over one protocol. And the golden rule, the one we never break, Eira drafts, human sends."
>
> — [6:05](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=365s) &middot; *Names a hard number and the non-negotiable human-in-the-loop constraint.*

> "a raw language model is basically a goldfish. Brilliant for about 30 seconds, and then you close the tab and forgets you ever existed."
>
> — [6:05](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=365s) &middot; *The case for engineered memory, stated vividly.*

> "A salience gate that decides what's even worth remembering, so the brain doesn't fill up with junk. When two facts disagree, corrections win."
>
> — [6:49](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=409s) &middot; *Two concrete, portable memory design decisions.*

> "Every night, Eira runs a sleep cycle. It replays the day, locks in useful stuff, hunts for contradictions, gently forgets the stale junk, and turns the day's work into reusable skills."
>
> — [6:49](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=409s) &middot; *Full description of the offline consolidation mechanism the talk is named for.*

> "Every agent has a conscience. And it is emphatically not to be helpful, be harmless."
>
> — [7:43](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=463s) &middot; *Explicitly positions against the standard alignment framing.*

> "It's a soul file written from the principles of a Jain family business that's been doing this for the last three generations."
>
> — [7:43](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=463s) &middot; *The unusual source of the system's operating values.*

> "Ancient philosophy running as guardrails in production."
>
> — [8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s) &middot; *Crisp summary of turning inherited values into engineering rules.*

> "There was no training bill. Zero. The expensive part was never compute. It was teaching a company to remember itself."
>
> — [8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s) &middot; *Reframes where cost actually lands in enterprise AI projects.*

> "An agency quoted us 230 grand to build this. We built it for around 30."
>
> — [8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s) &middot; *Hard cost comparison, the most checkable number in the talk.*

> "We are a 100 people factory with no data scientists. If we can grow a brain, you can too."
>
> — [9:13](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=553s) &middot; *The generalization claim the whole talk is built to support.*

## Positions

- Building a useful company-specific AI system requires no model training or fine-tuning — off-the-shelf models plus well-organized memory are sufficient. ([2:37](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=157s), confidence: stated)
- Capability comes from memory organization, not from having a smarter model. ([2:37](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=157s), confidence: stated)
- A single all-purpose prompt performs worse than many narrowly scoped agents. ([3:25](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=205s), confidence: stated)
- Biological metaphors (senses, gut, immune system, sleep) are a productive architectural template because evolution already solved long-term coherence. ([3:25](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=205s), confidence: stated)
- Agents should never send outbound communication autonomously; every draft passes through a human. ([6:05](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=365s), confidence: stated)
- Raw LLMs are unusable for long-running business processes without deliberately engineered external memory. ([6:05](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=365s), confidence: stated)
- When stored facts conflict, human corrections should take permanent precedence over model-derived facts. ([6:49](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=409s), confidence: stated)
- Generic 'be helpful, be harmless' alignment is inadequate for business agents; values should be domain- and culture-specific and encoded as concrete engineering rules. ([7:43](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=463s), confidence: stated)
- The system cost roughly $30,000 to build versus a $230,000 agency quote, and runs for a couple thousand dollars per month with zero training cost. ([8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s), confidence: stated)
- The architecture is transferable but the knowledge is not — no vendor can build another company's brain for it, so the right product is an empty forkable shell. ([9:13](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=553s), confidence: stated)
- Frameworks are unnecessary for production multi-agent systems; a conventional stack of databases, multiple model providers, and tools over one protocol suffices. ([6:05](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=365s), confidence: implied)
- Different model providers should be selected per task rather than standardizing on one. ([6:05](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=365s), confidence: stated)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [agent memory](../concepts/agent-memory.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

