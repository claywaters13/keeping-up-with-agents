---
title: "How Autoresearch is changing ML research"
type: "talk"
slug: "how-autoresearch-is-changing-ml-research"
track: "Autoresearch"
org: "Weco"
day: "Day 4 — Session Day 3"
room: "Expo Stage 2 NW"
video_id: "iCj_ATyThvc"
duration_sec: 976
word_count: 1796
speakers: ["Zubin Aysola"]
---

# How Autoresearch is changing ML research

*Program title: ARIA, how we built autoresearch with autoresearch*

**Speakers:** [Zubin Aysola](../speakers/zubin-aysola.md)

**Org:** Weco

**Track:** Autoresearch &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Expo Stage 2 NW &nbsp;|&nbsp; **Duration:** 16m 16s

[Watch on YouTube](https://www.youtube.com/watch?v=iCj_ATyThvc)

## Summary

Zhengyao Jiang, co-founder and CEO of Weco, reports on sending their autonomous research agent 'Aiden' into OpenAI's Parameter Golf hiring competition, where it ran for 22 days and set seven leaderboard records versus three for the best human, while achieving the highest H-index (10 vs. 7 for the top human) for PRs other participants built on. The talk's central argument is that the interesting test of an auto-research agent is not benchmark hill-climbing but whether a human community recognizes, merges, and builds on its work. Jiang breaks down where the agent's power actually comes from — tireless throughput (1,300 experiments on one H100 node using at most 4% of total competition compute), a ~6x higher hit rate than the community average, and strong execution on ideas mostly sourced from human papers and forum posts rather than original invention. He then argues that auto-research shifts the valuable human skills upward: your codebase abstraction is the architecture and your eval is the loss function, illustrated with a fraud-detection case where tightening a loose API drove data leakage from significant to zero. Worth watching if you want a concrete, numbers-backed account of human-AI division of labor in ML research rather than another benchmark chart.

## Key Points

- In OpenAI's Parameter Golf competition, roughly 1,000 participants filed 2,000 submissions but only 47 passed open review, and seven of those leaderboard entries came from agents.
- Weco's Aiden agent set seven leaderboard records over 22 days while the best human set three, and its PRs earned an H-index of 10 versus 7 for the next human, meaning the community actively built on its work.
- Aiden ran about 1,300 experiments on a single H100 node, used at most 4% of the competition's total compute, produced ~15% of the records, and got 28% of its submissions onto the leaderboard — roughly six times the community average hit rate.
- The agent did not win through massive parallelization; it won on sustained throughput combined with high per-submission quality, effectively raising the signal-to-noise ratio of the community's public PR channel.
- Nearly all of Aiden's record-setting ideas were sourced from human research papers, other participants, or adjacent communities like nanoGPT — including ideas humans had abandoned over implementation difficulty — with only a small fraction originating from the agent itself.
- A representative record combined a gated-attention idea from a Qwen paper, a quantization scheme the agent devised to fit the 16MB file-size limit, and another contributor's tokenizer improvement, which together produced a large synergistic jump.
- Jiang frames auto-research as analogous to model training: the codebase abstraction plays the role of architecture (biasing the search space) and the eval plays the role of loss function and data (defining what gets optimized).
- In a fraud-detection pipeline, a loose API that let one function process both train and test data produced great-looking but leakage-polluted scores; tightening the API to prevent test data reaching training dropped the leakage rate to zero.
- Competition and benchmark design itself becomes high-leverage work in the auto-research era, since a bad design can render an entire community's effort useless.
- Proprietary evaluation data and domain-specific judgment about what to measure are where defensible vertical moats will form as auto-research systems get stronger.

## Notable Quotes

> "The top contributor was one candidate that they couldn't hire. It wasn't a person, it's an agent we build called Aiden."
>
> — [0:01](https://www.youtube.com/watch?v=iCj_ATyThvc&t=1s) &middot; *The framing hook that sets up the whole talk's claim.*

> "About 1,000 machine learning engineers, researchers participate. They fired 2,000 submissions. Only 47 passed open review and made into the leaderboard. Seven of those are actually agents."
>
> — [0:01](https://www.youtube.com/watch?v=iCj_ATyThvc&t=1s) &middot; *Establishes the competition's scale and selectivity with concrete numbers.*

> "Can the auto research agent produce work that a human community actually recognize beyond a good score agent is optimizing for something that other engineers can merge fork and build on."
>
> — [1:17](https://www.youtube.com/watch?v=iCj_ATyThvc&t=77s) &middot; *States the talk's central research question and its departure from benchmark-chasing.*

> "By the end, Aid has set seven leaderboard records. Each one is a new best for the competition stampled by OpenAI and the best human only made three."
>
> — [2:18](https://www.youtube.com/watch?v=iCj_ATyThvc&t=138s) &middot; *The headline result, with an explicit human baseline.*

> "Roughly if you have X papers get cited X times then your Ach index is X. Computed over PRs. Aiden was 10 and the next human was seven."
>
> — [3:26](https://www.youtube.com/watch?v=iCj_ATyThvc&t=206s) &middot; *Introduces the community-adoption metric that distinguishes this claim from a leaderboard score.*

> "Over 22 days, it ran about 1,300 experiments on a single H100 node. But the throughput isn't the whole picture. A well tuned AI system can also keep its output quality high."
>
> — [3:26](https://www.youtube.com/watch?v=iCj_ATyThvc&t=206s) &middot; *Quantifies the compute footprint and refuses the pure-brute-force explanation.*

> "On the compute side, it uses at most 4% of competition's total compute. and it made about 15% of the records. Also, 28% of its submissions made the leaderboard. Roughly six times higher heat rate than the community average."
>
> — [4:30](https://www.youtube.com/watch?v=iCj_ATyThvc&t=270s) &middot; *The densest set of efficiency numbers in the talk.*

> "It didn't win through massive paralization even though auto research have a tons of a potential of paralyzation."
>
> — [4:30](https://www.youtube.com/watch?v=iCj_ATyThvc&t=270s) &middot; *Explicitly rules out the most common skeptical explanation for agent leaderboard wins.*

> "By those numbers it might feel like auto research already dominates human experts on ML engineering and research but that's not the full story I want to tell."
>
> — [4:30](https://www.youtube.com/watch?v=iCj_ATyThvc&t=270s) &middot; *Marks the turn from results to the more nuanced division-of-labor argument.*

> "When we trace the ideas, Aiden Aiden's record PR almost all of them come from human research papers other participants in parameter golf or in similar communities like nano GBT."
>
> — [5:38](https://www.youtube.com/watch?v=iCj_ATyThvc&t=338s) &middot; *The key limiting finding: the agent's wins were sourced from human creativity.*

> "There are also a very small fraction of original ideas Aiden came up by itself which emerged from its efforts to navigate the file size constraints."
>
> — [5:38](https://www.youtube.com/watch?v=iCj_ATyThvc&t=338s) &middot; *Honestly bounds the agent's originality and locates where it did emerge.*

> "So Aiden picked up an idea from Quen paper called gated attention and it worked but it introduced more parameters and it broke the 16 megapy file size limit."
>
> — [5:38](https://www.youtube.com/watch?v=iCj_ATyThvc&t=338s) &middot; *Grounds the abstract claim in a specific, traceable technical episode.*

> "Most of them are just a good execution. But in reality, execution is a mostly the bottleneck. What moves the frontier is usually exactly some belief on existing ideas and tons of good executions."
>
> — [8:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=490s) &middot; *The load-bearing opinion about what actually advances ML research.*

> "To step back, the state of a human AI collaboration is a human collectively provide a lot of creative ideas and agent do the execution to solve a concrete challenge."
>
> — [8:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=490s) &middot; *Crisp summary of the human-AI division of labor he observed.*

> "A bad design can make the whole community effort useless and their evil design work will have a few huge leverage in the auto research era."
>
> — [9:19](https://www.youtube.com/watch?v=iCj_ATyThvc&t=559s) &middot; *Argues benchmark/competition design is the newly scarce skill.*

> "I really like one tweet from Andre Kapasi about 10 years ago where he said greeting descent can write code better than you."
>
> — [9:19](https://www.youtube.com/watch?v=iCj_ATyThvc&t=559s) &middot; *The central analogy the rest of the talk is built on.*

> "I think how gradient descent change coding is a great metaphor for how auto research will change research and ML engineering."
>
> — [10:15](https://www.youtube.com/watch?v=iCj_ATyThvc&t=615s) &middot; *States the analogy as an explicit forecast about job displacement and creation.*

> "Your codebased abstraction is essentially the architecture. It sets the constraint and the priorities um for what the agent can explore. Your eval is the loss function and the data."
>
> — [11:06](https://www.youtube.com/watch?v=iCj_ATyThvc&t=666s) &middot; *The talk's most reusable conceptual mapping for practitioners.*

> "and a good evaluation would be amplified more and more as auto research are getting stronger. The other one I think is really underrated is codebased abstraction."
>
> — [12:01](https://www.youtube.com/watch?v=iCj_ATyThvc&t=721s) &middot; *Names evals and abstraction as the compounding leverage points.*

> "We then tighten the obstruction to a more strict API where the test data couldn't reach the training and the data leakage rate just dropped to zero."
>
> — [14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s) &middot; *Concrete evidence that API design controls reward hacking.*

> "So my point is using auto research is a new craft. It's about the designing a here for an agent to climb and we are still very early on it."
>
> — [14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s) &middot; *The prescriptive thesis for the audience.*

> "So the search is automated. the human would just move up the stack not out of it."
>
> — [15:04](https://www.youtube.com/watch?v=iCj_ATyThvc&t=904s) &middot; *The talk's one-line conclusion on what happens to human researchers.*

## Positions

- The right test of an auto-research agent is whether a human community merges, forks, and builds on its work — not just its benchmark score. ([1:17](https://www.youtube.com/watch?v=iCj_ATyThvc&t=77s), confidence: stated)
- Aiden set seven Parameter Golf leaderboard records in 22 days while the best human participant set three. ([2:18](https://www.youtube.com/watch?v=iCj_ATyThvc&t=138s), confidence: stated)
- Aiden's PR H-index was 10 versus 7 for the next-highest human, making it the highest-impact contributor in the community. ([3:26](https://www.youtube.com/watch?v=iCj_ATyThvc&t=206s), confidence: stated)
- The agent's advantage came from quality plus tireless iteration rather than parallelization or compute scale — it used at most 4% of total competition compute while producing ~15% of records. ([4:30](https://www.youtube.com/watch?v=iCj_ATyThvc&t=270s), confidence: stated)
- Almost all of the agent's record-setting ideas originated from humans (papers, other participants, adjacent communities); genuinely original agent ideas were a very small fraction. ([5:38](https://www.youtube.com/watch?v=iCj_ATyThvc&t=338s), confidence: stated)
- Execution, not idea generation, is the main bottleneck in ML research, so agents that execute well move the frontier. ([8:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=490s), confidence: stated)
- Competition and benchmark design is extremely high-leverage in the auto-research era because a bad design can waste an entire community's effort. ([9:19](https://www.youtube.com/watch?v=iCj_ATyThvc&t=559s), confidence: stated)
- Auto-research will commoditize execution skills while making higher-level skills more valuable, just as gradient descent did to hand-written code without eliminating software engineering jobs. ([10:15](https://www.youtube.com/watch?v=iCj_ATyThvc&t=615s), confidence: stated)
- In auto-research, the eval functions as the loss function and data, and the codebase abstraction functions as the model architecture. ([11:06](https://www.youtube.com/watch?v=iCj_ATyThvc&t=666s), confidence: stated)
- Proprietary evaluation data and domain-specific measurement understanding are a defensible moat for vertical AI companies. ([12:01](https://www.youtube.com/watch?v=iCj_ATyThvc&t=721s), confidence: stated)
- Tightening a codebase API so test data cannot reach training reduced the agent's data leakage rate to zero in a fraud detection pipeline. ([14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s), confidence: stated)
- Codebase abstraction is currently underrated relative to evals as a lever on auto-research outcomes. ([12:01](https://www.youtube.com/watch?v=iCj_ATyThvc&t=721s), confidence: stated)
- Individual human engineers will not become marginally less valuable; their contribution moves up the stack toward design and judgment. ([9:19](https://www.youtube.com/watch?v=iCj_ATyThvc&t=559s), confidence: stated)
- Good abstractions constrain reward hacking better than relying on the agent's intent, though a determined agent could still hack the reward. ([14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s), confidence: implied)

## Concepts

- [agent-readable codebases](../concepts/agent-readable-codebases.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [agentic science](../concepts/agentic-science.md)
- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark design](../concepts/benchmark-design.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [reward hacking](../concepts/reward-hacking.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)

