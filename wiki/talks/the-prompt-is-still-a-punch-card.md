---
title: "The Prompt Is Still a Punch Card"
type: "talk"
slug: "the-prompt-is-still-a-punch-card"
org: "JoinIn AI"
video_id: "hVJOnuhFmTA"
duration_sec: 1213
word_count: 3153
speakers: ["Ted Johnson"]
---

# The Prompt Is Still a Punch Card

**Speakers:** [Ted Johnson](../speakers/ted-johnson.md)

**Org:** JoinIn AI

**Duration:** 20m 13s

[Watch on YouTube](https://www.youtube.com/watch?v=hVJOnuhFmTA)

## Summary

Ted Johnson argues that while AI models have exploded in capability, the interface protocol we use to reach them has not moved since the punch card era. He separates three ideas — channel (the physical medium), expression (how much meaning it can carry), and protocol (the rules of the exchange) — and shows that natural language expanded expression enormously while the channel stayed a text box and the protocol stayed batch: you package a complete turn, submit, wait, and repair. Prompt engineering, in this framing, is not mastery but a set of incantations for assembling a deck so the job won't fail, and the friction users feel is the interface's fault, not theirs. He demos speech-to-speech failures (an AI answering a remark addressed to someone else in the room), NVIDIA's Personal Plex handling interruption and backchanneling, and his own company's system tracking who holds the floor in a multi-person meeting and taking a turn only when appropriate. Worth watching if you design AI products and want a vocabulary for why chat interfaces feel like work even when the model is excellent.

## Key Points

- Interfaces should be analyzed along three separate axes — channel (the physical transport), expression (the range of meaning it can carry), and protocol (the shape and rules of the exchange) — because they can and do advance independently.
- Natural language was a genuine leap in expression, but the channel (a keyboard and a text box) and the protocol (batch submission) did not change alongside it.
- Prompting is structurally identical to punch-card batch: assemble the full request offline, submit, wait, read the result, find what's wrong, resubmit — shrinking the wait from overnight to seconds fooled people into thinking it became interactive.
- Prompt engineering is a set of packaging rules dressed up as a power-user skill, and the fact that people got good at it should worry engineers rather than reassure them.
- Voice does not escape batch, because speech is simply transcribed into the same box and submitted as one complete turn.
- The mismatch — model capability curving upward while interface protocol stays flat — leaves humans doing all the surrounding work: deciding what context matters, choosing timing, noticing ambiguity, and repairing output.
- Users who feel bad at AI are experiencing an interface defect, not a personal deficiency.
- Turn-taking, backchanneling, and knowing whether words were even addressed to the machine are protocol problems; Johnson demos systems that yield on interruption and only speak when no one else holds the floor.
- The design question should become which burdens are still placed on humans only because machines used to be too limited to carry them, with the AI choosing modality and timing rather than the user.

## Notable Quotes

> "why do we still have to learn AI? Why does something this powerful so often feel unnatural to use?"
>
> — [0:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=51s) &middot; *States the animating question of the whole talk in the speaker's own framing.*

> "We carry these legacies of an arbitrary input device designed under constraints that haven't existed for a century. And we put it between ourselves and the most capable machines ever built. Nobody alive chose it. We all inherited it. And then we stopped noticing."
>
> — [3:01](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=181s) &middot; *The keyboard-as-inherited-constraint argument that sets up the channel concept.*

> "Humans use all these channels constantly without thinking. We never pick one channel and force everything through it. That would be absurd. And yet, that's what we ask people to do with machines over and over."
>
> — [3:43](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=223s) &middot; *Names the multimodality gap as a design failure rather than a technical limit.*

> "The keyboard didn't change. What improved is the range of what you're permitted to express through it."
>
> — [4:24](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=264s) &middot; *The sharpest statement of the channel/expression distinction.*

> "The channels for computers have been the same for 15 years, some 180 years. Now, with AI, we've poured an ocean of expression into it. So, why does it feel like we're still sipping through a straw"
>
> — [5:50](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=350s) &middot; *Quantifies the asymmetry between channel stasis and expression growth.*

> "Channel stayed the same. Expression exploded in the last 3 years with LLMs, but the protocol, prompting, is the protocol of a punch card."
>
> — [5:50](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=350s) &middot; *The title thesis, stated compactly with all three concepts in play.*

> "The machine never engaged with you while you were thinking. It engaged with the finished package after the fact."
>
> — [6:33](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=393s) &middot; *Defines batch in a way that transfers cleanly from punch cards to prompts.*

> "We shrank the wait time from overnight to a few seconds or few minutes, and the speed fooled us into thinking that it become interactive. It hasn't. It's still batch."
>
> — [7:16](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=436s) &middot; *Directly rebuts the obvious objection that modern chat is already interactive.*

> "And speaking doesn't change it. Your voice just gets transcribed into the box and submitted."
>
> — [7:16](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=436s) &middot; *Preempts voice as the assumed fix, a position many product teams would dispute.*

> "The protocol is the part we've had to learn. We just gave it a flattering name. We call it prompt engineering and treat it like it's a power user skill. Strip the label off and it's a set of rules for packaging up good old batch."
>
> — [7:56](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=476s) &middot; *The most contrarian claim in the talk — prompt engineering as inherited constraint, not craft.*

> "It feels like mastery, but it's the same sort of mastery a punch card operator had. Knowing exactly how to assemble the deck so the job wouldn't fail."
>
> — [8:34](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=514s) &middot; *The analogy that makes the prompt-engineering critique land.*

> "None of this means prompts are bad. Punch cards weren't bad. Command lines aren't bad. They're brilliant solutions for constraints of their time. But that's the whole question. Is batch still the right protocol?"
>
> — [8:34](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=514s) &middot; *Shows the argument is about fit to current constraints, not disparagement.*

> "Model capacity is shooting straight up. Reasoning, speech, vision, memory, planning, all curving upwards. The interface protocol, flat."
>
> — [9:54](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=594s) &middot; *The core diagnostic image of the talk.*

> "The human still decides what context matters, still remembers what to ask, still chooses the timing, still notices the ambiguity, still repairs the output, still has to carefully engineer a prompt."
>
> — [9:54](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=594s) &middot; *Enumerates the specific labor the current protocol offloads onto users.*

> "We are not bad at using AI. We are being asked to operate a brand new kind of intelligence through a protocol of a punch card. The mismatch isn't the user, it's the interface."
>
> — [10:35](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=635s) &middot; *The talk's rhetorical center, reassigning blame from user to design.*

> "That's not a good answer, but it's not a dumb model."
>
> — [11:11](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=671s) &middot; *Crisply separates model quality from protocol failure using the live 'Hey Ted' example.*

> "it's a protocol with exactly one slot. Your message, then it's reply. It has no concept of who's speaking, whether the words were even meant for it."
>
> — [11:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=711s) &middot; *Names addressee detection as a missing protocol primitive, not a model capability.*

> "We're seeing the field is converging on the same conclusion we built our company on. The interface has to stop being batch and start participating."
>
> — [11:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=711s) &middot; *States the speaker's commercial thesis and his read on where the field is heading.*

> "Making listening noises is not really the same as knowing who's in the room."
>
> — [13:08](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=788s) &middot; *Draws a tradeoff line between surface conversational polish and real participation.*

> "No one wrote the prompt, no one patched the turn and hit submit. The system was in the conversation, following it, understanding, and choosing its moment."
>
> — [15:44](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=944s) &middot; *Describes the demo's payoff and what a post-batch protocol actually looks like.*

> "AI is not just an intelligence technology. It's increasingly becoming an interface technology. And if so, then book smart models alone are not enough."
>
> — [16:40](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1000s) &middot; *The mindset shift the speaker explicitly frames as his takeaway.*

> "For 75 years, humans adapted to the machine. It's syntax, it's forms, it's timing, it's batch. A system that can reason, listen, infer, adapt should be able to meet us partway, if not all the way."
>
> — [17:39](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1059s) &middot; *Frames the normative claim about who should do the adapting.*

> "It needs to become what burden are we still putting on humans only because the machine used to be too limited to carry that burden itself."
>
> — [17:39](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1059s) &middot; *The single actionable design heuristic offered.*

> "The answer isn't always chat. It isn't always voice, and not a wall of markdown. It's definitely not a decade-old set of digital constructs."
>
> — [18:24](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1104s) &middot; *Rejects the two default modalities most AI products reach for.*

> "An interface where timing and modality aren't the humans' job anymore. Where choosing the right channel at the right moment is done by the AI."
>
> — [18:24](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1104s) &middot; *The concrete design target implied by the three-concept framework.*

> "Every step was progress and every step carried the old constraint forward into the next era. A translation tax, a precision tax, context tax, repair tax."
>
> — [19:11](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1151s) &middot; *Names the recurring costs of encoding intent for machines across computing history.*

## Positions

- The prompt interface is structurally the same batch protocol as the punch card: the machine only engages after the human packages and submits a complete turn. ([6:33](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=393s), confidence: stated)
- Current chat interfaces are not truly interactive; reduced latency created an illusion of interactivity without changing the protocol. ([7:16](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=436s), confidence: stated)
- Voice input does not escape the batch protocol, because speech is transcribed into the same single-slot text submission. ([7:16](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=436s), confidence: stated)
- Prompt engineering is not a genuine skill advance but a set of packaging rules, and human proficiency at it is evidence of a design failure. ([7:56](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=476s), confidence: stated)
- Model capability is rising rapidly while interface protocol capability has stayed flat. ([9:54](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=594s), confidence: stated)
- User frustration with AI is caused by the interface, not by user inadequacy or insufficient prompting skill. ([10:35](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=635s), confidence: stated)
- Current speech-to-speech models cannot determine whether spoken words were addressed to them, which is a protocol limitation rather than a model intelligence limitation. ([11:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=711s), confidence: stated)
- The field is converging on the conclusion that interfaces must stop being batch and start participating, as evidenced by OpenAI's GPT real-time 2 released in late May and NVIDIA's Personal Plex research model. ([11:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=711s), confidence: stated)
- Backchanneling and conversational flow are insufficient; real participation requires modeling who is in the room and who holds the floor. ([13:08](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=788s), confidence: stated)
- AI should be understood primarily as an interface technology, not only an intelligence technology. ([16:40](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1000s), confidence: stated)
- Choosing modality and timing should be the AI's responsibility rather than the user's. ([18:24](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1104s), confidence: stated)
- Removing interface burden from users is what drives adoption of AI systems. ([18:24](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1104s), confidence: implied)
- Chat and voice are both inadequate as universal default interfaces for AI. ([18:24](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=1104s), confidence: stated)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [background agents](../concepts/background-agents.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [vision-language models](../concepts/vision-language-models.md)
- [voice agents](../concepts/voice-agents.md)

