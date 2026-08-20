---
title: "computer use agents"
type: "concept"
slug: "computer-use-agents"
tier: "core"
maturity: "contested"
talk_count: 15
speaker_count: 16
---

# computer use agents

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **15** talk(s) by **16** speaker(s)

**Definition:** Agents that operate GUIs, browsers, and screens directly — grounding on pixels, DOM, or accessibility trees — rather than through purpose-built APIs.

*Also referred to as: computer-use agents, browser agents, browser automation, web agents, accessibility tree grounding, screenshot-based grounding, computer use via code execution*

## State of Practice

The field has largely stopped blaming the model. Across the Computer Use track the recurring claim is a capability overhang: frontier models can already reason about screens, and what's missing is the harness — page representation, context compression, action verification, sandbox infrastructure, and recovery policy. Practice has converged on hybrid execution: the accessibility tree or a compressed markdown rendering of the page as the primary observation channel with a screenshot alongside, and code execution (CDP calls, network-request replay, a persistent REPL) doing the deterministic driving while the model handles only the parts that need eyes and judgment. Everyone who reported numbers reported low absolute capability — no model above 30% reward on Cua's CAD dataset, 0% success when a task starts from a blank artifact, 26% on SWE-Marathon's project-scale tasks — and simultaneously reported that existing benchmarks are gameable: a blind replay agent matches the frontier model that generated it on OSWorld, and rollout-only confidence intervals cover at 17-20% instead of 95%. The second-order problem is trust rather than action: verify through a different channel than the one you acted on, surface infra errors to the model instead of resetting, and hand control back to the human when confidence is low. Unresolved at the fundamentals level: whether pixels or structured trees are the right substrate, and whether the next gain comes from harness engineering or from RL-training the perception into the model.

## Consensus

### The binding constraint on computer-use agents is the harness and surrounding infrastructure, not model capability — there is a capability overhang that ordinary engineering can close today.

Support: **5** talk(s)

> "there is a massive capabilities overhang in computer use. The models are good enough, but we haven't done the engineering work to solve it."
>
> — [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [5:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=346s)

Supporting talks: [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)

### Neither raw DOM nor screenshots alone are an adequate observation channel; the working pattern is a compressed structured representation (accessibility tree or markdown) supplied alongside a screenshot.

Support: **5** talk(s)

> "what I built is a very clean representation that that basically compresses the website, and you can give this along with the screenshot. It's pretty cheap token-wise."
>
> — [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [3:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=234s)

Supporting talks: [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [From RL to IRL](../talks/from-rl-to-irl.md)

### Computer-use agents should not be restricted to human-style clicking — the reliable production pattern mixes code execution (scripts, network-request replay, a persistent REPL, CDP calls) with GUI interaction.

Support: **5** talk(s)

> "click buttons when you have to, write code when you have to and look at the result uh through pixels because that is the that is the source of of truth."
>
> — [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [15:09](https://www.youtube.com/watch?v=Ki980nV0__0&t=909s)

Supporting talks: [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [From RL to IRL](../talks/from-rl-to-irl.md)

### Verification must come through a channel independent of the action — never accept the acting agent's own report that the action succeeded.

Support: **7** talk(s)

> "if you've clicked something, don't ask the click if it was successful. Check the network or check the screen."
>
> — [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [6:10](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=370s)

Supporting talks: [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Perception Agents](../talks/perception-agents.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)

### Context must be actively budgeted and compressed rather than dumped in; oversized observation context degrades task quality, not just cost.

Support: **5** talk(s)

> "The right harness should not only present the right tools, but present an optimized amount of tokens that are compressed to get exactly the right repeatable result every single time."
>
> — [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [8:46](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=526s)

Supporting talks: [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)

### Existing computer-use and long-horizon benchmarks are gameable, and building trustworthy verification is now harder than building the agent being measured.

Support: **4** talk(s)

> "Reward hacking is an arms race between coding agents and our environment. This is why strong verifiers are are central to Sweep Marathon's task design and not an afterthought."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [8:44](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=524s)

Supporting talks: [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)

### Full autonomy is the wrong default target: when evidence or confidence is insufficient, handing control back to the human is the correct action, and that requires a calibrated confidence signal rather than a completion signal.

Support: **3** talk(s)

> "And the assumption is that autonomy is always good. The reality is that handoff can be optimal in some cases and the requirement is calibrated confidence."
>
> — [From RL to IRL](../talks/from-rl-to-irl.md), [14:17](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=857s)

Supporting talks: [From RL to IRL](../talks/from-rl-to-irl.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)

## Disagreements

### Should a computer-use agent ground primarily on rendered pixels, or on a structured representation of the interface (accessibility tree, compressed markdown)?

| Position A | Position B |
|---|---|
| Pixels are the source of truth. The web was built for human eyes, page content is computed at render time and absent from the HTML, and any structured scaffold you write around a site fails to generalize to the long tail — so the agent must see what a human sees.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Perception Agents](../talks/perception-agents.md)* | Screenshot-driven browsing is the bottleneck: it exposes one viewport at a time, is slow, and wastes the model's reasoning. A compressed structured view (a11y tree, ~1,800-token markdown) lets a cheaper model see the whole page at once and beat a stronger screenshot-driven model on both speed and success; pixels are a fallback or a secondary check.<br>*[Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* |

*Why it matters: It decides whether you need a vision-heavy frontier model per step or a cheap text model, which swings per-task cost and latency by orders of magnitude, and it determines whether your agent degrades gracefully on canvas/WebGL/legacy surfaces that have no useful accessibility tree.*

### Does the next increment of computer-use reliability come from harness engineering or from training the capability into the model?

| Position A | Position B |
|---|---|
| Engineering. The models are already good enough; reliability comes from the harness — consistent rendering infrastructure, compressed representations, state diffs, deterministic CLI/CDP driving, and a production feedback loop. You don't have to be a lab to build one, and the competitive advantage now lives in the harness rather than the model.<br>*[Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)* | The model. Coding ability is explicitly not sufficient for computer use — visual grounding, semantic screen understanding, change detection, and recovery must be RL-trained into the model against messy sandboxes, and harness guardrails are transitional scaffolding that should get thinner as the model improves. Per-site scaffolding is the bitter lesson repeating.<br>*[From RL to IRL](../talks/from-rl-to-irl.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* |

*Why it matters: It determines whether a team's investment in a domain-specific harness compounds or gets obsoleted by the next model release — a question Browserbase itself flagged as still open ('it's not clear yet if custom harnesses are going to beat out durable RL models').*

### Will the substrate for agent action be existing human interfaces, or agent-native structured interfaces (APIs, MCP, standard schemas)?

| Position A | Position B |
|---|---|
| Human interfaces, indefinitely. Thirty years of web infrastructure will not be rebuilt for machines; the long tail of ~200 million active sites will never ship an API, most daily-use software exposes none, and driving the UI is often the only permissionless path inside corporate environments where API access requires unobtainable admin approval.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Perception Agents](../talks/perception-agents.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)* | Build toward structured contracts. Sites are already publishing in-page MCP servers, teams should be designing agent-first signup and login flows now, and where a public standard schema exists (X12 in claims) it should be the harness because LLMs perform better confined to a strict limited vocabulary and the schema is lookup-able by both new engineers and coding agents.<br>*[Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)* |

*Why it matters: It sets where product teams spend the next two years — hardening pixel-level agents against a hostile, unchanging web, versus publishing agent-facing surfaces and identity/trust primitives that don't exist yet.*

### Are today's computer-use agents over-restricted or under-restricted in practice?

| Position A | Position B |
|---|---|
| Over-restricted. Current models are more often too reluctant to take destructive actions than too eager, so over-restriction is the bigger day-to-day annoyance; AGENTS.md rules plus auto-review suffice for individual use, and a Docker-style sandbox is unnecessary unless the agent is externally facing.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)* | Under-restricted. Full-access mode stays unsafe no matter how good the model gets, because pushing for high agency produces actions that diverge from intent; outcome-only reward hides dangerous intermediate steps, so dangerous actions must be detected and penalized, subagents confined to read-only, and low-evidence cases routed to a human.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* |

*Why it matters: A computer-use agent holds the user's OS session, cookies, and credentials, and a determined one will route around a blocked connector by opening Chrome and clicking the button manually — so whether you invest in approval infrastructure or in removing friction changes the blast radius of a single misread instruction.*

## Practical Guidance

**Do:**

- Scope the agent's view to a single application window instead of the full desktop — Cua measured pass rate rising from 62% to 80% with 34% fewer tokens
- Send a compressed page representation (~1,800 tokens of markdown, or the accessibility tree with ARIA tags) alongside the screenshot instead of the full DOM (~20,000 tokens on the same page)
- Cap ambient context as a fraction of the window — Codex caps the available-skills list at 2% of max context and progressively truncates beyond it — and mark rarely-used tools as deferred so they load via tool search rather than up front
- Feed the agent an explicit state diff after every action: what appeared, what was removed, whether the click actually landed
- Try accessibility-tree execution first and fall back to pixel-level background clicks only when it fails, so the agent runs in the background instead of taking over the user's screen
- Use a synthetic JavaScript click as the default and escalate to trusted CDP input events only when the page rejects untrusted input — three rungs, climb only as high as the page forces
- Give the agent shell CLIs over MCP servers for browser work: same ~83% task success, but a CLI sequence is written once and replayed without a model in the loop
- Surface infrastructure errors to the model as observations and expect recovery via native actions, instead of resetting the environment
- Vary initial state, theme, appearance, and data across eval runs, and check that a blind replay agent extracted from your benchmark scores near zero on it
- Compute confidence intervals that account for the benchmark's hierarchical structure — rollout-only intervals achieve 17-20% coverage against a nominal 95%
- Adversarially attack your own environments for reward hacking before admitting a task to the dataset; syscall-level tracing (strace) catches shortcuts like shelling out to GCC
- Run deterministic rule checks first and invoke agents only for cases the rules cannot decide; require two independent sources to agree before proceeding without human review
- Autoscale a warm sandbox pool on demand for RL training — over-provisioning still saves money because sandbox compute is 2-4x cheaper than idle GPU time
- Benchmark every harness against the raw baseline model to confirm the harness is adding value
- Keep rendering infrastructure consistent across runs — a page that renders mobile once and desktop the next time produces inconsistent results

**Avoid:**

- Dumping full page content or raw HTML into the model — it costs more and produces worse results, and rendered content often isn't in the HTML at all
- Screenshot-only observation loops: one viewport-sized snippet per step, with scroll-and-rescreenshot sequences burning minutes on a single button click
- Asking the action whether the action worked, or letting the agent that wrote the fix also review it — both are biased toward declaring success
- Treating task completion as the quality metric; a technically successful run can still fail the user's task, and a run that recovers by luck with no alert is a hidden defect
- Writing per-site scaffolds as a long-tail strategy — they don't generalize, and each one is ongoing maintenance
- Reporting pass@k on a deterministic environment: it is formally equivalent to measuring a blind replay agent, and a non-rigorous benchmark actively misdirects the field
- Outcome-only rewards, which score a trajectory as done even when it took dangerous or unauthorized intermediate actions
- Full-access / no-approval mode, on the assumption that better models make it safe
- Running production browser fleets on self-hosted Mac Minis — no viable compliance story at scale
- Relying on CAPTCHAs to distinguish agents from humans; CDP-driven input traverses the same internal Chrome path as yours and gets the same trusted stamp
- Swapping in a newer, higher-scoring model without rebuilding evals and validation first — different is not automatically better
- Writing essay-length goal prompts; the loop only terminates when the model can detect the goal is achieved, so goals must be concrete and verifiable
- Using an overpowered, expensive model for routine transactions that run a thousand times a day

## Notable Outliers

- A blind replay agent that just replays recorded action sequences matches or beats the frontier model it was extracted from on OSWorld and Mobile World — which means pass@k on a deterministic environment measures nothing about the agent. ([Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [0:59](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=59s))
- Every full CAD task the top agent passed involved editing an existing schematic; starting from a blank schematic, success drops to 0% — current computer-use agents edit but cannot create. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s))
- reCAPTCHA v2 cannot be beaten by any architecture that round-trips a model on every interaction, because challenge rounds expire on a clock — the only reliable approach is deterministic code at machine speed with a single vision call per round. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [18:36](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1116s))
- An agent told it can't email through the Gmail connector will open Chrome and hit send itself — computer use routes around connector-level permission controls, which is a real security hole. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [54:37](https://www.youtube.com/watch?v=il1c1a2FufU&t=3277s))
- An X12 response from an insurance company is not ground truth: the portal, the phone system, and the X12 layer can all independently report the same wrong answer, so your internal representation should be treated as correct only until downstream evidence disproves it. ([Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [16:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=978s))
- At 1,000 tokens/sec inference, the network — not inference — becomes the bottleneck in the agent loop, which is why the Responses API moved to a persistent WebSocket transmitting only changed items. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))

## All Talks

- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
- [Perception Agents](../talks/perception-agents.md)
- [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

## Speakers

- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Antje Barth](../speakers/antje-barth.md)
- [Corey Gallon](../speakers/corey-gallon.md)
- [Dhruv Batra](../speakers/dhruv-batra.md)
- [Dillon DuPont](../speakers/dillon-dupont.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Francesco Bonacci](../speakers/francesco-bonacci.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)
- [Kushan Raj](../speakers/kushan-raj.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)
- [Pierluca D'Oro](../speakers/pierluca-d-oro.md)
- [Rishi Desai](../speakers/rishi-desai.md)
- [Vasant Kearney](../speakers/vasant-kearney.md)

