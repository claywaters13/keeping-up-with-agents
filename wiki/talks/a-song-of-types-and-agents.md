---
title: "A Song of Types and Agents"
type: "talk"
slug: "a-song-of-types-and-agents"
org: "Ratel"
video_id: "UlFB6efYN5Q"
duration_sec: 856
word_count: 1758
speakers: ["Roberto Stagi"]
---

# A Song of Types and Agents

**Speakers:** [Roberto Stagi](../speakers/roberto-stagi.md)

**Org:** Ratel

**Duration:** 14m 16s

[Watch on YouTube](https://www.youtube.com/watch?v=UlFB6efYN5Q)

## Summary

Roberto Stagi argues that TypeScript, not Python, is becoming the dominant language for building AI agents, framing the shift as a succession war for the AI throne. His core claim is that AI has moved up the stack from infrastructure to the application layer, and the application layer has belonged to TypeScript for years — a shift he backs with GitHub's language rankings flipping from Python (2024) to TypeScript (August 2025), both times attributed by GitHub to AI. He credits coding agents (Claude Code, Cursor, Codex) as the specific 2024-to-2025 change, since they default to emitting TypeScript, creating a feedback loop where future models get better at it. He concedes the inference layer — training, research, GPU serving — remains Python's indefinitely, and recommends a split: keep training in Python, ship agents and applications in TypeScript. Worth watching if you're choosing a stack for agent applications and want the ecosystem argument (NPM breadth, single-language codebases, Zod as one schema end to end) laid out concisely; skip it if you want benchmarks or code, since it's a 14-minute opinion talk with no implementation detail.

## Key Points

- AI has migrated from the infrastructure layer to the application layer, meaning AI stopped being something you train and became something you ship inside an application — and the application layer has long been TypeScript's territory.
- TypeScript overtook Python as the most-used language on GitHub in August 2025, and GitHub attributed the change to AI in both 2025 and 2024, when it had credited AI for Python's rise.
- The specific thing that changed between 2024 and 2025 was coding agents maturing: Claude Code, Cursor, and Codex became the default way to build applications, and their default output language is TypeScript.
- This creates a compounding feedback loop — more TypeScript applications feed the training of the next generation of coding agents, so their TypeScript output quality should keep improving relative to other languages.
- Building in TypeScript lets you keep one language and one codebase across the agent loop, tools, backend, and UI, whereas a Python agent typically forces a split into a FastAPI/Pydantic service plus a separate React app with a contract to maintain.
- Zod gives TypeScript a single schema definition reusable in the backend, the model layer, and the UI, eliminating the type-synchronization boundary Python stacks hit at the frontend.
- NPM is the richest package ecosystem available — authentication, payments, UI, infra — which matters more now that AI has to integrate with the whole application layer.
- The TypeScript AI ecosystem is growing fast: the Vercel AI SDK went from 1.6 million to 15.1 million weekly downloads in one year, roughly 9-10x.
- Stagi's recommendation is a division of labor rather than a replacement: models still run on pip, agents ship on NPM — keep training in Python, but build agents and applications in TypeScript or risk falling behind.

## Notable Quotes

> "a song that speaks about languages that fight each other to conquer what's the throne in the AI realm. And how I think that TypeScript might actually be winning this war."
>
> — [0:02](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=2s) &middot; *states the talk's thesis and framing device in one line*

> "AI stopped being something that you train, and it started being something that you ship inside your application."
>
> — [2:04](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=124s) &middot; *the conceptual pivot the entire argument rests on*

> "the application layer was not Python's. The application layer has been TypeScript's for pretty long time now"
>
> — [3:03](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=183s) &middot; *the central territorial claim, stated bluntly*

> "I still think that the brain of the of the agent and all the of all the AI world is actually still owned by Python. All the training, the research, the GPU serving is all Python's."
>
> — [3:03](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=183s) &middot; *explicit concession that bounds the argument and prevents strawmanning*

> "in August 2025, TypeScript TypeScript actually passed Python as the most used language on GitHub"
>
> — [4:04](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=244s) &middot; *the headline data point*

> "in 2024, it said AI leads Python to the top language. While in 2025, it said AI leads TypeScript as the first language."
>
> — [4:04](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=244s) &middot; *the ironic symmetry that is the talk's most memorable piece of evidence*

> "In 2020 2025, we even have one new developer joining GitHub every second."
>
> — [4:59](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=299s) &middot; *quantifies the developer influx behind the ranking shift*

> "What changed between 2024 and 2025 was actually coding agents."
>
> — [4:59](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=299s) &middot; *names the single causal mechanism the talk proposes*

> "since every new app pretty much every new app is an agent today because they ship these AI and agentic capabilities, they are hungry to embed AI inside themselves"
>
> — [6:01](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=361s) &middot; *a strong, contestable claim about what applications now are*

> "We even saw an AI lab acquiring a JavaScript runtime like last December Anthropic acquired Bun."
>
> — [6:01](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=361s) &middot; *concrete industry evidence of labs investing in the JS/TS layer*

> "since TypeScript is the default language for coding agents today, we can expect that they will become better and better in in TypeScript"
>
> — [7:21](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=441s) &middot; *articulates the compounding feedback loop, the strongest forward-looking argument*

> "if you use TypeScript, you are actually tapping into what is probably the richest package manager out there. NPM comes with everything"
>
> — [8:11](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=491s) &middot; *the ecosystem-breadth argument in its sharpest form*

> "While if you use Python, you probably have to split uh split it at least into two services."
>
> — [9:17](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=557s) &middot; *names the concrete architectural cost of the Python path*

> "if you use TypeScript, you can use Zod as a single schema throughout all your application"
>
> — [10:15](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=615s) &middot; *the specific tooling answer to the type-boundary problem*

> "take the Versatile AI SDK, for example, you can see that in just 1 year, it went from 1.6 million to 15.1 million downloads per week, which is between 9 and 10x in just 1 year."
>
> — [11:03](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=663s) &middot; *the talk's only ecosystem growth number, cited with precision*

> "Any application that can be written in JavaScript will eventually be written in JavaScript."
>
> — [11:54](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=714s) &middot; *Atwood's Law invoked as the historical precedent for the thesis*

> "any application that could be written in JavaScript will eventually be written in TypeScript"
>
> — [11:54](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=714s) &middot; *the updated corollary the speaker extends to agents*

> "the model can still run on pip. But the agents, which is the application layer today, so the agent that called the models will probably ship on NPM."
>
> — [12:48](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=768s) &middot; *the cleanest statement of the proposed division of labor*

> "keep training in Python. As I said, I don't see that's one going away soon. But please consider building the agents and the applications in TypeScript."
>
> — [12:48](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=768s) &middot; *the actionable recommendation the talk closes on*

> "if you don't do that now, if you overlook TypeScript, you are probably going to fall behind."
>
> — [13:45](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=825s) &middot; *the urgency claim, the most contestable line in the talk*

## Positions

- TypeScript is winning the competition to be the dominant language for building AI agents and AI-powered applications. ([0:02](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=2s), confidence: stated)
- Python retains permanent ownership of the inference layer — training, research, and GPU serving — and is not going away soon. ([3:03](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=183s), confidence: stated)
- TypeScript passed Python as the most-used language on GitHub in August 2025. ([4:04](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=244s), confidence: stated)
- The maturation of coding agents — Claude Code, Cursor, Codex — is the specific cause of TypeScript overtaking Python between 2024 and 2025. ([4:59](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=299s), confidence: stated)
- TypeScript is the default output language of today's coding agents. ([6:01](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=361s), confidence: stated)
- Essentially every new application today is an agent, because new apps ship AI and agentic capabilities. ([6:01](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=361s), confidence: stated)
- Coding-agent output quality in TypeScript will keep improving faster than in other languages, because more TypeScript applications will feed the next generation of training. ([7:21](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=441s), confidence: stated)
- NPM is the richest package manager available, covering authentication, payments, UI, and infrastructure. ([8:11](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=491s), confidence: stated)
- A Python-based agent stack forces splitting the application into at least two services with a contract that must be maintained and synchronized. ([9:17](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=557s), confidence: stated)
- Python stacks inevitably hit a typing boundary at the frontend, requiring a second set of types to keep in sync, which TypeScript plus Zod avoids. ([10:15](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=615s), confidence: stated)
- The Vercel AI SDK grew from 1.6 million to 15.1 million weekly downloads in one year, roughly 9-10x. ([11:03](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=663s), confidence: stated)
- The gap between TypeScript and Python at the application layer will widen over the next few years. ([12:48](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=768s), confidence: stated)
- Developers who overlook TypeScript for agent development now will fall behind. ([13:45](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=825s), confidence: stated)
- Anthropic's December acquisition of Bun signals that AI labs see the JavaScript/TypeScript runtime layer as strategically important. ([6:01](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=361s), confidence: implied)

## Concepts

- [agent-readable codebases](../concepts/agent-readable-codebases.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [build versus buy](../concepts/build-versus-buy.md)
- [data flywheels](../concepts/data-flywheels.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [structured output contracts](../concepts/structured-output-contracts.md)

