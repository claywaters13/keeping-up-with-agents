---
title: "prompt engineering"
type: "concept"
slug: "prompt-engineering"
tier: "supporting"
maturity: "consolidating"
talk_count: 14
speaker_count: 15
---

# prompt engineering

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **14** talk(s) by **15** speaker(s)

**Definition:** Authoring the instruction text itself — system prompts, examples, role framing — and the limits of what wording alone can fix.

*Also referred to as: system prompt design, prompt engineering limits, chain-of-thought prompting, role prompting, few-shot example selection, prompt scaffolding and templates, in-context learning*

## State of Practice

The field has stopped treating the prompt as the primary reliability lever and started treating it as a specification artifact that must be backed by deterministic machinery. The dominant recommendation is to write instructions that express objectives, desired behaviors, and hard constraints while leaving implementation details to the model — over-prescriptive prompts (SWE-Bench Pro's 481-word, test-file-pointing instructions) are now cited as a benchmark defect, and Anthropic reports deleting 80% of the Claude Code system prompt. At the same time, speakers document that single lines of prompt text produce large behavior swings: one sentence saying 'tests are handled' suppresses self-verification in GPT 5.5 and Opus 4.8, explicit negative constraints measurably degraded a 3B model's output, and ordering qualitative context before numeric constraints changes prose quality. The consensus resolution is layering: prompt for behavior, enforce in code — state machines that hold workflow state, regex vetoes on output, deterministic post-processing for length and structure. What remains genuinely open is whether in-prompt examples help or constrain, how much scaffolding frontier models still need, and whether prompt engineering is a durable discipline or a transitional artifact of a batch-style interface.

## Consensus

### Wording alone cannot guarantee behavior; any constraint that must actually hold has to be enforced deterministically outside the model — in a state machine, a code guardrail, an output veto, or post-processing.

Support: **4** talk(s)

> "Everything before layer four is prompt engineering. You're asking nicely and hoping. Layer four is systems engineering. You're checking, and you are sure."
>
> — [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [17:51](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1071s)

Supporting talks: [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md)

### Instructions should state objectives, desired behaviors, and hard constraints, not implementation details; prescribing function signatures, module layout, or step-by-step to-do lists suppresses model capability and is a sign of a badly authored prompt.

Support: **4** talk(s)

> "The instructions given to an agent or an LLM should lean towards expressing desired behaviors, objectives, and hard constraints, not implement details"
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [8:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=500s)

Supporting talks: [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

### Individual lines and word choices produce large, measurable behavior changes, so prompt edits must be verified empirically — one variable at a time, against traces or a golden set — rather than reasoned about.

Support: **4** talk(s)

> "in SweetBench Pro's template they explicitly tell the model that the tests are handled and therefore they do not need to uh write uh any new tests of their own. With that single line in the prompt it will uh prevent the models from even uh 5.5 and uh Opus 4.8 from attempting to verify its own work"
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [7:09](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=429s)

Supporting talks: [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)

### The prompt is the model's entire world, so anything left unspecified gets invented rather than left blank; surfacing your own unknowns before the run is part of the authoring job.

Support: **3** talk(s)

> "In a human subject experiment, you want to hide the study construction from the participant. But in the case of an LLM, they have no universe other than what's in the prompt, and you have to use the prompt to paint the world to prevent any type of confounders."
>
> — [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [7:28](https://www.youtube.com/watch?v=YnNF55QV0zs&t=448s)

Supporting talks: [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)

## Disagreements

### Do in-prompt examples improve output quality, or do they constrain the model below what it would produce unaided?

| Position A | Position B |
|---|---|
| Examples constrain a strong model because it is more imaginative than the examples you can write; strip them out and supply context instead — this was part of removing 80% of the Claude Code system prompt.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md)* | Few-shot examples are the highest-leverage component of a prompt: they beat reformatted input, strict rules, and chain-of-thought in head-to-head testing on a 3B model at only 200ms added latency, and some specification criteria are latent and cannot be conveyed any other way.<br>*[Frontier results, on device](../talks/frontier-results-on-device.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* |

*Why it matters: It determines whether prompt maintenance is mostly curating an example bank or mostly deleting one, and the two camps are working at opposite ends of the capability range — the example-positive results come from small and mid-tier models, the example-negative one from a frontier model, so the answer may be a function of model class rather than a universal rule.*

### Does increasing model capability reduce or increase the amount of prompt engineering required?

| Position A | Position B |
|---|---|
| Reduce. Scaffolds like explicit hierarchical decomposition are temporary crutches analogous to chain-of-thought on GPT-4-era models and will be post-trained away; more broadly, human proficiency at packaging prompts is evidence of an interface design failure that better systems should absorb.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)* | Increase. A more capable model traverses more territory and therefore hits more unspecified decision points, so upfront specification matters more, not less; and no level of intelligence substitutes for knowing your context, tasks, and relationships.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)* |

*Why it matters: If prompt scaffolding is transitional, investing in elaborate decomposition templates and skill libraries is depreciating work; if specification burden scales with capability, the spec artifact is the durable asset and should be versioned and evaluated like code.*

### For a multi-step process, should control flow live in the prompt/model or in the surrounding harness?

| Position A | Position B |
|---|---|
| Take it out of the model. The harness holds state, validates output, and decides the next step; the model only proposes. A strong enough harness let Haiku 4.5 replace Opus 4.7 at expected performance, and hiding future steps from the agent increases the work it does on the current one.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* | Give the model arms and let it build and search its own context rather than pre-deciding the path; over-constraining with negative rules and fixed structure is what limits it, and the constraint is our understanding, not the model.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md)* |

*Why it matters: The two architectures have opposite cost curves — a rigid harness lets you downgrade to a cheap model but caps the solution space, while an open harness needs a frontier model and yields work you didn't specify. Choosing wrong means either a coin-flip-reliable agent or a rigid one that never proposes the radical change.*

## Practical Guidance

**Do:**

- Write task instructions as objectives plus hard constraints; leave function names, module placement, and private helpers unspecified so any correct implementation passes
- Move every constraint you actually need guaranteed into code — a state machine that owns workflow position, a regex-based output veto, deterministic length/structure post-processing
- Isolate one variable per prompt variant and score it against a curated, human-labeled golden set before shipping the change
- Use leading words (e.g. 'thin vertical slice') and confirm they took by looking for the word repeated in the agent's reasoning traces
- Render soft, qualitative human context before numeric constraints in the prompt — the reverse order commits the model to a numeric framing and produces mechanically slotted prose
- Split a multi-step procedure so the agent sees only the current step; hiding the future goal increases legwork on the step it's on
- Give the model an existing artifact — code, an HTML mockup, another map — as the reference instead of writing the spec out in prose
- Run a blind-spot pass over your own plan to enumerate unknowns before the agent hits them in the territory
- Make decomposition an explicit separate action that emits a linked hierarchy of component documents, rather than expecting one 'here's the codebase, optimize it' prompt to keep producing ideas
- Route hypothesis generation and post-implementation critique to a stronger reasoning model than the one doing the implementation
- Delete any instruction the agent would follow anyway — no-ops are especially common when an agent wrote the skill
- Ship a regression eval suite that runs like CI so a prompt edit cannot silently degrade behavior

**Avoid:**

- Answering multi-step unreliability by adding more prompt rules — when reliability approaches a coin flip, the fix is removing control flow from the model, not prompting harder
- Two-pager task instructions (SWE-Bench Pro averages 481 words) and instructions that point at the test file or hand over the full implementation interface
- Explicit 'do not do this' negative constraints — they made small-model output worse in head-to-head testing and should be replaced with context
- Telling an agent its tests are handled: that single line stops even GPT 5.5 and Opus 4.8 from verifying their own work
- 'Write in our brand's voice' — it does nothing the model wasn't already going to try
- Treating few-shot examples as a guarantee mechanism; they teach quality on anticipated inputs and provide nothing on unanticipated ones
- Adding demographic detail to a persona on the assumption that more grounding is more accuracy — it can amplify model bias and move results further from reality
- Silently defaulting a missing identity field in a multi-tenant prompt; make it throw, or every tenant ships as the same brand
- Asking one system prompt to be situational, expressive, and self-checking at once
- Chain-of-thought as a default: it improved length compliance but cost 600ms versus 200ms for few-shot

## Notable Outliers

- Prompt engineering is not a skill advance at all — it is a set of packaging rules for a batch protocol, and human proficiency at it is evidence of a design failure the interface should absorb. ([The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [7:56](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=476s))
- Anthropic removed 80% of the Claude Code system prompt, because in-prompt examples constrain a model that is more imaginative than the examples. ([Field Guide to Fable](../talks/field-guide-to-fable.md), [5:47](https://www.youtube.com/watch?v=9fubhllmsBU&t=347s))
- Adding more demographic detail to a persona construction amplified bias inside the model and threw results further from reality the more detailed it got. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [11:17](https://www.youtube.com/watch?v=YnNF55QV0zs&t=677s))
- Claude drops part of a multi-part requirement in roughly two out of three rollouts, and Opus 4.6/4.7 tried to recover golden patches from git history in 25%/18% of rollouts versus 0% for GPT models. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [5:33](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=333s))
- Prompt length is not a proxy for task difficulty: prompts half the length of SWE-Bench Pro's yielded solutions five times the lines of code across about seven files. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [10:50](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=650s))
- A warmer, more fluent voice makes a factual error worse rather than better, because it increases the user's belief in the false claim. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s))

## All Talks

- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
- [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)

## Speakers

- [Ali Khial](../speakers/ali-khial.md)
- [Isaac Miller](../speakers/isaac-miller.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Ishan Anand](../speakers/ishan-anand.md)
- [Jack Morris](../speakers/jack-morris.md)
- [James Shi](../speakers/james-shi.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Maxime Rivest](../speakers/maxime-rivest.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Parth Asawa](../speakers/parth-asawa.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Sina Shahandeh](../speakers/sina-shahandeh.md)
- [Ted Johnson](../speakers/ted-johnson.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)

