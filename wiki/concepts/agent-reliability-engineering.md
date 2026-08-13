---
title: "agent reliability engineering"
type: "concept"
slug: "agent-reliability-engineering"
tier: "core"
maturity: "consolidating"
talk_count: 14
speaker_count: 13
---

# agent reliability engineering

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **14** talk(s) by **13** speaker(s)

**Definition:** Making agents fail rarely and recover gracefully — error compounding across steps, retries, degradation, and reliability as a system property.

*Also referred to as: agent reliability, multi-step agent reliability, agent failure modes, agentic failure modes, compounding error in multi-step agents, graceful degradation, retry amplification, recovery policies*

## State of Practice

The field has converged on reliability — not model capability — as the binding constraint on shipping agents, and has largely stopped treating hallucination as the main failure mode; the failures that hurt in production are infrastructure failures, distributed-state inconsistency, uncontrolled retries turning a single API error into a compute incident, unrenderable outputs crashing unpatchable mobile clients, and slow reliability drift that no single change makes catastrophic. The dominant architectural answer is to strip execution authority from the model: the model emits proposals (a next action, a UI intent from a fixed catalog, a decomposition), and a harness or control plane validates them, applies policy, advances workflow state, and enforces execution — several teams report that a sufficiently strong harness lets a much smaller model hit the same reliability bar (Haiku 4.5 replacing Opus 4.7 in a live voice tutor). Reliability is measured like SRE work, not research work: scenario-driven evals over production telemetry, agent traces of reasoning paths and state transitions rather than logs, and evaluation running continuously after deploy rather than as a pre-ship gate. Where practitioners still disagree is on where the reliability actually gets encoded — in harness scaffolding that stays permanent, or in model weights via post-training and RL with the harness deliberately thinning over time — and on whether a second non-deterministic layer (agent-as-a-judge, self-verifying perception agents) improves correctness or compounds the problem. Verifiability remains the field's stated frontier: coding got reliable first because it can be run and tested, and nobody has a good answer for the majority of knowledge work where there is no unit test.

## Consensus

### Reliability, not model intelligence, is the binding constraint on production agents; models are already capable enough for most deployed use cases.

Support: **8** talk(s)

> "The challenge is no longer in intelligence. The challenge is is reliability."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [0:03](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=3s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Perception Agents](../talks/perception-agents.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)

### The model should only propose; control flow, workflow state, and execution authority belong to the harness, gateway, or platform around it.

Support: **4** talk(s)

> "the model never really um has to think. It proposes, but ultimately it is the harness that decides."
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [4:04](https://www.youtube.com/watch?v=m24UKZomm7k&t=244s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Failure must be treated as persistent rather than self-clearing: systems need explicit recovery policies and graceful degradation, because agents fire actions and move on without checking what happened.

Support: **5** talk(s)

> "The assumption is that failure resets. the reality is that failure is often persistent. So we have to focus on recovery policies."
>
> — [From RL to IRL](../talks/from-rl-to-irl.md), [14:17](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=857s)

Supporting talks: [From RL to IRL](../talks/from-rl-to-irl.md), [Perception Agents](../talks/perception-agents.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### Benchmarks and demos do not predict production reliability; the highest-value signal comes from real deployment traces, and the gap widens as systems get more autonomous.

Support: **4** talk(s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [From RL to IRL](../talks/from-rl-to-irl.md)

### Human involvement is a permanent structural component of reliable agent systems — as evaluator, approver, and liability anchor — not a temporary crutch that better models remove.

Support: **5** talk(s)

> "Many people frame human involvement as temporarily temporary necessity. I don't think that's correct. The most successful systems are likely to remain human supervised."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [4:50](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=290s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [From RL to IRL](../talks/from-rl-to-irl.md)

### Agents become reliable exactly where their output is cheaply verifiable; domains without a verification mechanism are the open problem.

Support: **3** talk(s)

> "why was coding first solved? It's because code is verifiable. You can run it, you can test it, you can check it and you can be for sure that it worked. So reliability showed up in the first place you can actually verify the answer."
>
> — [Perception Agents](../talks/perception-agents.md), [5:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=355s)

Supporting talks: [Perception Agents](../talks/perception-agents.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [From RL to IRL](../talks/from-rl-to-irl.md)

## Disagreements

### Should reliability be engineered into the surrounding harness and infrastructure, or trained into the model weights via post-training and RL?

| Position A | Position B |
|---|---|
| Reliability is a systems property that lives outside the model permanently: a control plane, a state machine, a policy engine, and an execution gateway constrain a stochastic model that can never be trusted. Prompts and models are commoditizing; infrastructure is the durable differentiator.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Reliability should be pushed into the model itself. Post-training (mostly SFT, with RL for the last few points) is a more powerful lever than prompting or harness changes, and harness guardrails are explicitly transitional scaffolding that should get thinner as the model gets better — including making error recovery a native model action instead of an infrastructure reset.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [From RL to IRL](../talks/from-rl-to-irl.md)* |

*Why it matters: It determines whether your reliability budget buys orchestration engineers and a control plane or buys data curation and RL environments — and whether the scaffolding you write this quarter is a permanent asset or a write-off once the next model lands.*

### Who should decide how a task is decomposed — the model, or a pre-specified workflow?

| Position A | Position B |
|---|---|
| The harness fixes the decomposition. A lesson is a six-state machine; the model never tracks which step it is on, never judges whether the task is complete, and picks only from a fixed catalog of components or actions supplied in context. When reliability approaches a coin flip, that is the signal to remove control flow from the model entirely.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)* | Model-chosen decomposition is the point. A system only qualifies as an RLM if the model itself picks how to break the problem into sub-calls; hardcoded map-reduce pipelines do not count, and it is model-driven recursion over symbolic state that lets a 9B model beat frontier models on long-horizon tasks.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [From RL to IRL](../talks/from-rl-to-irl.md)* |

*Why it matters: Fixed decomposition caps an agent at the workflows you enumerated in advance but makes failures diagnosable and bounded; model-chosen decomposition generalizes to unseen tasks but makes every failure a novel one, which changes what you can trace, test, and certify.*

### Does adding another LLM or agent as a verification layer improve correctness, or compound the failure?

| Position A | Position B |
|---|---|
| Yes — the best way to evaluate an agent is another agent. Fixed-rubric LLM-as-a-judge cannot catch multi-step trajectory failures like silent looping; an evaluation agent with full trace access finds them and can even open the fixing PR. Perception agents similarly verify their own rendered output against design rules and user flows.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Perception Agents](../talks/perception-agents.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* | No — stacking a non-deterministic verifier on non-deterministic output makes correctness worse. Verification should be pushed toward static and deterministic checks (types as verification, tests, security scanners), and the only reliable defense against compounding slop is a human reading the output.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* |

*Why it matters: One path scales oversight with tokens and lets you run 100M evals a month; the other caps throughput at human reading speed and forces investment in static analysis and typed languages instead of judge fleets.*

### Is running agents in loops until they succeed a sound reliability strategy?

| Position A | Position B |
|---|---|
| Loops are the mechanism. Run the agent in a loop at roughly $10.42/hour, prevent the loop from closing until it satisfies your engineering certification, and accept that the model is unreliable but engineer away its failure domains.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Uncontrolled retries are among the biggest risks in agentic systems — a minor API error becomes a compute incident through exponential resource growth — and buying quality with more tokens does not survive company-scale budgets. Building a tighter harness so a smaller model suffices is the cheaper reliability path.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)* |

*Why it matters: This is the difference between an unbounded token budget as your reliability mechanism and a hard retry/resource ceiling as your safety mechanism; the loops camp itself concedes the current pattern of loops-on-loops is economically unsustainable at scale.*

## Practical Guidance

**Do:**

- Model multi-step workflows as an explicit state machine the harness owns: the harness validates what comes back, advances state, and decides what is next — the model never records which step it is on.
- Route every model action through proposal → infrastructure validation → policy approval → execution gateway; never let the model touch production systems directly.
- Give the model a closed catalog to select from (e.g. UI components gated by client app version, so a 2.0 flight card is only offered to 2.0+ clients) rather than letting it emit free-form structures a client must interpret.
- Pass infrastructure errors back to the model as observations and expect recovery via native tool use, instead of resetting the environment on infra failure.
- Detect and penalize dangerous intermediate actions during training — outcome-only reward accepts trajectories that reach 'done' by, for example, sending a resignation letter to the CEO.
- Make handoff-to-human a first-class agent action gated on calibrated confidence about risk, reversibility, authorization, and visibility.
- Instrument agent traces over reasoning paths, tool calls, memory access, and state transitions; for autonomous workflows the chain of decisions matters more than the final output.
- Run evaluation continuously as an always-on service in the control plane after deploy, since reliability degrades by drift rather than by any single catastrophic change.
- Drive offline evaluation from simulated scenarios rather than individual prompts, and treat humans as evaluators of those traces rather than as fallback handlers.
- Isolate data sources and fall back to last-verified context at serve time so a bad feed degrades the system gracefully instead of breaking it.
- Keep agent context under roughly 100k tokens (under 60k for the hardest problems) and deterministically re-allocate a fresh context each iteration rather than compacting.
- Push verification toward static and deterministic checks — statically typed languages, tests, and AI security scanning on PRs both before and after merge.
- Design object-storage-backed agent infrastructure against P99/P999 rather than P50, since one logical operation fans out into many ~200ms requests.
- Hard-crash on invariant violations (e.g. mismatched weight hashes across data-parallel replicas) instead of letting a run continue silently corrupted.

**Avoid:**

- Fixing multi-step unreliability by adding more prompt rules — it is a control problem, not a prompting problem, and long compliance rule lists also blow up latency.
- Letting the LLM decide whether the task is complete, whether the user succeeded, or what step comes next.
- Unbounded or uncontrolled retries, which turn a minor API error into a compute incident through exponential resource growth.
- Treating hallucination as the primary production failure mode; in production it is one category among tool failures, API outages, state inconsistency, and context changes.
- Assuming an agent failure resets cleanly — in real environments the account stays blocked and the tab stays stale.
- Reading benchmark scores as evidence of production reliability; benchmarks measure model capability, production measures system behavior.
- Layering another non-deterministic verifier on top of non-deterministic output and expecting correctness to improve.
- Relying on compaction to manage long contexts — it is lossy and degrades fidelity across iterations.
- Emitting content types the client has never seen: mobile clients cannot be meaningfully patched, so the crash persists for days or weeks.
- Framing human review as a fallback queue rather than as the evaluation layer.
- Shipping demo-tuned agents without adversarial and messy-environment testing (layout shift, slow loads, missing labels, pop-ups, focus stealing, random account states).

## Notable Outliers

- Many multi-agent failures blamed on reasoning are actually distributed-state consistency failures in disguise. ([Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:58](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=238s))
- With a strong enough harness, Haiku 4.5 replaced Opus 4.7 in a live voice tutor at the expected performance level while cutting cost and latency. ([Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s))
- Qwen 3.5 9B run as a recursive language model beats Opus and GPT-5.4 run as plain LLMs on long-reasoning tasks — reliability from orchestration, not scale. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [6:35](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=395s))
- Harness guardrails are transitional scaffolding: they should be strong early and get progressively thinner as model capability improves. ([From RL to IRL](../talks/from-rl-to-irl.md), [17:12](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=1032s))
- Open-source FP8 kernels contained a race condition silently corrupting ~0.5% of gradients, and replica hash checking cannot detect it because real training runs lack the redundancy to compare forward/backward passes. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s))
- Adding non-deterministic verification on top of agent output makes correctness worse, not better. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [25:38](https://www.youtube.com/watch?v=c35YoMdnI78&t=1538s))
- Targeting 100x speedup traps teams in meta-optimization; 2-3x from small incremental loops is the realistic target and still transforms every company. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [49:02](https://www.youtube.com/watch?v=c35YoMdnI78&t=2942s))

## All Talks

- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [Perception Agents](../talks/perception-agents.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

## Speakers

- [Antje Barth](../speakers/antje-barth.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Robert McHardy](../speakers/robert-mchardy.md)

