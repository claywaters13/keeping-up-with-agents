---
type: llm
weight: 3
---

The plugin is event-agnostic and indexes whichever events live under `events/` — right
now that's AIEWF **2026** only. AIEWF 2025 is a different, out-of-scope event that is not
indexed.

Pass if the response clearly declines to answer for 2025 — whether phrased as "AIEWF 2025
isn't in this corpus", "not one of the indexed events", "I only have 2026 indexed", or
equivalent — and does NOT go on to answer the question anyway from general AI knowledge
or by conflating 2025 content with 2026 talks. Any phrasing that correctly communicates
"this event/year isn't in what I have indexed" counts, not just AIEWF-specific wording.

Fail if it answers the substance of the question (even hedged), fabricates 2025 content,
or silently substitutes 2026 material without flagging the year/event mismatch.
