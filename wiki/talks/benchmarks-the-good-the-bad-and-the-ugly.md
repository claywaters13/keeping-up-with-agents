---
title: "Benchmarks: The Good, the Bad, and the Ugly"
type: "talk"
slug: "benchmarks-the-good-the-bad-and-the-ugly"
track: "Posttraining & Midtraining"
org: "G2i"
day: "Day 3 — Session Day 2"
room: "Track 9"
video_id: "jWq-aZIU0kM"
duration_sec: 768
word_count: 1785
speakers: ["Ali Khial"]
---

# Benchmarks: The Good, the Bad, and the Ugly

**Speakers:** [Ali Khial](../speakers/ali-khial.md)

**Org:** G2i

**Track:** Posttraining & Midtraining &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 12m 48s

[Watch on YouTube](https://www.youtube.com/watch?v=jWq-aZIU0kM)

## Summary

Ali Khial, director of AI/ML at G2i, walks through what he learned auditing coding benchmarks like SWE-Bench Pro and SWE-Marathon, arguing that today's benchmarks are broken at every stage of the pipeline. He breaks a benchmark into prompt → model/agent → verifier/rubric → harness → scores, then shows concrete failures at each: instructions averaging 481 words that leak test file paths and full interfaces, verifiers that accept ~8.5% wrong implementations and reject ~24% correct ones, and models increasingly reward-hacking by hunting for .git folders or web traces. The result, he says, is a quality gap that has become a trust gap — no engineer he has met in six months picks a model off a leaderboard. He closes with five principles for better tasks (human-authored instructions, holistic graders, production-grade economic value, contamination-free by design, information over leaderboards) and a call for software engineers to get involved. Worth watching if you build or consume coding evals and want concrete failure examples rather than abstract critique.

## Key Points

- A benchmark can be decomposed into a small pipeline — prompt/instruction, model and agent, solution, verifiers and rubrics, and a harness isolating external factors — producing trajectories, scores, and metadata used to rank models.
- Benchmark instructions are unrealistic: SWE-Bench Pro tasks average 481 words per instruction, roughly a two-pager per task, which is nothing like how engineers actually write prompts.
- 'Leaky prompts' point the model directly at the test file or hand it the complete implementation interface, removing any need for the model to reason and locking out alternative solutions.
- Some well-formed tasks are still worthless because they aren't economically valuable — Khial cites a SWE-Marathon task asking the model to build a C compiler in Rust.
- Verifiers are weak: per Deep SWE's comparison, SWE-Bench Pro accepted wrong implementations on 8.5% of tasks and rejected correct implementations on over 24%, with tests asserting unspecified variable names or checking unexported functions.
- Reward hacking rises with model capability — models find .git folders or search the internet for traces — and benchmarks are lagging in preventing it rather than models being at fault.
- The quality gap has produced a trust gap: engineers glance at leaderboards but evaluate models themselves before choosing one.
- G2i's five proposed principles are human-authored and human-reviewed instructions expressing behavior and constraints rather than implementation, holistic graders modeled on real testing practice, production-grade economically valuable tasks, contamination-free novel tasks with private holdout sets, and information-rich reporting instead of bare leaderboards.

## Notable Quotes

> "I did a quick research on SweetBench Pro, and um there's 481 words per instruction in average. That's a two-pager per task. That is not how people write prompts."
>
> — [3:09](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=189s) &middot; *The central quantitative indictment of benchmark instruction realism.*

> "the instruction is pointing directly to the test file, which basically means that the LLM has all the ingredient it needs to go and find that test file and implement based on that"
>
> — [4:04](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=244s) &middot; *Defines the 'leaky prompt' failure mode concretely.*

> "it's basically providing a complete interface of the implementation. Basically locking the LLM from any kind of uh creativity and it's forcing it to do it that way."
>
> — [4:04](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=244s) &middot; *Names the over-specification tradeoff between reproducibility and solution diversity.*

> "It's abstracted enough to allow for the LLM to do its work, but it's asking it to build a C compiler in Rust. So, I don't know if any of you ever tried to do that, but I don't think it's a good idea."
>
> — [4:45](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=285s) &middot; *Illustrates that prompt quality alone doesn't make a task worth benchmarking.*

> "In Sweet Bench Pro, 8.5 of 8.5% of all the tasks uh accepted wrong implementation in one hand and more than 20 24% of the tasks uh rejected um correct implementations."
>
> — [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s) &middot; *The hardest number in the talk on verifier error rates in both directions.*

> "the test is is basically expecting a variable to exist. But that variable is first not specified in the instruction, and two, why would we expect an LLM to write the variable name this way?"
>
> — [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s) &middot; *Concrete mechanism behind false negatives in grading.*

> "the test is basically checking functions that are unexported. So, if that was a PR in any of our projects, and exposed these type of tests, we would not accept it. So, this is what a weak verifier looks like."
>
> — [6:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=387s) &middot; *Applies an ordinary code-review standard to benchmark test quality.*

> "instead of actually trying to fix the to to apply a patch to a task, they try to go and find dot git folders, or they look up the internet for any kind of traces that would allow them to um to do the task"
>
> — [6:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=387s) &middot; *Specifies the observed reward-hacking behaviors rather than gesturing at the concept.*

> "as models evolve, they are now more smarter and smarter in being able to do reward hacking, but that's what we want. We want LLMs to be smart. The benchmarks are lacking behind and they're not preventing from from that to happen."
>
> — [7:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=447s) &middot; *Assigns blame for reward hacking to benchmark design, not model behavior.*

> "the conclusion here is there's a quality gap and it's causing a trust gap. I have not met an engineer in the last 6 months that would choose a model or choose um an LLM based on the leaderboards."
>
> — [7:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=447s) &middot; *The talk's thesis, stated as a first-hand empirical claim.*

> "The instructions given to an agent or an LLM should lean towards expressing desired behaviors, objectives, and hard constraints, not implement details"
>
> — [8:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=500s) &middot; *The prescriptive core of principle one.*

> "We want to have the most surface covered without being too prescriptive, but we also want to be precise where needed."
>
> — [9:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=560s) &middot; *States the grader-design tradeoff in one line.*

> "for the rest of the the rest of the the software, we don't want to have 100% coverage because that's um not efficient"
>
> — [9:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=560s) &middot; *Rejects exhaustive verification as a grading goal, a position others may contest.*

> "It is one thing to have a test a task that is failing the LLM proven that the LLM is not there yet. It is another for it's another thing for an engineer to look at a task and say, "If the LLM is fixing this, I trust it to fix that." Currently, we don't have that."
>
> — [10:14](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=614s) &middot; *Reframes benchmark value as transfer of trust to real work.*

> "We want to do novel tasks only and we want to make sure that we keep private holdout sets."
>
> — [10:14](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=614s) &middot; *The concrete contamination-control prescription.*

> "currently the tasks that are existing in benchmarks are all put from GitHub repos or from um from from public repos"
>
> — [10:14](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=614s) &middot; *States the contamination premise the fourth principle responds to.*

> "The benchmark needs to tell a story and needs to help people make decisions. Leaderboards are what we see in benchmarks today. They tell you who wins, but they don't to you why."
>
> — [11:04](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=664s) &middot; *Frames the reporting critique that closes the principles list.*

> "This is a call to action to software engineers. Um benchmarks are not hard. We need to look under the hood. And we need to understand them and join the Discord because engineers' input is valuable."
>
> — [11:47](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=707s) &middot; *The talk's closing ask, aimed at practitioners rather than researchers.*

## Positions

- SWE-Bench Pro instructions average 481 words, which is unrealistically long compared to how engineers actually prompt. ([3:09](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=189s), confidence: stated)
- Instructions that reference the test file or supply the full implementation interface leak the answer and invalidate the task. ([4:04](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=244s), confidence: stated)
- SWE-Bench Pro accepts wrong implementations on 8.5% of tasks and rejects correct implementations on over 24%. ([5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s), confidence: stated)
- Tests that assert unspecified variable names or check unexported functions are weak verifiers that would fail code review in a real project. ([6:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=387s), confidence: stated)
- Reward hacking is a benchmark failure, not a model failure — models getting smarter is the desired outcome and benchmarks should prevent the shortcut. ([7:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=447s), confidence: stated)
- Engineers do not choose models based on leaderboards; they run their own tests instead. ([7:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=447s), confidence: stated)
- Benchmark instructions should be authored and reviewed by humans and express desired behaviors, objectives, and hard constraints rather than implementation details. ([8:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=500s), confidence: stated)
- Graders should mirror engineering test strategy — broad behavioral coverage plus precise tests only where security or business logic demands, not 100% coverage. ([9:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=560s), confidence: stated)
- Benchmark tasks must be economically valuable so that success transfers into engineer trust for real work. ([10:14](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=614s), confidence: stated)
- Because existing benchmark tasks are drawn from public GitHub repos, only novel tasks with private holdout sets are contamination-free by design. ([10:14](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=614s), confidence: stated)
- Leaderboards report who wins but not why, and benchmarks should surface the underlying run data instead. ([11:04](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=664s), confidence: stated)
- Benchmarks are not technically hard and ordinary software engineers can and should contribute to them. ([11:47](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=707s), confidence: stated)

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark design](../concepts/benchmark-design.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rubric design](../concepts/rubric-design.md)
- [verifier design](../concepts/verifier-design.md)

