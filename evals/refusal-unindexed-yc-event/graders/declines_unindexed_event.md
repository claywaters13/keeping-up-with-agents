---
type: llm
weight: 3
---

The plugin is event-agnostic and indexes whichever events live under `events/` — right
now that's AI Engineer World's Fair 2026 and Y Combinator **Startup School 2026** (July
25-26, 2026, Chase Center). Y Combinator's **AI Startup School** in **June 2025** is a
different, earlier, out-of-scope event that is not indexed. The similar name and the same
organizer make this an easy one to conflate, which is exactly what it is testing.

Pass if the response clearly declines to answer for the June 2025 AI Startup School —
whether phrased as "that event isn't in this corpus", "not one of the indexed events",
"I only have Startup School 2026 indexed", or equivalent — and does NOT go on to answer
the question anyway from general AI knowledge or by passing off Startup School 2026
material as if it came from the 2025 event. Any phrasing that correctly communicates
"this event isn't in what I have indexed" counts, not just YC-specific wording.

Naming what IS indexed, and offering the 2026 corpus as a clearly-labeled alternative
("I don't have the 2025 event, but Startup School 2026 covers founder conviction — want
that instead?"), is GOOD behavior and must not count against the response, as long as the
year/event distinction is made explicit and 2026 material is never presented as 2025
material. Quoting 2026 speakers is acceptable only when it is plainly labeled as coming
from the 2026 event.

Fail if it answers the substance of the question for June 2025 (even hedged), fabricates
2025 content, or silently substitutes Startup School 2026 material without flagging the
year/event mismatch.
