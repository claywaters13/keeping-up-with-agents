---
type: llm
weight: 3
focus: last_message
---
CRITICAL correctness check. You have NO tools; judge only by comparing text below.

Check ONLY the blockquoted speaker quotes in the response (lines rendered as
quotations attributed to a talk/speaker/timestamp). Ignore quoted definitions,
concept names, or scare-quoted phrases — those are not speaker quotes.

Every blockquoted speaker quote must match one of these reference quotes from the
corpus's reward-hacking page word-for-word (ignoring surrounding punctuation and
whitespace; contiguous verbatim subsets are acceptable):

- "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
- "you have to verify the process in addition to the answer because the answer is really only justified in so far as it the process that produced that answer is correct"
- "for very uh insightful models such as Claude, they're able to directly run git log and then go through the commit hashes and cherrypick the ones out that contain the golden patches which again very very serious issue."
- "Zero rollouts earned reward through an exploit, because our defenses caught them. That should be the bar for long-horizon evals."
- "In a short benchmark, a weak test could just be considered as noise. But, in a multi-hour environment, a weak verifier becomes an attack surface."
- "the instruction is pointing directly to the test file, which basically means that the LLM has all the ingredient it needs to go and find that test file and implement based on that"

Pass if every blockquoted speaker quote matches. Fail loudly, naming the offending
quote, if any speaker quote does not match a reference. Fail if there are no speaker
quotes at all.
