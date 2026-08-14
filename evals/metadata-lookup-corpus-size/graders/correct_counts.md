---
type: llm
weight: 2
---

The corpus has 231 talks, 134 concepts, and 248 speakers (per wiki/README.md and
data/index.json).

Pass if the response states these three counts correctly (small variance, e.g. off by
one due to a since-added talk, is acceptable — but it must be close to these numbers and
clearly sourced from the corpus, not a round-number guess).

Fail if any count is substantially wrong or the response admits it doesn't know / can't
find this instead of reading the actual data.
