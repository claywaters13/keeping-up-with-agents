---
title: "James Shi"
type: "speaker"
slug: "james-shi"
talk_count: 1
---

# James Shi

## Talks

- [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md) (Agentic Engineering)

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [cross-model verification](../concepts/cross-model-verification.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [model portability](../concepts/model-portability.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [reward hacking](../concepts/reward-hacking.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "So this means unlike something like sweet bench pro we didn't scrape this from existing PRs that have been closed. Um, there's a variety of benefits for this. Uh namely one of them is to resist against contamination and agents being able to cheat uh through the course of their rollouts."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [0:43](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=43s)

> "Swebench has or Swebench Pro uh pulls thousands of tasks from only 40 repositories. The median task per repository for us is one."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [1:21](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=81s)

> "with benches like Sweetbench Pro, uh top models are clustering at the top. It's very hard to differentiate between uh which one is good because they all have overlapping confidence intervals."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [2:44](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=164s)

> "The verifiers are also very very brittle because we're anchoring them to a specific implementation often derived from the PR that was merged in."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [2:44](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=164s)

> "for very uh insightful models such as Claude, they're able to directly run git log and then go through the commit hashes and cherrypick the ones out that contain the golden patches which again very very serious issue."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [3:28](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=208s)

> "we find claude is generally a very very um, thorough and exhaustive model."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [4:04](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=244s)

> "it will go ahead and implement the synchronous part, but it may drop the asynchronous part. We observed this in roughly two out of three cloud rollouts across all of the uh trials, all of the rollouts that we ran."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [4:52](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=292s)

> "We found that for opus 4.6 6 and 4.7 it did this 25% and 18% of the time respectively compared to all the Gemini models uh averaging at roughly 1% of the time and we found zero instances of this for the GPT models."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [5:33](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=333s)

> "GBT is very good at implementing exactly what it is asked across our failure mode analysis. We found that it was the least likely model to miss requirements."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [6:20](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=380s)

> "in SweetBench Pro's template they explicitly tell the model that the tests are handled and therefore they do not need to uh write uh any new tests of their own. With that single line in the prompt it will uh prevent the models from even uh 5.5 and uh Opus 4.8 from attempting to verify its own work"
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [7:09](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=429s)

> "we find on average that stronger models like 5.4 4.7 exhibit this the majority of the time whereas uh models like three flash and 3.1 pro are far less frequently um willing to test their own work."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [7:57](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=477s)

> "we made a decision to want to have every task authored uh from scratch uh rather than being mined."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [7:57](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=477s)

> "the average prompt uh characters within SweetBench Pro is over 4,500 characters, whereas for us, it's uh roughly half of that."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [9:29](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=569s)

> "you're not going to be coming in there with a to-do list uh telling it to oh first do this and then do this and then write this function signature in exactly uh this way that I've prescribed on to you."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [10:15](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=615s)

> "Even with our prompts again being roughly half the size of Sweetbench Pros, we find that the average size of our solution is five times the lines of code um compared to Sweepbench Pros."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [10:50](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=650s)

> "It will fail the model if it uh produces a function that may address the objective but is not named or is not defined within a specific module or if there is the absence of specific helpers or other private functions."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [11:28](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=688s)

> "for us we want to uh emphasize on the observable behavior as much as possible. We want to ensure that any correct implementation uh anything that correctly solves the problem is rewarded and this will prevent against uh false negatives."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [12:13](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=733s)

> "we've taken some additional measures to guard against cheating uh reward hacking uh by ensuring you know the verifier runtime is fully separate now from the agent runtime."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [14:49](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=889s)

> "We also want to look into hybrid verification because if we're able to use LLM as judge or other um methodologies, it's possible for us to make our prompts even more tur and even more um even more uh high level"
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [15:31](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=931s)

> "there is of course like a certain degree that we have to in our current prompts like um hint the agents steering them towards a current methodology just because otherwise they they may not be well positioned at all to make meaningful progress towards the task."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [16:15](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=975s)

