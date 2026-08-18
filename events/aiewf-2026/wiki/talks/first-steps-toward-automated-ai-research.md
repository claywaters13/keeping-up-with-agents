---
title: "First Steps Toward Automated AI Research"
type: "talk"
slug: "first-steps-toward-automated-ai-research"
track: "Autoresearch"
org: "CEO Recursive AI"
day: "Day 3 — Session Day 2"
room: "Main Stage"
video_id: "pWXUkLP9uWM"
duration_sec: 1223
word_count: 3301
speakers: ["Richard Socher"]
---

# First Steps Toward Automated AI Research

**Speakers:** [Richard Socher](../speakers/richard-socher.md)

**Org:** CEO Recursive AI

**Track:** Autoresearch &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 20m 23s

[Watch on YouTube](https://www.youtube.com/watch?v=pWXUkLP9uWM)

## Summary

Richard Socher argues that the ultimate goal of AI should be a "Eureka machine" — a system that automates scientific discovery and eventually invents most of humanity's future inventions. He frames this as a continuation of open-ended evolution (biological → technological → scientific → AI), invoking Popper's view of theory selection as natural selection and Stanisław Lem's warning that scientific growth is bottlenecked by the shrinking number of people per subfield. He sketches four pillars for such a machine — existing knowledge, measurement data, simulation, and a physical lab — coordinated by an agent swarm, and argues the fastest path is recursive self-improvement, now feasible because AI is code and can code over long horizons. The concrete payload is three results from Recursive's auto-research system: pushing NanoChat's bits-per-byte from 0.93 to 0.91 in a day or two with genuinely novel architectural ideas, beating the NanoGPT speedrun record by over two seconds, and discovering CUDA kernels that beat Nvidia's leaderboard bests. Worth watching for the empirical proof points and for a clear articulation of what does and does not count as true RSI.

## Key Points

- Socher frames automated science as his personal moonshot — a "Eureka machine" that automates the full ideation → implementation → validation loop across physics, chemistry, biology, medicine, economics and beyond.
- The historical argument is that evolution, technology, and science are all open-ended selection processes, and that more science compounds into more technology, more growth, and more human flourishing.
- Citing Stanisław Lem, he argues exponential scientific growth will be halted not by ideas but by the lack of people available to staff each increasingly narrow subfield — which is the case for automating discovery.
- The Eureka machine rests on four pillars: existing human knowledge, scientific measurement data, simulation for what can't yet be measured, and a physical industrial lab for real-world experiments, with an agent swarm on top.
- He distinguishes auto-research (an AI improving some other system, e.g. a NanoChat run) from true recursive self-improvement, which requires self-awareness of shortcomings plus write access across pre-training, RL, and harnesses to produce the next version of itself.
- Concrete results: NanoChat bits-per-byte improved from the community's 0.93 to 0.91 in a day or two, with novel ideas like hash bi-gram and tri-gram embeddings gated into attention value paths rather than mere hyperparameter tuning.
- The system beat a NanoGPT speedrun benchmark that humans-plus-AI had worked on for over a year, shaving more than two seconds to reach 70 seconds, and found CUDA kernels beating Nvidia's leaderboard bests despite the team having no dedicated kernel experts.
- He argues every layer of human-facing infrastructure — web search, browsers, GPUs — should be rebuilt for agents, noting agents can consume thousands of long snippets rather than ten blue links, and that this is a large startup opportunity.
- On timelines and limits: he expects AI to go from worse than humans at everything to better at any specific task in roughly 30 years, and claims we remain astronomically far from the upper bounds of intelligence across every dimension he measures.

## Notable Quotes

> "we're like too late to explore Earth, we're too early to explore the stars, but we're right on time to build an AI that could actually do what flying did for some in one lifetime due to intelligence."
>
> — [5:51](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=351s) &middot; *The talk's framing thesis about generational timing, stated in one line.*

> "most of us are going to be excited about it cuz it means that we'll all become managers of such an AI rather than having to do the nitty-gritty ourselves."
>
> — [2:13](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=133s) &middot; *A deliberately provocative claim to a room of AI engineers about their own obsolescence.*

> "the exponential growth of science will actually be at some point halted by the lack of people working on it"
>
> — [8:37](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=517s) &middot; *The Lem-derived bottleneck argument that motivates automating research at all.*

> "more science lead to more technology which will lead to more growth which lead to more human flourishing."
>
> — [7:54](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=474s) &middot; *Compresses the entire techno-optimist causal chain the talk rests on.*

> "Anything you can simulate, you can verify, and you can then solve with AI. And if all else fails, or at the very end of these processes, you still need to have some kind of physical industrial like lab that actually can run real experiments in the real world."
>
> — [9:34](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=574s) &middot; *States the verification-drives-solvability principle plus the concession that physical experiment can't be eliminated.*

> "it's clear over and over again in AI that when we take out a manual process and we replace it with a learned system, improvements will follow."
>
> — [12:34](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=754s) &middot; *The bitter-lesson-style induction that justifies handing AI research to AI.*

> "This this ability to really code in longer and longer time horizons has really only happened in the last like 6 to 8 months."
>
> — [12:34](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=754s) &middot; *Dates the capability unlock that he claims makes RSI newly feasible.*

> "True recursive self-improvement is when you have an AI that has a sense of self-awareness of its own shortcomings"
>
> — [14:13](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=853s) &middot; *Draws the definitional line he uses to deflate looser RSI claims.*

> "And that is really exciting and it's an important milestone, but it's not actual RSI."
>
> — [15:02](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=902s) &middot; *Rare self-deflation of his own demo's significance.*

> "the whole community had worked on this for quite some time and got to 0.93 and after training this for a little more than a day or two, we basically got it down to 0.91."
>
> — [15:55](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=955s) &middot; *The headline number for the NanoChat result.*

> "it actually did find truly interesting novel ideas like hash bi-grams and tri-gram embeddings and tables for those and mixing that into various value paths of the intention through variety of learned gates."
>
> — [15:55](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=955s) &middot; *Specifies the discovered mechanism, which is his evidence that this exceeds hyperparameter search.*

> "after very short amount of time it got better than people working often together with the AI for over a year on on this very on this benchmark and made the whole thing another two seconds over two seconds faster at 70 seconds."
>
> — [16:42](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1002s) &middot; *Reports the NanoGPT speedrun result against a strong human+AI baseline.*

> "it's actually kind of shocking how inefficient a lot of mixture of expert models still are running very large clusters that cost billions of dollars and then only have like 30% or so utilization."
>
> — [16:42](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1002s) &middot; *A concrete efficiency number motivating automated kernel work.*

> "after a couple days it discovered better kernels than the leader boards best on the Nvidia benchmark website by again quite quite a sizable margin across all the different categories of those kernels."
>
> — [17:33](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1053s) &middot; *The strongest empirical claim in the talk.*

> "we do just enough to make sure and work together with Nvidia to make sure that there no reward hacks here"
>
> — [18:23](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1103s) &middot; *Acknowledges reward hacking as the main failure mode for auto-research results.*

> "Agents can read thousands of very long snippets, rather than just 10 blue links with like a very short snippet."
>
> — [11:08](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=668s) &middot; *Crisp statement of why human-facing infrastructure needs rebuilding for agents.*

> "there are a lot of startups possible in rethinking every single one of the layers of technology as infrastructure for superintelligence"
>
> — [10:20](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=620s) &middot; *Names the market thesis behind the technical argument.*

> "on the upper bounds of intelligence, we're still astronomically far away from reaching those"
>
> — [19:16](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1156s) &middot; *His answer to the 'when does the exponential flatten' question that closes the talk.*

## Positions

- There is no material problem that cannot be solved with more technology. ([4:18](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=258s), confidence: stated)
- The exponential growth of science will be halted by the lack of people available to work on each narrow subfield, not by a shortage of problems. ([8:37](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=517s), confidence: stated)
- The best way to build superintelligence is to have it build itself via recursive self-improvement, rather than through human architecture engineering. ([11:55](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=715s), confidence: stated)
- Whenever a manual process in AI is replaced by a learned system, improvements follow. ([12:34](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=754s), confidence: stated)
- Long-horizon coding ability only emerged in the last 6 to 8 months, and that is what makes recursive self-improvement newly possible. ([12:34](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=754s), confidence: stated)
- NanoChat-style auto-research is not true recursive self-improvement; true RSI requires an AI with self-awareness of its shortcomings and full access from pre-training through RL and harnesses to update its own next version. ([14:13](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=853s), confidence: stated)
- Recursive's system improved NanoChat bits-per-byte from the community best of 0.93 to 0.91 in a little more than a day or two. ([15:55](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=955s), confidence: stated)
- The system's NanoChat gains came from genuinely novel architectural ideas (hash bi-gram/tri-gram embeddings mixed into attention value paths via learned gates), not hyperparameter tuning. ([15:55](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=955s), confidence: stated)
- The system beat a NanoGPT speedrun benchmark that humans working with AI had pushed on for over a year, improving it by more than two seconds to 70 seconds. ([16:42](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1002s), confidence: stated)
- Many mixture-of-expert models run on billion-dollar clusters at only around 30% utilization. ([16:42](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1002s), confidence: stated)
- The system discovered CUDA kernels beating Nvidia's benchmark leaderboard bests across all categories within a couple of days, despite the team having no dedicated kernel experts. ([17:33](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1053s), confidence: stated)
- AI will move from being worse than humans at everything to better at any specific task within roughly 30 years, faster than the 60-year flight-to-moon analogue. ([6:30](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=390s), confidence: stated)
- Infrastructure layers built for humans — search, browsers, GPUs — should be rebuilt for AI agents, and doing so is a large startup opportunity. ([10:20](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=620s), confidence: stated)
- We are astronomically far from the upper bounds of intelligence across every dimension, so the AI exponential is nowhere near flattening. ([19:16](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1156s), confidence: stated)
- AI engineers will shift from doing the work to managing AI systems that do AI research. ([2:13](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=133s), confidence: implied)

## Concepts

- [agentic retrieval](../concepts/agentic-retrieval.md)
- [agentic science](../concepts/agentic-science.md)
- [benchmark saturation](../concepts/benchmark-saturation.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [reward hacking](../concepts/reward-hacking.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [simulation environments](../concepts/simulation-environments.md)

