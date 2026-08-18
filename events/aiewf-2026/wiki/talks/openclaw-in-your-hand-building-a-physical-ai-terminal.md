---
title: "OpenClaw in Your Hand: Building a Physical AI Terminal"
type: "talk"
slug: "openclaw-in-your-hand-building-a-physical-ai-terminal"
track: "Autoresearch"
org: "Callstack"
day: "Day 3 — Session Day 2"
room: "Main Stage"
video_id: "akk6KRlcwW4"
duration_sec: 1475
word_count: 2391
speakers: ["George Cameron", "Micah Hill-Smith"]
---

# OpenClaw in Your Hand: Building a Physical AI Terminal

*Program title: Trends in AI*

**Speakers:** [George Cameron](../speakers/george-cameron.md), [Micah Hill-Smith](../speakers/micah-hill-smith.md)

**Org:** Callstack

**Track:** Autoresearch &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 24m 35s

[Watch on YouTube](https://www.youtube.com/watch?v=akk6KRlcwW4)

## Summary

Lech Kalinowski, a physicist at Callstack, walks through a hardware side project: a handheld, AI-native text terminal built around an ESP32 microcontroller, a small OLED 'live surface' display, and a bistable e-paper display, used as a remote control for an OpenClaw agent running on a local DGX Spark. The talk is mostly a build log — dual-display rendering with pre-allocated one-bit image buffers and no malloc on the MCU, a custom power supply after blowing up two displays, I2C pull-up and GPIO failures, and a TensorRT-served open-source 120B model behind an OpenAI-style proxy. Its most interesting turn is the RPG mode: four generated text-adventure worlds where the LLM produces characters, maps, and mood, which he argues is a natural fit for a quiet, distraction-free, text-only device. He frames the whole thing as a bet on a market niche — AI-native operating systems on cheap microcontrollers rather than audio/video-first devices — and has filed a provisional patent. Watch it if you want a concrete, hands-on account of putting an agent behind physical hardware; skip it if you want model or agent-architecture depth.

## Key Points

- The device pairs a fast one-color OLED display for live typing with a slower bistable e-paper display for the committed render, giving both responsiveness and energy efficiency in one terminal.
- The firmware avoids a markdown engine and dynamic allocation entirely: pages are fixed static buffers of one-bit images living in pre-allocated MCU memory.
- The system is organized into four modes — an internal shell for device settings and Wi-Fi, an agent control mode for OpenClaw, and an RPG mode among them — across roughly 16 classes.
- Heavy compute is offloaded to a backend: an open-source 120-billion-parameter GPT model served with TensorRT behind an OpenAI-style LLM proxy, because not all open-source models match the OpenAI API shape.
- Hardware lessons dominated the build: software I2C without physical pull-ups, a silent GPIO 13 failure requiring a port move, a regulator that destroyed displays and cost weeks waiting on replacement parts, and a cheap encoder needing added pull-ups and capacitors.
- The design is deliberately fault-tolerant with redundant I/O paths: if the OLED fails the e-paper works, if the keyboard fails the encoder works, and if Wi-Fi drops the local shell still works.
- The RPG mode generates four worlds with NPCs, memory, maps, skills, and mood entirely from the LLM, which the speaker presents as a demonstration of generative AI building games without any 3D graphics.
- The speaker identifies a market gap — everyone is building audio- and video-interface AI devices, while nobody serves quiet, text-only, distraction-free reading and writing — and filed a provisional patent on it.
- The project totals about three months of work and 130 commits, running on a single lithium polymer cell, with the ironic result that a purely textual game consumes one of the most powerful GPUs available.

## Notable Quotes

> "I just wanted to build a device which is physical and AI native like the device which comes from the future."
>
> — [0:53](https://www.youtube.com/watch?v=akk6KRlcwW4&t=53s) &middot; *states the design goal that motivates the entire build*

> "the whole story begins because I just simply wanted to build a remote controller to my open claw instance on my DJX park"
>
> — [2:12](https://www.youtube.com/watch?v=akk6KRlcwW4&t=132s) &middot; *names the concrete origin use case behind the hardware*

> "And then with this simple, let's say, dual display approach, I realized I can build quite a powerful and energy-efficient terminal to play with my claw."
>
> — [3:25](https://www.youtube.com/watch?v=akk6KRlcwW4&t=205s) &middot; *the core hardware insight: two displays instead of one*

> "but from other side there is such a niche on the market and this is the AI-native operational systems"
>
> — [3:25](https://www.youtube.com/watch?v=akk6KRlcwW4&t=205s) &middot; *articulates the market thesis, not just the hobby project*

> "But not with a super powerful powerful computers, but with a small microcontrollers."
>
> — [4:39](https://www.youtube.com/watch?v=akk6KRlcwW4&t=279s) &middot; *the platform bet — AI-native OS on MCUs, a contestable position*

> "the pages live in a pre-allocated memory. There's a no markdown engine and no malloc on the MCU side."
>
> — [6:44](https://www.youtube.com/watch?v=akk6KRlcwW4&t=404s) &middot; *the single most specific engineering constraint stated in the talk*

> "there is a huge need to build a to build a power management system because I just blow up two these place over my prototype build"
>
> — [6:44](https://www.youtube.com/watch?v=akk6KRlcwW4&t=404s) &middot; *concrete failure that justified a whole subsystem*

> "here inside you have an MCU, which is ESP32 dual-core microcontroller. Here you have an OLED display, keyboard, and an encoder."
>
> — [7:54](https://www.youtube.com/watch?v=akk6KRlcwW4&t=474s) &middot; *the full bill of materials in one line*

> "I just want to demonstrate you um the device connected to an open-source GPT 120 billion parameters model."
>
> — [8:55](https://www.youtube.com/watch?v=akk6KRlcwW4&t=535s) &middot; *names the specific model class powering the demo*

> "I just exposed OpenAI style to uh also like LLM proxy because I just hit a lot of walls with uh other open source models um because that's not all models match the style of the Open AI API."
>
> — [8:55](https://www.youtube.com/watch?v=akk6KRlcwW4&t=535s) &middot; *reports a real interoperability pain point in open-source model serving*

> "I was I was possible to hit a command like write a Java example uh and store it on my local machine and Open Claw with the with the LLM support just did work and make it happened."
>
> — [10:02](https://www.youtube.com/watch?v=akk6KRlcwW4&t=602s) &middot; *the actual agentic capability demonstrated through the device*

> "encoder cheap and low quality give me a lot of rotational noise and there was a need to build up the the pull-ups and to and to wire it up additional capacitors there"
>
> — [11:06](https://www.youtube.com/watch?v=akk6KRlcwW4&t=666s) &middot; *names a specific component-quality tradeoff and its cost*

> "the device is really bulletproof. Um if the LED doesn't work, you the e-paper works. If the cardboard doesn't work, that means the keyboard, uh then you'll you have an encoder."
>
> — [14:03](https://www.youtube.com/watch?v=akk6KRlcwW4&t=843s) &middot; *spells out the redundancy design principle*

> "everyone just wants to build the devices around the audio interfaces, the video capture, you know, but for the quiet places"
>
> — [15:01](https://www.youtube.com/watch?v=akk6KRlcwW4&t=901s) &middot; *positions the product against the prevailing AI-device design trend*

> "In my project I just pushed 130 comments around 3 months of work. Two deep displays. Each of the display do other job. Four modes."
>
> — [16:09](https://www.youtube.com/watch?v=akk6KRlcwW4&t=969s) &middot; *the project's headline numbers*

> "Keep the model of the metal because it's really heavy. That means for now we don't have such a models which runs really on the super tiny MCUs."
>
> — [17:21](https://www.youtube.com/watch?v=akk6KRlcwW4&t=1041s) &middot; *a clear takeaway on the limits of on-device inference today*

> "And try narrative narrative. The context matters and in general not numbers."
>
> — [17:21](https://www.youtube.com/watch?v=akk6KRlcwW4&t=1041s) &middot; *compact statement of his prompting/design philosophy for the RPG mode*

> "the quiet game with the you know, text interface requires the the most powerful computer computer graphics card in the in the world"
>
> — [21:24](https://www.youtube.com/watch?v=akk6KRlcwW4&t=1284s) &middot; *the talk's central irony, stated by the speaker himself*

> "the presentation was about the handle device to control uh agent and open close with the local LLMs, but in general, it was about the Game Boy."
>
> — [23:49](https://www.youtube.com/watch?v=akk6KRlcwW4&t=1429s) &middot; *the closing reframe of what he actually built*

## Positions

- E-paper alone is too slow for dynamically updating LLM text, so a fast OLED must be paired with it for the live typing surface. ([2:12](https://www.youtube.com/watch?v=akk6KRlcwW4&t=132s), confidence: stated)
- There is an unserved market niche for AI-native operating systems running on small microcontrollers rather than powerful computers. ([4:39](https://www.youtube.com/watch?v=akk6KRlcwW4&t=279s), confidence: stated)
- A reliable embedded AI terminal should use pre-allocated fixed buffers with no markdown engine and no malloc on the MCU side. ([6:44](https://www.youtube.com/watch?v=akk6KRlcwW4&t=404s), confidence: stated)
- Not all open-source models conform to the OpenAI API style, which forced the use of an OpenAI-style LLM proxy layer. ([8:55](https://www.youtube.com/watch?v=akk6KRlcwW4&t=535s), confidence: stated)
- Current LLMs cannot run on very small MCUs, so the model must be kept off the device and served from a backend. ([17:21](https://www.youtube.com/watch?v=akk6KRlcwW4&t=1041s), confidence: stated)
- For LLM-driven experiences, narrative context matters more than numbers or stats. ([17:21](https://www.youtube.com/watch?v=akk6KRlcwW4&t=1041s), confidence: stated)
- The AI device market is over-focused on audio and video interfaces and neglects quiet, distraction-free text-only interaction. ([15:01](https://www.youtube.com/watch?v=akk6KRlcwW4&t=901s), confidence: stated)
- Text-based RPGs are an especially good fit for a low-power, text-only handheld device driven by an LLM. ([13:08](https://www.youtube.com/watch?v=akk6KRlcwW4&t=788s), confidence: stated)
- Redundant input and output paths (OLED/e-paper, keyboard/encoder, Wi-Fi/local shell) are what make the device dependable. ([14:03](https://www.youtube.com/watch?v=akk6KRlcwW4&t=843s), confidence: implied)
- Cheap components are a false economy in this kind of build — a low-quality encoder cost extra pull-ups and capacitors, and a bad regulator cost weeks in replacement parts. ([11:06](https://www.youtube.com/watch?v=akk6KRlcwW4&t=666s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [local inference](../concepts/local-inference.md)
- [model routing](../concepts/model-routing.md)
- [world models](../concepts/world-models.md)

