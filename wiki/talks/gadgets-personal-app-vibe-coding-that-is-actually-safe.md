---
title: "Gadgets: Personal app vibe coding that is actually safe"
type: "talk"
slug: "gadgets-personal-app-vibe-coding-that-is-actually-safe"
track: "Software Factories"
org: "Cloudflare"
day: "Day 2 — Session Day 1"
room: "Track 1"
video_id: "RmS5s6Wbin4"
duration_sec: 1133
word_count: 3109
speakers: ["Kenton Varda"]
---

# Gadgets: Personal app vibe coding that is actually safe

**Speakers:** [Kenton Varda](../speakers/kenton-varda.md)

**Org:** Cloudflare

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 18m 53s

[Watch on YouTube](https://www.youtube.com/watch?v=RmS5s6Wbin4)

## Summary

Kenton Varda, creator of Cloudflare Workers, argues that personal AI codegen fundamentally breaks traditional cloud infrastructure. His premise: the developer-in-an-ivory-tower model, where feature requests die in Jira and rewrites for plugin systems drag on for years, can be replaced by users asking an AI agent to add features to their own copy of an app — but nothing about today's infrastructure supports it, since web apps run one blessed version on the developer's server and mobile platforms gatekeep unsigned code. He demos 'Gadgets,' a side project built entirely on Cloudflare Workers and durable objects (no containers, no database) that treats apps like documents in an office suite: each gadget is an instance with its own code, sharing and access control are implemented by the platform rather than the app, and agents can modify the app's own code mid-task. The security argument is the core technical claim: client code runs in a null-origin sandboxed iframe with CSP, server code runs in a dynamic worker sandbox, they can only talk to each other, so vibe-coded XSS bugs are structurally harmless. The talk is short, opinionated, and worth watching for the sandboxing architecture and the 'personalization requires new infrastructure' thesis — though the promised open-source release was pulled days before the talk.

## Key Points

- The traditional software distribution model funnels user feature requests into Jira or into perpetually-delayed plugin-system rewrites, leaving most personalization needs unmet.
- AI codegen offers an alternative where users have their agent add the features they need to their own instance, keeping the developer's core app clean.
- Existing cloud architecture is the wrong substrate for this: web apps run one blessed version on the developer's server, which structurally prevents per-user customization.
- Mobile platforms are worse — Varda argues Apple and Google's 15 years of gatekeeping mean effectively only a handful of companies can ship mobile apps, making the web the practical escape hatch.
- Gadgets treats applications like documents in an office suite: each gadget is a single shareable instance with its own code, so multiple slide decks means multiple gadget instances.
- Sharing and access control are implemented by the platform rather than by each app, so a vibe-coded gadget cannot get its permission model wrong.
- The sandbox is the safety mechanism: client UI runs in a null-origin iframe with CSP and only postMessage to the parent, and server code runs in a dynamic worker sandbox, so neither can leak anything and XSS bugs stop mattering.
- Agents can extend the app itself mid-task — Claude added strikethrough, text centering, and an arbitrary-SVG-paste feature to the slides app in order to satisfy the requested slide content.
- The whole system runs on Cloudflare Workers with durable objects and no containers or database, and runs locally on workerd, the open-source runtime, enabling self-hosted use cases like home automation.
- The planned open-source release at the end of the talk was cancelled the prior Thursday when Cloudflare's CTO decided the project had become too serious to 'yeet'.

## Notable Quotes

> "My, uh, key point is personal AI codegen breaks traditional cloud infrastructure."
>
> — [0:01](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=1s) &middot; *The single thesis statement of the talk, stated up front.*

> "if we want to see this future where um everyone has personal apps and like can personalize uh the apps that they run um the infrastructure we're using today um for for software in general is is not the right thing and we need something completely different"
>
> — [0:01](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=1s) &middot; *Expands the thesis into its strong form: not an adaptation but a replacement.*

> "the the developer's representative, the product manager takes these feature requests and files them into Jira where they are never seen again."
>
> — [1:08](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=68s) &middot; *The comedic framing of the problem the whole architecture is meant to solve.*

> "the users if they need a new feature could say that could ask their AI agent to write that feature just for them, add it to the app."
>
> — [3:21](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=201s) &middot; *The proposed replacement for the feature-request pipeline.*

> "You've got uh Apple and Google for the past 15 years uh gatekeeping their systems to the point where there's like five companies that can build mobile apps now and uh because everyone else has been banned."
>
> — [4:13](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=253s) &middot; *A pointed, checkable claim about platform gatekeeping with a number attached.*

> "On the web, everyone can build whatever they want. And it turns out it's fine. It's not the security disaster that Apple and Google keep telling us would happen."
>
> — [4:51](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=291s) &middot; *Takes a side in the open-platform security debate that others would dispute.*

> "for the past uh 25 years of uh cloud architecture we've been running in the wrong direction."
>
> — [4:51](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=291s) &middot; *The strongest contrarian claim in the talk, from someone who built major cloud infrastructure.*

> "most of them are targeting web apps because that's the easy thing to target but they're all targeting this existing infrastructure which is actually like not the right way to do it."
>
> — [5:35](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=335s) &middot; *Directly criticizes the current crop of vibe coding platforms.*

> "I created Cloudflare workers. I started the project um back in 2017 when I joined Cloudflare. I am still the lead engineer today."
>
> — [7:15](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=435s) &middot; *Establishes the credentials behind the infrastructure critique.*

> "We have millions of developers. We serve trillions requests per day."
>
> — [7:15](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=435s) &middot; *Concrete scale numbers for the platform the project is built on.*

> "This is the same thing except instead of documents, you have gadgets. And each gadget is an application with code. They can all be different code."
>
> — [8:49](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=529s) &middot; *The core mental model for the product in one sentence.*

> "the sharing model is implemented by the platform instead of by the app itself."
>
> — [10:49](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=649s) &middot; *The key design decision that makes vibe-coded apps safe to share.*

> "because each gadget is just the one thing that you want to share, that means that the platform can implement the sharing model and the access control such that the gadget itself can't possibly get that wrong."
>
> — [10:49](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=649s) &middot; *States the tradeoff: one-instance-per-shared-thing buys correctness of access control.*

> "I said, if you need uh if you need to add any new features to the slides app itself to support some of these slides, feel free to do so. And it did."
>
> — [12:14](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=734s) &middot; *The concrete demonstration of user-level app modification by an agent.*

> "that's not very useful for any human, but it was perfectly useful for Claude who then generated the SVG."
>
> — [12:52](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=772s) &middot; *A sharp observation that agent-authored features can target agent users, not humans.*

> "the UI that you see for the app here is running inside a null origin iframe sandbox um with content security policy set so that it basically cannot talk to anything any of the rest of the world can't access any cookies"
>
> — [13:42](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=822s) &middot; *The specific client-side isolation mechanism.*

> "if you have an XSS bug, it actually doesn't end up mattering because these can't leak anything. Um they're prevented from doing so. And it basically there is no security bug you can have in this code that matters."
>
> — [15:12](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=912s) &middot; *The talk's boldest security claim, and the justification for the 'actually safe' in the title.*

> "a lot of people don't know this but you can actually build complex apps on workers. There are no containers involved here. There's just dynamic workers. There are no there's no database involved. It just uses durable objects."
>
> — [16:09](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=969s) &middot; *Names the full architecture and what it deliberately omits.*

> "last Thursday Dne our CTO pulled me uh into a room and said Kenton I don't think you should yeet this. I don't think this is yeet material."
>
> — [17:41](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=1061s) &middot; *Explains the retracted open-source promise and signals the project's shift to a serious product.*

## Positions

- Personal AI codegen is incompatible with traditional cloud infrastructure and requires an entirely new infrastructure model. ([0:01](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=1s), confidence: stated)
- The last 25 years of cloud architecture, centered on one blessed app version running on the developer's server, moved in the wrong direction for user personalization. ([4:51](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=291s), confidence: stated)
- Apple and Google's 15 years of platform gatekeeping have reduced viable mobile app development to roughly five companies. ([4:13](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=253s), confidence: stated)
- The open web permits anyone to publish code and has not produced the security disaster mobile platform vendors predict. ([4:51](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=291s), confidence: stated)
- Current vibe coding platforms are building on the wrong foundation by targeting conventional web hosting infrastructure. ([5:35](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=335s), confidence: stated)
- If sharing and access control are implemented by the platform rather than the app, a generated app cannot get its permission model wrong. ([10:49](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=649s), confidence: stated)
- With a null-origin sandboxed iframe client and an isolated server sandbox that can only talk to each other, no security bug in the generated code can matter. ([15:12](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=912s), confidence: stated)
- Complex, full-featured applications can be built on Cloudflare Workers alone, without containers or a traditional database, using only dynamic workers and durable objects. ([16:09](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=969s), confidence: stated)
- Because workerd is open source and self-hostable, this class of personal app platform can run entirely on local hardware without cloud dependency beyond the LLM. ([16:56](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=1016s), confidence: stated)
- Agent-generated features need not be ergonomic for humans, because the agent itself may be the primary user of the feature. ([12:52](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=772s), confidence: implied)

## Concepts

- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)

