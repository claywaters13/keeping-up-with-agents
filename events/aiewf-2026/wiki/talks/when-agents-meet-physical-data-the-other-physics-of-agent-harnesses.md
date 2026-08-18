---
title: "When Agents Meet Physical Data: The Other Physics of Agent Harnesses"
type: "talk"
slug: "when-agents-meet-physical-data-the-other-physics-of-agent-harnesses"
track: "Posttraining & Midtraining"
org: "DataChain"
day: "Day 3 — Session Day 2"
room: "Track 9"
video_id: "bUJgirn4_yc"
duration_sec: 1652
word_count: 3405
speakers: ["Sean Cai"]
---

# When Agents Meet Physical Data: The Other Physics of Agent Harnesses

*Program title: State of Data*

**Speakers:** [Sean Cai](../speakers/sean-cai.md)

**Org:** DataChain

**Track:** Posttraining & Midtraining &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 27m 32s

[Watch on YouTube](https://www.youtube.com/watch?v=bUJgirn4_yc)

## Summary

Dmitry Petrov argues that coding agents fail on unstructured 'physical' data — video, sensor streams, robot telemetry — not because the models are weak but because the environment obeys different physics than the SQL/warehouse world the frontier-lab data-agent posts assume. He frames the fix as a data harness with four faculties: sight (Pydantic schemas over binary files instead of millions of S3 JSONs), hands (a distributed execution engine with incremental updates and checkpoints), verification (pre-built dimensional metadata layers so tests and questions answer in one query), and memory (a markdown knowledge base capturing why a dataset was built, its schema, stats, and above all its source code). He demos DataChain, an open-source implementation, running Claude Code over 91 dashcam clips: 24 minutes of compute produced ~100,000 detection records queryable in fast Python-to-SQL. The core claim is that stronger frontier models won't close the gap — everyone already uses them — so the leverage is in the harness. Worth watching if you build multimodal or physical-AI pipelines and keep re-running expensive extraction jobs.

## Key Points

- Frontier labs have independently documented that agents underperform on data work — Petrov cites Anthropic reporting 21% accuracy on data projects absent a data harness, and OpenAI prescribing six layers of context — but both were operating on structured business data, which is the easy case.
- Unstructured data is a 'neutron star': a few thousand video files look small on the surface, but clips contain frames containing objects containing labels and confidences, so 90 videos in the demo generated roughly 100,000 records and thousands would reach millions.
- The two common coping strategies both fail — millions of sidecar JSONs on S3 give terrible latency and no consistency, while a centralized metadata database splits the team across two stacks and two programming languages.
- Petrov's answer is Pydantic as the single schema language so data models, code, and the SQL transpilation all live in Python with no 'SQL island' in the codebase.
- An unstructured-data harness has to reinvent the execution engine that a warehouse provides for free; he favors a Dask-like model that binds Python functions, Pydantic input/output types, storage files, and the metadata warehouse into one distributable unit you scale by naming a machine count.
- Incremental updates and checkpoints are non-negotiable because extraction runs are long and LLM-expensive: a failure midway must resume rather than recompute, and new files in the bucket must process without touching old ones.
- Correctness matters more in data than in software because, as Petrov reads Anthropic's finding, software problems admit many valid solutions while a data question typically has exactly one correct answer.
- Rather than answer a question by scripting over raw data, the agent first asks whether a metadata layer exists that answers it in one SQL-ish query, and if not builds one general enough to serve a class of related questions — reviving star schemas and one-big-table modeling for multimodal metadata.
- Expensive results should be shared, not re-derived: a knowledge base of plain MD files per dataset — session context for why it was built, LLM-written description, storage dependency, data preview, schema, stats, and source code — gives teammates and their agents lineage so the recompute never happens twice.

## Notable Quotes

> "Anthropic published that accuracy for data projects on their agents is only 21% until you add specific data harnesses to them and provide context."
>
> — [0:02](https://www.youtube.com/watch?v=bUJgirn4_yc&t=2s) &middot; *The headline number motivating the entire talk.*

> "OpenAI published a whole layers of context, six layers of context in order to make the data agent to work."
>
> — [0:02](https://www.youtube.com/watch?v=bUJgirn4_yc&t=2s) &middot; *Second lab data point, establishing this is an industry-wide finding rather than a vendor pitch.*

> "In my life, I don't have this luxury unfortunately because I live in a very extreme side of the data universe, messy unstructured data."
>
> — [1:03](https://www.youtube.com/watch?v=bUJgirn4_yc&t=63s) &middot; *Names the scope boundary — his claims are about unstructured data, not the warehouse world the lab posts studied.*

> "2000 objects, 2000 files of videos could easily generate you millions of objects inside the videos."
>
> — [2:55](https://www.youtube.com/watch?v=bUJgirn4_yc&t=175s) &middot; *The neutron-star metaphor made concrete as a cardinality explosion.*

> "First step, let's put this meta information to JSON files and put it on S3 next to the images, right? And they end up with a millions of JSONs."
>
> — [3:52](https://www.youtube.com/watch?v=bUJgirn4_yc&t=232s) &middot; *Names the first anti-pattern most teams reach for.*

> "But this way you end up with a two system with a two programming languages"
>
> — [3:52](https://www.youtube.com/watch?v=bUJgirn4_yc&t=232s) &middot; *States the tradeoff that kills the centralized-database approach.*

> "We found that the easiest way for researchers and developers to deal with the schema is Pydantic."
>
> — [4:41](https://www.youtube.com/watch?v=bUJgirn4_yc&t=281s) &middot; *The concrete design choice at the center of his 'sight' layer.*

> "you use the same language for the data, for the schemas, as well as code. Uh there are no SQL island in your code base."
>
> — [4:41](https://www.youtube.com/watch?v=bUJgirn4_yc&t=281s) &middot; *Articulates the specific benefit claimed for Pydantic-as-schema.*

> "It's not supposed to be big because we analyze only like 90 videos and 90 videos generated 100,000 of records, right?"
>
> — [10:53](https://www.youtube.com/watch?v=bUJgirn4_yc&t=653s) &middot; *Live demo number grounding the scale argument.*

> "In the sequel or structured data world, execution engine is your data warehouse, right? That's obvious and easy. In an unstructured data world, you have to reinvent one."
>
> — [13:52](https://www.youtube.com/watch?v=bUJgirn4_yc&t=832s) &middot; *Cleanest statement of why unstructured tooling can't be borrowed from the warehouse stack.*

> "Incremental update and data checkpoints it's a must-have in this data world."
>
> — [18:31](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1111s) &middot; *A flat requirement claim others building agent data pipelines might treat as optional.*

> "In data, there is usually only one way and only one current correct answer"
>
> — [19:22](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1162s) &middot; *The asymmetry between software and data agents that justifies the emphasis on verification.*

> "instead of answering the question right away, agent ask itself, do I have a proper data sets, proper metadata to answer this question quickly in a single like SQL-ish query."
>
> — [20:19](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1219s) &middot; *Describes the actual behavioral change baked into the harness.*

> "It tries to make sure this layer is general enough to answer not your particular question, but a set of questions related to the one that you asked."
>
> — [21:21](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1281s) &middot; *The generalization heuristic that turns one-off compute into reusable infrastructure.*

> "People are doing the same job over and over and over again. You're paying double, triple, quadruple price to solving the same problem."
>
> — [21:21](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1281s) &middot; *The economic argument for shared dataset memory.*

> "Uh description of the data set, which usually enrich by LLMs, source code. Probably the most important part here is the source code."
>
> — [23:10](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1390s) &middot; *Ranks source code above other metadata as the key context artifact.*

> "This is a world when your favorite coding agents, such as Copilot, Codex, Cloud Code, do not operate efficiently."
>
> — [25:40](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1540s) &middot; *Blunt claim that general coding agents are the wrong tool here as-shipped.*

> "Their intuition pushes them in a wrong direction because laws of physics changes. And in order to make it, you don't use stronger models. Everyone use frontiers. Instead, you are building data harness."
>
> — [26:42](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1602s) &middot; *The thesis in one breath: harness beats model scale for this problem class.*

## Positions

- Agent accuracy on data projects is only about 21% without a purpose-built data harness and supplied context, per Anthropic's published results. ([0:02](https://www.youtube.com/watch?v=bUJgirn4_yc&t=2s), confidence: stated)
- The frontier-lab findings on data agents apply to structured business data and therefore understate the problem for unstructured, physical data. ([5:27](https://www.youtube.com/watch?v=bUJgirn4_yc&t=327s), confidence: stated)
- Storing extracted metadata as millions of JSON files alongside objects in S3 is unworkable on latency, efficiency, and consistency. ([3:52](https://www.youtube.com/watch?v=bUJgirn4_yc&t=232s), confidence: stated)
- A separate centralized metadata database is the wrong fix because it forces teams into two systems and two programming languages that researchers won't adopt. ([3:52](https://www.youtube.com/watch?v=bUJgirn4_yc&t=232s), confidence: stated)
- Pydantic is the most accessible schema mechanism for researchers and developers, and schemas should transpile to SQL rather than exist as a separate SQL layer. ([4:41](https://www.youtube.com/watch?v=bUJgirn4_yc&t=281s), confidence: stated)
- Unstructured data needs its own execution engine because warehouses don't cover it; Dask's model of binding compute to data is the right template, adapted for binaries. ([14:43](https://www.youtube.com/watch?v=bUJgirn4_yc&t=883s), confidence: stated)
- Incremental updates and checkpoints are mandatory, not optional, for physical-data pipelines. ([18:31](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1111s), confidence: stated)
- Quality and accuracy matter more in data projects than software projects because data questions typically have exactly one correct answer while software problems have many valid solutions. ([19:22](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1162s), confidence: stated)
- Running Python scripts directly over raw data to answer questions is the slowest and most expensive approach; a pre-built metadata layer should answer them instead. ([20:19](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1219s), confidence: stated)
- Decades-old dimensional modeling techniques — star schemas, one big table — should be applied to unstructured metadata and are currently underused. ([20:19](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1219s), confidence: stated)
- Source code is the single most important piece of context to store about a derived dataset, a conclusion OpenAI also reached in its data agent blog post. ([23:10](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1390s), confidence: stated)
- A shared knowledge base of plain markdown files per dataset is sufficient infrastructure for agent-and-human dataset memory. ([23:54](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1434s), confidence: implied)
- Using stronger models will not fix agent performance on physical data because everyone already uses frontier models; the harness is the differentiator. ([26:42](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1602s), confidence: stated)
- General coding agents' trained intuitions actively mislead them on physical data because the operating constraints differ from software repositories. ([26:42](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1602s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [document parsing](../concepts/document-parsing.md)
- [durable execution](../concepts/durable-execution.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [semantic layer](../concepts/semantic-layer.md)
- [structured output contracts](../concepts/structured-output-contracts.md)

