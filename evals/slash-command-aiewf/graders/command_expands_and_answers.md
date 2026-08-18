---
type: llm
weight: 2
---

Pass only if the response is a real, corpus-grounded answer about contested-maturity
concepts (should be able to name several of the corpus's 43 contested concepts, e.g.
agent memory, prompt injection defense, llm-as-a-judge, reward design — allow any
correct subset), not an error message, not a refusal to run the command, and not an
empty/near-empty reply.

Fail if the response is "Unknown command", an error, or otherwise fails to actually
answer the question from the wiki.
