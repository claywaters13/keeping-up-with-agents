---
title: "Bringing agents onto the world wide web"
type: "talk"
slug: "bringing-agents-onto-the-world-wide-web"
track: "Computer Use"
org: "Browserbase"
day: "Day 3 — Session Day 2"
room: "Track 7"
video_id: "GqoNrUz8hEU"
duration_sec: 1105
word_count: 3834
speakers: ["Paul Klein IV"]
---

# Bringing agents onto the world wide web

**Speakers:** [Paul Klein IV](../speakers/paul-klein-iv.md)

**Org:** Browserbase

**Track:** Computer Use &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 18m 25s

[Watch on YouTube](https://www.youtube.com/watch?v=GqoNrUz8hEU)

## Summary

Paul Klein IV of Browserbase argues that browser and computer-use agents have stalled not because of model capability but because of missing engineering: harnesses, tools, and infrastructure. He claims there is a massive capabilities overhang in computer use — models are already good enough, as evidenced by RL environments for computer use and the gains coding harnesses like Cursor, Claude Code, and Factory extract from the same models — and that the work of closing it is available to any company, not just labs. He lays out three properties of browser agents that work (multimodal model routing plus code generation, harness engineering with memory and skills, and consistent scalable infrastructure), then turns to the web-side problems: accessibility trees and Web MCP, agent authentication and service accounts, and a missing trust/certificate layer distinguishing good agents from bad bots. He closes with a pitch for Browserbase Agents (launched the day before) and the thesis that solving computer use is what diffuses AI into the real economy — logistics firms, banks, factories running PHP forms. Worth watching if you're building web agents and want a clear framing of where the remaining bottlenecks actually sit.

## Key Points

- The bottleneck for web agents has shifted from model capability to harness and tooling: models a year ago were weak at long-horizon tasks, but that has largely been solved and heavy RL-environment investment has since gone into computer use specifically.
- Harness engineering is an engineering problem, not a lab problem — Cursor, Factory, and Claude Code demonstrate that a domain-optimized harness on the same underlying model produces above-baseline results, and any company can do this for its own domain.
- There is a large capabilities overhang in computer use: task completion rates for coding agents far exceed CUA rates not because models can't, but because the tools and scaffolding haven't been built.
- The most reliable production browser agents are multimodal and mix modalities — routing simpler pages to cheaper models, intercepting network requests, and having a coding agent write and replay scripts rather than clicking through every step.
- Harnesses should carry memory and skills so agents don't rediscover a site each run; Browserbase's browse.sh publishes per-website skills and Web MCP lets sites expose tool calls, both of which cut token usage.
- Infrastructure consistency matters as much as capability — the same page must render identically across runs (same layout, same viewport) or results become non-reproducible, and hobbyist setups like SSHing into a home Mac Mini don't survive contact with SOC 2 or production scale.
- The web itself must change: accessibility trees and ARIA tags, LLMs.txt / skills.md / agents.md, Web MCP in Chrome, and agent-first signup flows (e.g. WorkOS's OM.md) are all steps toward an agent-first web.
- Authentication and trust are the next unsolved gates — agents need secure credential delegation with human-in-the-loop approval, and the industry lacks a certificate-issuer-like authority to vouch that a given agent is a good agent rather than a bad bot.
- Observability with screen recordings, logs, and network activity fed back into the agent is what lets each run improve on the last; Browserbase's auto browse product is built around that self-improvement loop.

## Notable Quotes

> "until recently the the bottleneck was the models models one year ago really weren't good at long context horizon tasks but that's clearly been you know solved in a major way"
>
> — [1:55](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=115s) &middot; *states the talk's core premise shift from model limits to engineering limits*

> "I'd argue that agents are missing the right harness and tools."
>
> — [3:11](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=191s) &middot; *the thesis in one sentence*

> "when you build a harness optimized for the domain that your agent is operating in, it can actually achieve, you know, above model results in that domain"
>
> — [4:08](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=248s) &middot; *the mechanism claim behind harness engineering, backed by the Factory vs Claude Code comparison*

> "building a good harness is an engineering problem. You don't have to be a lab to build a good harness."
>
> — [4:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=286s) &middot; *directly addresses who can act on the overhang*

> "Now, it's not clear yet if custom harnesses are going to beat out durable, you know, RL models."
>
> — [5:16](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=316s) &middot; *a rare hedge naming the open question others would contest*

> "there is a massive capabilities overhang in computer use. The models are good enough, but we haven't done the engineering work to solve it."
>
> — [5:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=346s) &middot; *the central diagnosis of the talk*

> "the wrong answer is to sit around and just wait for the models to get better. You can actually solve this today. Solving overhang is an engineering problem."
>
> — [6:23](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=383s) &middot; *explicit call to action against the wait-for-the-next-model posture*

> "It turns out automating the web isn't always just clicking the button on the screen. It might be intercepting the network requests and writing a coding agent or having coding write a script to actually replay those network requests."
>
> — [7:01](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=421s) &middot; *names the tradeoff between pixel-level computer use and code generation*

> "The most reliable browser agents that we see in production right now are often writing code alongside using the browser to actually automate a task."
>
> — [7:40](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=460s) &middot; *an empirical claim from production that contradicts pure computer-use approaches*

> "The right harness should not only present the right tools, but present an optimized amount of tokens that are compressed to get exactly the right repeatable result every single time."
>
> — [8:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=526s) &middot; *defines what a harness owes the model, in context-efficiency terms*

> "I've yet to see a sock 2 compliant Mac Mini setup at scale, but please tell me afterwards if you found one."
>
> — [9:18](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=558s) &middot; *memorable jab at the OpenClaw-on-a-Mac-Mini pattern as an infrastructure dead end*

> "If your infrastructure renders a page in like a mobile layout one time and then like in a desktop layout the second time, it's going to have inconsistent results."
>
> — [9:50](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=590s) &middot; *concrete illustration of why environment consistency is a base-layer requirement*

> "Websites can now publish MCP servers within their page that your agent can take advantage of without pre-installing the actual MCP."
>
> — [11:00](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=660s) &middot; *clearest explanation of what Web MCP changes for agent-site interaction*

> "if you're building software now, you should think about what does my agent first sign up and login flow look like? Because agents are going to be using your software whether you like it or not."
>
> — [12:16](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=736s) &middot; *prescriptive advice to builders outside the agent space*

> "The web was built to stop bad bots, but now there's good agents and bad bots. How do we delineate between the two?"
>
> — [12:41](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=761s) &middot; *frames the trust problem the anti-bot stack was never designed for*

> "building reliable browser agents is is not a model problem. It's an engineering problem that all of us can solve."
>
> — [13:12](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=792s) &middot; *the talk's summary claim, stated plainly*

> "As a developer, I don't want to be locked into a single model provider. As models continually change and get better, I want to be able to move my agent around."
>
> — [14:19](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=859s) &middot; *takes a side on model-agnostic infrastructure as a requirement*

> "my core belief with this company is that solving computer use accelerates the diffusion of AI to the real economy"
>
> — [15:29](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=929s) &middot; *the strategic argument for why computer use matters beyond SF*

> "the real economy is companies like the logistics company in Singapore, the bank in South Africa, or the lumber factory in Mexico. These people are built on PHP websites with forms and human beings clicking buttons every single day."
>
> — [15:29](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=929s) &middot; *grounds the market claim in specific non-tech use cases*

> "I think one year from now, this room is going to be overfilled with people because the models are getting better, the techniques are getting better, the tools are getting better."
>
> — [17:51](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=1071s) &middot; *a dated, checkable prediction closing the talk*

## Positions

- The bottleneck for web agents is no longer model capability but the surrounding harness, tools, and infrastructure. ([3:11](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=191s), confidence: stated)
- A domain-optimized harness on top of a given model produces results above that model's baseline capability, as shown by Factory versus Claude Code on the same model. ([4:08](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=248s), confidence: stated)
- Building a competitive agent harness does not require being a frontier lab; ordinary companies can do it for their own domain. ([4:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=286s), confidence: stated)
- It is still an open question whether custom harnesses will outperform models RL-trained end-to-end for the task. ([5:16](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=316s), confidence: stated)
- Every agent should be measured against the baseline model to verify the harness is adding value. ([5:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=346s), confidence: stated)
- Non-coding agent use cases represent a larger opportunity than coding. ([6:23](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=383s), confidence: stated)
- The most reliable production browser agents combine code generation and network-request replay with visual browser interaction rather than relying on clicking alone. ([7:40](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=460s), confidence: stated)
- Dumping the full page content into a model produces subpar results and higher cost; harnesses must compress context. ([8:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=526s), confidence: stated)
- Running agents on self-hosted Mac Minis is not a viable production or compliance path for serving thousands of customer agents. ([9:18](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=558s), confidence: stated)
- Inconsistent rendering across runs (mobile versus desktop layout) causes inconsistent agent results, so infrastructure consistency is a prerequisite for reliability. ([9:50](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=590s), confidence: stated)
- Best-in-class browser agents no longer consume raw DOM and HTML, instead using the accessibility tree and ARIA tags. ([10:24](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=624s), confidence: stated)
- CAPTCHAs are no longer effective at distinguishing agents from humans, and the good-agent identity problem remains unsolved. ([12:41](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=761s), confidence: stated)
- The web needs a certificate-authority-like trust issuer for agents, and no one has built it yet. ([13:12](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=792s), confidence: stated)
- Browser agent infrastructure should be model agnostic so developers are not locked into one model provider. ([14:19](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=859s), confidence: stated)
- Teams should buy browser agent infrastructure rather than build it, and spend their time on customer problems instead. ([17:14](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=1034s), confidence: stated)
- Solving computer use is the mechanism by which AI diffuses into the non-tech real economy. ([15:29](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=929s), confidence: stated)
- Interest and attendance in computer use will grow substantially over the next year as models, techniques, and tools improve. ([17:51](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=1071s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent identity and authorization](../concepts/agent-identity-and-authorization.md)
- [agent memory](../concepts/agent-memory.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [token efficiency](../concepts/token-efficiency.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)

