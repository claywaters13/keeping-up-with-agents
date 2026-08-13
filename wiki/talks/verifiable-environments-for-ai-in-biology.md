---
title: "Verifiable Environments for AI in Biology"
type: "talk"
slug: "verifiable-environments-for-ai-in-biology"
track: "Autoresearch"
org: "LatchBio"
day: "Day 3 — Session Day 2"
room: "Main Stage"
video_id: "3ZMUiFaQ3qg"
duration_sec: 1062
word_count: 3308
speakers: ["George Cameron", "Micah Hill-Smith"]
---

# Verifiable Environments for AI in Biology

*Program title: Trends in AI*

**Speakers:** [George Cameron](../speakers/george-cameron.md), [Micah Hill-Smith](../speakers/micah-hill-smith.md)

**Org:** LatchBio

**Track:** Autoresearch &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 17m 42s

[Watch on YouTube](https://www.youtube.com/watch?v=3ZMUiFaQ3qg)

## Summary

Kenny Workman, co-founder and CTO of LatchBio, argues that data analysis can serve biology the way code served software: as a verifiable, executable substrate on which agents can be benchmarked and trained. He traces LatchBio's path from a data-infrastructure vendor for biotech to a 'vertical AI lab' that builds benchmarks and agents, starting with spatial biology, where single experiments can produce multiple terabytes and no consensus analysis pipeline exists. The core of the talk is benchmark design: SpatialBench (146 problems, released December) modeled loosely on SWE-bench, the three properties they demand of a good biological task (verifiable, durable across valid analysis paths, requiring interaction with data rather than recall), and what human verification revealed about ambiguous task statements and arbitrary numerical thresholds inherited from bioinformatics practice. He then reports on long-horizon tasks that simulate whole paper results sections — no model solves them yet — and on rubric-based grading via path-invariant 'choke points', which correlate only loosely with verifiable outcomes. Worth watching for anyone designing evals in a domain where ground truth is contested, or tracking how frontier labs are absorbing external scientific benchmarks.

## Key Points

- Biological data volume is growing log-linearly, driven by single-cell (2–6 TB per run), spatial (up to 7 TB per run), and proteomics (hundreds of GB), to the point where one experiment can exceed what a scientist can store on a laptop.
- The central thesis is that data analysis code is to biology what code was to software engineering: an executable, verifiable substrate that makes otherwise unverifiable scientific work benchmarkable and trainable.
- Frontier models can write code and know biology but cannot be trusted with real scientific work, because the missing capability is extracting insight from real-world experimental data.
- Because end-to-end outcome grading is too sparse when models are weak, LatchBio decomposes the analysis DAG into intermediate nodes and grades those with deterministic Python functions.
- Good biological evals must be verifiable by a function, durable across multiple valid analysis paths, and constructed so the answer requires interacting with data rather than recalling memorized knowledge.
- Human verification — scientists grading each other's work — exposed that many tasks were badly specified, leaving open choices like how to split a gene list, how to normalize, or what counts as an 'appropriate radius'.
- Writing evals forces more rigorous reasoning than doing the analysis yourself, and revealed that many canonical bioinformatics QC thresholds are arbitrary.
- Long-horizon tasks simulating full paper results sections take a team of three about a week each to author, and no current model solves the metastatic-niche reconstruction example.
- Rubrics built from path-invariant choke points correlate with verifiable outcomes but only loosely, so the team does not yet trust them for RL or benchmarking.
- In a new biosecurity collaboration, red-team tasks disguised as innocuous requests (e.g. cloning a claimed GFP gene that is actually a toxin) are refused far less often than routine tasks are answered.

## Notable Quotes

> "Single cell experiments can yield two to six terabytes per run. Spatial runs can yield seven terabytes of run. Proteomics a few hundred gigs."
>
> — [1:30](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=90s) &middot; *concrete scale numbers that motivate the whole infrastructure argument*

> "the output of a single experiment can exceed what a scientist can safely store on a consumer laptop in many cases"
>
> — [1:30](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=90s) &middot; *vivid framing of why agents and remote compute are necessary in bio*

> "just like code provided a verifiable substrate for complex software tasks that are not inherently verifiable, uh data analysis might do the same thing in bio"
>
> — [2:47](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=167s) &middot; *the thesis of the talk in one sentence*

> "there became this strong interaction uh with the agents uh using the infrastructure components as tools and the loop context you guys are familiar with. Except in our domain, the tools can take days or weeks."
>
> — [3:28](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=208s) &middot; *names the key difference between bio agent loops and coding agent loops*

> "It became clear to us at this time that agentic biology might look a lot like code."
>
> — [4:44](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=284s) &middot; *the analogy that structures LatchBio's entire strategy*

> "frontier models cannot be trusted to do real work. They're missing some capability between knowing biology and writing code. And this is exactly extracting scientific insight from real-world data."
>
> — [5:23](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=323s) &middot; *a sharp capability claim that others might contest*

> "the existing benchmarks we saw at the time did not measure the tasks relevant to this category of work"
>
> — [7:16](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=436s) &middot; *justifies building a new benchmark rather than reusing Q&A-style science evals*

> "the the grading of these end outcomes in biology uh is too sparse because the models are pretty bad. So, you have to break things up into manageable chunks to get some semblance of verifiability."
>
> — [7:50](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=470s) &middot; *states the core eval-design tradeoff between task realism and reward density*

> "A task prompt carefully describing some scientific goal, configuration for a grader, and then a deterministic grader, so a Python function. If you guys notice, this looks a lot like SweetBench."
>
> — [8:33](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=513s) &middot; *spells out the eval schema and its explicit debt to SWE-bench*

> "Durability is particularly important. Science does not admit clear ground truth."
>
> — [9:05](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=545s) &middot; *the distinguishing constraint of scientific evals versus code evals*

> "if you are lazy with your ground truth construction of the task, a possible valid analysis path can come with the correct answer, um and you'll fail it uh incorrectly"
>
> — [9:05](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=545s) &middot; *names a specific, common failure mode in benchmark authoring*

> "You want the conclusion to require interaction with the data, not some memorized knowledge. In practice, that's pretty difficult."
>
> — [9:37](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=577s) &middot; *the anti-memorization criterion, with an honest admission of difficulty*

> "in the absence of like a canonical answer, uh having a bunch of scientists grade each other's work ended up being like the best proxy"
>
> — [10:15](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=615s) &middot; *the fallback method when deterministic ground truth is unavailable*

> "How do you split the gene list? How do you count what inflammatory genes are? It's like somewhat ambiguous word. How do you normalize the data? Um what what what the hell is an appropriate radius?"
>
> — [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s) &middot; *concrete illustration of task ambiguity only surfaced by human verification*

> "cool thing about evaluation like coding is it forces you to reason about things more rigorously than you would when you're doing the thing yourself"
>
> — [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s) &middot; *argues eval writing has epistemic value for the field independent of AI*

> "these tasks took like a week for a group of three people to make each"
>
> — [12:39](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=759s) &middot; *quantifies the authoring cost of long-horizon scientific evals*

> "None of the models get this right. Um but they're getting there."
>
> — [13:11](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=791s) &middot; *current state of the art on the hardest tasks in their set*

> "they're associated with the verifiable outcomes, uh which is exciting, but they're loosely correlated numerically, um making us not fully have confidence in them for things like RL or benchmarking"
>
> — [13:46](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=826s) &middot; *an unusually candid negative result about rubric grading*

> "We found that the routine tasks like drastic get drastic used drastically more frequently than the red team tasks, which is uh not great."
>
> — [16:29](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=989s) &middot; *the headline biosecurity finding: models comply with disguised harmful requests*

> "We try to get the labs to compete um on the benchmarks cuz then it makes the models better at our products."
>
> — [17:03](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=1023s) &middot; *explains the business flywheel behind publishing open benchmarks*

## Positions

- Data analysis code can serve as a verifiable substrate for biology in the same way code did for software engineering, enabling benchmarking and capability gains. ([2:47](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=167s), confidence: stated)
- Frontier models cannot currently be trusted to do real scientific work; the gap between knowing biology and writing code is extracting insight from real-world experimental data. ([5:23](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=323s), confidence: stated)
- Existing biology benchmarks measure Q&A-style academic knowledge rather than the data-analysis tasks that constitute actual research work. ([7:16](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=436s), confidence: stated)
- End-to-end outcome grading in biology is too sparse a signal given current model ability, so tasks must be decomposed into intermediate analysis-DAG nodes. ([7:50](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=470s), confidence: stated)
- A good biological eval must be durable — invariant across the multiple valid analysis paths a scientist could take — or it will incorrectly fail correct work. ([9:05](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=545s), confidence: stated)
- Human verification, with scientists grading each other's work, is the best available proxy for ground truth in science and is necessary to expose badly specified tasks. ([10:15](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=615s), confidence: stated)
- Many canonical numerical QC thresholds in bioinformatics are arbitrary, and building evals exposes this by forcing more rigorous reasoning than doing the analysis oneself. ([10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s), confidence: stated)
- Rubric scores built from path-invariant choke points correlate only loosely with verifiable outcomes and are not yet trustworthy for RL or benchmarking. ([13:46](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=826s), confidence: stated)
- Verifiability structure, rather than scale alone, is what will continue to drive intelligence gains in this domain. ([13:46](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=826s), confidence: stated)
- Current models refuse disguised harmful biology requests far less often than they answer routine ones, which is a safety problem best framed as an evaluation problem. ([16:29](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=989s), confidence: stated)
- The multi-agent trajectory seen in software engineering — a faulty single agent improving until teams of agents can be orchestrated — will repeat in science. ([5:23](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=323s), confidence: stated)
- Publishing benchmarks that frontier labs adopt is a viable commercial strategy, because lab competition on those benchmarks directly improves the vendor's own products. ([17:03](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=1023s), confidence: stated)

## Concepts

- [agentic science](../concepts/agentic-science.md)
- [benchmark design](../concepts/benchmark-design.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [reward design](../concepts/reward-design.md)
- [rubric design](../concepts/rubric-design.md)
- [verifier design](../concepts/verifier-design.md)

