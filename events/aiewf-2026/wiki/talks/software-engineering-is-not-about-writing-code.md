---
title: "\"Software engineering is not about writing code\""
type: "talk"
slug: "software-engineering-is-not-about-writing-code"
track: "Google DeepMind"
org: "Google DeepMind VP of Research"
video_id: "1P1hJ36rxM0"
duration_sec: 1226
word_count: 3198
speakers: ["Benoit Schillings"]
---

# "Software engineering is not about writing code"

**Speakers:** [Benoit Schillings](../speakers/benoit-schillings.md)

**Org:** Google DeepMind VP of Research

**Track:** Google DeepMind &nbsp;|&nbsp; **Duration:** 20m 26s

[Watch on YouTube](https://www.youtube.com/watch?v=1P1hJ36rxM0)

## Summary

Benoit Schillings, VP of Research at Google DeepMind, argues that the era in which writing code was the expensive, bottleneck activity in software has ended, and that the discipline should reorganize around what remains hard: specification, architecture, security, and verification. He traces three eras of software — machine-limited assembly, human-brain-limited modular design, and the current AI frontier — and claims models already exceed humans at syntax-level generation while still struggling with multi-step changes across huge codebases and cross-domain transfer. With human-written training data running out (he estimates 80% of new GitHub code is machine-generated), he sees self-play, in the AlphaZero mold, as the path to superhuman coding, bounded mainly by compute. He calls for new benchmarks with open-ended loss functions instead of pass/fail harnesses, languages designed for models rather than humans (possibly not human-readable), models trained to write secure code from the start rather than patch vulnerabilities after, and multimodal/spatial reasoning about programs. He closes on code as a universal experimental substrate for chemistry and biology, and on the breakthroughs humans are structurally biased not to see. Worth watching for a frontier-lab research leader's concrete agenda for what comes after code generation is solved.

## Key Points

- Software has passed through three limiting constraints — machine capability, then human cognitive capacity for modular design, and now an AI frontier where generating code is no longer the hard part.
- Frontier models have achieved superhuman syntax-level code generation, but multi-step changes across large legacy codebases and long-horizon architectural judgment remain open frontiers.
- Code was uniquely tractable for ML because of the abundance of scrapable training data and because verification is cheap: you can compile it, run it, and unit-test it.
- Human-written training data is running out — Schillings estimates 80% of new code added to GitHub is machine-generated — so self-play, in the AlphaZero mold, becomes the engine of further progress, bounded largely by available compute.
- As writing code becomes free, code volume will explode and humans will stop reading it, much as compiler users stopped reading assembly output, which demands new process and guardrails rather than more code review.
- Vulnerability-patching is a treadmill: smarter models will keep finding subtler flaws, so the real goal is training models to write correct, secure code from the start — hard because correctness is deeply context-dependent.
- Benchmarks like SWE-bench only check whether code runs and produces the right output; evaluation should include open-ended problems with continuous loss functions (e.g. write the best lossless compressor, scored on compressed size plus source size) that force novel algorithms.
- It may be time to design programming languages for models rather than humans — strongly typed, proof-oriented, inspired by Lean — since the pain of writing verbose safe code no longer applies and human readability may no longer matter.
- Programming is a visual, spatial activity for humans, so multimodal models that reason in spatial and dynamic representations rather than pure token chains are likely a must-have for real software engineering.
- Because experimentation in code is nearly free, the intersection of code with atoms — chemistry beyond ~20-atom molecules, undocumented biology — is where genuine novelty will appear.

## Notable Quotes

> "Software engineering is not about writing code. Software engineering is the first time you join a company and you realize that there are 35 million lines of PHP in the codebase and that you need to make some changes."
>
> — [7:29](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=449s) &middot; *the thesis of the talk, stated as a concrete image rather than an abstraction*

> "I think that 80% of the new code added to GitHub today is machine generated."
>
> — [9:33](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=573s) &middot; *a specific, checkable number underpinning his data-exhaustion argument*

> "We're now in a world where writing code is free or nearly free. That's why I've got the tilda there."
>
> — [10:58](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=658s) &middot; *names the economic shift the rest of the talk builds on*

> "I would predict that in one year we'll let Gemini or other model generate the code and nobody will actually look at it."
>
> — [11:42](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=702s) &middot; *a dated, falsifiable prediction that many practitioners would dispute*

> "My team goal in deep mind is basically to develop whatever technology will be needed to make Gemini incredible between one months and one year from now."
>
> — [1:16](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=76s) &middot; *defines the speaker's mandate and the horizon his claims are calibrated to*

> "Alpha Zero became a superhuman go and chess player without any human knowledge just by playing against itself."
>
> — [9:33](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=573s) &middot; *the precedent he uses to argue self-play can replace exhausted human code data*

> "Take a a brilliant software engineer, lock him in a room, lock him or her in a room for two years and feed pizza and give the mission you need to become a better software engineer."
>
> — [10:18](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=618s) &middot; *his intuition pump for why self-play should work for software, not just games*

> "It is also a domain where doing verification is reasonable. You can run a piece of code, you can compile it, you can have unit test."
>
> — [8:53](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=533s) &middot; *states the verifiability property that made code the first domain to fall*

> "instead of detecting the vulnerability and then suggesting some fix how about teaching model to write correct things from the start and that is very very hard to do because it is very context dependent"
>
> — [12:29](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=749s) &middot; *names his team's actual security research direction and admits why it is hard*

> "threebench is infamous in in my book because threebench verifies if a piece of code runs and produce the right output"
>
> — [14:10](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=850s) &middot; *a direct criticism of the field's dominant coding benchmark*

> "You just take a piece of 10 megabyte of code and you tell the model write the best compressor you can that is lossless"
>
> — [14:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=889s) &middot; *concrete proposal for an open-ended eval with a continuous, unbounded loss*

> "How about we make writing the code much harder by having you know very strongly typed languages or you know some inspiration from lean on how to write code that by design it's not going to be perfect."
>
> — [17:17](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1037s) &middot; *inverts the usual ergonomics argument now that the writer is a model*

> "So, I don't know if we have some language designers here, but I I I think there's something really to be done there and it doesn't need to be human readable."
>
> — [17:17](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1037s) &middot; *the most contrarian design claim in the talk*

> "Some people were talking about vibe coding writing code in English and at the time honestly I totally dismissed that. I was that's why we have programming language. English is not a programming language."
>
> — [3:33](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=213s) &middot; *a frontier-lab leader owning a wrong prediction, which frames his epistemic stance*

> "Uh a traditional human typical human is able to get the context between seven and nine tokens."
>
> — [5:19](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=319s) &middot; *the human working-memory limit he says silently shaped all of modular software design*

> "this ability to experiment very quickly in code is impacting other domain very quickly because doing experiment becomes basically free"
>
> — [17:55](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1075s) &middot; *the bridge from coding progress to scientific progress*

> "biology is the case of nature did an incredible engineering job and terrible job at documentation"
>
> — [18:41](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1121s) &middot; *memorable framing of why ML pattern-finding suits biology*

> "Humans are incredibly biased in what we feel is the correct solution. I mean, we're the result of an evolutionary training that help us survive in the jungle, right? Not doing quantum computing."
>
> — [19:20](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1160s) &middot; *the closing argument for why models will find solutions humans structurally cannot*

## Positions

- Models have already surpassed humans at generating individual functions and other syntax-level code; that competition is settled. ([6:47](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=407s), confidence: stated)
- Roughly 80% of new code added to GitHub today is machine-generated, so mining human-written code for training data is reaching an end. ([9:33](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=573s), confidence: stated)
- Self-play — models generating their own coding challenges and judging the answers — is what will produce superhuman coding, and the limiting factor is compute and self-play time. ([10:18](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=618s), confidence: stated)
- Within about a year, generated code will ship without any human reading it, analogous to how nobody inspects compiler assembly output. ([11:42](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=702s), confidence: stated)
- Detecting and patching vulnerabilities is a never-ending treadmill; the correct approach is teaching models to write correct code from the start. ([12:29](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=749s), confidence: stated)
- SWE-bench-style benchmarks that only check whether code runs and produces correct output measure only a small part of software engineering. ([14:10](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=850s), confidence: stated)
- Benchmarks should include open-ended problems with continuous loss functions, such as compression scored on compressed size plus source size, to force models to invent novel algorithms. ([14:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=889s), confidence: stated)
- Existing languages like Python were designed for humans and are not good for writing safe or reliable code; a new model-oriented language should be created and need not be human-readable. ([17:17](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1037s), confidence: stated)
- Treating code purely as a chain of emitted tokens has limits; spatial and dynamic multimodal representations will become a must-have for software reasoning. ([15:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=949s), confidence: stated)
- Current models are still weak at transferring knowledge across domains and at intersecting concepts, which is required for building genuinely complex systems. ([12:29](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=749s), confidence: stated)
- Humans retain a durable near-term edge in architecture, specification of intent, and inductive pattern-detection over wide context. ([6:01](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=361s), confidence: stated)
- The software industry's culture, infrastructure, and company formation are built on the now-false assumption that writing code is the expensive part. ([10:58](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=658s), confidence: stated)
- The biggest true novelty from AI will come at the intersection of code and physical science — chemistry and biology — because experimentation there becomes essentially free. ([17:55](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1075s), confidence: stated)
- Human evolutionary bias hides whole classes of solutions, so ML's different viewpoint will surface breakthroughs that were in front of us the whole time. ([19:20](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1160s), confidence: stated)

## Concepts

- [agent-readable codebases](../concepts/agent-readable-codebases.md)
- [benchmark design](../concepts/benchmark-design.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [secure code generation](../concepts/secure-code-generation.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)
- [verifier design](../concepts/verifier-design.md)
- [vision-language models](../concepts/vision-language-models.md)

