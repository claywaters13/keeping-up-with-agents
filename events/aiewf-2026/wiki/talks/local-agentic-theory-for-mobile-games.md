---
title: "Local Agentic Theory For Mobile Games"
type: "talk"
slug: "local-agentic-theory-for-mobile-games"
track: "Neo4j Graphs Track"
org: "The New York Times"
video_id: "418t26CVz-w"
duration_sec: 1084
word_count: 3129
speakers: ["Joanne Song", "Shafik Quoraishee"]
---

# Local Agentic Theory For Mobile Games

**Speakers:** [Joanne Song](../speakers/joanne-song.md), [Shafik Quoraishee](../speakers/shafik-quoraishee.md)

**Org:** The New York Times

**Track:** Neo4j Graphs Track &nbsp;|&nbsp; **Duration:** 18m 04s

[Watch on YouTube](https://www.youtube.com/watch?v=418t26CVz-w)

## Summary

Two New York Times Games engineers argue that the next useful place for agents in mobile games is on the device, not in the cloud, and not for generating puzzle content. Shafik Quoraishee traces game AI from finite state machines through the AlphaZero/EfficientZero reinforcement-learning lineage to agentic systems that reason over game state via in-context learning and tool calls instead of grinding a reward function, then shows two prototypes: an agentic Space Invaders player and a constraint-satisfaction agent that solves the Mini Crossword by backtracking over a satisfaction graph. The engineering core of the talk is a three-way constraint budget — space (weights, state history, planning artifacts, render headroom), time (a full plan must fit inside a 16 ms frame at 60 Hz), and energy (battery, pre-NPU) — with soft-constraint tuning across them. Joanne Song then makes the payoff case: accessibility should move from binary WCAG 2.2 pass/fail toward WCAG 3.0's graded bronze/silver/gold, with an on-device agent continuously tuning dials like input tolerance and step granularity from gaze, shaky taps, and focus-trap detection. Worth watching if you care about tight-latency on-device agent loops or about accessibility as a live, adaptive system rather than a static easy mode.

## Key Points

- The New York Times' puzzles are authored by people and contain no AI features; this work is experimental research on solvability and playability, not content generation.
- Reinforcement learning changes a model's weights to master one game, whereas an agentic system reasons over game state in context with no reward loop to grind, making it far more adaptable to new situations.
- On-device inference is pitched on four grounds — lower latency by removing the cloud round trip, privacy because computation never leaves the device, offline playability (e.g. in a subway tunnel), and personalization.
- Local game agents face a joint constraint graph of space (model weights, compressed state history, planning artifacts, render headroom), time, and energy, optimized with soft constraints so one budget isn't over-penalized.
- The hard timing target is a 16 ms frame at 60 Hz refresh: agent planning must complete inside it or the game visibly janks.
- Battery is a live limit because current phones aren't optimized for agentic workloads; NPUs and AI chips are arriving but the loop must currently be hand-curated for minimum energy.
- Model base intelligence is still a ceiling — the speaker invokes ARC-AGI scores to argue current models can't yet make the complex decisions the most interesting future games would require.
- Accessibility should shift from deterministic toggles and static menus to continuously tuned dials (input tolerance, step granularity), mirroring WCAG 3.0's move from pass/fail to graded bronze/silver/gold.
- The agent should act, not just observe: detecting a keyboard focus trap and injecting an exit route, or auditing layout on the fly and resizing tap targets that violate size rules.
- Remaining gaps named for local game agents: faster planning, predictive models of layout changes, long-term per-person memory, a shared cross-game state language, better chips, and honest benchmarks.

## Notable Quotes

> "Our puzzles are made by people. They're not made by AI."
>
> — [0:01](https://www.youtube.com/watch?v=418t26CVz-w&t=1s) &middot; *Sets the hard editorial boundary the entire research program operates within.*

> "There's no AI in the games themselves."
>
> — [0:01](https://www.youtube.com/watch?v=418t26CVz-w&t=1s) &middot; *Unambiguous product claim that separates this research from AI-generated puzzle content.*

> "most AI infrastructure today runs really on the cloud and if you're running mobile application, most practical scenarios involve cloud architecture"
>
> — [3:05](https://www.youtube.com/watch?v=418t26CVz-w&t=185s) &middot; *States the status quo the talk's central thesis pushes against.*

> "So, RL changes the model itself and changes the weights in the model."
>
> — [6:23](https://www.youtube.com/watch?v=418t26CVz-w&t=383s) &middot; *Half of the talk's core RL-versus-agentic distinction, stated crisply.*

> "the agentic system reasons over a space in the game, um and there's no reward system to grind out"
>
> — [6:23](https://www.youtube.com/watch?v=418t26CVz-w&t=383s) &middot; *The other half of the distinction, and the reason the speaker favors agents for dynamic situations.*

> "you get a new frame every 16 ms a pound if your refresh rate is 60 Hz"
>
> — [8:44](https://www.youtube.com/watch?v=418t26CVz-w&t=524s) &middot; *The hard latency number that defines the on-device agent's planning budget.*

> "if you go outside of that budget, what will happen in the agent execution, you're going to see jank and other things on mobile devices that that are very hard to pull out"
>
> — [8:44](https://www.youtube.com/watch?v=418t26CVz-w&t=524s) &middot; *Names the concrete failure mode of missing the frame budget.*

> "the agentic design of the loop on the device has to be very curated to do as minimum energy processing as possible, otherwise your phones die fast as it is and they'll die even faster"
>
> — [9:18](https://www.youtube.com/watch?v=418t26CVz-w&t=558s) &middot; *Frames battery as a first-class design constraint, not an afterthought.*

> "the base intelligence of a lot of these models aren't capable yet of being fully cognizant of all the complex decisions that an agent can make in the most intelligent and possibly interesting games in the future"
>
> — [10:51](https://www.youtube.com/watch?v=418t26CVz-w&t=651s) &middot; *A candid limitation claim tied to ARC-AGI-style capability measurement.*

> "this is called a constraint satisfaction agent which uses a satisfaction graph to figure out how to put the words in the crossword puzzle at the right place"
>
> — [10:51](https://www.youtube.com/watch?v=418t26CVz-w&t=651s) &middot; *Describes the second prototype's architecture, a graph-based solver rather than a raw LLM.*

> "traditionally games live in a world of fixed state models, rigid, hand-authored. A player's choice is often limited to a toggle or a static menu."
>
> — [12:11](https://www.youtube.com/watch?v=418t26CVz-w&t=731s) &middot; *Sets up the accessibility argument by naming what current systems get wrong.*

> "We ground our design in an existing international standard, WCAG 2.2."
>
> — [12:52](https://www.youtube.com/watch?v=418t26CVz-w&t=772s) &middot; *Anchors the approach in established accessibility standards rather than ad hoc heuristics.*

> "A static easy mode can't fix a crossword grid that remains fundamentally blind to our players."
>
> — [13:43](https://www.youtube.com/watch?v=418t26CVz-w&t=823s) &middot; *The sharpest one-line indictment of difficulty toggles as an accessibility answer.*

> "WCAG 3.0, spoiler alert, is following the trends of dropping the binary pass/fail to a graded bronze, silver, and gold scoring."
>
> — [13:43](https://www.youtube.com/watch?v=418t26CVz-w&t=823s) &middot; *External standards evidence for the talk's continuous-dial framing.*

> "The agent rewrites the layout live adapting to the human and not the other way around."
>
> — [15:52](https://www.youtube.com/watch?v=418t26CVz-w&t=952s) &middot; *Compresses the accessibility thesis into a single design principle.*

> "Accessibility and challenge stop being treated separately and become two ends of one dial constantly tuning for the moment."
>
> — [15:52](https://www.youtube.com/watch?v=418t26CVz-w&t=952s) &middot; *A genuinely contestable reframing of accessibility versus game difficulty.*

> "We need a plan we need plans and decisions within a 16-ms frame to prevent stuttering for games."
>
> — [16:40](https://www.youtube.com/watch?v=418t26CVz-w&t=1000s) &middot; *Restates the frame budget as an open research requirement, not a solved problem.*

> "We need a shared game state language so one agent can work across multiple games instead of being rebuilt from scratch for different releases"
>
> — [16:40](https://www.youtube.com/watch?v=418t26CVz-w&t=1000s) &middot; *Identifies a missing standard that would make local game agents portable.*

> "the future of AI doesn't have to be one giant centralized brain. It can be billions of small local brains, each running on a personal device, each shaped entirely by the individual it serves."
>
> — [17:16](https://www.youtube.com/watch?v=418t26CVz-w&t=1036s) &middot; *The talk's closing thesis on decentralized, personalized on-device intelligence.*

## Positions

- New York Times puzzles are authored entirely by people, with no AI in the games and no AI features shipped (Wordle Bot is not an AI feature). ([0:01](https://www.youtube.com/watch?v=418t26CVz-w&t=1s), confidence: stated)
- Cloud inference for mobile games is expensive and slow because of round-trip calls, so intelligence should be offloaded onto the device. ([3:05](https://www.youtube.com/watch?v=418t26CVz-w&t=185s), confidence: stated)
- Local computation keeps gameplay AI inside the device's security zone and is not needed upstream for telemetry. ([3:40](https://www.youtube.com/watch?v=418t26CVz-w&t=220s), confidence: stated)
- Agentic systems differ fundamentally from RL: RL retrains weights per game, while agents reason over game state via in-context learning and tool calls with no reward system, making them more dynamic. ([6:23](https://www.youtube.com/watch?v=418t26CVz-w&t=383s), confidence: stated)
- An on-device game agent must complete planning within a 16 ms frame at 60 Hz or the game will show jank. ([8:44](https://www.youtube.com/watch?v=418t26CVz-w&t=524s), confidence: stated)
- Current mobile devices are not optimized for agentic workloads, though NPUs and AI chips are moving toward it. ([9:18](https://www.youtube.com/watch?v=418t26CVz-w&t=558s), confidence: stated)
- Time constraints should be penalized harder than space constraints because exceeding time disrupts the user experience. ([10:02](https://www.youtube.com/watch?v=418t26CVz-w&t=602s), confidence: stated)
- Current models' base intelligence, as indicated by ARC-AGI-style scores, is insufficient for the most complex future game agents. ([10:51](https://www.youtube.com/watch?v=418t26CVz-w&t=651s), confidence: stated)
- Deterministic, hand-authored accessibility settings are blind to players' real-time needs and a static easy mode cannot fix an inaccessible crossword grid. ([13:43](https://www.youtube.com/watch?v=418t26CVz-w&t=823s), confidence: stated)
- Accessibility should be a graded, continuously tuned scale rather than a binary checkbox, following WCAG 3.0's bronze/silver/gold direction. ([13:43](https://www.youtube.com/watch?v=418t26CVz-w&t=823s), confidence: stated)
- Accessibility and challenge are not separate systems but two ends of the same continuously tuned dial. ([15:52](https://www.youtube.com/watch?v=418t26CVz-w&t=952s), confidence: stated)
- Local game agents will require a shared game state language so one agent can transfer across games instead of being rebuilt per release. ([16:40](https://www.youtube.com/watch?v=418t26CVz-w&t=1000s), confidence: stated)
- Claims that on-device agents improve the experience require real benchmarks and honest testing, which do not yet exist. ([17:16](https://www.youtube.com/watch?v=418t26CVz-w&t=1036s), confidence: stated)
- AI's future is decentralized — billions of small per-device models personalized to individuals — rather than one centralized brain. ([17:16](https://www.youtube.com/watch?v=418t26CVz-w&t=1036s), confidence: stated)

## Concepts

- [agentic loop design](../concepts/agentic-loop-design.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [latency budgets](../concepts/latency-budgets.md)
- [local inference](../concepts/local-inference.md)
- [post-training](../concepts/post-training.md)
- [rl environment design](../concepts/rl-environment-design.md)

