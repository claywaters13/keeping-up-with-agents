---
title: "LLM Knowledge Bases: a practical guide"
type: "talk"
slug: "llm-knowledge-bases-a-practical-guide"
track: "Memory & Continual Learning"
org: "Warp"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "I3bpdgFJCUY"
duration_sec: 1277
word_count: 4518
speakers: ["Ben Holmes"]
---

# LLM Knowledge Bases: a practical guide

**Speakers:** [Ben Holmes](../speakers/ben-holmes.md)

**Org:** Warp

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 21m 17s

[Watch on YouTube](https://www.youtube.com/watch?v=I3bpdgFJCUY)

## Summary

Ben Holmes, developer relations lead at Warp, walks through a practical pipeline for turning messy personal notes into an agent-maintained knowledge base. The pipeline has four stages: capture raw thoughts via voice dictation (which he argues is the fastest input method available), run an 'enrich note' agent skill that adds tags, sources, and backlinks, generate browsable wikis on top of the enriched corpus using Andrej Karpathy's LLM-wiki gist as the pattern, and finally have an agent build HTML/Tailwind graph views of the whole thing. The key operational move is scheduling these skills as cloud automations that sync a markdown vault down (via the Obsidian headless CLI), run enrichment, and sync back — so you wake up to a refreshed wiki without your laptop being open. It's a concrete, tool-level demo rather than a conceptual talk: worth watching if you keep a personal notes vault and want a working blueprint for agent-maintained knowledge, less so if you want theory about memory or retrieval architectures.

## Key Points

- Voice dictation at roughly 200 words per minute is presented as the fastest practical way to capture raw thought, and it no longer requires a paid tool — local, on-device models like Handy and Voice Ink cover it.
- The capture stage should optimize for volume and rawness, not polish; rambly unformatted transcripts are fine because LLMs need a large pile of raw material to work from later.
- An 'enrich note' agent skill does the structuring work: it adds topic tags, researches and links the original source via web search, finds related notes by key-term search, and writes backlinks at the bottom of each file.
- Tags are constrained to a checked-in reference folder of allowed tags because agents (Claude specifically) otherwise invent new ones on every pass.
- Each enrichment writes a timestamp into the note, which makes repeat passes idempotent — a later agent run only picks up notes that have not yet been enriched.
- Wiki generation follows Karpathy's publicly circulated gist: point an agent at a raw directory plus a focus area, and it produces a browsable set of people, concepts, organizations, and sources with links back to the raw notes.
- Running these skills on a schedule in a cloud sandbox beats local automations (like the Codex app's) because local ones require your laptop to be open; the sandbox syncs the vault via the Obsidian headless CLI rather than git push/pull.
- Visualization is now a build-on-demand step rather than a tool you install — Holmes had an agent generate an interactive HTML/Tailwind graph view and a GitHub-style writing-habit chart directly over the markdown files.

## Notable Quotes

> "because you may not be aware, but voice dictation, even though it is pretty awkward to talk into your computer with a bunch of co-workers around, it is the fastest way to get your thoughts onto paper."
>
> — [2:46](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=166s) &middot; *States the talk's core input-side claim and acknowledges the social friction against it.*

> "It's going to be like 200 words per minute, I believe, is the average."
>
> — [2:46](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=166s) &middot; *The one concrete number backing the dictation argument.*

> "Unless you're an absolute Olympic typist, it will be faster than any other method that you have."
>
> — [3:21](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=201s) &middot; *Sharpens the dictation claim into a near-universal recommendation.*

> "And by the way, for the people who aren't paying for Whisper Flow subscriptions, you're in luck. You don't have to pay anymore for this kind of stuff. There are local models that can do this."
>
> — [3:21](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=201s) &middot; *Names a cost/tooling shift — local models have commoditized paid dictation.*

> "So don't worry if you're being a little bit scrappy, a little bit rambly. You're not formatting things with perfect bullet points. That's fine. The goal should just be get down as many thoughts in the moment as possible."
>
> — [4:59](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=299s) &middot; *Explicit tradeoff: capture volume over capture quality, because structuring is deferred to the agent.*

> "Put a little time stamp on there so if we ask the agent to do another pass it remembers that some other agent did it in the past."
>
> — [6:34](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=394s) &middot; *The idempotency mechanism that makes scheduled re-runs cheap.*

> "I actually put all of my tags into this little uh reference folder over here. That way the agent isn't inventing new tags every time it goes through and tries to add more detail."
>
> — [6:34](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=394s) &middot; *Concrete design pattern for keeping an agent-maintained taxonomy from drifting.*

> "I actually instruct the agent to be reluctant to add new tags because Claude loves to get creative."
>
> — [7:08](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=428s) &middot; *Names a specific model behavior he has to prompt against.*

> "So if you're someone that likes following Wikipedia rabbit holes, it kind of invents a Wikipedia rabbit hole of your own thoughts. It's kind of fun."
>
> — [9:45](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=585s) &middot; *The clearest articulation of what the enriched backlink graph is actually for.*

> "and all of that is generated programmatically. I didn't write any of this because all I have time to do is generate the raw ingredients not connecting it all together myself."
>
> — [11:24](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=684s) &middot; *States the division of labor the whole system is built around.*

> "We want to take a raw directory which is where we're taking all of our spare Apple notes from earlier and we want to combine it into whatever focus area that we care about."
>
> — [12:04](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=724s) &middot; *Compresses the Karpathy wiki-generation pattern into one sentence.*

> "they have an automations tool that spins up tasks to run on your machine every day, but it means your laptop has to be cracked open when it runs because it's a local automation."
>
> — [13:43](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=823s) &middot; *Names the concrete limitation motivating the move to cloud-scheduled agents.*

> "You could also just do like a git clone too if you want to be a little bit less creative, put all of your notes in a GitHub folder so that way a cloud agent could pull it down and do it for you."
>
> — [15:09](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=909s) &middot; *Gives the low-tech alternative to the Obsidian CLI sync, useful for anyone replicating this.*

> "I prefer using Obsidian CLI for this just because it avoids having to like push and pull your notes. No one has time for that."
>
> — [15:09](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=909s) &middot; *States the tradeoff he actually chose and why.*

> "So that way when I come back to my computer in the morning, I wake up to a perfectly fresh wiki that I can review. It's like the daily paper, but it's your own, which is so exciting."
>
> — [16:11](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=971s) &middot; *The payoff framing for scheduled background enrichment.*

> "And this is not a tool that you have to install. By the way, I told an agent, build this for me."
>
> — [18:10](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=1090s) &middot; *Argues visualization tooling has shifted from installed software to generated software.*

> "It's useful just to get an idea of what you're actually interested in and where you have gaps in your thinking, but it's also useful if you want to drill down."
>
> — [19:10](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=1150s) &middot; *Justifies the graph view as a thinking tool rather than decoration.*

## Positions

- Voice dictation at ~200 words per minute is faster than typing for anyone who isn't an elite typist, making it the best default for capturing raw notes. ([2:46](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=166s), confidence: stated)
- Paid dictation subscriptions like Whisper Flow are no longer necessary because open-source local models (Handy, Voice Ink) do the job on-device. ([3:21](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=201s), confidence: stated)
- Notes should be captured scrappy and unformatted; the volume of raw material matters more than its structure because LLMs need lots of raw data to generate wikis and visualizations later. ([4:59](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=299s), confidence: stated)
- Agents should be given a fixed reference list of tags and instructed to be reluctant to add new ones, because models like Claude will otherwise invent new tags on every pass. ([7:08](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=428s), confidence: stated)
- Writing an enrichment timestamp into each note makes repeat agent passes safe and cheap, since later runs only process notes lacking the marker. ([8:46](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=526s), confidence: stated)
- Karpathy's LLM-wiki gist — point an agent at a raw directory plus a focus area — is a sufficient recipe for generating an organized personal wiki, tweakable to taste. ([12:04](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=724s), confidence: stated)
- Local automation tools that run on your machine (e.g. the Codex app's automations) are inferior for this workflow because they require your laptop to be open when the schedule fires. ([14:22](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=862s), confidence: stated)
- Syncing a markdown vault into a cloud sandbox via the Obsidian headless CLI is preferable to a git clone/push workflow because it avoids manual push and pull. ([15:09](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=909s), confidence: stated)
- Knowledge-base visualizations no longer require installing a tool; an agent can build a clickable HTML/Tailwind graph view over your markdown on request. ([18:37](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=1117s), confidence: stated)
- A graph view over personal notes surfaces both your actual areas of interest and the gaps in your thinking, which browsing wiki links alone does not. ([19:10](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=1150s), confidence: stated)
- Once this pipeline is scheduled, the only human work required is voice dictation — everything downstream is generated. ([17:39](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=1059s), confidence: implied)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [background agents](../concepts/background-agents.md)
- [durable execution](../concepts/durable-execution.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [ontology design](../concepts/ontology-design.md)
- [voice agents](../concepts/voice-agents.md)

