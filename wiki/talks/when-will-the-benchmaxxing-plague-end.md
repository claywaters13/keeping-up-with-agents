---
title: "When Will The Benchmaxxing Plague End?"
type: "talk"
slug: "when-will-the-benchmaxxing-plague-end"
track: "AI Architects: Show my Workflow"
org: "Surge AI"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "-npY6XjM8CQ"
duration_sec: 1044
word_count: 2951
speakers: ["Nick Heiner"]
---

# When Will The Benchmaxxing Plague End?

**Speakers:** [Nick Heiner](../speakers/nick-heiner.md)

**Org:** Surge AI

**Track:** AI Architects: Show my Workflow &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 17m 24s

[Watch on YouTube](https://www.youtube.com/watch?v=-npY6XjM8CQ)

## Summary

Nick Heiner of Surge AI argues that 'benchmaxxing' — labs over-optimizing for benchmarks in ways that diverge from real-world value — is driven jointly by bad benchmark construction and by lab incentives, and that it is fixable rather than intrinsic to benchmarking. He walks through concrete anti-patterns in widely cited benchmarks: the prohibitive cost of building good tasks (he prices a 1,000-task agentic coding benchmark at ~$15M), contamination (he claims evidence Opus memorized much of SWE-bench Verified, undisclosed in the model card), reward hacking, hard-coded string-match verifiers that can't distinguish Haiku from Fable, prompt sets with impossible or unverified instructions (IFEval), and unverified synthetic data (APEX) that induces eval awareness. On the lab side he describes hill-climbing benchmarks while human eval stays flat or declines, crowdsourced vote-buying on LMArena via model watermarks, and undisclosed multi-model testing. His prescription is to anchor benchmarks in expensive human expertise plus product sense, with two-way prompt/verifier alignment, working tools, thorough QC, and private holdout sets — exemplified by Surge's Hemingway Bench, which uses thousands of professional writers doing blind model comparisons. Worth watching if you consume or build model evals and want a specific catalogue of failure modes rather than general skepticism.

## Key Points

- Benchmarks gain influence through popularity and incumbency rather than quality, because most consumers can't assess whether a benchmark is good but can observe what everyone else cites.
- Building a serious agentic benchmark is genuinely expensive — roughly $15M for 1,000 tasks at 60 hours each, plus ~$5M/year to replace tasks models outgrow — which pushes teams toward AI-generated or cheap-labor shortcuts that don't work.
- Contamination is the default outcome, not an exception: Surge found clear evidence Opus memorized large portions of SWE-bench Verified, and the Opus 4.8 model card discloses no such contamination.
- Hard-coded string-match verifiers destroy signal — on Automation Bench, Haiku and Fable both score 20% for entirely different reasons (mistakes vs. valid alternative phone-number formats), making the task useless for ranking.
- IFEval contains prompts that are logically impossible (repeat verbatim + translate to Hindi), prompts no real user would issue, and verifiers that don't check the main instruction — letting responses reward-hack with Cyrillic characters and still get full marks.
- Synthetic, obviously-fake benchmark data (APEX) both mismatches its own rubrics and increases eval awareness, where the model recognizes it is being tested and the measurement is undermined.
- Labs can deliberately hill-climb a benchmark past the point where human eval flattens or declines, and can game LMArena directly via crowdsourced voters and model watermarks, or via undisclosed multi-model testing.
- Good benchmarks start with high-quality human experts plus product/domain sense, use real-world input data, working tools, two-way prompt–verifier alignment, thorough QC, and a private holdout set.
- Claimed 'saturation' at ~80% may actually mean the remaining 20% of tasks are broken — and you can't tell which 20% until everything else is solved, so the noise biases relative model rankings.

## Notable Quotes

> "Benchmaxing, of course, being when labs are training too hard on benchmarks in a way that deviates from what people actually care about."
>
> — [0:12](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=12s) &middot; *The talk's operative definition, stated crisply up front.*

> "It's past time for the Elm Marina people to sit down and think about whether they're doing more harm than good."
>
> — [1:38](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=98s) &middot; *Names a specific institution as net-negative, the talk's sharpest public call-out.*

> "unfortunately the teams are not getting better models overall but better Elm Marina models whatever that is possibly something with a lot of nested list bullet points and emojis"
>
> — [1:38](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=98s) &middot; *Karpathy's diagnosis of leaderboard-specific optimization, cited as outside corroboration.*

> "if you don't have the ability to assess if a benchmark is good, what you do have is the ability to assess what's popular"
>
> — [2:19](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=139s) &middot; *Explains the feedback loop that keeps bad benchmarks dominant.*

> "That's $15 million to make your benchmark. And if you think that over time about a third of those tasks are going to get washed away every year due to models getting better, that's $5 million to replace them."
>
> — [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s) &middot; *Puts a concrete price on quality benchmark construction and its ongoing maintenance.*

> "Like you can't push the frontier forward from within the frontier. You need to inject that external human expertise and it needs to be good expertise."
>
> — [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s) &middot; *Core argument against AI-generated benchmarks and LLM-as-judge, repeated later.*

> "Contamination is often thought of as when labs are explicitly training on the test set and that does happen sometimes but really contamination is the default outcome unless you are very very good."
>
> — [4:17](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=257s) &middot; *Reframes contamination from misconduct to baseline expectation.*

> "It does not disclose this contamination. We as an industry aren't really in the habit of doing those disclosures. And so what that means is that as benchmarking consumers, we're just missing that information."
>
> — [5:41](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=341s) &middot; *Specific disclosure failure attached to a named, current model card.*

> "Gradient descent is basically like water flowing downhill looking for the path of least resistance. And so your verifiers need to be robust to that."
>
> — [5:41](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=341s) &middot; *Compact framing of verifier design as adversarial rather than descriptive.*

> "Haiku scores 20% because it makes a bunch of mistakes and Fable scores 20% because it gets it right 80% of the time but then just happens to pick different formats."
>
> — [6:27](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=387s) &middot; *Reports a number and shows exactly how a verifier collapses real capability differences.*

> "Here's one that says write a riddle that includes exactly one bullet point. Make sure to include a few bullet points. Again this is just fully impossible."
>
> — [8:22](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=502s) &middot; *Concrete evidence that a widely cited benchmark contains unsolvable items.*

> "There's nothing in the verifier that checks that a story was written. It just checks that the asky character I is not used more than once, which means that all of these responses get a full score, including response D."
>
> — [9:03](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=543s) &middot; *The most damning single example of verifier–prompt misalignment plus reward hacking.*

> "the model is more likely to develop eval awareness where it realizes that it's being tested which undermines the entire exercise"
>
> — [9:44](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=584s) &middot; *Links synthetic data quality to eval awareness, a distinct and underrated failure mode.*

> "there is a point where you can keep hill climbing on a benchmark and the human eval stays flat. And you can actually take it even further if you want where you keep hill climbing on a benchmark even as the human eval goes down."
>
> — [11:17](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=677s) &middot; *States the mechanism of benchmaxxing in terms of divergence from the human-eval ground truth.*

> "you can actually hire a crowdsource army to vote for you in Elmarina since Elmarina basically does no filtering of their workforce"
>
> — [11:54](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=714s) &middot; *A direct, checkable accusation about arena vulnerability.*

> "in this instance, the specific chart we're seeing is that Meta tested 27 models without disclosing that it was doing so."
>
> — [12:44](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=764s) &middot; *Named-lab example of undisclosed testing distorting leaderboard results.*

> "as you're hill climbing you don't know what 20% are broken until you solve all the others"
>
> — [14:44](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=884s) &middot; *Reinterprets benchmark 'saturation' as measurement noise rather than capability ceiling.*

> "we believe that writing is just too rich and deep and nuanced and frankly human of an activity to measure with mechanical benchmarks and LM as a judge doesn't really work either because LLMs don't have good taste in writing"
>
> — [15:22](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=922s) &middot; *States the design thesis behind Hemingway Bench and a clear anti-LLM-judge position.*

> "it is quite expensive, right? Human eval is very expensive. Getting the time of these professionals is quite expensive. But again, our goal is to maximize quality, not to minimize costs."
>
> — [16:04](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=964s) &middot; *Names the central tradeoff the talk asks the industry to accept.*

## Positions

- Benchmark-reality divergence is not intrinsic to benchmarks; it is caused by incentives and poor methodology and can be fixed. ([0:59](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=59s), confidence: stated)
- LMArena does more harm than good and should be reconsidered by its operators. ([1:38](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=98s), confidence: stated)
- A serious 1,000-task agentic coding benchmark costs about $15M to build and ~$5M/year to maintain, which prices it out of most projects. ([3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s), confidence: stated)
- You cannot use AI assistance or cheap labor to build frontier-quality benchmarks — external human expertise must be injected. ([3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s), confidence: stated)
- Contamination is the default outcome for any public benchmark, not an occasional lapse. ([4:17](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=257s), confidence: stated)
- Opus has memorized substantial portions of SWE-bench Verified, and the Opus 4.8 model card reports SWE scores without disclosing this. ([4:58](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=298s), confidence: stated)
- A benchmark task that assigns the same score to a weak and a strong model for different reasons is not a useful task. ([7:02](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=422s), confidence: stated)
- IFEval is a poor benchmark: its prompts are unrealistic, some are logically impossible, and some verifiers don't check what the prompt asks. ([7:46](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=466s), confidence: stated)
- Benchmarks are aspirational artifacts expressing values, so building one requires product sense and taste, not just domain question-writing. ([7:46](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=466s), confidence: stated)
- Obviously synthetic benchmark data increases eval awareness and pushes models out of distribution, invalidating the measurement. ([9:44](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=584s), confidence: stated)
- Human evaluation is the ground truth all benchmarks are trying to approximate; benchmarks are lossy distillations of human preference. ([10:31](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=631s), confidence: stated)
- LMArena can be gamed by hiring crowdsourced voters, using model output watermarks to identify which response to vote for. ([11:54](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=714s), confidence: stated)
- Claimed benchmark saturation around 80% often reflects broken tasks rather than exhausted headroom, and that broken remainder biases model rankings. ([14:44](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=884s), confidence: stated)
- LLMs lack good taste in writing, so LLM-as-a-judge cannot validly evaluate writing quality. ([15:22](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=922s), confidence: stated)
- Journalists and others reporting on benchmarks share responsibility for benchmaxxing, alongside the labs and benchmark makers. ([16:48](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=1008s), confidence: stated)

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark saturation](../concepts/benchmark-saturation.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [reward hacking](../concepts/reward-hacking.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [verifier design](../concepts/verifier-design.md)

