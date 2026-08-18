---
title: "Computer-use models will agentify the web, not APIs"
type: "talk"
slug: "computer-use-models-will-agentify-the-web-not-apis"
track: "Computer Use"
org: "Yutori"
day: "Day 3 — Session Day 2"
room: "Track 7"
video_id: "Ki980nV0__0"
duration_sec: 1259
word_count: 3485
speakers: ["Dhruv Batra"]
---

# Computer-use models will agentify the web, not APIs

**Speakers:** [Dhruv Batra](../speakers/dhruv-batra.md)

**Org:** Yutori

**Track:** Computer Use &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 20m 59s

[Watch on YouTube](https://www.youtube.com/watch?v=Ki980nV0__0)

## Summary

Dhruv Batra of Yutori attacks the widely-repeated claim that the web will be 'agentified' via APIs, MCP servers, and payment protocols. His argument: the head of the distribution may expose APIs, but the long tail — restaurants whose menus are JPEGs of PDFs in a gallery, school districts that answer procurement questions via FOIA requests scanned onto Google Drive — never will, and reading raw HTML fails too because modern pages compute their content via async JSON fetches and render logic rather than storing it as text. Since the web was built for human eyes, pixels are the source of truth, and machines therefore need vision; this is the 'bitter lesson' for web agents, where scaffolding per-site breaks on the long tail and the general screenshot-in/actions-out solution wins. He backs this with numbers from Yutori's Navigator models: N 1.5 hits 97% human eval on Mind2Web (saturating it), and matches Opus 4.7 and GPT-5.5 on accuracy while costing ~80 cents per task versus ~$230 with lower per-step latency. Worth watching if you're deciding between building API/MCP integrations and betting on computer-use agents, or want a concrete cost/latency picture of vision-based browsing.

## Key Points

- The common agentification thesis has three steps — agents will drive web actions, the web must be agentified, and this will happen via APIs — and Batra accepts the first two while rejecting the third.
- The long tail of the web (roughly 200 million active sites, close to a billion total) will never ship APIs, because the institutions behind it change on decade timescales and some still communicate by fax and FOIA request.
- Real-world examples show the difficulty gradient: restaurant menus range from scrapable text to PDFs to pixelated JPEG galleries, and school-district procurement info can require filing a Freedom of Information Act request answered with scanned PDFs on Google Drive.
- Throwing coding agents at raw HTML also fails, because content like a live NBA score arrives via an asynchronous JSON fetch after page load, and stock status is computed by a rendering script that grays out zero-quantity options without ever writing 'sold out' as text.
- The browser is a rendering engine, so extracting meaning from source is an inversion problem; the information users see is calculated, not stored, which makes pixels the actual source of truth.
- This is a bitter-lesson dynamic: per-site scaffolds don't generalize to the long tail, while the most general solution — screenshots in, clicks and scrolls out — does.
- Vision-first does not mean vision-only: Yutori's newer Navigator writes and executes JavaScript on demand (e.g., filling multiple form fields at once) while still verifying results through pixels.
- Progress claims are backed by benchmarks: Navigator N 1.5 scores 97% human eval on Mind2Web with only 8 of 300 trajectories incorrect over 30-50 step interactions, which Batra says means the benchmark should be retired.
- On cost and speed, the smaller-footprint model is roughly at parity with frontier models on accuracy but delivers about 80 cents per task versus $230 and lower latency per step, since it isn't a trillion-plus parameter model.
- Batra's endgame is that computer use becomes indistinguishable from an API — sub-penny, sub-100ms, structured output — meaning the web gets agentified by piling another layer of mess on top of the existing mess.

## Notable Quotes

> "My claim today and argument and what I hope to convince you today is that this last bit is wrong. I think the first two I generally agree with. This last bit that suddenly the web will provide you APIs for accessing things is is just delusional."
>
> — [1:03](https://www.youtube.com/watch?v=Ki980nV0__0&t=63s) &middot; *States the talk's central thesis and exactly which part of the consensus he rejects.*

> "my claim is computer use agents and computer use models will identify the web not APIs and more specifically the long tail of the web."
>
> — [1:03](https://www.youtube.com/watch?v=Ki980nV0__0&t=63s) &middot; *The title claim in the speaker's own words, with the long-tail qualifier that carries the argument.*

> "the head of the distribution the most popular website perhaps will give you the API but the long tail will not."
>
> — [1:42](https://www.youtube.com/watch?v=Ki980nV0__0&t=102s) &middot; *Concedes the head of the distribution, which is what makes the position falsifiable rather than absolute.*

> "I want to rid you of the delusion that such an endpoint exists."
>
> — [3:08](https://www.youtube.com/watch?v=Ki980nV0__0&t=188s) &middot; *Compact statement of the rhetorical move driving the whole first half.*

> "I am looking at JPEGs embedded in a gallery which contain the PDF items. You download this and you put it into chat GPT and it's having it's struggling doing OCR on this thing."
>
> — [4:36](https://www.youtube.com/watch?v=Ki980nV0__0&t=276s) &middot; *Concrete worst-case of long-tail web structure that no API story addresses.*

> "in order to find information, you have to file a request for access of in information under Freedom of Information Act."
>
> — [6:08](https://www.youtube.com/watch?v=Ki980nV0__0&t=368s) &middot; *The strongest single counterexample to the idea that institutions will expose machine endpoints.*

> "These are the people you're telling me will give you an MCP server. The the amount of delusion here is off the chart."
>
> — [7:04](https://www.youtube.com/watch?v=Ki980nV0__0&t=424s) &middot; *Names MCP directly as the target of the critique.*

> "the active websites are somewhere 200 million."
>
> — [7:04](https://www.youtube.com/watch?v=Ki980nV0__0&t=424s) &middot; *The scale number underpinning the long-tail argument.*

> "there are still places that are faxing each other you're you're not going to be able to suddenly change this overnight."
>
> — [7:56](https://www.youtube.com/watch?v=Ki980nV0__0&t=476s) &middot; *Institutional-inertia argument, distinct from the technical one.*

> "If you just read the HTML when you load it, the answer is not in the HTML and so your your chatbot doesn't have access to that either."
>
> — [9:14](https://www.youtube.com/watch?v=Ki980nV0__0&t=554s) &middot; *Kills the 'just scrape the HTML' fallback with a specific mechanism.*

> "this information that you are seeing on screen is not written somewhere as pure text. It is calculated. It is rendered."
>
> — [11:09](https://www.youtube.com/watch?v=Ki980nV0__0&t=669s) &middot; *The core technical insight the vision argument rests on.*

> "Fundamentally the web was built for human eyes. Pixels are the source of the truth because the consumers of the websites are humans."
>
> — [11:52](https://www.youtube.com/watch?v=Ki980nV0__0&t=712s) &middot; *The talk's thesis sentence for why vision is required.*

> "in a way this is the bitter lesson uh for web agents that the more you end up writing scaffolds around existing websites the it doesn't actually generalize to the long tail of the web."
>
> — [11:52](https://www.youtube.com/watch?v=Ki980nV0__0&t=712s) &middot; *Frames the design choice in a widely understood ML idiom.*

> "my claim is the web was built for human eyes. Machines will need vision. But of course they do not need to be limited to human ways."
>
> — [13:57](https://www.youtube.com/watch?v=Ki980nV0__0&t=837s) &middot; *Important qualification that prevents the position from collapsing into pixels-only purism.*

> "click buttons when you have to, write code when you have to and look at the result uh through pixels because that is the that is the source of of truth."
>
> — [15:09](https://www.youtube.com/watch?v=Ki980nV0__0&t=909s) &middot; *The actionable architectural recommendation, including pixel-based verification.*

> "the model that we just released navigator N 1.5 is sitting at 97% human eval eight trajectories out of 300 are incorrect at this point of time you should just retire the benchmark build something harder."
>
> — [16:31](https://www.youtube.com/watch?v=Ki980nV0__0&t=991s) &middot; *Reports the headline number and calls the benchmark saturated.*

> "if you have something like on these data sets something like 20 30 steps of interaction, you're looking at 80 cents per task versus $230. And that makes a big difference."
>
> — [18:07](https://www.youtube.com/watch?v=Ki980nV0__0&t=1087s) &middot; *The cost tradeoff that answers the 'computer use is too expensive' objection.*

> "this hypothesis that suddenly overnight 30 years of infrastructure that was built layer upon layer for human consumption will in what two five 10 years be reinvented is I think a fantasy."
>
> — [18:51](https://www.youtube.com/watch?v=Ki980nV0__0&t=1131s) &middot; *Puts a timescale on the disagreement with API-first advocates.*

> "We will just pile on another layer of mess on top of the mess that the web is"
>
> — [19:41](https://www.youtube.com/watch?v=Ki980nV0__0&t=1181s) &middot; *Honest framing of the aesthetic cost of his own prediction.*

> "It will cost less than a penny. It will run in your browser. Sometimes it will, you know, run in less than 100 milliseconds. And at some point you will say, "Yeah, that's an API. Like why do I care?""
>
> — [20:20](https://www.youtube.com/watch?v=Ki980nV0__0&t=1220s) &middot; *The closing synthesis: computer use converges on API-like ergonomics.*

## Positions

- The web will be agentified by computer-use models operating on pixels, not by websites exposing APIs. ([1:03](https://www.youtube.com/watch?v=Ki980nV0__0&t=63s), confidence: stated)
- Popular head-of-distribution websites may provide APIs, but the long tail will not. ([1:42](https://www.youtube.com/watch?v=Ki980nV0__0&t=102s), confidence: stated)
- For structured, aggregator-backed tasks like flight search, using a computer-use agent to click buttons is the wrong design — you should call the existing API. ([2:17](https://www.youtube.com/watch?v=Ki980nV0__0&t=137s), confidence: stated)
- There are roughly 200 million active websites and close to a billion total, and their infrastructure changes very slowly. ([7:04](https://www.youtube.com/watch?v=Ki980nV0__0&t=424s), confidence: stated)
- Coding agents pointed at raw HTML cannot reliably extract page content, because content is fetched asynchronously and computed by rendering logic rather than present as text. ([9:14](https://www.youtube.com/watch?v=Ki980nV0__0&t=554s), confidence: stated)
- Writing per-site scaffolds is a losing strategy because it fails to generalize to the long tail; the general screenshot-in solution wins. ([11:52](https://www.youtube.com/watch?v=Ki980nV0__0&t=712s), confidence: stated)
- Computer-use agents should not be restricted to human-like interaction; they should write and execute code when useful while verifying outcomes through pixels. ([13:57](https://www.youtube.com/watch?v=Ki980nV0__0&t=837s), confidence: stated)
- The perception that progress on computer use has been slow is wrong and is not supported by benchmark numbers. ([15:46](https://www.youtube.com/watch?v=Ki980nV0__0&t=946s), confidence: stated)
- Mind2Web is saturated at 97% human eval and should be retired in favor of a harder benchmark. ([16:31](https://www.youtube.com/watch?v=Ki980nV0__0&t=991s), confidence: stated)
- Yutori's accuracy edge over Opus 4.7 and GPT-5.5 is within statistical noise; the real advantage is latency per step and cost per task. ([17:28](https://www.youtube.com/watch?v=Ki980nV0__0&t=1048s), confidence: stated)
- Smaller-footprint computer-use models are substantially faster than trillion-plus parameter frontier models on browser tasks. ([17:28](https://www.youtube.com/watch?v=Ki980nV0__0&t=1048s), confidence: stated)
- The claim that computer-use agents are slow and expensive is largely true today but is being optimized away. ([17:28](https://www.youtube.com/watch?v=Ki980nV0__0&t=1048s), confidence: stated)
- AI agents becoming the primary drivers of action on the web is essentially uncontestable. ([18:07](https://www.youtube.com/watch?v=Ki980nV0__0&t=1087s), confidence: stated)
- Thirty years of human-oriented web infrastructure will not be reinvented for machines within 2-10 years. ([18:51](https://www.youtube.com/watch?v=Ki980nV0__0&t=1131s), confidence: stated)
- Once computer-use agents are sub-penny, sub-100ms, and return structured output, the distinction between them and an API stops mattering. ([20:20](https://www.youtube.com/watch?v=Ki980nV0__0&t=1220s), confidence: stated)
- Multi-agent orchestration of parallel browser sandboxes enables superhuman throughput no individual human could match. ([15:09](https://www.youtube.com/watch?v=Ki980nV0__0&t=909s), confidence: stated)

## Concepts

- [benchmark saturation](../concepts/benchmark-saturation.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [vision-language models](../concepts/vision-language-models.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)

