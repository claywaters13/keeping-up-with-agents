---
title: "agent reliability engineering"
type: "concept"
slug: "agent-reliability-engineering"
tier: "core"
maturity: "consolidating"
talk_count: 15
speaker_count: 14
---

# agent reliability engineering

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **15** talk(s) by **14** speaker(s)

**Definition:** Making agents fail rarely and recover gracefully — error compounding across steps, retries, degradation, and reliability as a system property.

*Also referred to as: agent reliability, multi-step agent reliability, agent failure modes, agentic failure modes, compounding error in multi-step agents, graceful degradation, retry amplification, recovery policies*

## State of Practice

The conference's near-unanimous framing is that model capability is no longer the binding constraint on agentic products — reliability is, and reliability is a systems property rather than a model property. Speakers from Meta Superintelligence Labs, Microsoft, Amazon AGI Lab, and OpenProse independently arrived at the same architecture: the model emits proposals (a next action, a UI intent, a lesson step), and a deterministic layer around it — harness, policy engine, execution gateway, BFF — validates, approves, and advances state, with workflow state never held in the model's head. Failure is assumed to be persistent rather than transient, so recovery policies, bounded retries, graceful degradation, and human handoff are first-class design objects; the canonical horror story is a minor API error escalating into a compute incident through uncontrolled retries. Verification is the recognized substrate of reliability — coding got reliable first because code runs — and the open problem is knowledge work where no unit test exists. Evaluation is being repositioned as always-on infrastructure fed by production traces (reasoning chains, tool calls, memory access, state transitions) rather than a pre-deployment benchmark gate, because the benchmark-to-production gap widens as autonomy increases. The live arguments are where the reliability investment belongs (harness versus weights) and whether the verifier itself is allowed to be probabilistic.

## Consensus

### Reliability, not model intelligence, is the binding constraint on production agents; the models are already good enough and the failures live in the system around them.

Support: **8** talk(s)

> "The challenge is no longer in intelligence. The challenge is is reliability."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [0:03](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=3s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Perception Agents](../talks/perception-agents.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### The model should only propose; a deterministic layer (harness, policy engine, execution gateway, backend-for-frontend) validates the proposal, decides, and holds the workflow state — the model must never hold multi-step state or drive control flow.

Support: **5** talk(s)

> "the model never really um has to think. It proposes, but ultimately it is the harness that decides."
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [4:04](https://www.youtube.com/watch?v=m24UKZomm7k&t=244s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Reliability appears exactly where verification is cheap; domains without a mechanical check on the answer remain unsolved, so teams should manufacture verifiability (tests, types, explicit design rules, rendered-screen checks) rather than trust output.

Support: **5** talk(s)

> "why was coding first solved? It's because code is verifiable. You can run it, you can test it, you can check it and you can be for sure that it worked. So reliability showed up in the first place you can actually verify the answer."
>
> — [Perception Agents](../talks/perception-agents.md), [5:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=355s)

Supporting talks: [Perception Agents](../talks/perception-agents.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)

### Failure in agent systems is persistent, not transient — systems must be built with explicit recovery policies, bounded retries, isolated sources, and graceful degradation, because agents by default fire an action and move on without checking whether it landed.

Support: **5** talk(s)

> "The assumption is that failure resets. the reality is that failure is often persistent. So we have to focus on recovery policies."
>
> — [From RL to IRL](../talks/from-rl-to-irl.md), [14:17](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=857s)

Supporting talks: [From RL to IRL](../talks/from-rl-to-irl.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Perception Agents](../talks/perception-agents.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### Demos and benchmarks systematically hide the failure modes that matter, and the gap widens with autonomy; production telemetry and traces are the highest-value reliability signal, so evaluation must run continuously after deployment.

Support: **6** talk(s)

> "And as systems become more autonomous, the gap between the benchmark performance and production performance grows."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)

### Errors compound across steps, so agent systems must be designed against tail behavior rather than average behavior — per-step success rates in the 60–80% range and P50-based infrastructure assumptions both collapse once a single logical task fans out into many steps or requests.

Support: **4** talk(s)

> "So in aggregate you have like you want to look at the P99 probably even the P999 to design the system properly because you will need to minimize the number of round trips that you had to make."
>
> — [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [25:34](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1534s)

Supporting talks: [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [Perception Agents](../talks/perception-agents.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)

## Disagreements

### Should reliability be engineered around the model in the harness, or into the model through post-training on messy environments?

| Position A | Position B |
|---|---|
| Constrain the model: take control flow, state, and judgment calls out of it and put them in deterministic infrastructure. A strong enough harness lets a smaller model (Haiku 4.5) hit the performance level of a frontier model, and the model should choose only from a fixed catalog of actions or components it can never extend.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md)* | Train the model into reliability: post-training is a more powerful lever than prompting or harness changes, infra errors should be passed to the model so recovery becomes a native model action, and training should deliberately include layout shifts, pop-ups, stale tabs, and adversarial tasks rather than shielding the model from them.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [From RL to IRL](../talks/from-rl-to-irl.md)* |

*Why it matters: It determines whether a reliability budget buys orchestration engineering and eval infrastructure or data curation and RL environments — and whether hard-won harness logic is a durable asset or scaffolding you will delete after the next model release.*

### Can the verification layer itself be probabilistic, or must checks on agent output be deterministic?

| Position A | Position B |
|---|---|
| Stacking non-deterministic verification on non-deterministic output makes correctness worse; push verification toward static, deterministic checks — types, compilers, harness validation, policy engines — and read the output yourself, because you cannot prevent loops from compounding slop any other way.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)* | Fixed rubrics cannot catch the failure modes of multi-step agents whose trajectories differ every run, so the evaluator must itself be an agent doing adaptive trace analysis — up to opening the PR that fixes what it found — or a perception agent visually confirming its own work against brand and flow rules.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Perception Agents](../talks/perception-agents.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* |

*Why it matters: If probabilistic verifiers are legitimate, reliability scales with eval spend and agents can close their own loops; if not, agent autonomy is capped by whatever a deterministic checker or a human reviewer can cover, and unverifiable knowledge work stays out of reach.*

### Is the guardrail/harness layer permanent infrastructure or transitional scaffolding?

| Position A | Position B |
|---|---|
| Guardrails are a transitional scaffold — strong early, progressively thinner as the model gets better at recovery, grounding, and calibrated handoff.<br>*[From RL to IRL](../talks/from-rl-to-irl.md)* | The control layer is a durable architectural tier, analogous to Kubernetes for containers and service meshes for microservices; human supervision is permanent rather than a temporary necessity, and infrastructure is the next differentiator now that prompts and models have commoditized.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md)* |

*Why it matters: It sets the amortization horizon for orchestration work: scaffolding you expect to delete should stay cheap and disposable, while a control plane you expect to own justifies building a real platform team around it.*

## Practical Guidance

**Do:**

- Model the workflow as an explicit state machine in the harness (intro, teach, check, grade, advance, wrap) and let the harness — not the model — decide task completion, success, and what comes next.
- Treat reliability approaching a coin flip as the trigger to remove control flow from the model rather than to add prompt rules.
- Route every model action through validate → policy-approve → execution-gateway; never let the model touch production systems directly.
- Bound and budget retries explicitly; assume an unbounded retry path turns a minor API error into a compute incident.
- Give the model a fixed catalog of actions/components and gate availability by client version, so an unpatchable mobile client never meets a content type it cannot render.
- Pass infrastructure errors back to the model as observations and expect recovery via native tool use, instead of resetting the environment on infra failure.
- Penalize dangerous intermediate actions during training, not just wrong final outcomes — a trajectory can reach 'done' having sent a resignation letter to the CEO.
- Train calibrated handoff as an action, conditioned on risk, reversibility, authorization, and visibility, rather than treating full autonomy as the objective.
- Adopt SRE metrics as the North Star — reliability, availability, latency, cost, recovery — and drop accuracy from the business-outcome dashboard.
- Emit traces of reasoning paths, tool calls, memory access, and state transitions; run evals continuously on live production traces, not just before deploy.
- Isolate data sources and fall back to last-verified context so one bad feed degrades the system instead of breaking it.
- Design storage/retrieval paths against P99/P999, not P50, when one logical operation fans out into many round trips (~200ms P99 for a 256–512KB S3 read).
- Hard-crash training runs on invariant violations such as weight-hash mismatches across data-parallel replicas.
- Use time to first chunk as the primary latency metric for AI UX, and show 'thinking' state sparingly to keep long waits legible.
- Run AI security scanning on PRs both before and after they land — roughly $5 per PR — since it reliably finds real issues humans overlook.

**Avoid:**

- Fixing multi-step unreliability by prompting harder or adding more rules — it is a control problem, and long rule lists also blow up latency.
- Letting the model remember which step of the workflow it is on, or invent an action/component outside the supplied catalog.
- Treating hallucination as the primary production failure mode; infrastructure and distributed-state failures dominate, and many 'reasoning' failures in multi-agent systems are consistency failures.
- Believing demos or benchmark scores — step-skipping, premature completion, and looping only surface with real users — or making infrastructure decisions from benchmarks that measure the wrong thing.
- Assuming failure resets, or firing actions and moving on without checking whether they landed.
- Deploying agents at 60–80% end-to-end success for real work; one-in-four destructive failures permanently destroys trust in the agent.
- Buying quality with more tokens by stacking loops on loops — the token budget per engineer cracks before the quality problem does.
- Relying on compaction to preserve fidelity; it is lossy, and re-allocating a fresh context per iteration (keeping working context under ~100k tokens, under 60k for the hardest problems) beats it.
- Running loops over dynamically typed codebases, where the absence of types removes the cheapest verification signal.
- Storing secrets as files in agent environments, and running coding agents on a local laptop given existing NPM supply-chain risk.
- Automating an intake-to-implementation pipeline without scoping discipline — the result is a high-volume, low-quality output cannon.

## Notable Outliers

- Many multi-agent failures blamed on reasoning are actually distributed-state consistency failures masquerading as reasoning failures. ([Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:58](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=238s))
- A strong enough harness let a Haiku 4.5-class model replace an Opus 4.7-class model at the expected performance level for live voice tutoring, saving cost and latency. ([Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s))
- A race condition in open-source FP8 kernels silently corrupted about 0.5% of gradients, and replica hash checking cannot detect it because real runs have no forward/backward redundancy — reliability failures start below the model layer. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s))
- Running a coding agent in a loop works out to $10.42 an hour, which is the whole economic argument for loops. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [20:42](https://www.youtube.com/watch?v=c35YoMdnI78&t=1242s))
- Trust in an agent reduces entirely to its reliability — one day it ships a working SaaS app from a single prompt, the next it empties a Solana wallet. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [0:52](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=52s))
- Error accumulation in causally-masked real-time video generation was solved well enough to run 8–16 hours of continuous frame-by-frame generation with no noticeable drift and no reset. ([Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [12:36](https://www.youtube.com/watch?v=z1dqv74SpUs&t=756s))
- Targeting a 100x speedup traps teams in meta-optimization; small incremental loops that yield 2–3x while humans still read the code and own the architecture is the achievable target. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [49:02](https://www.youtube.com/watch?v=c35YoMdnI78&t=2942s))

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
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)

## Speakers

- [Antje Barth](../speakers/antje-barth.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Robert McHardy](../speakers/robert-mchardy.md)

