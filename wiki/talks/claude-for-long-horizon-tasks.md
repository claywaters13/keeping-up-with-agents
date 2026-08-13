---
title: "Claude for Long-Horizon Tasks"
type: "talk"
slug: "claude-for-long-horizon-tasks"
track: "Claws & Personal Agents"
org: "Anthropic"
day: "Day 2 — Session Day 1"
room: "Track 1"
video_id: "9QebvrrY3KY"
duration_sec: 1518
word_count: 4469
speakers: ["Lance Martin"]
---

# Claude for Long-Horizon Tasks

*Program title: Claude for long-horizon tasks*

**Speakers:** [Lance Martin](../speakers/lance-martin.md)

**Org:** Anthropic

**Track:** Claws & Personal Agents &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 25m 18s

[Watch on YouTube](https://www.youtube.com/watch?v=9QebvrrY3KY)

## Summary

Lance Martin of Anthropic lays out four architectural themes for building asynchronous, long-horizon agents, framed by the observation that model task horizons have grown from ~10-20 minutes (Opus 3, 2024) to 12+ hours, which in turn changed what API surfaces make sense (Messages API → Agent SDK → Managed Agents). The core technical arguments are: decouple the harness ("brain") from execution containers ("hands") so sessions survive crashes and credentials never touch the sandbox; run verification in a separate context window from the build agent, because a model grading its own work in the same context confabulates; and treat memory as a two-system process, with in-band writing during a session plus an offline "dreaming" consolidation pass that corrects errors written earlier. He backs the memory claims with concrete experiments — Claude Plays Pokémon traces where 5/5 raw-memory replicates fell through the same trapdoor from a bad memory while dreaming fixed it, plus Continual Learning Bench results showing in-band memory writing improves across model generations. The fourth theme, org-level harnesses (Claude Tag), argues that multiplayer agents with their own identity and organizational context level the playing field for new employees. Worth watching for anyone designing agent infrastructure; the Q&A on memory substrates (general and model-managed, never a prescribed schema) is the sharpest opinionated moment.

## Key Points

- Model task horizons have grown from 10-20 minutes of autonomous work in the Opus 3 era to a 12+ hour regime for frontier models, and each jump made a different product surface viable — autocomplete/chat, then local synchronous coding agents, then genuinely async agents.
- Managed Agents decouples the stateless harness from the execution containers, with an append-only session event log and credentials stored in a separate vault, so a dead harness or dead container doesn't lose the session and a long-running agent never holds your secrets.
- The append-only session log doubles as an external, immutable context object the model can interrogate, which is strictly better than naive compaction where non-compacted context is discarded permanently.
- Verification should live in its own context window with its own tuning, because a model that both did the work and grades it in a shared context produces confabulation and odd artifacts.
- The build-agent/verifier-agent loop encodes the steering signal into the environment rather than into the human, letting high-capacity models self-correct; Martin demonstrated this on OpenAI's parameter golf ML-research benchmark using Managed Agents outcomes.
- Memory works best as two systems mirroring hippocampus and cortex: fast in-band writes during a session, plus an out-of-band 'dreaming' pass that consolidates and corrects memories that were wrong or only locally optimal.
- In Claude Plays Pokémon, an incorrect memory caused mislocalization and a trapdoor fall in 5 out of 5 raw-memory replicates, while dreaming traces corrected the error and advanced to the next level; a no-memory baseline made essentially no progress.
- The main capability difference in memory writing between weaker and stronger models is the distillation step — high-capacity models save generalizable abstractions for future sessions rather than specific facts.
- Memory substrates should be general and programmable (file system or database both work); prescribing an explicit memory schema for the model is where performance drops, a classic bitter-lesson failure.
- Org-level harnesses like Claude Tag matter not because they're in Slack but because they're multiplayer, hold their own identity and credentials separate from any user, carry organizational context, and let new employees skip weeks of harness configuration.

## Notable Quotes

> "you can think about Claude as a light source and you can think about products as windows that allow the light to pass through"
>
> — [0:01](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1s) &middot; *the framing device for the whole talk's model-capability-drives-product-surface argument*

> "models could only do, you know, maybe 10 to 20 minutes of autonomous work. This is measured by meter. And in that regime, only certain product surfaces made sense."
>
> — [0:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=44s) &middot; *anchors the task-horizon thesis with a specific number and measurement source*

> "when models can only do like an hour of work, async as an experience is kind of bad. Um the model goes off and it like hits an error and it comes back to you over a short period of time."
>
> — [1:25](https://www.youtube.com/watch?v=9QebvrrY3KY&t=85s) &middot; *explains why async agents failed before, not just that they did*

> "we released a new API called Managed Agents, which basically packages both the harness as well as all the managed deployment infrastructure for you"
>
> — [2:33](https://www.youtube.com/watch?v=9QebvrrY3KY&t=153s) &middot; *names the product and precisely what it bundles beyond the Agent SDK*

> "giving Claude access to a bunch of your secrets and letting it run for 10 hours and not watching it can be a little bit spooky and have some security concerns, especially as models get extremely capable"
>
> — [4:01](https://www.youtube.com/watch?v=9QebvrrY3KY&t=241s) &middot; *the security rationale for brain/hands decoupling, stated bluntly*

> "the harness becomes a stateless process that talks to a session. The session is an append-only event log and that can reach out to hands, which are just containers."
>
> — [4:01](https://www.youtube.com/watch?v=9QebvrrY3KY&t=241s) &middot; *the clearest one-sentence statement of the Managed Agents architecture*

> "If the session, uh sorry, if the harness dies or sandbox dies, it's completely fine because the session is always backed up in this append-only log and credentials are never actually added to the sandbox."
>
> — [4:38](https://www.youtube.com/watch?v=9QebvrrY3KY&t=278s) &middot; *states the two concrete reliability and security guarantees the architecture buys*

> "when you're doing something like compaction, you're choosing some logic to retain some amount of context, and naively in a typical in a kind of a typical step, you're discarding all the context that you didn't compact"
>
> — [5:17](https://www.youtube.com/watch?v=9QebvrrY3KY&t=317s) &middot; *names the specific failure mode of compaction that persistent sessions avoid*

> "when you ask them to do a bunch of work and then say, "Okay, grade your work." If that same context is being used to both do the work and grade, you can get lots of odd artifacts and confabulation"
>
> — [5:54](https://www.youtube.com/watch?v=9QebvrrY3KY&t=354s) &middot; *the empirical basis for separating verification into its own context*

> "what we found is it's quite effective to separate verification into a separate context window. This is a very general trend."
>
> — [6:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=404s) &middot; *the actionable recommendation, framed as generalizable beyond Anthropic's stack*

> "in Claude code you have goal and manage agents you have outcomes and the principles are really the same. You're setting up a measurable end state in both cases."
>
> — [7:24](https://www.youtube.com/watch?v=9QebvrrY3KY&t=444s) &middot; *maps the verifier abstraction onto two shipping products*

> "instead of encoding steering me and into like me as the human, you're encoding the signal into the environment"
>
> — [8:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=524s) &middot; *the conceptual payoff of the loops paradigm in one line*

> "this paradigm of loops, which a lot of people been talking about today, paired with very capacity models is a very good general primitive for long-running asynchronous work"
>
> — [9:40](https://www.youtube.com/watch?v=9QebvrrY3KY&t=580s) &middot; *his explicit summary of the verifier section's thesis*

> "higher capacity models have a better sense of like what abstraction to save to memory that'll be useful later. Like they're not just writing a specific fact."
>
> — [13:02](https://www.youtube.com/watch?v=9QebvrrY3KY&t=782s) &middot; *identifies distillation as the specific axis on which memory writing improves*

> "when I'm writing memory in band over the course of a day over the course of a session, sometimes you can write incorrect memories. And or you're writing things that are locally optimal, but not globally optimal."
>
> — [13:02](https://www.youtube.com/watch?v=9QebvrrY3KY&t=782s) &middot; *the precise problem statement that motivates offline dreaming*

> "Five out of five replicates with raw memory store fell down this trap. With the dreaming, this error is corrected, and it's able to properly localize itself and not fall fall down this trap."
>
> — [14:14](https://www.youtube.com/watch?v=9QebvrrY3KY&t=854s) &middot; *the talk's most concrete experimental result on memory consolidation*

> "those mistakes get stuck in memory unless you have an offline process to kind of correct them"
>
> — [15:40](https://www.youtube.com/watch?v=9QebvrrY3KY&t=940s) &middot; *the one-line case for dreaming as infrastructure, not novelty*

> "we released Claude Tag and a lot of the reaction was like, "Ah, Slack bot.""
>
> — [16:17](https://www.youtube.com/watch?v=9QebvrrY3KY&t=977s) &middot; *sets up his defense of org-level harnesses against the obvious dismissal*

> "Its identity and credentials are not tied to a given user and has access to organizational level context, not just my local context."
>
> — [16:51](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1011s) &middot; *defines what actually distinguishes a multiplayer harness from a personal one*

> "when you your own personal harness, often new employees takes them weeks or maybe even months to kind of ramp up fully to configure all the right connectors"
>
> — [16:51](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1011s) &middot; *quantifies the onboarding cost that org-level harnesses eliminate*

> "to build real agents that can operate in these long time horizons, a bunch of things need to come together in terms of like architecture, infrastructure, security, memory"
>
> — [21:05](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1265s) &middot; *his answer to why frontier labs lead on long-horizon agents — it isn't only model capability*

> "what I've seen doesn't work is when you specify the structure of memory for the model very explicitly, whether that's in a file system or database or whatever"
>
> — [22:41](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1361s) &middot; *the sharpest contrarian take in the Q&A, against schema-driven memory design*

> "Let the model structure and maintain its own memory. Don't give it a prescribed memory schema."
>
> — [23:25](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1405s) &middot; *the memory guidance compressed to an imperative*

> "Models can reason about their own memory and context structure much better than you can prescribe for them a way to structure their own memories."
>
> — [23:25](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1405s) &middot; *explicitly invokes the bitter lesson as applied to memory engineering*

> "we've actually run a lot of different evals showing that dreaming can indeed improve performance for very intuitive reasons as you see here. But of course, evals are important in like your own context to confirm it's actually worth the offline compute."
>
> — [24:13](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1453s) &middot; *acknowledges dreaming has a compute cost that needs local justification*

## Positions

- Async agent experiences are only viable once model task horizons exceed roughly an hour; below that, the agent errors out and returns too quickly for async to be a good UX. ([1:25](https://www.youtube.com/watch?v=9QebvrrY3KY&t=85s), confidence: stated)
- Putting the harness and the sandbox in the same container is the wrong architecture for long-horizon agents, because a container death loses the entire session. ([3:17](https://www.youtube.com/watch?v=9QebvrrY3KY&t=197s), confidence: stated)
- Credentials should live in a separate vault and never be added to the agent's sandbox container. ([4:38](https://www.youtube.com/watch?v=9QebvrrY3KY&t=278s), confidence: stated)
- An append-only, immutable session log is superior to destructive compaction because the model can always fetch back old context. ([5:17](https://www.youtube.com/watch?v=9QebvrrY3KY&t=317s), confidence: stated)
- Self-grading in the same context window that produced the work causes confabulation and odd artifacts; verification must be a separate, separately tuned context. ([5:54](https://www.youtube.com/watch?v=9QebvrrY3KY&t=354s), confidence: stated)
- Build/verifier loops paired with high-capacity models are a good general primitive for long-running asynchronous work. ([9:40](https://www.youtube.com/watch?v=9QebvrrY3KY&t=580s), confidence: stated)
- Claude's in-band memory writing has improved measurably across model generations, from Sonnet 3.5 to 4.6, on both Pokémon progress and Continual Learning Bench. ([11:32](https://www.youtube.com/watch?v=9QebvrrY3KY&t=692s), confidence: stated)
- The key capability difference between low- and high-capacity models at memory writing is distillation — knowing which generalizable abstraction to save rather than which specific fact. ([13:02](https://www.youtube.com/watch?v=9QebvrrY3KY&t=782s), confidence: stated)
- In-band memory writing alone is insufficient; an out-of-band consolidation pass is required to correct incorrect or only-locally-optimal memories. ([13:35](https://www.youtube.com/watch?v=9QebvrrY3KY&t=815s), confidence: stated)
- Frontier models operate in a 12+ hour task horizon regime on METR, including OpenAI's Codex, while non-frontier models do not. ([19:48](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1188s), confidence: stated)
- The frontier gap in long-horizon agent products comes from combined investment in architecture, infrastructure, security, and memory — not model capability alone. ([21:05](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1265s), confidence: stated)
- The choice between file system and database as a memory substrate does not matter much; what matters is that the substrate is highly programmable with simple primitives. ([21:37](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1297s), confidence: stated)
- Prescriptive memory schemas that pre-specify what types of memories to save cause performance to drop relative to letting the model manage memory freely. ([22:41](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1361s), confidence: stated)
- Agent harnesses will shift from single-player and reactive to multiplayer, org-scoped, and proactive. ([18:19](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1099s), confidence: stated)
- Dreaming's offline compute cost needs to be justified with evals in your own context rather than assumed worthwhile. ([24:13](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1453s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [background agents](../concepts/background-agents.md)
- [context compaction](../concepts/context-compaction.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [verifier design](../concepts/verifier-design.md)

