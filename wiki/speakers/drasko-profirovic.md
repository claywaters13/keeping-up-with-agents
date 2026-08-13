---
title: "Drasko Profirovic"
type: "speaker"
slug: "drasko-profirovic"
talk_count: 1
---

# Drasko Profirovic

## Talks

- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [context window management](../concepts/context-window-management.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

## Quotes

> "It's not always straightforward to rank these asks, but as humans, we often have to decide how we'll spend our time. The same is not true for LLMs. We can easily scale out knowledge and capabilities on demand."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [0:52](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=52s)

> "Our vision for a diagnostics agent was to ask it simply, "Why did a job fail?" and get back a deep research document which provides evidence on the root cause of the failure."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [0:52](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=52s)

> "This worked in practice, but it required a lot of careful prompting from the human operator."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [1:44](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=104s)

> "Prompt tuning became unsustainable. One prompt had to do everything, and adding detail in one area degraded the behavior in another."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [2:26](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=146s)

> "As an example, large tool outputs from logs would click quickly consume tokens and brought a halt to the agent's reasoning."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [3:20](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=200s)

> "Lastly, our end-to-end testing strategy up to this point relied on manual tests from production. This felt anecdotal since production data would be retentioned away."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [3:20](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=200s)

> "In record mode, the agent calls real downstream systems, and tool responses are captured as fixtures. These are then saved to the file system and checked in as code."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [4:15](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=255s)

> "For example, an offline eval might check for a limit of three suggested fixes."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [4:15](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=255s)

> "Our end-to-end tests allowed us to quantify quality instead of relying on intuition."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s)

> "Logs are noisy, and many exceptions we see in logs are benign. So, simply focusing the last exception may not always be suitable."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s)

> "Initially, we kept it simple with a heuristics based approach using regex to filter out certain exceptions. But, this didn't scale well."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s)

> "The core idea was we would learn which exceptions commonly appear in successful jobs, treat those as likely red herrings, and filter them out in the future analysis."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [5:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=356s)

> "The agent stopped consuming logs directly, and instead was given two MCP tools. Get the top K truncated exceptions, or get full log details for a specific exception."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [5:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=356s)

> "Raw time series metrics are not context window friendly. Simply feeding the raw data to an LLM works in the small scale, but fails for long-running jobs in production. Not to mention, it's horribly token inefficient."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [6:44](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=404s)

> "Images worked better because we could guarantee how many input tokens would be used for analyzing any given Spark job irrespective of its duration."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s)

> "Examples of useful signals we would be able to get included executors dropping down to zero or near zero, long plateaus or bottlenecks, effectively any resource behavior inconsistent with healthy progress."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s)

> "Our sub agent would summarize its findings and return the results back to the parent agent, thereby ensuring the context window is kept healthy."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s)

> "A pleasant consequence of this architecture was that the effort to expand the scope of the project was as simple as adding a new prompt."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [9:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=547s)

> "The supervisor selects the highest confidence root cause and invokes the healer agent to offer remediations based on runbooks ingested into our vector database."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [9:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=596s)

> "We trialed using LangGraph's workflows to make the agent more deterministic, but this approach proved to be brittle compared to the reasoning and acting agent paradigm."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [9:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=596s)

