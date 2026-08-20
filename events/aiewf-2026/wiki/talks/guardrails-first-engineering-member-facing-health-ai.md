---
title: "Guardrails First: Engineering Member-Facing Health AI"
type: "talk"
slug: "guardrails-first-engineering-member-facing-health-ai"
track: "AI in Healthcare"
org: "Hinge Health"
day: "Day 4 — Session Day 3"
room: "Track 7"
video_id: "YXEqC05WEI0"
duration_sec: 1309
word_count: 2847
speakers: ["Rashi Agrawal"]
---

# Guardrails First: Engineering Member-Facing Health AI

**Speakers:** [Rashi Agrawal](../speakers/rashi-agrawal.md)

**Org:** Hinge Health

**Track:** AI in Healthcare &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 21m 49s

[Watch on YouTube](https://www.youtube.com/watch?v=YXEqC05WEI0)

## Summary

Rashi Agrawal, who leads AI/ML at Hinge Health, argues that safety in member-facing healthcare AI is an architecture problem, not a prompting problem. She opens with real-world failures — a man hospitalized after an LLM told him to replace salt with sodium bromide, a Mount Sinai study finding a consumer health AI under-triaged life-threatening emergencies half the time, and ECRI naming AI chatbot misuse the #1 health technology hazard of 2026 — and treats these as the current production baseline rather than edge cases. The first half lays out three foundations: strip PHI at the pipeline boundary rather than redacting at runtime, put must-not-fail behavior in a deterministic code layer that runs above the model on every turn, and treat evaluation as continuous live-traffic scoring rather than a pre-launch gate. The second half is a five-rule decisioning framework for when architecture runs out and humans have to choose what ships — including scoring by worst plausible outcome, calibrating to revealed rather than stated risk tolerance, and verifying the judge before changing the agent. Worth watching if you ship LLM features in a regulated or high-stakes domain and need concrete structure for both the system design and the launch-day arguments.

## Key Points

- Most AI safety failures in healthcare are architectural decisions made before any token is generated, so guardrails have to be designed in rather than bolted on — HIPAA, FDA good machine learning practice, and state laws are grounding inputs to the design, not afterthoughts.
- PHI should be stripped at the pipeline boundary at ingestion, before data reaches the data lake, so that dashboards have nothing to redact; production and non-production environments stay fully separate with no pipes between them, and PHI access is gated on both role and geographic region.
- Behavior that can never be wrong belongs in a deterministic code layer that runs above the model on every turn: emergency escalation to 911/988, high-stakes intent routing, and identity verification are irreversible decisions the model should not get a vote on.
- A model is not a guardrail and neither is a model with a system prompt — the frontier labs' own authority hierarchy (root, system, developer, user, guideline) shows every layer above user is one prompt injection away from being overridden, so prompts are not a security boundary.
- Continuous evaluation should combine three signals: dozens of automated judges scoring live traffic across dimensions like clinical accuracy, escalation, drift and refusal; per-message thumbs up/down member feedback as the ground-truth signal; and random trace sampling with 100% sampling on high-stakes cases.
- Some failure classes never get prompted away to a zero rate — each fix buys less than the last — so monitoring is the first resort, and every new production failure becomes a new judge the system must be able to absorb.
- The five decisioning rules are: severity is set by the worst plausible outcome, severity is independent of who has capacity to fix it, default to the safer mistake (hold for safety bugs, ship for polish bugs), calibrate the launch bar to revealed rather than stated risk tolerance, and design for humans in the loop because interpretation doesn't scale.
- In a non-deterministic system the judge is also non-deterministic, so a score drop should first trigger the question 'is the judge right?' — fixing a judge prompt is legitimate, and judges are software that must keep evolving.

## Notable Quotes

> "We do have a lot of frontier models which are running and believe it or not, 40 million people actually use these models for triaging their health care issues."
>
> — [0:01](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1s) &middot; *Sizes the exposure that makes the rest of the talk urgent.*

> "The first independent safety test of a consumer health AI out of Mount Sinai found that this health AI is under triaging life-threatening emergency 50% of the times."
>
> — [0:50](https://www.youtube.com/watch?v=YXEqC05WEI0&t=50s) &middot; *Hard number from an outside evaluation, not a vendor claim.*

> "In February, ECRI the patient safety group that hospitals trust to rank their top risks named AI chatbot misuse as the number one health technology hazard of 2026."
>
> — [1:44](https://www.youtube.com/watch?v=YXEqC05WEI0&t=104s) &middot; *Anchors the risk framing in an institutional ranking rather than anecdote.*

> "Most AI safety failures in health care are not model failures. They are architectural decisions that were made before even a single token was generated."
>
> — [2:34](https://www.youtube.com/watch?v=YXEqC05WEI0&t=154s) &middot; *The thesis of the entire talk in two sentences.*

> "Two, deterministic rules belong above the model, not inside it. What can never be wrong cannot be left to probability."
>
> — [2:34](https://www.youtube.com/watch?v=YXEqC05WEI0&t=154s) &middot; *States the code-above-model principle as a design rule.*

> "Launch of your product is where the real risk starts, not where it ends."
>
> — [2:34](https://www.youtube.com/watch?v=YXEqC05WEI0&t=154s) &middot; *Compact argument against treating evals as a pre-launch gate.*

> "The architecture version strips PHI at the pipeline boundary. At ingestion before it ever reaches the data lake. By the time the data is stored, the PHI is gone."
>
> — [3:30](https://www.youtube.com/watch?v=YXEqC05WEI0&t=210s) &middot; *The concrete mechanism behind 'don't policy what you can architect'.*

> "You cannot slap on HIPAA on top of, you know, an underlying system or an architecture. You start with it and let the architecture grow around it."
>
> — [5:09](https://www.youtube.com/watch?v=YXEqC05WEI0&t=309s) &middot; *Names compliance as a design input rather than a review step.*

> "A model is not a guardrail. A model with a system prompt is also not a guardrail. Code that runs above the model is closer."
>
> — [6:48](https://www.youtube.com/watch?v=YXEqC05WEI0&t=408s) &middot; *Directly contradicts the common practice of encoding safety rules in system prompts.*

> "If the labs themselves don't trust the prompt as a security boundary, neither should you."
>
> — [6:48](https://www.youtube.com/watch?v=YXEqC05WEI0&t=408s) &middot; *Turns the labs' published authority hierarchy into an argument against prompt-based safety.*

> "If a member mentions self-harm, suicidal ideation, or an acute medical emergency, the system must route to 911 or 988. The model should not even see this turn."
>
> — [7:49](https://www.youtube.com/watch?v=YXEqC05WEI0&t=469s) &middot; *The sharpest concrete instance of code running before the model.*

> "Anything that touches member data has to check that the right member is at the other end. That's an authentication check. And authentication is a security bound boundary. Prompts are not."
>
> — [8:40](https://www.youtube.com/watch?v=YXEqC05WEI0&t=520s) &middot; *Applies the security-boundary argument to identity verification specifically.*

> "What actually holds up in production is judges that continuously keep scoring real conversations as they happen. Not a saved golden data set. Live traffic."
>
> — [9:41](https://www.youtube.com/watch?v=YXEqC05WEI0&t=581s) &middot; *Takes a side against static golden datasets as the primary eval mechanism.*

> "The bottleneck is not the compute, the models, the capability. It's actually having enough people to read the signal and act on it."
>
> — [11:27](https://www.youtube.com/watch?v=YXEqC05WEI0&t=687s) &middot; *Names the real scaling constraint, against the usual compute-bound framing.*

> "A new failure that you see in production simply means you now have a new judge."
>
> — [12:14](https://www.youtube.com/watch?v=YXEqC05WEI0&t=734s) &middot; *A reusable operating rule for turning incidents into monitoring.*

> "A bug that lightly annoys 100% of users is way less severe than one that could cause serious harm in 0.1% of cases."
>
> — [13:56](https://www.youtube.com/watch?v=YXEqC05WEI0&t=836s) &middot; *Makes the worst-case-over-average severity rule concrete and checkable.*

> "You never quietly downgrade a bug just because you can't get to it."
>
> — [14:54](https://www.youtube.com/watch?v=YXEqC05WEI0&t=894s) &middot; *Names the specific organizational failure mode the severity rule exists to prevent.*

> "Shipping a real safety bug is much worse than delaying for a false alarm."
>
> — [15:44](https://www.youtube.com/watch?v=YXEqC05WEI0&t=944s) &middot; *The asymmetry that justifies defaulting to hold on safety issues.*

> "Your launch bar is what your org already accepts in production, not what it says it will accept."
>
> — [16:32](https://www.youtube.com/watch?v=YXEqC05WEI0&t=992s) &middot; *Revealed vs. stated risk tolerance — the most contestable rule in the framework.*

> "Fast follows are committed debt, not an optional backlog."
>
> — [17:32](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1052s) &middot; *Reframes a near-universal shipping compromise as an obligation.*

> "In a non-deterministic system, the judge is also non-deterministic. Before you trust the score, verify the scorer."
>
> — [17:32](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1052s) &middot; *The core discipline of the LLM-judge section, stated as a rule.*

> "The rule is always ask, is the judge right before changing the agent's response? Fixing a judge prompt is not cheating. Judges are software, too."
>
> — [19:19](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1159s) &middot; *Pushes back on the instinct that editing a judge is gaming the eval.*

> "Don't policy what you can architect. Don't prompt what you can code. Don't gate what you can monitor."
>
> — [20:14](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1214s) &middot; *The talk's three architecture takeaways compressed into one memorable pattern.*

> "We are not building a generic low-stakes chatbot. We are building a system that has to be worthy of someone's health."
>
> — [21:07](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1267s) &middot; *The closing justification for accepting slower guardrails-first development.*

## Positions

- Most AI safety failures in healthcare are architectural decisions made before generation, not model failures. ([2:34](https://www.youtube.com/watch?v=YXEqC05WEI0&t=154s), confidence: stated)
- Consumer health AI under-triages life-threatening emergencies 50% of the time, per the first independent safety test out of Mount Sinai. ([0:50](https://www.youtube.com/watch?v=YXEqC05WEI0&t=50s), confidence: stated)
- ECRI named AI chatbot misuse the number one health technology hazard of 2026. ([1:44](https://www.youtube.com/watch?v=YXEqC05WEI0&t=104s), confidence: stated)
- PHI should be stripped at ingestion, at the pipeline boundary, rather than redacted at runtime when logs or dashboards are written. ([3:30](https://www.youtube.com/watch?v=YXEqC05WEI0&t=210s), confidence: stated)
- Production and non-production environments must have no data pipes between them, because a single pipe is enough to leak member data into dev. ([4:26](https://www.youtube.com/watch?v=YXEqC05WEI0&t=266s), confidence: stated)
- Engineers outside the certified geographic region should have no access to raw PHI at all. ([4:26](https://www.youtube.com/watch?v=YXEqC05WEI0&t=266s), confidence: stated)
- A system prompt is not a guardrail, because every authority layer above user is one prompt injection away from being overridden. ([6:48](https://www.youtube.com/watch?v=YXEqC05WEI0&t=408s), confidence: stated)
- Emergency escalation, high-stakes intent routing, and identity verification must be handled by deterministic code that runs before the model on every turn. ([7:49](https://www.youtube.com/watch?v=YXEqC05WEI0&t=469s), confidence: stated)
- Pre-launch eval checklists on saved golden datasets are necessary but insufficient; continuous scoring of live traffic is what holds up in production. ([9:41](https://www.youtube.com/watch?v=YXEqC05WEI0&t=581s), confidence: stated)
- Per-message thumbs up/down member feedback is the truth signal and catches tone problems that automated judges miss. ([10:35](https://www.youtube.com/watch?v=YXEqC05WEI0&t=635s), confidence: stated)
- High-stakes cases should be sampled and human-reviewed 100% of the time, with random sampling across other capabilities. ([10:35](https://www.youtube.com/watch?v=YXEqC05WEI0&t=635s), confidence: stated)
- The scaling bottleneck for safe AI is human capacity to read and act on signal, not compute or model capability. ([11:27](https://www.youtube.com/watch?v=YXEqC05WEI0&t=687s), confidence: stated)
- Some failure classes cannot be prompted away — each fix buys less, and the failure rate never reaches zero. ([12:14](https://www.youtube.com/watch?v=YXEqC05WEI0&t=734s), confidence: stated)
- Severity must be set by the worst plausible outcome rather than by frequency or average impact. ([13:56](https://www.youtube.com/watch?v=YXEqC05WEI0&t=836s), confidence: stated)
- A bug's severity is independent of who owns it, whether the team has capacity, and how hard the fix is; the only options are fix, delay, or accept with explicit sign-off. ([14:54](https://www.youtube.com/watch?v=YXEqC05WEI0&t=894s), confidence: stated)
- Under uncertainty, hold and fix safety bugs but ship polish bugs, because the cost asymmetry runs in opposite directions. ([15:44](https://www.youtube.com/watch?v=YXEqC05WEI0&t=944s), confidence: stated)
- A behavior already live in production for weeks or months without escalation or complaints cannot be called a launch blocker for a new feature. ([16:32](https://www.youtube.com/watch?v=YXEqC05WEI0&t=992s), confidence: stated)
- Fast follows are committed debt rather than optional backlog items. ([17:32](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1052s), confidence: stated)
- When a judge score drops, the first action should be verifying the judge, not changing the agent's prompts. ([18:28](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1108s), confidence: stated)
- Editing a judge prompt is legitimate engineering, not gaming the eval, because judges are software that must evolve. ([19:19](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1159s), confidence: stated)
- Building guardrails first is slower than bolting them on later, and that cost is an accepted design tradeoff for health-stakes products. ([20:14](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1214s), confidence: stated)
- The bar for safety architecture should scale with stakes — generic low-stakes chatbots do not need this apparatus. ([21:07](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1267s), confidence: implied)

## Concepts

- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [online evaluation](../concepts/online-evaluation.md)
- [output guardrails](../concepts/output-guardrails.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)

