---
title: "deterministic versus probabilistic system design"
type: "concept"
slug: "deterministic-versus-probabilistic-system-design"
tier: "supporting"
maturity: "consolidating"
talk_count: 19
speaker_count: 22
---

# deterministic versus probabilistic system design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **19** talk(s) by **22** speaker(s)

**Definition:** Deciding which parts of a system must be deterministic code and which can be model-driven, and how to layer the two.

*Also referred to as: deterministic vs agentic layering, deterministic vs agentic workflow separation, deterministic validation vs probabilistic instruction, deterministic execution, deterministic feedback loops, latent vs deterministic computation, deterministic decision engine, determinism-novelty tradeoff*

## State of Practice

The field has converged on a single architectural primitive: the model decides, deterministic code executes and verifies. Speakers across finance, healthcare, security, infrastructure and games independently described the same layering — a probabilistic layer that handles ambiguity, planning, and natural-language framing, wrapped in a deterministic substrate that owns arithmetic, set logic, structural traversal, side effects, credentials, and the final validation step. The debate has moved off 'is the model good enough' (most speakers assert it has been for a year or more) and onto where exactly to cut the boundary: agent autonomy is now framed as a property of your codebase's density of deterministic validation loops, not of the model. Nobody credible argued for probabilistic self-verification — evals, citations, and model-checking-model were all explicitly rejected as verification, with hard numbers (frontier models find the same vulnerability in only 50% of five runs; 75% of what a boring deterministic check finds; 40% F1). What remains genuinely open is who chooses task decomposition at runtime, whether the deterministic scaffolding is a durable asset or something models will obsolete, and whether deterministic validation can ever fully substitute for a human reading the output.

## Consensus

### Never route work to a model that deterministic code can do — arithmetic, set operations, counting, dedup, SQL, structural traversal, and signal detection belong in code.

Support: **7** talk(s)

> "I don't think you should ever send an agent to do deterministic code's job, but you certainly can."
>
> — [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [11:19](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=679s)

Supporting talks: [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Notion's Token Town](../talks/notions-token-town.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)

### The model proposes; the deterministic layer performs the consequential action. Write credentials, commits, DB mutations, and the final numeric computation must sit outside the agent.

Support: **6** talk(s)

> "The dangerous ones, the get up right access, um and trigger UCI is something that we did not give the agent. Instead, we pushed um that functionality out to the deterministic part"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [11:53](https://www.youtube.com/watch?v=LqLoYksJ6do&t=713s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Respect The Process](../talks/respect-the-process.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)

### Probabilistic checking of probabilistic output — evals, citations, models grading models — is not verification; a verification must be a deterministic, repeatable mechanism.

Support: **5** talk(s)

> "Evals are not verifiable. You cannot take a non-deterministic LLM and eval your way to something deterministic. These are probability machines."
>
> — [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [1:26](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=86s)

Supporting talks: [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Respect The Process](../talks/respect-the-process.md)

### Autonomy and output quality are gated by the density of deterministic validation available to the agent, not by model capability — the models are already good enough.

Support: **5** talk(s)

> "What agent readiness really is is it's a measure of how many of these deterministic validation loops are present inside of your code base"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [12:23](https://www.youtube.com/watch?v=wpOA-UXynoM&t=743s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)

### Stop chasing determinism inside the model; make the surrounding system reproducible instead. Model-level nondeterminism is unfixable and often desirable.

Support: **4** talk(s)

> "We don't need the model to return the exact same token back every time. We just need our system to execute the exact same state transition."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [4:49](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=289s)

Supporting talks: [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Verification must arrive through a channel independent of the actor — never trust the agent's own report that its action succeeded.

Support: **4** talk(s)

> "if you've clicked something, don't ask the click if it was successful. Check the network or check the screen."
>
> — [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [6:10](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=370s)

Supporting talks: [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Respect The Process](../talks/respect-the-process.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)

## Disagreements

### Should task decomposition be decided by the model at runtime, or fixed in advance by deterministic control code?

| Position A | Position B |
|---|---|
| The model must choose its own decomposition into sub-calls — that is precisely what makes a system agent-native; hardcoded map-reduce pipelines don't count, and coordination among many agents is the higher-leverage direction.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)* | Decomposition should be fixed by deterministic code: a bounded two-or-three-step plan-then-resolve pipeline, or a controller that picks N units of work and gives each its own context window. Model-chosen sharding produces phantom entities, silent omissions, and unbounded cost.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* |

*Why it matters: It determines whether cost and correctness are bounded by construction or emergent — Phaidra's fixed pipeline held 100% accuracy at flat 9,000 tokens per query across a 7,000x scale range, while the model-driven approach fell to 30% and burned 116M tokens per pass.*

### Can a probabilistic system ever be a legitimate checker of another probabilistic system's output?

| Position A | Position B |
|---|---|
| No. The generator and the validator must not be the same class of system. Frontier models find the same vulnerability in only 50% of five repeated runs and catch 75% of what a deterministic check catches; layering non-deterministic verification on top of agent output makes correctness worse, and a regex veto is preferable to a classifier even at the cost of coverage.<br>*[How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Yes, in bounded roles. Two independent probabilistic sources agreeing on the same fact is grounds to skip human verification entirely; LLM-as-a-judge is the correct tool for the subjective/behavioral half of testing; AI security scanning on PRs beats human reviewers at finding real issues at ~$5 per PR.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)* |

*Why it matters: If probabilistic corroboration counts, whole classes of workflow (clinical prior-auth, tone/behavior QA) can go no-touch today; if it doesn't, every such workflow needs a deterministic substrate built first, which is a far larger engineering investment.*

### Can deterministic validation substitute for a human actually reading the agent's output?

| Position A | Position B |
|---|---|
| No. The only way to stop loops from compounding slop is to read what comes out; a loop should never open a second PR while the first is unreviewed, and bad code is more expensive in the age of agents than ever before.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Yes, if the deterministic layer is built right. Non-engineer users should never have to read agent-written code — the deterministic final step should emit structured review artifacts instead; the goal is signal flowing to deploy uninterrupted by a human, with the no-touch share growing incrementally.<br>*[Respect The Process](../talks/respect-the-process.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* |

*Why it matters: This sets the ceiling on throughput: if human reading is load-bearing, review capacity caps the whole factory regardless of token budget; if deterministic artifacts suffice, the work shifts entirely into building validators.*

### Should the scaffolding around the model be specified in advance by engineers, or allowed to emerge and reorganize at runtime?

| Position A | Position B |
|---|---|
| Fixed harnesses buy reliability by suppressing the variance novelty requires; determinism and emergence pull in opposite directions. The harness should be the output of the engineering process, emerging from agent interaction and local coordination without central authority, and a carefully built one can be irrelevant within a month.<br>*[Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)* | The constraints are the product. Judgment should be consolidated in exactly one agent, a knowledge graph should act as a control plane dictating which hypotheses may be pursued, a typed SDK should be the only door to consequential effects, and the loop must not be allowed to close until it satisfies certification.<br>*[Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Respect The Process](../talks/respect-the-process.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)* |

*Why it matters: It decides whether engineering effort goes into writing constraints and validators that will still be load-bearing next year, or into designing selection pressures and coupling rates for systems whose structure you deliberately cannot specify — and whether legibility is a requirement or an accepted casualty.*

## Practical Guidance

**Do:**

- Start every workflow with deterministic checks and invoke agents only for the cases rules cannot decide, then grow the no-touch share incrementally
- Have the model emit a reference to a number rather than the number itself (atomic provenance), so it can never write or manipulate a value it doesn't understand
- Keep the dangerous capabilities — git push, PR creation, CI triggering, DB mutation — in the deterministic wrapper; let the agent only modify files on disk
- Measure agent readiness as the count of deterministic validation loops present in the codebase before concluding the model is the problem
- Use out-of-band sensors like AST-grep rather than lint or tsconfig rules, which coding agents disable with inline comments; scan main once, sort violations deterministically, and track the count in version control
- Grow context with hierarchy depth rather than instance count — describe the root-to-leaf paths, not the leaves (9,000 tokens per query whether the system has 64 or 460,000 GPUs)
- Independently verify that claimed edits actually landed; agents will report completed work that never happened
- Record inputs and outputs at each node boundary (not the network layer) plus the full envelope — model version, build ID, RAG chunks — then replay traces as free regression tests by stubbing every node except the one you changed
- Deterministically re-allocate a fresh context per unit of work instead of compacting; keep working context under ~100k tokens, under 60k for the hardest problems
- Put hard identity and safety rules in a post-generation deterministic veto that every surface passes through by default, rather than as instructions competing with other instructions
- Make the deterministic final step emit review artifacts a non-engineer can validate — the code is a means to an end
- Run agents in a micro VM (Firecracker) with Vsock-mediated networking if they need Docker; built-in Codex/Claude sandboxes are worthless once a Docker socket is exposed

**Avoid:**

- Having several probabilistic models check each other's work and calling the result verified
- Letting the same system that generates code also validate it
- Treating 94% extraction accuracy as sufficient for a consequential decision — a wrong number is still wrong if you're in the 6%
- Sharding entity enumeration across parallel LLM calls: you get invented equipment that doesn't exist and silent drops of equipment that does
- Holding large combinatorial state (an 800-person seating arrangement) in the context window instead of in deterministic space
- Setting temperature to zero and expecting reproducibility — greedy decoding fixes the selection rule, not the logits, and batching with other traffic still flips tokens
- Giving an agent a Docker socket or a general-purpose VM; it will spawn a privileged container and escape, or write Python because it found Python there after you told it to write TypeScript
- Using a language model for signal detection over metrics that statistical methods already handle
- Distributing judgment across a chain of specialized agents — every handoff loses context and no agent owns the end-to-end picture
- Relying on few-shot examples for guarantees; they teach quality on anticipated inputs and provide nothing on unanticipated ones
- Silently defaulting a missing brand identity field in a multi-tenant system — it should crash, not fall back
- Bumping dependencies to latest when remediating a specific CVE; make the smallest effective change
- Severity-based triage that ignores lows, since agents can chain low-severity vulnerabilities into working exploits

## Notable Outliers

- Legacy software drifts from Software 1.0 toward 3.0, but AI-native software should run that arrow backwards — start pure 3.0 with everything in the context window to find what's worth building, then migrate toward 1.0 for the use cases that earn it. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s))
- Determinism and emergence pull in opposite directions: the reliability of a fixed harness is bought by suppressing exactly the variance that novelty requires, which imposes a hard ceiling on what the system can discover. ([Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [8:27](https://www.youtube.com/watch?v=qdZzND79mcg&t=507s))
- Hallucination is a feature of large language models rather than a defect — the fix is not to eliminate it but to pair the LLM with a formal ontology whose reasoner keeps it on guardrails. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- You cannot get bitwise determinism from a hosted API and you do not want it — the generation-time randomness is what brings agency into your agent. ([Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s))
- reCAPTCHA v2 cannot be beaten by any architecture that round-trips a model on every interaction, because challenge rounds expire on a clock; only deterministic code at machine speed with a single vision call per round works. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [18:36](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1116s))
- Dynamically typed languages produce unmaintainable results under agent loops while Haskell and Rust work far better, because types are verification. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [57:24](https://www.youtube.com/watch?v=c35YoMdnI78&t=3444s))

## All Talks

- [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)
- [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [Respect The Process](../talks/respect-the-process.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)
- [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Corey Gallon](../speakers/corey-gallon.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Joanne Song](../speakers/joanne-song.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Rajiv Chandegra](../speakers/rajiv-chandegra.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

