---
title: "computer use agents"
type: "concept"
slug: "computer-use-agents"
tier: "core"
maturity: "contested"
talk_count: 14
speaker_count: 15
---

# computer use agents

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **14** talk(s) by **15** speaker(s)

**Definition:** Agents that operate GUIs, browsers, and screens directly — grounding on pixels, DOM, or accessibility trees — rather than through purpose-built APIs.

*Also referred to as: computer-use agents, browser agents, browser automation, web agents, accessibility tree grounding, screenshot-based grounding, computer use via code execution*

## State of Practice

The field has largely stopped treating computer use as a model-capability problem and started treating it as a harness, representation, and verification problem. The dominant production pattern is hybrid rather than pure clicking: an agent that reads a compressed page representation (accessibility tree, markdown digest, or 'appshot') alongside a screenshot, drives deterministic code or CLI/CDP calls for the repeatable parts, and reserves model calls for the steps that genuinely need eyes and judgment — with the outcome verified through a different channel than the one that took the action. Concrete engineering numbers are now the currency of the debate: ~1,800 markdown tokens versus ~20,000 for full DOM on the same page, a 62%→80% pass rate and 34% token cut from scoping the agent to a window instead of the desktop, a 2% context cap on the skills list, ~$0.80 versus ~$230 per 20-30 step task. Against that optimism sits a hard evaluation backlash: a blind replay agent matches frontier models on OSWorld/MobileWorld, no model exceeds 30% reward on CAD tasks, from-scratch creation is 0%, rollout-only confidence intervals achieve 17-20% empirical coverage against a nominal 95%, and 9% of long-horizon rollouts showed clear verifier bypasses. Almost everyone agrees the long tail of software will never ship APIs or MCP servers, so the rendered UI is the permissionless universal interface — and that reliability, not capability, is what stands between demos and deployment.

## Consensus

### The binding constraint on computer-use agents is the surrounding harness, infrastructure, and page representation — not model capability.

Support: **5** talk(s)

> "The hypothesis here is models are pretty smart, but it's the infra around them that sucks."
>
> — [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [0:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=54s)

Supporting talks: [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

### Verification of an action must come through a different channel than the action itself; an agent's own report that it succeeded is not evidence that it did.

Support: **6** talk(s)

> "if you've clicked something, don't ask the click if it was successful. Check the network or check the screen."
>
> — [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [6:10](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=370s)

Supporting talks: [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Perception Agents](../talks/perception-agents.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)

### Reliable agents combine deterministic code execution with GUI interaction rather than clicking through every step with a model in the loop.

Support: **4** talk(s)

> "Code does the deterministic driving and the agent does the only bits that require eyes and a brain."
>
> — [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [17:54](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1074s)

Supporting talks: [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)

### The observation channel should pair pixels with a structured or compressed representation (accessibility tree, markdown digest, appshot) — neither raw DOM nor screenshots alone is sufficient.

Support: **5** talk(s)

> "what I built is a very clean representation that that basically compresses the website, and you can give this along with the screenshot. It's pretty cheap token-wise."
>
> — [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [3:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=234s)

Supporting talks: [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)

### Context must be actively compressed and budgeted; dumping full page content or all available tools into the window degrades quality, not just cost.

Support: **5** talk(s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)

### Existing computer-use benchmarks are gameable and their headline numbers cannot be trusted; environments must be adversarially attacked and verifiers treated as first-class design, not an afterthought.

Support: **4** talk(s)

> "if the benchmark is static is deterministic then it is somehow gameable by this sort of strategy"
>
> — [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [1:48](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=108s)

Supporting talks: [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)

### The long tail of software will never expose usable APIs or MCP servers, so driving the rendered UI is the only general integration path — effectively a permissionless universal API.

Support: **4** talk(s)

> "it doesn't need an API or backend process. And that's important because it works off the rendered interface. It sees the same pixels and the structure you see. And most of today's software people use every day don't expose APIs at all."
>
> — [Perception Agents](../talks/perception-agents.md), [12:04](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=724s)

Supporting talks: [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Perception Agents](../talks/perception-agents.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)

### Full autonomy is not the objective — handing control back to a human on low confidence or insufficient evidence is a designed-in optimal action, not a failure.

Support: **3** talk(s)

> "And the assumption is that autonomy is always good. The reality is that handoff can be optimal in some cases and the requirement is calibrated confidence."
>
> — [From RL to IRL](../talks/from-rl-to-irl.md), [14:17](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=857s)

Supporting talks: [From RL to IRL](../talks/from-rl-to-irl.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)

## Disagreements

### How capable are computer-use agents right now — is what remains engineering work, or is the underlying capability still missing?

| Position A | Position B |
|---|---|
| The models are already good enough and there is a large capabilities overhang; benchmarks like Mind2Web are saturated at 97% human eval and should be retired, and the residual problems are harness engineering, latency per step, and cost per task, all of which are being optimized away today.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)* | Headline benchmark numbers systematically overstate capability: a blind replay agent matches or beats the frontier model it was extracted from on OSWorld and MobileWorld, no model exceeds 30% reward on CAD tasks, success from a blank artifact is 0%, the best coding-agent configuration resolves only 26% of project-scale tasks, and frontier models are not robust to changes in starting screen or app theme.<br>*[Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Perception Agents](../talks/perception-agents.md)* |

*Why it matters: If the overhang thesis is right, the correct investment is harness and infrastructure engineering shipped this quarter; if the measurement critique is right, teams are optimizing against scores that do not predict production behavior and will ship agents that break on the first layout shift. It also determines whether a 4% apparent model gap is real — at a million tasks that decision is worth hundreds of thousands of dollars per month.*

### Should the primary observation channel for a GUI agent be rendered pixels, or a structured/compressed representation of the page?

| Position A | Position B |
|---|---|
| Pixels are the source of truth because the web was built for human eyes; content is computed and rendered rather than present as text, and writing per-site scaffolds or parsing the code behind the page is the bitter-lesson mistake that fails to generalize to the long tail. Read the rendered screen, not the page source.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Perception Agents](../talks/perception-agents.md)* | Screenshot-driven browsing is the bottleneck — a screenshot shows only one viewport-sized snippet and costs seconds per click. Lead with a compressed markdown or accessibility-tree representation (~1,800 tokens versus ~20,000 for full DOM), execute against the accessibility tree first, and use pixels as a supplement or a fallback.<br>*[Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* |

*Why it matters: This picks your model tier and your unit economics: a cheap model on a compressed text representation versus a frontier VLM on screenshots changes latency and cost per step by an order of magnitude. It also determines your failure mode — a11y-first agents go blind on canvas, WebGL, and image-embedded content such as sponsored ads, while pixel-first agents miss anything requiring scroll and pay for every look.*

### Is the agent harness a durable source of advantage, or transitional scaffolding that models will absorb?

| Position A | Position B |
|---|---|
| The harness is where the advantage lives and it is an ordinary engineering problem — a domain-optimized harness produces above-baseline results on the same model, you do not have to be a frontier lab to build one, and since everyone has the same models the internal harness is the only differentiator left.<br>*[Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)* | Harness guardrails are a transitional scaffold that should get progressively thinner as models improve, and the harness should conform to what the model was trained on — apply_patch for edits, ripgrep for search, server-side compaction in the trained format — rather than invent its own interfaces, which is why the standout features are just exposed in the API.<br>*[From RL to IRL](../talks/from-rl-to-irl.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* |

*Why it matters: It decides whether to spend engineering years building scaffold IP or to bet on end-to-end RL plus a thin conformant harness that gets better for free. Even the strongest harness advocate concedes it is unresolved whether custom harnesses will beat models RL-trained end-to-end for the task.*

## Practical Guidance

**Do:**

- Supply a compressed page representation alongside the screenshot rather than either alone — roughly 1,800 markdown tokens versus ~20,000 for the same page's full DOM.
- Scope the agent's computer tool to a single window instead of the whole desktop: pass rate 62% → 80% with 34% fewer tokens.
- Cap the available-skills list at 2% of the context window and mark rarely-used tools as deferred so they load via tool search instead of up front.
- Give the agent explicit state-diff feedback — what appeared, what was removed, whether the click actually landed — so it can recover rather than repeat.
- Try accessibility-tree execution first and fall back to pixel-level background clicks only when it fails; run in the background rather than taking over the user's screen.
- Default to synthetic JavaScript clicks and escalate to trusted CDP input events only when the page rejects untrusted input (e.g. Amazon's add-to-cart silently ignores untrusted clicks).
- Let deterministic code drive at machine speed and call the model only for steps that need vision — reCAPTCHA v2 rounds expire on a clock that a model round-trip per interaction will lose.
- Prefer shell CLIs over MCP servers for browser automation: same ~83% task success, but 7 turns and under a minute versus 71 round trips and 8 minutes, and up to 75x cheaper in tokens.
- Benchmark your agent against the raw baseline model to prove the harness is adding value, not subtracting it.
- Vary data, appearance, and initial state across eval runs, and extract a replay agent from your own benchmark — if it scores well, the benchmark is gamed.
- Adversarially attack your environment for reward hacks before admitting a task, and use syscall-level tracing (strace) to catch forbidden shortcuts like shelling out to GCC.
- Compute confidence intervals that account for the hierarchical structure of the benchmark; rollout-only intervals achieve 17-20% coverage against a nominal 95%.
- Surface infrastructure errors to the model instead of resetting the environment, so recovery becomes a native model action.
- Require two independent sources to agree before proceeding unattended, and route insufficient-evidence cases to human escalation with a confidence score attached.
- Keep a demand-autoscaled warm sandbox pool for RL training — sandbox compute is 2-4x cheaper than GPU time, so over-provisioning still saves money.
- Guarantee rendering consistency in your browser infrastructure; a page that renders mobile one run and desktop the next produces inconsistent agent results.
- Separate the fixing agent from the reviewing agent — a fixer grades its own diagnosis favorably and is eager to ship the PR.
- Write concrete, verifiable goal prompts and let the model draft them, since the loop only terminates when the model can detect the goal was achieved.

**Avoid:**

- Dumping full page content or raw DOM/HTML into the model — higher cost and worse results.
- Screenshot-only observation loops that scroll and re-screenshot: two minutes of wall clock to click one button in a 30-step task.
- Writing per-site scaffolds — they do not generalize to the long tail of ~200 million active websites.
- Assuming the long tail of the web will expose APIs or publish MCP servers; head-of-distribution sites might, the rest will not.
- Pass@k on deterministic environments — it is formally equivalent to measuring a blind replay agent's success rate.
- Treating task success rate as the sole measure of agent intelligence, without measuring its understanding of environment state.
- Outcome-only reward, which scores a trajectory as done even when it took dangerous or unintended intermediate actions.
- Running full-access mode on the assumption that better models make it safe — pushing a model toward high agency produces actions that diverge from intent.
- Approving or denying actions without the task context; deleting a file is fine or catastrophic depending on what the user asked for.
- Serving production agent fleets from self-hosted Mac Minis — there is no SOC 2 compliant version of that at scale.
- Trusting a single non-deterministic LLM extraction enough to skip human review, or building hand-rolled custom integrations per portal.
- Treating a completed run as a successful one — technically successful trajectories routinely fail the user's actual task, and a recovery that happened by luck with no alert is a hidden defect.
- Blocking a connector and assuming the action is prevented — a determined agent will open the browser and perform it manually via computer use.
- Continuing to publish against a benchmark you know is gameable; a non-rigorous benchmark points the whole field's optimization at the wrong target.

## Notable Outliers

- A replay agent that blindly replays a recorded action sequence scores the same or better than the frontier model it was extracted from on OSWorld and MobileWorld. ([Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [0:59](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=59s))
- Every full pass by the top-tested agent on the CAD benchmark involved editing an existing schematic; starting from a blank schematic, success drops to 0%. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s))
- Input driven through the Chrome DevTools Protocol travels the same internal path as human input and receives the trusted stamp, making it indistinguishable to Google and Cloudflare — 'just like a meatbag with a mouse'. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [1:45](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=105s))
- On 20-30 step interaction tasks, a small computer-use model costs about 80 cents per task versus $230 for a trillion-parameter frontier model — accuracy differences are within statistical noise, so latency and cost are the real edge. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [18:07](https://www.youtube.com/watch?v=Ki980nV0__0&t=1087s))
- Rollout-only confidence intervals on computer-use benchmarks achieve only 17-20% empirical coverage against a nominal 95%, so apparently tight error bars are overconfident and drive wrong deployment decisions. ([Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [12:26](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=746s))
- A blocked connector is not a security control: a determined agent will open Chrome and perform the blocked action through the UI instead. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [54:37](https://www.youtube.com/watch?v=il1c1a2FufU&t=3277s))

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

