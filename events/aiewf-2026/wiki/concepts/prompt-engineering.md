---
title: "prompt engineering"
type: "concept"
slug: "prompt-engineering"
tier: "supporting"
maturity: "contested"
talk_count: 16
speaker_count: 17
---

# prompt engineering

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **16** talk(s) by **17** speaker(s)

**Definition:** Authoring the instruction text itself — system prompts, examples, role framing — and the limits of what wording alone can fix.

*Also referred to as: system prompt design, prompt engineering limits, chain-of-thought prompting, role prompting, few-shot example selection, prompt scaffolding and templates, in-context learning*

## State of Practice

The field has largely stopped treating prompt text as the place where reliability is won. Speakers converged on a division of labor: instructions express objectives, desired behaviors, and context, while anything that must be guaranteed — state transitions, hard identity rules, format and length compliance, safety vetoes — is enforced in the harness or in code, because 'a prompt will eventually lose.' At the same time, empirical results show wording still has outsized and non-obvious effects: one sentence in SWE-Bench Pro's template ('tests are handled') suppresses self-verification in GPT 5.5 and Opus 4.8; explicit negative constraints measurably degraded small-model output where few-shot examples helped; ordering qualitative tone context before numeric constraints changes prose quality. The live arguments are about direction of investment, not whether wording matters: Anthropic removed 80% of the Claude Code system prompt on the theory that examples and 'do not' rules constrain a model more imaginative than its instructions, while other teams report that explicit decomposition scaffolds, layered prompt architectures, and curated few-shot sets measurably widen what an agent will attempt. Benchmark authors have turned this into a critique of evaluation itself — 481-word instructions that point at the test file or hand over the implementation interface leak the answer and lock the model out of its own approach. And a growing UX contingent argues the whole activity is a symptom: prompting is a batch protocol inherited from the punch card, and expecting end users to be good at it is a design failure to be engineered away with templates, plans, and participating interfaces.

## Consensus

### Guarantees cannot be obtained by wording; anything that must always hold belongs in deterministic code or the harness, not in the prompt.

Support: **5** talk(s)

> "Everything before layer four is prompt engineering. You're asking nicely and hoping. Layer four is systems engineering. You're checking, and you are sure."
>
> — [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [17:51](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1071s)

Supporting talks: [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)

### Instructions should state objectives, desired behavior, and hard constraints, not prescribe the implementation — over-specification both leaks answers and suppresses better solutions.

Support: **3** talk(s)

> "The instructions given to an agent or an LLM should lean towards expressing desired behaviors, objectives, and hard constraints, not implement details"
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [8:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=500s)

Supporting talks: [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)

### Single sentences, phrasing polarity, and clause ordering produce large behavioral swings, including suppressing capabilities the model would otherwise exercise.

Support: **5** talk(s)

> "in SweetBench Pro's template they explicitly tell the model that the tests are handled and therefore they do not need to uh write uh any new tests of their own. With that single line in the prompt it will uh prevent the models from even uh 5.5 and uh Opus 4.8 from attempting to verify its own work"
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [7:09](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=429s)

Supporting talks: [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)

### No prompting technique is universally best; variants must be tested one variable at a time against your own task and model rather than adopted on reputation or general advice.

Support: **3** talk(s)

> "You want to isolate one variable per prompt variant to test whether what you're trying to accomplish is moving the needle when you're using the different prompts."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [20:52](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1252s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)

### End users should not be asked to author prompts; products should supply templates, directional presets, examples, or an approvable plan instead of a blank input box.

Support: **3** talk(s)

> "when we place a blank text box in front of a user and just tell them to ask AI, we're actually kind of asking them to do a lot of work in figuring out how to really use it"
>
> — [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [31:32](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1892s)

Supporting talks: [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)

### Today's prompting tricks are transitional scaffolding that shrinks as models are post-trained to do the same work internally — proficiency at prompting is a temporary artifact, not a durable skill.

Support: **3** talk(s)

> "going forward with the newer models that are much better post-trained to compartmentalize the problems and break down the problems. Uh we probably get need less and less of these tricks down the road"
>
> — [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s)

Supporting talks: [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)

## Disagreements

### Do in-prompt examples improve output quality, or do they constrain a model that would otherwise do better?

| Position A | Position B |
|---|---|
| Few-shot examples are the highest-leverage prompt lever: they beat reformatted input, strict negative rules, and chain-of-thought in head-to-head tests, and they are the only way to convey latent specification criteria that cannot be written as instructions.<br>*[Frontier results, on device](../talks/frontier-results-on-device.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* | Examples and full interface specifications cap the model at the quality of the examples; strip them out and give context instead, because current models are more imaginative than what you would show them.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)* |

*Why it matters: It determines whether teams invest in curating and maintaining few-shot sets or delete them — and the two camps differ systematically by model size, with the pro-example evidence coming from 3B-class local models and the anti-example evidence from frontier coding models, which suggests the right answer is model-dependent rather than universal.*

### When a multi-step agent is unreliable, should control flow be moved out of the model into the harness, or should the model be given more latitude and better tools?

| Position A | Position B |
|---|---|
| Take control flow out of the model: the harness owns state, validates each result, and decides what comes next; skills should be explicitly invoked rather than left for the model to discover; the final check should be deterministic regex, not a probabilistic classifier.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* | What contains the model is the harness and prompt, so the fix is to give it arms — tools to search and build its own context — and let it choose its own moment and modality rather than routing it through a fixed protocol.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)* |

*Why it matters: The first path lets a Haiku-class model do work a frontier model was doing, at lower cost and latency, but caps behavior at what you enumerated; the second path bets on capability overhang and pays for it in unpredictability and eval burden.*

### Do more capable models need more explicit prompt structure or less?

| Position A | Position B |
|---|---|
| Less: remove the scaffolding. Anthropic cut 80% of the Claude Code system prompt, and on Continual Learning Bench 1.0 vanilla in-context learning outperformed more sophisticated context-management systems on reward and on both cost Pareto frontiers.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)* | More: explicit structure measurably expands what the agent attempts. Making decomposition a separate action producing a linked document hierarchy escapes the saturation that a bare 'here's the codebase, optimize it' prompt hits; a single system prompt cannot be situational, expressive, and self-checking at once and must be split into layers; splitting a process so the agent sees one step at a time increases the legwork it does on that step.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)* |

*Why it matters: Structure has a standing token cost and a maintenance cost, and the two camps predict opposite results from the same edit — deleting a scaffold either unlocks the model or drops it back into local, incremental changes.*

## Practical Guidance

**Do:**

- Split a monolithic system prompt into layers with distinct jobs, and place hard identity rules where the voice layer physically cannot override them rather than as one instruction among many
- Render soft qualitative context (tone, empathy, what not to say) before numeric constraints, since reversing the order commits the model to a mechanical framing
- Use leading words that pack meaning into few tokens, then verify they landed by checking whether the agent repeats the word back in its reasoning traces
- Give the model another artifact as the spec — existing code or an HTML mockup — rather than writing the spec out in prose
- Make decomposition an explicit, separate action that produces a linked hierarchy of component documents before asking for improvements
- Test one variable per prompt variant and measure latency alongside quality: few-shot added ~200ms while chain-of-thought added ~600ms for the same length-compliance gain
- Route hypothesis generation and post-implementation critique to a stronger reasoning model than the one doing implementation
- Fix structural and length failures with deterministic post-processing in the harness instead of reaching for a larger model
- Keep skill.md as small as possible and push branch-specific reference material behind a context pointer to an external file
- For persona and simulation prompts, paint the entire world in the prompt including the study's own construction, inverting the human-research norm of hiding study design
- Delete any instruction the agent would follow anyway if it were removed — no-ops are especially common when an agent wrote the skill
- Show the user a plan for approval before executing an agentic action, with a setting to skip it on repeated flows

**Avoid:**

- Two-page task instructions — SWE-Bench Pro averages 481 words and over 4,500 characters per instruction, which is not how engineers actually prompt
- Instructions that reference the test file or hand over the complete implementation interface, which leak the answer and lock the model out of its own approach
- Telling the model that tests are handled: one line is enough to stop even GPT 5.5 and Opus 4.8 from verifying their own work
- Negative 'do not do this' rules — replace them with context; explicit negative constraints measurably worsened small-model output
- 'Write in our brand's voice' and similar instructions that do nothing the model was not already going to attempt
- Adding more demographic detail to a persona in the belief it gets closer to reality — it can amplify model bias and move results further astray
- Reaching for more prompt rules when a multi-step agent skips steps or loops; at coin-flip reliability the fix is removing control flow from the model
- Treating prompt length as a proxy for task difficulty — DeepSWE prompts are half the length of SWE-Bench Pro's and yield five times the lines of code
- Letting a shared prompt or skill file accumulate sediment, duplication, and no-ops because contributors won't delete each other's text
- Trusting LLM-judge scores on prompt variants without manual inspection, since judges favor models from their own family

## Notable Outliers

- More capable models increase rather than decrease the need for upfront specification, because they traverse more territory and hit more decision points you never specified — the human's bottleneck becomes finding their own unknowns. ([Field Guide to Fable](../talks/field-guide-to-fable.md), [9:37](https://www.youtube.com/watch?v=9fubhllmsBU&t=577s))
- Prompt engineering is not a skill advance at all but a set of packaging rules for a batch protocol; human proficiency at it is evidence of a design failure, the same mastery a punch card operator had. ([The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [7:56](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=476s))
- Production diffusion systems now essentially require a separately trained prompt-expander LLM that rewrites the user's prompt into a long detailed one, because longer prompts are more in-distribution with training data. ([Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [17:33](https://www.youtube.com/watch?v=-tviRdpmHvs&t=1053s))
- Vanilla in-context learning topped the Continual Learning Bench 1.0 leaderboard over more expensive context-management systems, holding across both the reward-vs-cost and gain-vs-cost Pareto frontiers. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- Purely test-based verification forces some methodological hinting into the prompt, because without steering the agent may not be positioned to make meaningful progress at all — hybrid LLM-as-judge verification is what would allow genuinely objective-only prompts. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [16:15](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=975s))
- Claude drops part of a multi-part requirement in roughly two out of three rollouts, while GPT models were the least likely family to miss stated requirements — so the same prompt needs different redundancy depending on model family. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [4:52](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=292s))

## All Talks

- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
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
- [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)

## Speakers

- [Ali Khial](../speakers/ali-khial.md)
- [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)
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
- [Sangwu Lee](../speakers/sangwu-lee.md)
- [Sina Shahandeh](../speakers/sina-shahandeh.md)
- [Ted Johnson](../speakers/ted-johnson.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)

