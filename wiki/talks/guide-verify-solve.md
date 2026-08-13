---
title: "Guide, Verify, Solve"
type: "talk"
slug: "guide-verify-solve"
track: "Agentic Engineering"
org: "Sonar"
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "03l29gJXpCE"
duration_sec: 1351
word_count: 4749
speakers: ["Anirban Chatterjee"]
---

# Guide, Verify, Solve

*Program title: Guide, Verify, Solve: The Engineering Discipline Agentic Development Demands*

**Speakers:** [Anirban Chatterjee](../speakers/anirban-chatterjee.md)

**Org:** Sonar

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 22m 31s

[Watch on YouTube](https://www.youtube.com/watch?v=03l29gJXpCE)

## Summary

Anirban Chatterjee (product marketing, Sonar) argues that AI coding tools create a 'verification debt' — a gap between the quality AI produces by default and the quality high-criticality software requires — and that automated verification is the unblocker for scaling AI-driven development. He cites a Carnegie Mellon study finding AI-assisted GitHub projects showed a ~3-month productivity spike followed by a persistent increase in static analysis warnings and code complexity, and a Wharton study showing humans followed confidently-wrong AI advice nearly 80% of the time, undermining human review as a backstop. His proposed framework is ACDC (agent-centric development cycle): guide the agent with context and constraints, verify with zero-trust multi-layered automated review, then let agents solve their own issues. The talk doubles as a product tour of SonarQube, the Gitarr acquisition, Sonar Vortex (in-loop verification for agents), and a remediation agent for tech debt. Worth watching if you want a concrete argument for putting deterministic, tool-independent verification inside the agentic inner loop as well as CI/CD — but expect a substantial vendor pitch.

## Key Points

- A Carnegie Mellon study of GitHub projects found AI tooling produced a productivity spike that lasted only about three months, alongside a persistent increase in static analysis warnings and code complexity that outlasted the gains.
- The required quality bar scales with application criticality: for throwaway or internal projects the gap between AI output quality and needed quality is tolerable, but for large, long-lived, adversarially-exposed codebases it becomes verification debt that humans must close before shipping.
- Human review is a compromised backstop — a Wharton study found participants followed AI advice 92.7% of the time when it was right and nearly 80% of the time when the AI was deliberately, confidently wrong.
- Verification should be zero trust: use a different methodology to review code than the one used to write it, so that code from any human or any model gets the same auditable, algorithmic, repeatable treatment.
- Verification should be multi-layered, combining computational/static review with LLM-driven review, because no single technique catches every class of defect.
- Sonar's ACDC framework has three phases — guide (context, guardrails, constraints up front), verify (multi-layered reasoning-based review across quality, security, compliance), and solve (agents remediate their own findings and repeat the loop).
- Models differ measurably in code quality: Sonar's LLM leaderboard scores models across correctness, complexity, maintainability, reliability, and security, and the speaker claims Sonnet 4.6 is strong on correctness while Opus is preferable when maintainability, security, or lower complexity matter.
- Verification must run in both the inner agentic loop (so issues get fixed before propagating into later loops) and the outer CI/CD loop, gated by encoded quality criteria that block PRs that fail.
- Context should be selectively supplied rather than dumping the whole codebase at an agent, which otherwise thrashes, explores, and burns tokens.
- Sonar announced Sonar Vortex (in-loop agent verification) and a remediation agent for backlog tech debt as GA that week, following its acquisition of AI-code-review company Gitarr.

## Notable Quotes

> "I think this year there's really been a turning point from experimentation to engineering."
>
> — [0:01](https://www.youtube.com/watch?v=03l29gJXpCE&t=1s) &middot; *Frames the whole talk's thesis about the industry's current moment.*

> "They found that there was, in fact, a temporary spike in productivity, um but it lasted about 3 months and then it went back down."
>
> — [2:04](https://www.youtube.com/watch?v=03l29gJXpCE&t=124s) &middot; *The headline empirical claim underpinning the verification-debt argument.*

> "there was also a persistent increase in static analysis warnings and code complexity"
>
> — [2:04](https://www.youtube.com/watch?v=03l29gJXpCE&t=124s) &middot; *Names the specific mechanism behind the productivity reversal.*

> "as you move to higher levels of criticality, as you run into situations where you're supporting many, many users, it's a larger code base with many lines of code and many changes happening across that code base all the time"
>
> — [2:42](https://www.youtube.com/watch?v=03l29gJXpCE&t=162s) &middot; *States the tradeoff: quality requirements are a function of criticality, not a constant.*

> "the quality level you need is quite a bit higher than the quality level you're getting by default from these AI tools. And that's where this verification debt comes in."
>
> — [3:26](https://www.youtube.com/watch?v=03l29gJXpCE&t=206s) &middot; *Defines the talk's central coined term.*

> "They're also missing context, right? They only know what you tell it. They don't know the broader things that are happening elsewhere in the code base."
>
> — [3:58](https://www.youtube.com/watch?v=03l29gJXpCE&t=238s) &middot; *Concise statement of why model capability alone won't close the gap.*

> "We give them, you know, 4,000 or so coding tasks and we evaluate them using all of the metrics that SonarCube uses to evaluate code"
>
> — [4:59](https://www.youtube.com/watch?v=03l29gJXpCE&t=299s) &middot; *Reports the scale and method of the model leaderboard being cited.*

> "if you're requiring higher levels of maintainability or higher levels of security, if you're trying to get a lower complexity out of your code, you might benefit from switching to Opus for tasks like that"
>
> — [5:32](https://www.youtube.com/watch?v=03l29gJXpCE&t=332s) &middot; *A rare concrete, checkable model-selection recommendation grounded in their eval axes.*

> "None of these models are ever going to be perfect. You're always going to have some kind of need for verification in the loop to make sure that the code that you're getting is the code you actually want to ship."
>
> — [6:05](https://www.youtube.com/watch?v=03l29gJXpCE&t=365s) &middot; *The load-bearing position of the talk, stated flatly.*

> "while participants did follow the AI advice 92.7% of the time when the AI was correct, they unfortunately also listened to the AI nearly 80% of the time when the AI was wrong"
>
> — [6:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=395s) &middot; *The strongest number in the talk and the case against relying on human review.*

> "there's a lot of rubber stamping that I'm sure is happening in all of your organizations. It's happening everywhere. And so we need to backstop that somehow with an automated verification tool."
>
> — [7:11](https://www.youtube.com/watch?v=03l29gJXpCE&t=431s) &middot; *Names the failure mode of code review under high AI throughput.*

> "software is not provable in the same way that code is provable"
>
> — [7:58](https://www.youtube.com/watch?v=03l29gJXpCE&t=478s) &middot; *The talk's sharpest conceptual distinction, separating deterministic code from emergent system behavior.*

> "you're not going to want to use that same AI to to validate the code because you're going to want a diversity of of tools being used to make sure that you're catching all the different issues that can happen"
>
> — [9:15](https://www.youtube.com/watch?v=03l29gJXpCE&t=555s) &middot; *The zero-trust principle stated as an actionable rule about self-review.*

> "Use a different methodology to review the code that was used to write the code."
>
> — [9:49](https://www.youtube.com/watch?v=03l29gJXpCE&t=589s) &middot; *The single most portable design guideline in the talk.*

> "You need to use computational review, you also need to use LLM driven review, and everything else in between"
>
> — [10:21](https://www.youtube.com/watch?v=03l29gJXpCE&t=621s) &middot; *Defines what 'multi-layered' concretely means here.*

> "We call it ACDC, or agentic agent-centric development cycle."
>
> — [10:21](https://www.youtube.com/watch?v=03l29gJXpCE&t=621s) &middot; *Names the framework the talk title refers to.*

> "You have to manage the context window of the agent you can't just throw your entire code base at the agent up front. It's going to spend a lot of time thrashing and exploring and burning tokens while it's doing it."
>
> — [16:57](https://www.youtube.com/watch?v=03l29gJXpCE&t=1017s) &middot; *Practical context-engineering guidance with a stated cost rationale.*

> "The verification needs to run in both the inner agentic loop and also in the outer loop for CICD."
>
> — [18:11](https://www.youtube.com/watch?v=03l29gJXpCE&t=1091s) &middot; *The architectural takeaway distinguishing this from ordinary CI static analysis.*

> "We have over 7 million developers around the world using us and we analyze close to 750 billion lines of code across our solutions every single day."
>
> — [20:49](https://www.youtube.com/watch?v=03l29gJXpCE&t=1249s) &middot; *The talk's scale claim for Sonar's install base.*

> "establish some bounded autonomy guidelines for your AI agents. Give them the freedom to generate code, but also make sure that you're enforcing a centralized scheme of verification and constraints"
>
> — [21:16](https://www.youtube.com/watch?v=03l29gJXpCE&t=1276s) &middot; *The closing prescriptive stance on how much autonomy to grant agents.*

## Positions

- AI coding tools produce a productivity gain that decays after roughly three months while leaving a persistent increase in static analysis warnings and code complexity. ([2:04](https://www.youtube.com/watch?v=03l29gJXpCE&t=124s), confidence: stated)
- The quality gap between AI-generated code and required code quality is acceptable for low-criticality projects but must be closed by humans for high-criticality ones. ([2:42](https://www.youtube.com/watch?v=03l29gJXpCE&t=162s), confidence: stated)
- Human code review is an unreliable backstop because people accept confidently-wrong AI output nearly 80% of the time. ([6:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=395s), confidence: stated)
- Rubber-stamping of AI-generated code is already widespread in most organizations. ([7:11](https://www.youtube.com/watch?v=03l29gJXpCE&t=431s), confidence: implied)
- You should not use the same AI that wrote the code to validate it; verification must use a different methodology than generation. ([9:15](https://www.youtube.com/watch?v=03l29gJXpCE&t=555s), confidence: stated)
- No single verification technique suffices — computational/static and LLM-driven review must be combined. ([10:21](https://www.youtube.com/watch?v=03l29gJXpCE&t=621s), confidence: stated)
- Software, unlike code, is not provable, because requirements, scale, and user behavior create unpredictable interactions. ([7:58](https://www.youtube.com/watch?v=03l29gJXpCE&t=478s), confidence: stated)
- Verification must run inside the inner agentic loop, not only in CI/CD, so defects are fixed before propagating into subsequent loops. ([18:56](https://www.youtube.com/watch?v=03l29gJXpCE&t=1136s), confidence: stated)
- Claude Sonnet 4.6 scores well on correctness and task-solving, but Opus is the better choice when maintainability, security, or low complexity are priorities. ([5:32](https://www.youtube.com/watch?v=03l29gJXpCE&t=332s), confidence: stated)
- Dumping an entire codebase into an agent's context is counterproductive; selectively supplied context reduces thrashing and token burn. ([16:57](https://www.youtube.com/watch?v=03l29gJXpCE&t=1017s), confidence: stated)
- Organizations should standardize on a single independent multi-layered verification platform across all teams, projects, and AI coding tools to eliminate blind spots. ([21:16](https://www.youtube.com/watch?v=03l29gJXpCE&t=1276s), confidence: stated)
- Agents should be given the agency and tooling to remediate their own verification findings rather than routing every fix to a human. ([11:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=695s), confidence: stated)

## Concepts

- [agent identity and authorization](../concepts/agent-identity-and-authorization.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [automation bias](../concepts/automation-bias.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [context engineering](../concepts/context-engineering.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [legacy code migration](../concepts/legacy-code-migration.md)
- [secure code generation](../concepts/secure-code-generation.md)

