---
title: "agent reliability engineering"
type: "concept"
slug: "agent-reliability-engineering"
tier: "core"
maturity: "contested"
talk_count: 17
speaker_count: 16
---

# agent reliability engineering

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **17** talk(s) by **16** speaker(s)

**Definition:** Making agents fail rarely and recover gracefully — error compounding across steps, retries, degradation, and reliability as a system property.

*Also referred to as: agent reliability, multi-step agent reliability, agent failure modes, agentic failure modes, compounding error in multi-step agents, graceful degradation, retry amplification, recovery policies*

## State of Practice

The conference's dominant claim is that model capability has stopped being the binding constraint and reliability has replaced it: speakers from Meta Superintelligence Labs, Amazon AGI Lab, Microsoft, Bespoke Labs and OpenProse all independently framed the gap between a demo and a product as a systems problem, not an intelligence problem. The concrete architecture that emerged is a control-plane pattern — the model emits proposals (typed UI blocks, X12 transactions, tool calls, state-machine transitions), and validation, policy, state advancement, and execution live in deterministic code outside the model. Failure modeling has shifted away from hallucination toward infrastructure and state failures: uncontrolled retries turning a minor API error into a compute incident, distributed-state inconsistency misdiagnosed as bad reasoning, unknown content types crashing unpatchable mobile clients, and failures that persist rather than reset. Measurement has followed: teams are adopting SRE framing (reliability, recovery, latency, cost, tail percentiles) over accuracy, running each test case many times against a sustained pass-rate bar such as 90%, and treating production traces as the largest and most representative eval set they will ever have. Where the field splits is on mechanism — whether reliability is engineered around a permanently untrustworthy model or trained into it via post-training and RL on messy environments, and whether verification should be agentic or forced down to deterministic and static checks.

## Consensus

### Reliability, not model intelligence, is the binding constraint on production agents; the models are already capable enough for most deployed workflows.

Support: **8** talk(s)

> "The models are intelligent enough. They know all kinds of things. They know the entire internet. But they can't reliably deliver outcomes. And so I can't trust them."
>
> — [Recursive Coding Agents](../talks/recursive-coding-agents.md), [0:52](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=52s)

Supporting talks: [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Perception Agents](../talks/perception-agents.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### The model should only propose; validation, state advancement, and execution authority belong to deterministic code outside the model, and model output should be constrained to a fixed vocabulary it cannot extend.

Support: **5** talk(s)

> "Never let the model directly control production systems. The model should generate proposals, infrastructure validates them, policy engine approves them, execution gateway enforces them."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:09](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=189s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Hallucination is not the dominant production failure mode; the expensive failures are infrastructure, control-flow, and delivery failures around the model.

Support: **4** talk(s)

> "Many teams still think hallucinations are the primary AI failure modes. In production, they are often just one category."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [1:43](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=103s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)

### Failure in real environments is persistent rather than transient, so recovery policy and graceful degradation must be designed explicitly instead of assumed from retry or reset.

Support: **5** talk(s)

> "The assumption is that failure resets. the reality is that failure is often persistent. So we have to focus on recovery policies."
>
> — [From RL to IRL](../talks/from-rl-to-irl.md), [14:17](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=857s)

Supporting talks: [From RL to IRL](../talks/from-rl-to-irl.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Perception Agents](../talks/perception-agents.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### Human supervision is a permanent architectural component, not a temporary crutch that better models will remove; the design question is where to spend human attention (evaluation, taste, handoff), not how to eliminate it.

Support: **6** talk(s)

> "Many people frame human involvement as temporarily temporary necessity. I don't think that's correct. The most successful systems are likely to remain human supervised."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [4:50](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=290s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [From RL to IRL](../talks/from-rl-to-irl.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Evaluation must continue after deployment against real production traffic; pre-launch benchmarks and demo conditions systematically miss the failures real users trigger.

Support: **5** talk(s)

> "after we launch the software, we have our auto evolve system evaluate carefully evaluate each conversation. We have predefined a lot of rubrics, what we think is good, what is bad."
>
> — [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [15:49](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=949s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [From RL to IRL](../talks/from-rl-to-irl.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Reliability must be measured as a distribution over many repeated runs and at the tail, not as single-shot accuracy — a system that works once or at P50 is not a system that works.

Support: **5** talk(s)

> "if your agent one in four times deletes a database, you will never touch that agent again, right? So when you need this reliability, you really need to be it in the nines."
>
> — [Perception Agents](../talks/perception-agents.md), [3:30](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=210s)

Supporting talks: [Perception Agents](../talks/perception-agents.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)

### Reliability appears first where outputs are verifiable, so teams should engineer verifiability into the task representation rather than trying to make unverifiable work reliable.

Support: **5** talk(s)

> "why was coding first solved? It's because code is verifiable. You can run it, you can test it, you can check it and you can be for sure that it worked. So reliability showed up in the first place you can actually verify the answer."
>
> — [Perception Agents](../talks/perception-agents.md), [5:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=355s)

Supporting talks: [Perception Agents](../talks/perception-agents.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [From RL to IRL](../talks/from-rl-to-irl.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)

## Disagreements

### Should agent reliability be engineered around the model in the harness, or trained into the model itself?

| Position A | Position B |
|---|---|
| Reliability is a control problem solved outside the model: take control flow, state, and completion judgments out of the model permanently, and treat the model as an untrustworthy component whose failure domains are engineered away.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Reliability is a training problem: post-training and RL on messy, failure-rich environments are the strongest lever, infra errors should be surfaced to the model so recovery becomes a native model action, and harness guardrails are transitional scaffolding that should get thinner as the model improves.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [From RL to IRL](../talks/from-rl-to-irl.md)* |

*Why it matters: It determines whether engineering investment goes into a durable orchestration/control-plane layer or into data and environment pipelines, and whether an infrastructure error should be caught and handled by code or deliberately passed through to the model to recover from.*

### Should verification of agent output be done by other models/agents, or pushed down to deterministic and static checks?

| Position A | Position B |
|---|---|
| Use models to check models: agent-as-a-judge with full trace analysis catches multi-step failures fixed rubrics cannot, cross-model agreement gates high-stakes actions, and a perception agent can read the rendered screen to confirm its own work.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Perception Agents](../talks/perception-agents.md)* | Stacking non-deterministic verification on non-deterministic output makes correctness worse; verification should be static and deterministic (types, schemas, structured contracts, harness validation), with a human actually reading the output as the backstop.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)* |

*Why it matters: It decides whether the reliability budget buys more inference (judge agents, multi-model quorums, eval fleets) or buys stricter representations and type systems — and whether a passing agentic eval is admissible evidence for shipping.*

### Is reliability a single high bar the system must clear, or a per-action risk budget that varies by stakes?

| Position A | Position B |
|---|---|
| End-to-end reliability must reach 'the nines' and hold across 10,000 to 1,000,000 executions; 60-80% success is not usable and one bad action destroys trust in the whole system.<br>*[Perception Agents](../talks/perception-agents.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)* | Eliminating failure entirely is costly and often unnecessary; classify failures by consequence — a one-in-a-thousand failure is fine where the user can retry, zero tolerance applies to irreversible actions — and use calibrated confidence about risk, reversibility, and authorization to decide when to hand back to a human.<br>*[How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [From RL to IRL](../talks/from-rl-to-irl.md)* |

*Why it matters: A uniform nines target blocks shipping anything until the weakest path is fixed, while a graded risk budget ships most of the surface immediately and concentrates cost on irreversible actions — very different roadmaps and very different cost structures.*

### Does reliability come from adopting the strongest available model, or from harnessing a smaller one?

| Position A | Position B |
|---|---|
| A sufficiently strong harness lets a much smaller model hit the required performance bar at lower cost and latency, and an overpowered model on high-frequency routine transactions defeats the purpose; upgrading to a newer higher-scoring model can break a working system and requires rebuilding evals from scratch.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md)* | Teams must scale with model capabilities or fall behind — frontier models can one-shot medium-sized features from a good spec, and planning should assume model capability keeps improving.<br>*[How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)* |

*Why it matters: It sets whether the reliability roadmap is 'build scaffolding so cheap models suffice' or 'keep the pipeline model-agnostic and ride upgrades', which changes eval strategy, unit economics, and how much work is thrown away on each model release.*

## Practical Guidance

**Do:**

- Model multi-step workflows as an explicit state machine in the harness (e.g. intro, teach, check, grade, advance, wrap); the harness validates the model's return, advances state, and decides what comes next.
- Give the model a fixed catalog to select from rather than free generation — a closed component list, a standard public schema, or an X12-style transaction vocabulary — and gate catalog entries by client version so old clients are never offered types they cannot render.
- Cap and budget retries explicitly; treat uncontrolled retry as a resource-exhaustion vector that converts a minor API error into a compute incident.
- Emit traces of the decision chain — reasoning path, tool calls, memory access, state transitions — not just logs, since debugging an autonomous workflow depends on the chain more than the final output.
- Run each integration test many times and gate on a sustained pass rate (e.g. 90%) rather than a single green run.
- Adopt SRE metrics as the North Star — reliability, availability, latency, cost, recovery — and stop treating accuracy as the headline number.
- Design against P99/P999 rather than P50 when one logical operation fans out into many calls, because per-call tail latency compounds through traversal.
- Train and test in high-fidelity messy sandboxes: layout shift, slow loads, missing labels, pop-ups, focus stealing, random account states, stale tabs.
- Surface infrastructure errors to the agent as recoverable events rather than resetting the environment, so recovery becomes a learned action.
- Penalize dangerous intermediate actions, not just wrong final outcomes — a trajectory can reach 'done' having done something irreversible along the way.
- Isolate data sources and fall back to last-verified context at serve time so a bad feed degrades the system instead of breaking it.
- Gate irreversible high-stakes actions on agreement between two different models, escalating to a human when they disagree.
- Keep working context well under the window — roughly 100k tokens, under 60k for the hardest problems — and re-allocate a fresh context each iteration rather than compacting.
- Maintain your own internal representation of external system state, treated as correct only until downstream evidence disproves it.
- Replace total latency with time-to-first-chunk as the primary UX metric, and show intermediate progress rather than an opaque spinner.
- Cap PRs at 500 lines so review remains meaningful when agents are producing thousands of lines a day.

**Avoid:**

- Fixing multi-step unreliability by adding more prompt rules — it is a control problem, and long rule lists also blow up latency.
- Letting the model hold the state of a multi-step workflow or decide whether it is finished.
- Assuming failure resets: firing off actions and moving on without watching whether the step actually succeeded.
- Treating hallucination as the primary production risk while leaving retry storms, distributed-state inconsistency, and delivery-layer crashes unaddressed.
- Shipping unknown content types to clients you cannot patch — a mobile client that meets an unfamiliar type crashes, and keeps crashing for days or weeks.
- Trusting benchmark scores or demo runs as evidence of production reliability; the benchmark-to-production gap widens as autonomy increases.
- Positioning humans as fallback handlers instead of evaluators, or rubber-stamping agent-authored PRs, which manufactures false confidence.
- Swapping in a newer, higher-scoring model without rebuilding evals and validation first — different is not automatically better.
- Stacking loops on loops and buying quality with more tokens; the token spend is not sustainable at company scale and it does not fix correctness.
- Running loop-driven code generation in dynamically typed languages where there is no type system doing verification for you.
- Using an expensive frontier model for routine transactions executed thousands of times a day, which defeats the cost case for the system.
- Storing secrets as files in an agent's environment, since increasingly goal-seeking models will find and use them.

## Notable Outliers

- Many multi-agent failures blamed on model reasoning are actually distributed-state consistency failures in disguise. ([Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:58](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=238s))
- When reliability on a step approaches a coin flip, that is the explicit signal to remove control flow from the model entirely. ([Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [5:17](https://www.youtube.com/watch?v=m24UKZomm7k&t=317s))
- Reliability failures reach below the agent stack: a race condition in widely used open-source FP8 kernels silently corrupted about 0.5% of gradients, and replica hash checking cannot detect it because real training runs have no redundancy in the forward/backward pass. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s))
- A structured response from an authoritative external system is not ground truth — the payer's phone line, portal, and X12 feed can all agree on the same wrong answer, and the claim is still denied. ([Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [15:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=918s))
- Treat the model as a drunk you cannot trust, and engineer away the failure domains: the loop must not be allowed to close until the output satisfies your engineering certification for the domain. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [22:53](https://www.youtube.com/watch?v=c35YoMdnI78&t=1373s))
- Acceptable failure rate should be set per action class: one-in-a-thousand is fine for appointment scheduling because the user can retry, but reimbursement claims tolerate zero because every error escalates immediately. ([How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [14:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=867s))
- Error accumulation in an autoregressive, past-only generator is solvable well enough to run 8 to 16 hours of continuous frame-by-frame generation with no reset and no noticeable drift. ([Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [12:36](https://www.youtube.com/watch?v=z1dqv74SpUs&t=756s))

## All Talks

- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
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
- [Dan Feng](../speakers/dan-feng.md)
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
- [Vasant Kearney](../speakers/vasant-kearney.md)

