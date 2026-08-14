---
type: llm
weight: 2
focus: last_message
---
You have NO tools; judge only by comparing against the reference below.

The response synthesizes what AIEWF 2026 says about agent memory. Reference section
headings from the corpus's agent-memory page include:
- Durable agent state must live outside the model's context window and outside the process running the harness — in an app
- Simple, highly programmable stores — plain markdown in a central Git repo, a structured event log, a reference index — a
- Writing memory in-band during a session is insufficient on its own; a scheduled out-of-band consolidation pass over tran
- Model capability is no longer the binding constraint on agent usefulness; the constraint is durable, environment-specifi
- Memory should be scoped to the organization and shared across agents and developers, not siloed per-agent or per-user, b
- Storing user preferences, profiles, and conversation history is the wrong abstraction for production agent memory; what 
- Should long conversations be carried forward by compacting or summarizing history, or by keeping an immutable log and re
- Do plain files loaded into context scale as agent memory, or does memory require an engineered retrieval structure (grap

Pass if the response's substance clearly derives from these corpus themes (at least two
of the reference themes recognizably present) AND it cites at least one talk by title.
Fail if the response reads as generic AI knowledge unmoored from these themes, or cites
no talks. General knowledge phrasing alone is not failure if the reference themes are
clearly present.
