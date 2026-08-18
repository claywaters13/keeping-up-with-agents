---
title: "Enterprise Agents Have a Structure Problem"
type: "talk"
slug: "enterprise-agents-have-a-structure-problem"
org: "Tesla"
video_id: "B8l81jhvHbI"
duration_sec: 727
word_count: 1751
speakers: ["Ishita Daga"]
---

# Enterprise Agents Have a Structure Problem

**Speakers:** [Ishita Daga](../speakers/ishita-daga.md)

**Org:** Tesla

**Duration:** 12m 07s

[Watch on YouTube](https://www.youtube.com/watch?v=B8l81jhvHbI)

## Summary

Ishita Daga, an ML engineer building enterprise data agents at Tesla, argues that enterprise agent failures are structural rather than model-capability problems — reaching for a bigger model, more context, or more MCP servers won't fix them. She names three root causes: ambiguity (the agent doesn't know which table, column, or knowledge base is the source of truth), staleness (definitions, KPIs, and processes change faster than .md files and skills get updated), and preference (different teams legitimately compute the same metric different ways). Her proposed structure is a hierarchy of sources of truth ordered from cleanest/least flexible to messiest/most flexible — semantic layer, then canonical parametric queries, then a full database graph — plus a context lifecycle that embeds continuously-updated live sources and closes a log/evaluate/update feedback loop. She claims the first two layers are cheap to build and solve ~80% of the problem, and that most teams' agents fail because they never build evaluation at all. She's candid that preference remains unsolved: semantic layers and agent memory each address half of it, and routing an agent to the right metric based on who's asking is still open research.

## Key Points

- Enterprise agent failures are usually structural, not model-capability failures, so reaching for a larger model, a longer context window, or more knowledge bases and MCP servers does not address the actual cause.
- The three core problems are ambiguity about which source of truth to use, staleness of rapidly-changing definitions and processes, and per-team or per-individual preference in how metrics are computed.
- Sources of truth should be treated as a ranked hierarchy rather than weighted equally, with the agent starting from the cleanest and least flexible source and only falling back to messier, more dynamic ones.
- The three-tier hierarchy is a semantic layer of curated KPI and business definitions, then canonical parametric queries that allow more flexibility, then a database graph linking tables, columns, and metrics for maximum coverage.
- The database graph tier gives the widest question coverage but takes the most effort to build and maintain, so enterprises should build the first two tiers first — Daga estimates they solve about 80% of problems.
- Combating staleness requires a context lifecycle: embed live, continuously-curated sources such as GitHub, CRM tools, Tableau, or dbt semantic layers rather than hand-maintained .md files.
- The feedback loop most enterprise agents lack is logging every correction event — a wrong definition, a new metric calculation, a missing filter — and feeding those events back into the agent's context.
- Evaluation can be a human-annotated question suite or an automated comparison of recent questions against known-correct answers, and teams that skip evaluation have no visibility into whether their agent is improving or regressing.
- Preference is genuinely unsolved: semantic layers store multiple valid metric definitions but re-introduce ambiguity by requiring the user to prompt for one, while agent memory (mem0, memory.md) stores preferences but can't distinguish which metric applies when.
- The goal Daga wants is routing — sending the agent to the right metric definition based on which individual or team is asking, effectively a 'hive mind' for the data agent.

## Notable Quotes

> "when an agent gives a bad answer, the first reflect that we have is that we need a bigger model, we need a the latest model, we want a model with a lot of context so that it can hold a lot of information"
>
> — [0:01](https://www.youtube.com/watch?v=B8l81jhvHbI&t=1s) &middot; *Names the reflexive non-solution the whole talk is arguing against.*

> "while all of these are fair solutions, they're not the answer to actually improving the data agent itself"
>
> — [0:48](https://www.youtube.com/watch?v=B8l81jhvHbI&t=48s) &middot; *The talk's central negative claim, stated plainly.*

> "it doesn't know what table is right, what column is right, which data source, or which knowledge base to access when, which one holds the source of truth"
>
> — [0:48](https://www.youtube.com/watch?v=B8l81jhvHbI&t=48s) &middot; *Concrete definition of the ambiguity problem in data-agent terms.*

> "The agent needs to understand what source of truth to use, or what knowledge base to use. It can't weight all the knowledge bases equally."
>
> — [2:42](https://www.youtube.com/watch?v=B8l81jhvHbI&t=162s) &middot; *States the core design position: hierarchy over flat retrieval.*

> "the source of truth actually is a hierarchy, which goes from the cleanest, least flexible source of truth to the messiest, uh but most flexible, most dynamic source of truth"
>
> — [2:42](https://www.youtube.com/watch?v=B8l81jhvHbI&t=162s) &middot; *The organizing axis of the proposed framework — cleanliness traded against flexibility.*

> "The first one being the semantic layer, which is the best source of truth, a very curated list of all the different queries, KPI definitions, metric uh or how to calculate the metric, um the business definitions"
>
> — [3:29](https://www.youtube.com/watch?v=B8l81jhvHbI&t=209s) &middot; *Defines tier one of the hierarchy.*

> "The last one is the database graph, which I feel is the most trickiest because it takes a lot of effort, but it gives you a lot of flexibility in the kind of questions that can be answered."
>
> — [4:27](https://www.youtube.com/watch?v=B8l81jhvHbI&t=267s) &middot; *Names the effort-versus-coverage tradeoff at the bottom tier.*

> "they should start adding the first and the second layer first. These are easy to set up, solve I think 80% of the problems, and then the 20% can be solved by the database graph."
>
> — [5:18](https://www.youtube.com/watch?v=B8l81jhvHbI&t=318s) &middot; *The talk's one quantified, actionable sequencing recommendation.*

> "the context gets rotten, or it gets deprecated, or processes change so often that it's hard to maintain dot MD files, or keep on updating your skills with the most latest context"
>
> — [5:18](https://www.youtube.com/watch?v=B8l81jhvHbI&t=318s) &middot; *Argues hand-maintained markdown context files don't survive enterprise change rates.*

> "By life, I mean something or the data sources that are going to be always updated, would be reviewed and well curated, and always provide the newest, or the most up-to-date data."
>
> — [6:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=363s) &middot; *Defines the 'live source' criterion for what belongs in agent context.*

> "The second part is a feedback loop, which is something that a lot of enterprise or data agents actually miss."
>
> — [6:54](https://www.youtube.com/watch?v=B8l81jhvHbI&t=414s) &middot; *Identifies the specific missing component she claims causes most failures.*

> "All of these events need to be captured, logged, and used to update your data agent context."
>
> — [6:54](https://www.youtube.com/watch?v=B8l81jhvHbI&t=414s) &middot; *The concrete mechanism behind the context lifecycle.*

> "a lot of teams do not focus on evaluation that much, and which is why the agents actually fail so often because you don't know how the agent is progressing or how is the performance"
>
> — [8:04](https://www.youtube.com/watch?v=B8l81jhvHbI&t=484s) &middot; *Directly attributes agent failure to absent evaluation.*

> "Different teams will calculate the same metric differently or um use the same query but different filters. So, there is a lot of subjectivity which needs to be captured"
>
> — [8:48](https://www.youtube.com/watch?v=B8l81jhvHbI&t=528s) &middot; *Frames preference as legitimate divergence rather than user error.*

> "while both of these are correct metrics or the correct way to calculate the metric. They both will give you very different answers and it's just about preference."
>
> — [9:33](https://www.youtube.com/watch?v=B8l81jhvHbI&t=573s) &middot; *The milestone-timing example crystallizes why preference can't be resolved by correctness alone.*

> "while this is a great question, I feel the industry still does not have a correct answer or correct way to solve the problem itself"
>
> — [9:33](https://www.youtube.com/watch?v=B8l81jhvHbI&t=573s) &middot; *Explicit admission that a third of the framework is unsolved.*

> "So you can solve it but still is not storing the preference of the user. And the second thing is you again bump into the first challenge, which is ambiguity."
>
> — [10:21](https://www.youtube.com/watch?v=B8l81jhvHbI&t=621s) &middot; *Explains why the semantic-layer fix for preference collapses back into ambiguity.*

> "It stores your preference but it can't understand the distinction between two different metrics or which one to use when."
>
> — [10:21](https://www.youtube.com/watch?v=B8l81jhvHbI&t=621s) &middot; *A specific limitation claim about agent memory systems like mem0.*

> "What we actually want is a way to route the agent to the right metric based on who what what a team or which individual is using that agent."
>
> — [11:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=663s) &middot; *States the research goal she's pointing the field toward.*

> "It requires not just understanding how the agent works, but also embedding an individual preference, like creating a hive mind for your data agent."
>
> — [11:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=663s) &middot; *The closing framing that gives the preference problem its shape.*

## Positions

- Bad agent answers are not fixed by a bigger model, a longer context window, or adding more knowledge bases and MCP servers. ([0:48](https://www.youtube.com/watch?v=B8l81jhvHbI&t=48s), confidence: stated)
- An agent must not weight all knowledge bases equally; sources of truth must be ranked and consulted cleanest-first. ([2:42](https://www.youtube.com/watch?v=B8l81jhvHbI&t=162s), confidence: stated)
- The semantic layer is the best source of truth for a data agent. ([3:29](https://www.youtube.com/watch?v=B8l81jhvHbI&t=209s), confidence: stated)
- The semantic layer and canonical queries solve roughly 80% of enterprise data-agent problems; the database graph covers the remaining 20%. ([5:18](https://www.youtube.com/watch?v=B8l81jhvHbI&t=318s), confidence: stated)
- Enterprises should build the semantic layer and canonical query tiers before attempting a database graph, because the graph is high-effort and hard to maintain. ([5:18](https://www.youtube.com/watch?v=B8l81jhvHbI&t=318s), confidence: stated)
- Hand-maintained .md files and skills cannot keep pace with how fast enterprise definitions, KPIs, and processes change. ([5:18](https://www.youtube.com/watch?v=B8l81jhvHbI&t=318s), confidence: stated)
- Agent context should be sourced from live, continuously-updated systems (GitHub, CRM, Tableau, dbt) rather than static documents. ([6:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=363s), confidence: stated)
- Most enterprise data agents lack a feedback loop that logs correction events and feeds them back into context. ([6:54](https://www.youtube.com/watch?v=B8l81jhvHbI&t=414s), confidence: stated)
- Agents fail often specifically because teams do not invest in evaluation and therefore cannot track performance over time. ([8:04](https://www.youtube.com/watch?v=B8l81jhvHbI&t=484s), confidence: stated)
- Two teams can compute the same metric in different but equally correct ways, so preference conflicts cannot be resolved by picking the 'right' definition. ([9:33](https://www.youtube.com/watch?v=B8l81jhvHbI&t=573s), confidence: stated)
- Neither semantic layers nor agent memory (e.g. mem0, memory.md) actually solves the preference problem — the former requires the user to prompt for a choice, the latter can't tell which metric applies when. ([10:21](https://www.youtube.com/watch?v=B8l81jhvHbI&t=621s), confidence: stated)
- The right solution to preference is automatic routing to the correct metric definition based on the identity of the requesting individual or team. ([11:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=663s), confidence: stated)
- Preference in enterprise agents is an open research problem that frontier labs and industry have not yet solved. ([1:43](https://www.youtube.com/watch?v=B8l81jhvHbI&t=103s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [context engineering](../concepts/context-engineering.md)
- [context rot](../concepts/context-rot.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [rlhf and preference training](../concepts/rlhf-and-preference-training.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [semantic layer](../concepts/semantic-layer.md)

