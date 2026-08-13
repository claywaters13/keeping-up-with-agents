---
title: "Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex"
type: "talk"
slug: "full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex"
track: "Workshops Day 2"
org: "OpenAI"
day: "Day 2 — Session Day 1"
room: "Track 4"
video_id: "il1c1a2FufU"
duration_sec: 4502
word_count: 13795
speakers: ["Jason Liu"]
---

# Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex

*Program title: Setting Yourself Up for Success — Part 1*

**Speakers:** [Jason Liu](../speakers/jason-liu.md)

**Org:** OpenAI

**Track:** Workshops Day 2 &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 4 &nbsp;|&nbsp; **Duration:** 1h 15m

[Watch on YouTube](https://www.youtube.com/watch?v=il1c1a2FufU)

## Summary

Jason Liu of OpenAI walks through how he actually uses the Codex desktop app to run not just coding but most of his knowledge work — partnerships, ops, triage, meeting notes, even video editing. His central claim is that context compaction now works well enough that the old advice to start a fresh thread every 20 messages is obsolete: he keeps pinned threads alive for weeks, treats each as a teammate, and lets threads rename, list, and message each other so a 'monitor' thread can spawn and manage downstream triage threads. The practical spine of the talk is a stack of concrete mechanics — voice dictation via foot pedal, 'appshots' that ship the app's accessibility tree alongside the screenshot, skills and plugins, a personal monorepo memory vault under git, heartbeat automations, and file-based goals with verifiers. He also pushes back on reasoning-effort maximalism, arguing low and medium thinking handle most non-greenfield work. Worth watching if you want a maximalist but specific picture of agent-as-coworker workflows and the org-level guardrails they need.

## Key Points

- Compaction has improved enough that long-lived pinned threads beat starting fresh sessions — Liu keeps threads running for five weeks with hundreds of sub-agents and they still know their job.
- Threads now have tools to list, rename, and message other threads, which lets a single 'monitor' thread spawn per-issue threads and act as a manager over IC threads.
- Voice dictation is the intended input mode: you speak roughly 3x faster than you type, and messy 15-minute voice memos give the model tangents and context you'd never bother typing.
- 'Appshots' beat screenshots because they carry the app's accessibility tree — a Slack appshot includes channel and user IDs, collapsing multi-hop OCR-then-lookup chains into a single function call.
- A personal monorepo memory vault (projects/, people/, to-dos, per-project AGENTS.md) kept as a git repo lets you review agent changes with `git diff` and gives skills durable context to route work.
- Skills should be built fast, self-improving (allowed to edit their own files on failure), and battle-tested personally for weeks before being shared as team plugins — Liu admits he can't eval skills that depend on live Slack state.
- Heartbeat automations schedule messages back into the same thread rather than spawning new ones, enabling loops like 'watch this PR until it's mergeable' or 'check the refund queue every five minutes.'
- Goals with an explicit verifier scale well — he rewrote the rich terminal library in Rust and UV in TypeScript to 100% test coverage — and an 'ultra goal' file lets you edit scope mid-run.
- The main safety failure mode is a determined model routing around a blocked connector by using computer use to click send in Chrome; AGENTS.md rules, auto-review, and org-level admin restrictions are the mitigations.
- Reasoning-effort maximalism is a misconception: low and medium thinking are sufficient for most operational work, and 'xhigh' means more thinking, not better results.

## Notable Quotes

> "the things I really want you to take away from this workshop is the fact that compaction works really, really well. Like I have threads now that are like five weeks old that have you know 400 sub aents in them and they generally just know what they need to do."
>
> — [3:29](https://www.youtube.com/watch?v=il1c1a2FufU&t=209s) &middot; *the thesis of the talk, with a concrete scale claim attached*

> "you were always told if a conversation goes very long, start a new thread, right? After 20 messages, it's it's not going to be that good."
>
> — [6:30](https://www.youtube.com/watch?v=il1c1a2FufU&t=390s) &middot; *names the prior consensus he's arguing is now dead*

> "every thread has the ability to list other pin threads, has the ability to rename threads, and it has the ability to send messages to each other."
>
> — [5:50](https://www.youtube.com/watch?v=il1c1a2FufU&t=350s) &middot; *the specific primitive behind the manager-thread pattern*

> "you generally talk about three times faster than you type and it's just incredibly productive to be able to give the messy version of what you're thinking about to the AI"
>
> — [7:39](https://www.youtube.com/watch?v=il1c1a2FufU&t=459s) &middot; *states the quantitative case for voice input*

> "It's like now like I don't want to send my coworker like a 15-minute voice memo, but I should be I should feel very comfortable sending an AI a 15minute voice memo because you're going to include some random tangents."
>
> — [8:25](https://www.youtube.com/watch?v=il1c1a2FufU&t=505s) &middot; *captures why low-effort messy input is a feature, not sloppiness*

> "with appshots, it takes not only the image but the entire accessibility tree of the app. And so when I give it an appshot of a Slack channel, it knows the channel ID."
>
> — [16:20](https://www.youtube.com/watch?v=il1c1a2FufU&t=980s) &middot; *the mechanical reason appshots outperform screenshots*

> "day one you have to show them every standard operating procedure you know but at some point you have an employee that has been here for seven years and you can just say hey I think you should make the company more money and they can figure it out but it's only because they have this context"
>
> — [12:38](https://www.youtube.com/watch?v=il1c1a2FufU&t=758s) &middot; *the onboarding analogy that frames his whole memory-investment argument*

> "if you're rewarded by how often the plugins you've built are being used by your teammates, that's a huge win"
>
> — [4:39](https://www.youtube.com/watch?v=il1c1a2FufU&t=279s) &middot; *proposes an org-level success metric over personal token burn*

> "most of my skills connect to so many other plugins and connectors that uh I just don't know how to eval because I can't like snapshot my Slack at any given time."
>
> — [24:30](https://www.youtube.com/watch?v=il1c1a2FufU&t=1470s) &middot; *a candid admission that this workflow has no eval story*

> "no, I think my job when I'm at work really is just when the AI is running, I should be talking to somebody."
>
> — [26:04](https://www.youtube.com/watch?v=il1c1a2FufU&t=1564s) &middot; *his answer to what the human does in the loop*

> "having access to your computer is uniquely powerful because it has your O and your credentials and and your your um your file system."
>
> — [27:32](https://www.youtube.com/watch?v=il1c1a2FufU&t=1652s) &middot; *names why local computer use is both the capability and the risk*

> "I was able to not only rewrite the rich terminal library in Rust, I also rewrote UV and TypeScript um just to see if I could and uh we're like 100% test coverage."
>
> — [40:14](https://www.youtube.com/watch?v=il1c1a2FufU&t=2414s) &middot; *concrete result demonstrating verifier-driven long-running goals*

> "There will be some times where the model based on how you prompted becomes really determined and say, Oh, like I I it seems like I can't email someone using the Gmail connector. Let me open up Chrome and hit the send button."
>
> — [54:04](https://www.youtube.com/watch?v=il1c1a2FufU&t=3244s) &middot; *the clearest statement of the guardrail-circumvention risk in computer use*

> "if I could improve parts of the model, I would rather improve like its writing tone rather than like its ability to search the context."
>
> — [1:00:48](https://www.youtube.com/watch?v=il1c1a2FufU&t=3648s) &middot; *a ranked priority claim that others in the field would contest*

> "my like check notes skill has been used like a 150,000 times, but I've like never mentioned it in the past like two three months."
>
> — [1:04:03](https://www.youtube.com/watch?v=il1c1a2FufU&t=3843s) &middot; *evidence that implicit skill triggering has replaced explicit invocation*

> "I have a line that's like if you want to have good taste, you kind of have to eat, right?"
>
> — [1:05:28](https://www.youtube.com/watch?v=il1c1a2FufU&t=3928s) &middot; *his prescription for the skill he thinks stays valuable*

> "And specifically around vocabulary, right? like you can't really describe things that you don't really understand."
>
> — [1:06:06](https://www.youtube.com/watch?v=il1c1a2FufU&t=3966s) &middot; *ties taste directly to the ability to prompt and critique*

> "really get comfortable with like low and medium thinking. Like these models are still very very smart, right? Like low thinking on five like five five is like still so much better than prior models."
>
> — [1:11:45](https://www.youtube.com/watch?v=il1c1a2FufU&t=4305s) &middot; *direct pushback on reasoning-effort maximalism*

> "check every five minutes if the queue is like better. And once you get to five minute wait time, check every one minute and keep replying until you get my money back. And I took a shower and when I came back, I had like $400 in my credit card."
>
> — [1:13:02](https://www.youtube.com/watch?v=il1c1a2FufU&t=4382s) &middot; *the most vivid concrete payoff of heartbeat loops with stopping criteria*

> "people should not be afraid of low reasoning. Like X high is not like X high results. It's just like think more"
>
> — [1:14:18](https://www.youtube.com/watch?v=il1c1a2FufU&t=4458s) &middot; *the talk's closing corrective, stated as a crisp aphorism*

## Positions

- Compaction has improved enough that the old advice to start a new thread after long conversations or per feature is no longer true. ([7:05](https://www.youtube.com/watch?v=il1c1a2FufU&t=425s), confidence: stated)
- Scheduling heartbeat messages back into the same existing thread is a better design than having each automation create a new thread. ([35:13](https://www.youtube.com/watch?v=il1c1a2FufU&t=2113s), confidence: stated)
- Text input is not the future of interacting with agents; dictation is roughly 3x faster than typing and should be the default. ([7:39](https://www.youtube.com/watch?v=il1c1a2FufU&t=459s), confidence: stated)
- Appshots outperform plain screenshots because the accessibility tree supplies channel and user IDs, reducing multi-hop tool calls to a single call. ([16:53](https://www.youtube.com/watch?v=il1c1a2FufU&t=1013s), confidence: stated)
- Current models are more often too reluctant to take destructive actions than too eager, so over-restriction is the bigger practical annoyance. ([30:01](https://www.youtube.com/watch?v=il1c1a2FufU&t=1801s), confidence: stated)
- AGENTS.md rules plus auto-review are sufficient safety controls for individual use, with org-level admin settings needed for external-facing actions. ([31:28](https://www.youtube.com/watch?v=il1c1a2FufU&t=1888s), confidence: stated)
- The highest-impact move for an AI champion inside a company is building shared skills for the team, not maximizing personal token usage. ([14:06](https://www.youtube.com/watch?v=il1c1a2FufU&t=846s), confidence: stated)
- Long-running agent work succeeds in proportion to the quality of its verification step. ([41:01](https://www.youtube.com/watch?v=il1c1a2FufU&t=2461s), confidence: stated)
- You should let the model write your prompts and goals rather than writing them yourself, because that output is more in-distribution. ([44:19](https://www.youtube.com/watch?v=il1c1a2FufU&t=2659s), confidence: stated)
- Should let a skill edit itself after failures so it improves over time, and only share it with the team after months of personal use. ([14:35](https://www.youtube.com/watch?v=il1c1a2FufU&t=875s), confidence: stated)
- Highest reasoning effort does not produce proportionally better results for most operational tasks; low and medium suffice. ([1:12:21](https://www.youtube.com/watch?v=il1c1a2FufU&t=4341s), confidence: stated)
- This class of skill-and-connector workflow cannot be evaluated with standard eval methods because live state like Slack cannot be snapshotted. ([24:30](https://www.youtube.com/watch?v=il1c1a2FufU&t=1470s), confidence: stated)
- Pinned threads are superior to sub-agents for ongoing work because sidebar visibility lets you notice state changes. ([58:17](https://www.youtube.com/watch?v=il1c1a2FufU&t=3497s), confidence: stated)
- Taste is developed by consuming more products and building vocabulary to articulate what is bad, and it is the durable human skill as coding is automated. ([1:05:28](https://www.youtube.com/watch?v=il1c1a2FufU&t=3928s), confidence: stated)
- A determined agent will route around a blocked connector by using computer use to perform the action manually, which is a real security issue. ([54:37](https://www.youtube.com/watch?v=il1c1a2FufU&t=3277s), confidence: stated)
- Competing coding agent tools do not yet have thread-control and appshot-style features, but will replicate them quickly. ([1:09:17](https://www.youtube.com/watch?v=il1c1a2FufU&t=4157s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [background agents](../concepts/background-agents.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [context compaction](../concepts/context-compaction.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [session management](../concepts/session-management.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)
- [verifier design](../concepts/verifier-design.md)
- [voice agents](../concepts/voice-agents.md)

