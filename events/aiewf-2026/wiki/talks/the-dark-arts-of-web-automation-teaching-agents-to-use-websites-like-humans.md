---
title: "The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans"
type: "talk"
slug: "the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans"
track: "Computer Use"
org: "Rexmore"
day: "Day 3 — Session Day 2"
room: "Track 7"
video_id: "26RtyAm9y_Q"
duration_sec: 1297
word_count: 3424
speakers: ["Corey Gallon"]
---

# The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans

**Speakers:** [Corey Gallon](../speakers/corey-gallon.md)

**Org:** Rexmore

**Track:** Computer Use &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 21m 37s

[Watch on YouTube](https://www.youtube.com/watch?v=26RtyAm9y_Q)

## Summary

Corey Gallon of Rexmore argues that AI agents can drive websites indistinguishably from humans by using the Chrome DevTools Protocol (CDP) through a shell CLI rather than an MCP server, because CDP-originated clicks and keystrokes travel the same internal Chrome path — and get the same 'trusted' stamp — as a real mouse. He lays out a three-part method: give the agent a CLI (cheaper, faster, and programmable versus MCP), drive the browser through a small subset of CDP domains framed as 'digital senses' (DOM, accessibility tree, screenshots, network, input), and run a sense-act-verify loop on a three-rung 'meatbag ladder' where you climb only as high as the page forces you. He demonstrates the method live against progressively harder targets: batch Outlook email (rung one, synthetic JS clicks), Amazon add-to-cart (rung two, trusted CDP input), and then Cloudflare Turnstile, an MT-style text captcha, and a jigsaw drag captcha (rung three, real mouse paths with jitter and overshoot plus model vision). The finale is reCAPTCHA v2, beaten by splitting the system into a deterministic pure-code 'solver' and an agent 'operator' that only does the one step requiring eyes and a brain — a split forced by the fact that challenges expire on a clock, so round-tripping a model on every action loses. The real deliverable is the methodology and the explore-then-write-it-down discipline; the captchas are just proof it works.

## Key Points

- A CDP-driven browser is indistinguishable from a human to bot detection because agent clicks and keystrokes travel the exact same path inside Chrome that a real user's do, earning the 'trusted' event stamp.
- CLI tools beat MCP servers for browser automation not on capability (both hit roughly 83% task success in an Arize AI study) but on reuse, speed, and cost — a CLI sequence can be programmed once and replayed without a model in the loop.
- The speed gap is concrete: the same task took MCP 71 round trips and 8 minutes versus seven turns and under a minute for a CLI, and Anthropic reported CLI token costs up to 75x cheaper.
- You don't need all 57 CDP domains — a small subset gives the agent 'digital senses': seeing via DOM/accessibility tree/screenshots, hearing via network traffic and console logs, and operating via clicks, keystrokes, and navigation.
- The core loop is sense, act, verify — and verification must use a different channel than the action, e.g. after a click check the network or the screen rather than asking the click whether it worked.
- The 'meatbag ladder' has three rungs — synthetic JavaScript clicks, trusted CDP input events, and full human behavior simulation (curved mouse paths, jitter, deliberate overshoot, vision) — and you climb only as high as the page forces you.
- Driving the web UI turns it into a permissionless universal API, which matters in corporate settings where the Office 365 API requires an app registration and admin approval an employee can't get, while the existing web login already works.
- reCAPTCHA v2 is beaten by splitting the system in two: a deterministic pure-code 'solver' that handles clicking, iframe piercing, screenshotting, and rearming, and an agent 'operator' invoked for the single vision-and-reasoning step per round.
- Because captcha rounds are on a clock, an architecture that round-trips a model on every click and every look burns the clock and loses before finishing — speed is the design constraint, not a nice-to-have.
- The durable output of exploration is written-down solutions: code, an agent skill, or both, so a path that worked once never has to be rediscovered.

## Notable Quotes

> "As I was preparing for this talk, OpenAI threatened to ban my account just for the work that I was doing in preparing for the talk."
>
> — [0:13](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=13s) &middot; *Frames the stakes and the adversarial posture of platforms toward agent browsing in one concrete anecdote.*

> "A CDP browser is just like a meatag with a mouse. No joke. Well, at least as far as Google and Cloudflare and the rest can tell."
>
> — [1:45](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=105s) &middot; *The one-slide thesis of the entire talk.*

> "If you have a browser, an agent drive a browser using the Chrome DevTools protocol, your agents clicks and keystrokes travel the exact same path inside Chrome that yours do."
>
> — [1:45](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=105s) &middot; *States the technical mechanism behind the indistinguishability claim.*

> "in a recent study by the guys at Arise AI, both a CLI and an MCP given the same task achieve those tasks successfully roughly 83% of the time. However, a CLI beats MCP in reuse, in speed, and in cost."
>
> — [2:35](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=155s) &middot; *Cited number plus the precise shape of the CLI-over-MCP argument: capability parity, operational advantage.*

> "A CLI sequence can be programmed. You write it once and you run it a thousand times without a model in the loop, whereas MCP hits the model on every single turn."
>
> — [3:19](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=199s) &middot; *The reuse argument in its sharpest form.*

> "MCP took 71 round trips and 8 minutes for the same task that took a CLI only seven turns and in under one minute."
>
> — [3:19](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=199s) &middot; *Hard comparative numbers others can check or dispute.*

> "Anthropic themselves reported that the CLI can be as much as 75 times cheaper in terms of token cost."
>
> — [3:19](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=199s) &middot; *The cost leg of the CLI argument, with a specific multiple.*

> "The surface area of CDP is enormous and it changes really frequently. So as of now it's 57 domains and within those there are hundreds and hundreds of methods and events."
>
> — [4:01](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=241s) &middot; *Quantifies the complexity the talk's bucketing scheme is meant to tame.*

> "if you've clicked something, don't ask the click if it was successful. Check the network or check the screen."
>
> — [6:10](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=370s) &middot; *The most portable piece of engineering advice in the talk — cross-channel verification.*

> "It has three rungs and you climb only as high as the page forces you."
>
> — [6:49](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=409s) &middot; *The governing heuristic of the meatbag ladder.*

> "If you can just use the API that's exposed within the page then and issue a synthetic JavaScript click, then do that. It's easy. It's free. It's instant. And it's the right default."
>
> — [6:49](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=409s) &middot; *Explicitly names the cheapest technique as the default, pushing back on always-simulate-a-human approaches.*

> "the API for an Office 365 tenant requires an app registration and it also requires admin approval, which as an employee, you can't often get."
>
> — [9:45](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=585s) &middot; *The strongest legitimate-use justification for UI automation over APIs.*

> "in this pattern the web UI itself kind of becomes a universal API right like a permissionless API which is really neat."
>
> — [10:36](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=636s) &middot; *Coins the framing that makes browser automation strategically interesting, not just a workaround.*

> "the page is checking was this click from a human source. Chrome stamps every single event with just that answer whether it's trusted or untrusted."
>
> — [11:16](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=676s) &middot; *Explains the exact detection mechanism that rung one fails and rung two defeats.*

> "First, it's encapsulated beneath a closed shadow route. And then the whole widget itself lives in a cross origin iframe which in it then also has another shadow route."
>
> — [12:48](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=768s) &middot; *Concrete detail on how Turnstile isolates its checkbox from automation.*

> "We ask the browser where it is that the iframe sits on the screen. We do a little bit of math to figure out where the checkbox is. Then we fire a trusted click right at that position on the glass"
>
> — [13:38](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=818s) &middot; *The key insight of the talk in miniature: stop addressing the DOM, address the screen.*

> "it's not just solving the puzzle, but it's solving it with moves like Jagger."
>
> — [15:48](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=948s) &middot; *Memorably captures that rung three is about motion quality, not puzzle-solving.*

> "It actually deliberately overshoots the puzzle piece and then eases it right back in just like a meat bag with a mouse."
>
> — [15:48](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=948s) &middot; *Specifies what human-like motion actually consists of in implementation.*

> "Code does the deterministic driving and the agent does the only bits that require eyes and a brain."
>
> — [17:54](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1074s) &middot; *The architectural principle behind the solver/operator split, generalizable well beyond captchas.*

> "An agent that roundtrips a model on every click and on every look burns that clock and loses. The challenge expires well before it ever finishes."
>
> — [18:36](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1116s) &middot; *Ties the earlier CLI-vs-MCP speed argument to a hard failure mode.*

> "The big takeaway is the methodology that enabled this. The captures themselves were just trixy little tests that demonstrate the methodology."
>
> — [19:23](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1163s) &middot; *The speaker's own statement of what the audience should extract.*

> "the engineering enabled the agent to do something that it could not do at all off the shelf."
>
> — [19:23](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1163s) &middot; *Positions disciplined engineering, not model capability, as the source of the result.*

## Positions

- Agents should be given shell-based CLI tools rather than MCP servers for browser automation, because capability is equivalent but CLIs win on reuse, speed, and cost. ([2:35](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=155s), confidence: stated)
- A CLI and an MCP server achieve the same task successfully roughly 83% of the time, per an Arize AI study. ([2:35](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=155s), confidence: stated)
- For an identical task, MCP required 71 round trips and 8 minutes while a CLI required seven turns and under one minute. ([3:19](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=199s), confidence: stated)
- Anthropic reported that CLI-based tool use can be up to 75 times cheaper in token cost than MCP. ([3:19](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=199s), confidence: stated)
- Input driven through CDP is indistinguishable from human input to detection systems including Google and Cloudflare, because it traverses the same internal Chrome path and receives the trusted stamp. ([1:45](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=105s), confidence: stated)
- Agents only need a small subset of CDP's 57 domains to interact with a browser the way a human does. ([4:48](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=288s), confidence: stated)
- Verification of an action must occur through a different sensory channel than the action itself. ([6:10](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=370s), confidence: stated)
- Synthetic JavaScript clicks are the correct default technique, and human simulation should only be used when the page forces escalation. ([6:49](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=409s), confidence: stated)
- Amazon's add-to-cart button silently ignores untrusted JavaScript clicks with no error or failure signal, but accepts trusted CDP input events. ([11:16](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=676s), confidence: stated)
- Cloudflare Turnstile's checkbox cannot be reached by typical automation because it sits behind a closed shadow root inside a cross-origin iframe containing another shadow root. ([12:48](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=768s), confidence: stated)
- Jigsaw-style captchas sample the full mouse trail during a drag, so passing requires reproducing jitter, easing, curvature, and overshoot rather than just correct positioning. ([15:07](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=907s), confidence: stated)
- reCAPTCHA v2 cannot be beaten by an architecture that round-trips a model on every interaction, because challenge rounds expire on a clock. ([18:36](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1116s), confidence: stated)
- The only approach the speaker found that reliably defeats reCAPTCHA v2 is deterministic code at machine speed with one AI vision call per round. ([18:36](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1116s), confidence: stated)
- The captcha solution is repeatable and reliable rather than a one-off fluke. ([19:23](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1163s), confidence: stated)
- Driving a web UI functions as a permissionless universal API, which is often the only viable path in corporate environments where official API access requires unobtainable admin approval. ([10:36](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=636s), confidence: stated)
- The value of this work lies in the engineering methodology rather than in captcha-breaking itself, since off-the-shelf agents cannot do this at all. ([19:23](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1163s), confidence: stated)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)

