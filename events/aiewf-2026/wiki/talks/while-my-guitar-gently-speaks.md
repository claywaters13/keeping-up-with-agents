---
title: "While my guitar gently speaks"
type: "talk"
slug: "while-my-guitar-gently-speaks"
track: "Generative Media"
org: "Philo Ventures"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "E_Txocq-Lrw"
duration_sec: 1115
word_count: 3216
speakers: ["Todd Fisher"]
---

# While my guitar gently speaks

**Speakers:** [Todd Fisher](../speakers/todd-fisher.md)

**Org:** Philo Ventures

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 18m 35s

[Watch on YouTube](https://www.youtube.com/watch?v=E_Txocq-Lrw)

## Summary

Todd Fisher walks through a personal side project: a Logic Pro audio plugin that makes an electric guitar talk and eventually sing. He traces the guitar's chain of augmentation — pickups, effects pedals, Peter Frampton's talk box, software emulation — and positions LLM-driven speech as the next step, then shows the actual signal path he built: text-to-speech audio sliced per word, YIN pitch detection on the guitar signal, a synthesized sawtooth note pushed through the voice clip and a vocoder, and a Whisper + local-LLM loop so the guitar can answer audience questions. Most of the talk is honest engineering detail about where it breaks: energy-gap segmentation fails when there is no silence between spoken words, sonority-peak syllabification only partly fixes it, and the sample-based singing path (VocalSet samples pitch-shifted with World) is too heavy to run live and must be pre-baked. Live demos misfire on stage and he keeps going, which is part of the point. Watch it if you want a concrete tour of real-time audio DSP plus AI glue code, or a low-stakes nudge to build the passion project sitting in your backlog; skip it if you want production AI-engineering practice.

## Key Points

- The project's core signal chain is: detect the guitar's fundamental pitch with the YIN algorithm, generate a synthesized sawtooth note with an ADSR envelope, fill it with TTS voice content, and push it through a vocoder so the note carries speech.
- Slicing TTS audio into individual words by energy-gap segmentation is unreliable because natural speech often has no silence between words, so the cut points are not 100% foolproof.
- Adding sonority-peak syllabification — finding vowels as syllable markers — on top of energy gaps improved segmentation but still did not work well enough, so Fisher fell back to manually dragging segment boundaries in the plugin UI.
- Making the guitar conversational required only off-the-shelf glue: Whisper for speech-to-text, any local LLM for the response, and the existing TTS-to-guitar path for output; Fisher says the choice of LLM does not matter.
- The singing version uses open-source VocalSet recordings pitch-shifted with the World library and mapped per fret, but the processing is heavy enough that it must be pre-baked offline rather than run live.
- He demoed only the five vowel sounds because pre-baking a fuller sample set takes too long, and concedes the result is 'not quite your opera singer' — the singing goal is not yet reached.
- JUCE is his recommended framework for building audio software, and a DAW is framed as the musician's equivalent of an IDE, with the plugin dropping into Logic Pro like any other effect.
- The framing argument is that AI has collapsed the time cost of side projects, so the backlog of 'cool idea' projects engineers keep is now worth actually building.

## Notable Quotes

> "part of uh my goal today is to inspire you guys to find whatever project you're passionate about, go start building it because it's super easy now with AI it's easier with AI."
>
> — [2:21](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=141s) &middot; *states the talk's thesis about AI lowering the cost of passion projects*

> "There is the argument made hot take uh that maybe you don't need all those physical effects pedals anymore."
>
> — [3:34](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=214s) &middot; *an explicitly flagged hot take about software emulation displacing hardware*

> "And then of course looking forward it's what is that next evolution of the guitar uh with AI in the picture?"
>
> — [3:34](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=214s) &middot; *frames the whole project as the next entry in the guitar's augmentation lineage*

> "And I settled on this idea of like, "Hey, how hard would it be to make my guitar speak?" It sounds easy, maybe, maybe not."
>
> — [5:29](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=329s) &middot; *names the project's driving question and hedges the difficulty up front*

> "And for those that are not aware, your DAW is effectively your IDE but for musicians and and music producers."
>
> — [6:02](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=362s) &middot; *the analogy that makes the rest of the plugin architecture legible to software engineers*

> "the idea there is there's typically silence in between words. So, let's just cut it whenever the decibels are are very much close to zero, right?"
>
> — [8:03](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=483s) &middot; *states the naive segmentation heuristic he tried first*

> "there's actually no silence in between some of my words. So, it gets a little bit challenging to where it's not 100% foolproof, right?"
>
> — [8:03](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=483s) &middot; *names the concrete failure mode of energy-gap segmentation*

> "I effectively identifying the syllables of the audio signal and identifying that there's vowels in here. Vowels typically lead to syllables."
>
> — [8:32](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=512s) &middot; *explains the sonority-peak fallback layered on top of the energy-gap approach*

> "long story short, uh I settled on just the ability to go and actually I could drag this and manually edit some of these uh uh segments in here."
>
> — [9:21](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=561s) &middot; *admits the automated segmentation was not good enough and a human-in-the-loop editor won*

> "there is definitely a fundamental frequency or the the kind of the the one that we identify as the note, but there's a bunch of other frequencies."
>
> — [9:53](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=593s) &middot; *sets up why pitch detection is a nontrivial problem, not a lookup*

> "Uh we then push it through uh the the voice clip effectively. So, think of the talk box. Uh we're kind of filling up the cavity of the talk of the voice, that is. And we push it through a vocoder, and it should sing."
>
> — [10:59](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=659s) &middot; *the clearest statement of the full synthesis architecture and its talk-box analogy*

> "was going to uh play a song that is very much related to the talk or the the title of my talk, uh while my guitar gently speaks, but because it's going to be posted online, I don't want to muddy up the waters with any copyright things."
>
> — [11:44](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=704s) &middot; *a working musician-engineer navigating copyright constraints on recorded demos*

> "Uh it doesn't really matter what LLM, just any local model. I have a conversation coming and then from that output go and plop it on the guitar."
>
> — [14:16](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=856s) &middot; *takes the position that model choice is interchangeable for this application*

> "Uh this is a very heavy process, and so I can't really do that live. I have to effectively pre-bake that. And then once it's already pre-baked, I could then go and jam out with it."
>
> — [16:03](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=963s) &middot; *names the central real-time compute constraint that shapes the singing feature*

> "Go and build awesome things because nowadays with AI, we could build so many really cool things, and time is typically not the the big time suck that that it once was, right?"
>
> — [17:41](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=1061s) &middot; *the closing argument, and the reason the project is presented as a template rather than a product*

## Positions

- Software emulation of effects has advanced far enough that guitarists may no longer need physical effects pedals. ([3:34](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=214s), confidence: stated)
- Energy-gap segmentation alone cannot reliably split speech audio into words, because real speech often contains no silence between words. ([8:03](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=483s), confidence: stated)
- Combining sonority-peak syllabification with energy-gap detection still does not produce good enough automatic word slicing; manual segment editing is required. ([9:21](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=561s), confidence: stated)
- For a conversational guitar loop, the specific LLM is irrelevant — any local model suffices. ([14:16](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=856s), confidence: stated)
- Sample-based singing synthesis using World pitch shifting is too computationally heavy to run live and must be pre-baked ahead of performance. ([16:03](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=963s), confidence: stated)
- The current system speaks but does not yet sing convincingly — it is closer to singing but 'not quite your opera singer.' ([16:48](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=1008s), confidence: stated)
- AI has removed time as the main barrier to side projects, so engineers should start building the projects on their backlog now. ([17:41](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=1061s), confidence: stated)
- JUCE is the framework to use for building audio software. ([6:02](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=362s), confidence: stated)
- The talk box is the right conceptual model for AI-driven guitar speech: a synthesized pitched note carries the voice content through a vocoder rather than the voice being generated directly at pitch. ([10:59](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=659s), confidence: implied)

## Concepts

- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [latency budgets](../concepts/latency-budgets.md)
- [local inference](../concepts/local-inference.md)
- [voice agents](../concepts/voice-agents.md)

