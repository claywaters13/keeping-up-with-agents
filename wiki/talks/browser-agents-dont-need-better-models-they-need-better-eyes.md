---
title: "Browser Agents Don't Need Better Models. They Need Better Eyes."
type: "talk"
slug: "browser-agents-dont-need-better-models-they-need-better-eyes"
org: "ARK"
video_id: "JnubYCYunk8"
duration_sec: 265
word_count: 937
speakers: ["Kushan Raj"]
---

# Browser Agents Don't Need Better Models. They Need Better Eyes.

**Speakers:** [Kushan Raj](../speakers/kushan-raj.md)

**Org:** ARK

**Duration:** 4m 25s

[Watch on YouTube](https://www.youtube.com/watch?v=JnubYCYunk8)

## Summary

Kushan Raj argues that browser agents underperform not because frontier models are too weak, but because the environment and representation given to them is bad. He demos a benchmark ('the browser challenge') where a standard agent takes 10–20 seconds just to click a start button, then shows his own system doing the same work far faster on a cheaper model. The core technique is a compressed markdown representation of the full page — roughly 1,800 tokens versus ~20,000 for a full DOM — paired with a screenshot and explicit end-to-end feedback about what appeared, disappeared, or blocked a click. Concrete failure comparisons (Claude stuck scrolling and screenshotting for two minutes on an Aadhaar download; failing to pick a date on a Canadian trekking booking site) illustrate the gap. Worth watching if you build browser automation and want a cheap, concrete alternative to screenshot-loop agents; it's a short, demo-heavy lightning talk rather than a rigorous evaluation.

## Key Points

- The bottleneck for browser agents is the surrounding infrastructure and page representation, not model intelligence.
- A compressed markdown representation of the page lets the agent see the entire site in very few tokens, versus a screenshot that shows only one visible snippet.
- On a sample page, the full DOM is about 20,000 tokens, a screenshot about 1,100 tokens, and the speaker's markdown about 1,800 tokens — near screenshot cost with whole-page coverage.
- With a better environment, a much cheaper model outperforms Claude driving a conventional screenshot-and-scroll loop.
- Typical failure mode observed: the agent gets stuck in a screenshot/scroll debug loop because it cannot tell what is actually happening on the page.
- Explicit diff-style feedback matters — telling the agent what newly appeared, what is gone, what was blocking a click, and that its click did not land.
- The agent needs to plan long sequences of tasks and recover from failures, which requires state tracking of the end-to-end browser page.
- The speaker plans to open source the project and expose it as an API taking a URL plus an intent, and possibly a website or browser plugin.

## Notable Quotes

> "The hypothesis here is models are pretty smart, but it's the infra around them that sucks."
>
> — [0:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=54s) &middot; *The thesis of the talk in one line.*

> "the browser this agent took like maybe 10-20 seconds just to click the start button. And now, we're on step one. There are 30 steps, and it has taken so long just to click one button."
>
> — [0:28](https://www.youtube.com/watch?v=JnubYCYunk8&t=28s) &middot; *Quantifies the latency problem that motivates the work.*

> "my core thesis here has been give a nice environment for the agent to use, right? So, where it can plan long sequences, it can figure out where it failed, what is going on, and it can plan the click correctly."
>
> — [0:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=54s) &middot; *States the proposed solution as an environment-design problem.*

> "I figured out is a cool representation which compresses the website and lets the agent see the entire page in very few few tokens."
>
> — [0:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=54s) &middot; *Names the specific mechanism behind the speedup.*

> "The full DOM for this would be around 20,000 tokens. But so, let's say we have this screenshot. All right, this screenshot's about 1,100 tokens. My markdown's about 1,800 tokens"
>
> — [3:15](https://www.youtube.com/watch?v=JnubYCYunk8&t=195s) &middot; *The only hard numbers in the talk, and the crux of the cost argument.*

> "instead in one screenshot where you could see only one particular snippet, you can see the entire website, right?"
>
> — [3:15](https://www.youtube.com/watch?v=JnubYCYunk8&t=195s) &middot; *Articulates the tradeoff screenshots make that markdown avoids.*

> "it took a screenshot, it scrolled for some reason, it took a screenshot. Basically, this entire process took 2 minutes, whereas in my case, in our video, so, it just boots, and boom, done."
>
> — [1:24](https://www.youtube.com/watch?v=JnubYCYunk8&t=84s) &middot; *Concrete head-to-head failure case with a time figure.*

> "as you can see, it is so much faster and so much quicker, and I'm using a much cheaper model, right?"
>
> — [0:28](https://www.youtube.com/watch?v=JnubYCYunk8&t=28s) &middot; *The central claim that better representation substitutes for model capability.*

> "we give it feedback that you tried to click this, but that didn't happen because you know, we're keeping track of the entire end-to-end browser page."
>
> — [3:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=234s) &middot; *Describes the failure-feedback loop that complements the page representation.*

> "we say that okay, hey, these are the new things that have popped up on the page."
>
> — [3:15](https://www.youtube.com/watch?v=JnubYCYunk8&t=195s) &middot; *Concrete detail on the diff-based observation format.*

> "what I built is a very clean representation that that basically compresses the website, and you can give this along with the screenshot. It's pretty cheap token-wise."
>
> — [3:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=234s) &middot; *Clarifies that markdown supplements rather than replaces the screenshot.*

> "the model can reason really well, and then it can construct this long sequence of tasks to execute."
>
> — [3:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=234s) &middot; *States the claimed downstream benefit: long-horizon planning.*

> "I'm thinking of open sourcing this project because again my this code is not super defensible."
>
> — [2:39](https://www.youtube.com/watch?v=JnubYCYunk8&t=159s) &middot; *Unusually candid on why the moat isn't in the code.*

> "Give me a URL, give me your intent and I will execute it for you and give it back to you"
>
> — [2:39](https://www.youtube.com/watch?v=JnubYCYunk8&t=159s) &middot; *The intended product interface in one sentence.*

> "I want to make browser agents faster, cheaper and more reliable and just make sure everybody in the world is using them"
>
> — [2:39](https://www.youtube.com/watch?v=JnubYCYunk8&t=159s) &middot; *Names the three axes he's optimizing.*

> "Browser agents as an idea are so cool, right? The browser agent should go crazy, right? I personally have not seen that adoption, and me myself, I don't use browser agents that much."
>
> — [0:00](https://www.youtube.com/watch?v=JnubYCYunk8&t=0s) &middot; *Frames the adoption gap that the whole talk responds to.*

## Positions

- Browser agent performance is limited by surrounding infrastructure and page representation, not by model capability. ([0:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=54s), confidence: stated)
- A compressed markdown page representation costs roughly 1,800 tokens versus ~20,000 tokens for the full DOM on the same page. ([3:15](https://www.youtube.com/watch?v=JnubYCYunk8&t=195s), confidence: stated)
- A cheaper model with a better page representation beats a stronger model like Claude using screenshot-driven browsing, on both speed and task success. ([0:28](https://www.youtube.com/watch?v=JnubYCYunk8&t=28s), confidence: stated)
- Screenshots are insufficient as the primary observation channel because they only expose one viewport-sized snippet of the page. ([3:15](https://www.youtube.com/watch?v=JnubYCYunk8&t=195s), confidence: stated)
- Agents need explicit state-diff feedback (what appeared, what was removed, whether a click landed) to recover from failures. ([3:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=234s), confidence: stated)
- The markdown representation should be supplied alongside a screenshot rather than replacing it. ([3:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=234s), confidence: stated)
- The technical approach is not defensible as proprietary code, so open sourcing it and selling an API is the better path. ([2:39](https://www.youtube.com/watch?v=JnubYCYunk8&t=159s), confidence: implied)
- Low adoption of browser agents is caused by their slowness and unreliability rather than by lack of useful applications. ([0:00](https://www.youtube.com/watch?v=JnubYCYunk8&t=0s), confidence: implied)

## Concepts

- [agentic loop design](../concepts/agentic-loop-design.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [model routing](../concepts/model-routing.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [task decomposition](../concepts/task-decomposition.md)
- [token efficiency](../concepts/token-efficiency.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)

