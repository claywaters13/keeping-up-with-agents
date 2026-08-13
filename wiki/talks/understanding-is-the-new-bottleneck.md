---
title: "Understanding is the new bottleneck"
type: "talk"
slug: "understanding-is-the-new-bottleneck"
track: "Design Engineering"
org: "Notion"
day: "Day 3 — Session Day 2"
room: "Track 6"
video_id: "WkBPX-oDMnA"
duration_sec: 1173
word_count: 3771
speakers: ["Geoffrey Litt"]
---

# Understanding is the new bottleneck

**Speakers:** [Geoffrey Litt](../speakers/geoffrey-litt.md)

**Org:** Notion

**Track:** Design Engineering &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 6 &nbsp;|&nbsp; **Duration:** 19m 33s

[Watch on YouTube](https://www.youtube.com/watch?v=WkBPX-oDMnA)

## Summary

Geoffrey Litt, a design engineer at Notion, argues that as agents write ever-larger volumes of code, the bottleneck is no longer correctness checking but human understanding. He distinguishes 'understanding to verify' (which agents are increasingly able to do themselves) from 'understanding to participate' — the accumulated conceptual grasp that lets you have the next creative idea, and whose erosion he calls cognitive debt. The bulk of the talk is three concrete practices borrowed from education research: agent-generated explainer docs with background, intuition, interactive figures, and literate code diffs; quizzes that gate whether he sends a PR for review; and 'microworlds' — throwaway debuggers, simulations, and step-through UIs an agent builds so you can feel how a system works. He closes with shared spaces (multiplayer human-agent threads and commentable docs in Notion) and an Alan Kay–inflected argument that cheap code should put humans more deeply in the loop, not out of it. Watch it for immediately usable techniques and a well-argued frame for why review-as-correctness-check is the wrong mental model.

## Key Points

- The common framing that humans review agent output to check correctness is incomplete, and the human role in correctness checking is genuinely shrinking as verification loops improve.
- The durable reason to understand code is 'understanding to participate': rich conceptual structures in your head are what let you fluently recombine ideas and take creative leaps on the next loop.
- Cognitive debt is the analogue of technical debt — you can get away with not understanding for a while, but at some point you can no longer participate in your own project.
- Litt's 'explaindiff' skill produces a code explainer doc structured like good teaching: background first, intuition before details, interactive figures where useful, and a literate prose-ordered diff rather than a raw file list.
- Reading is not proof of understanding, so each explainer doc ends with a five-question quiz, and Litt's personal rule is not to send code for review until he can pass it — a deliberate 'speed regulator' against moving at the speed of correctness rather than understanding.
- Microworlds — an ephemeral debugger visualizing an interpreter's step-by-step state, or a click-through 'video game' version of a framework migration — give an intuitive feel for a system that fixing the bug via an agent would not produce.
- Understanding is also a team property: multiplayer chat threads containing multiple humans and agents, and commentable plan documents, build collective understanding the way Slack channels beat one-on-one DMs.
- Because code is now effectively free, ephemeral UIs, simulations, debuggers, and playgrounds built purely for comprehension are newly practical — recovering Alan Kay's and Papert's original vision that computers exist to level up humans.

## Notable Quotes

> "I think it is still important for people to understand how code works."
>
> — [0:01](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=1s) &middot; *The talk's thesis, framed by Litt as a hot take for this audience.*

> "Agents are writing tons of code for us. They're landing 50,000 line PRs. And it is getting harder to keep up."
>
> — [0:47](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=47s) &middot; *States the scale problem that motivates the whole talk.*

> "When people say things like code review is the new bottleneck, I think that's the first thing that pops into people's heads is correctness checking."
>
> — [2:39](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=159s) &middot; *Names the mental model he's arguing against.*

> "The the role of humans in correctness checking is decreasing. And you know what? I actually don't hate that."
>
> — [3:16](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=196s) &middot; *A concession that sharpens the argument — he is not defending human review on correctness grounds.*

> "There is a deeper reason to understand what's going on, and that's understanding to participate."
>
> — [3:50](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=230s) &middot; *The central distinction the talk turns on.*

> "Your understanding of what's going on is the foundation for you having that next idea and being an active creative participant in a project."
>
> — [4:29](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=269s) &middot; *The positive case for understanding, stated directly.*

> "when you have rich conceptual structures in your head that you can fluently recombine really fast without going out to like ask some some agent or some human how it works, that gives you the ability to fluidly take creative leaps"
>
> — [4:29](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=269s) &middot; *Explains the mechanism behind why offloaded understanding costs you something.*

> "similarly to tech debt, you might get away with it for a little bit, but at some point you get burned if your understanding degrades"
>
> — [5:09](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=309s) &middot; *Defines cognitive debt via its closest existing analogy.*

> "You're vibe coding, things are going well, and then at some point you realize, wait, I've no idea what's going on. I basically can't participate anymore"
>
> — [5:42](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=342s) &middot; *The concrete failure mode the audience is likely to recognize.*

> "if you sent a team away for a year to come up with a personalized curriculum just to explain this one code change to you, what would that look like? I think this is a very generative question to ask."
>
> — [7:00](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=420s) &middot; *The design prompt behind his explainer-doc tooling.*

> "Second important principle is intuition before details."
>
> — [8:01](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=481s) &middot; *One of the explicit pedagogical rules structuring the explainer format.*

> "I think you have to be careful with interactivity. It can just be a crutch, and it can be kind of slop, to be honest. But used tastefully, it can provide understanding that's hard to achieve with just static pictures."
>
> — [9:12](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=552s) &middot; *Names a tradeoff rather than selling the technique unconditionally.*

> "I print these out and take them to the coffee shop sometimes and just read them."
>
> — [9:47](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=587s) &middot; *Vivid evidence that the artifact changes the work practice, not just the output.*

> "it's really easy to read a book and not realize you didn't understand it"
>
> — [10:21](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=621s) &middot; *The Matuschak premise that justifies quizzing yourself on your own PRs.*

> "my rule is I don't send code to uh others on my team to review unless I can pass the quiz about what my agents wrote"
>
> — [10:55](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=655s) &middot; *The single most actionable, checkable commitment in the talk.*

> "How do we make sure we're not just moving at the speed of correctness, but also of understanding? And the quiz is that speed regulator"
>
> — [11:28](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=688s) &middot; *Reframes a quiz as a rate limiter on velocity, which is the interesting claim.*

> "as I was fixing the bugs, I was getting a feel for the machine, right? That's something that if you just have an agent go fix the bug, you don't get that peripheral vision."
>
> — [13:19](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=799s) &middot; *States precisely what full delegation costs you.*

> "agents can write code to help us understand code. Where the point isn't building software to ship, it's building these little micro worlds for us."
>
> — [14:49](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=889s) &middot; *The generalizable takeaway from the microworlds section.*

> "instead of me and my PM both talking to our own agents, we're in a shared space, we can see each other's communication"
>
> — [15:31](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=931s) &middot; *The argument for multiplayer agent surfaces over per-person chats.*

> "With AI, we can kind of empower ourselves more, not just taking ourselves out of loops, but actually putting ourselves more deeply in loops than we ever have before."
>
> — [18:27](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=1107s) &middot; *The closing inversion of the standard automation narrative.*

## Positions

- The human role in checking agent output for correctness is declining and will keep declining as verification loops improve, and that is a good thing. ([3:16](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=196s), confidence: stated)
- Better agents will not remove the need for humans to understand their code, because understanding is the prerequisite for creative participation rather than for verification. ([5:09](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=309s), confidence: stated)
- Degraded understanding accumulates like technical debt and eventually makes you unable to contribute to your own project. ([5:09](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=309s), confidence: stated)
- Reading an explanation is insufficient evidence of understanding; an explicit test is required to catch self-deception. ([10:21](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=621s), confidence: stated)
- Engineers should gate sending code for team review on being able to pass a quiz about what their agent wrote. ([10:55](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=655s), confidence: stated)
- Interactive figures are frequently slop and are only worth adding where static explanation genuinely falls short. ([9:12](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=552s), confidence: stated)
- Delegating a bug fix entirely to an agent forfeits the peripheral understanding of the system you would gain by debugging it yourself. ([13:19](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=799s), confidence: stated)
- Understanding is a team-level property, so agent conversations and plans belong in shared, commentable spaces rather than in individuals' local terminals. ([15:31](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=931s), confidence: stated)
- Because generating code is now nearly free, building throwaway software purely to understand other software is a practical everyday technique rather than a luxury. ([18:27](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=1107s), confidence: stated)
- Mainstream computing drifted away from Alan Kay's original goal of using computers to amplify human understanding, and AI is an opportunity to return to it. ([17:53](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=1073s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent-readable codebases](../concepts/agent-readable-codebases.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [code comprehension and indexing](../concepts/code-comprehension-and-indexing.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [generative ui](../concepts/generative-ui.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [world models](../concepts/world-models.md)

