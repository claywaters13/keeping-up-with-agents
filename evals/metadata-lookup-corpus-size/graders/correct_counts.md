---
type: llm
weight: 2
---

The corpus has 256 talks, 134 concepts, and 276 speakers (per wiki/README.md and
data/index.json).

You have no tools. Judge ONLY the three counts as stated in the response text. Do not
attempt to assess whether the numbers were "sourced from the corpus" versus guessed —
that is not observable from the text, and treating it as a requirement produces false
failures.

Pass if the response states all three counts correctly (off by one, e.g. from a
since-added talk, is acceptable).

Additional detail — maturity breakdowns, word counts, quote counts, notes about
livestream compilations or multi-speaker talks — is welcome and must NOT count against
the response. Ignore it unless it directly contradicts one of the three counts above.

Fail only if one of the three counts is substantially wrong, or the response says it
doesn't know / can't find them.
