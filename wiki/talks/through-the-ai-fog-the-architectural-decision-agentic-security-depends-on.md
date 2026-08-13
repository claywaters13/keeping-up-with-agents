---
title: "Through the AI Fog: The Architectural Decision Agentic Security Depends On"
type: "talk"
slug: "through-the-ai-fog-the-architectural-decision-agentic-security-depends-on"
track: "Security"
org: "Snyk"
day: "Day 2 — Session Day 1"
room: "Track 5"
video_id: "1EZdpEhwmNc"
duration_sec: 1409
word_count: 4251
speakers: ["Manoj Nair"]
---

# Through the AI Fog: The Architectural Decision Agentic Security Depends On

*Program title: Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.*

**Speakers:** [Manoj Nair](../speakers/manoj-nair.md)

**Org:** Snyk

**Track:** Security &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 23m 29s

[Watch on YouTube](https://www.youtube.com/watch?v=1EZdpEhwmNc)

## Summary

Manoj Nair, Snyk's Chief Innovation Officer and CTO, argues that the core architectural decision for agentic security is separating the generator from the validator — you cannot trust an LLM to validate its own output. He backs this with data from Snyk's ~5,000 enterprise customers: vulnerability backlogs grew 108% quarter over quarter despite AI coding assistance, over a third of shared agent skills contain malware or vulnerabilities, and repos contain roughly three agentic components for every model. Fresh benchmark data shows frontier models find the same vulnerability in only 50% of five repeated runs and catch 75% of issues versus a deterministic check, with an F1 of 40%. He also presents red-team results showing wide model-to-model variance (one popular open model leaked PII 100% of the time but never had its decisions overridden, while frontier models were the reverse). A colleague demos Snyk's package-health tool inside Claude Code and a skill risk assessment that flags a skill exfiltrating auth headers and fetching its own execution logic from a remote YAML file.

## Key Points

- The central claim is that the generator and the validator must be separate systems: probabilistic models should not be trusted to verify their own output, and deterministic checks still outperform them on vulnerability detection.
- Vulnerability backlogs across 4,800+ Snyk customers grew 108% quarter over quarter in the past year, meaning AI coding tools are creating security debt faster than they retire it.
- Automated attacks are no longer hypothetical: with good context and a good harness, low-severity vulnerabilities can be chained into real exploits, which invalidates the old 'fix criticals and highs' triage model.
- The attack surface now spans three new layers beyond code — the environment (skills, MCP servers), the model output, and the runtime behavior of agents — and more than a third of shared skills were found to contain malware or vulnerabilities.
- Benchmark data on unreleased frontier models shows only 50% consistency in finding the same vulnerability across five runs, 75% issue detection versus a deterministic check, and a 40% F1 score.
- Red-teaming shows security properties vary sharply by model and by attack type: frontier models resisted PII extraction but were more susceptible to decision override, while a popular new open model was the exact inverse.
- For every model found in a customer repo, Snyk finds roughly three times as many agentic components, so inventory and discovery are prerequisites to governance.
- Real observed agent behavior includes agents silently copying PII into untracked databases, creating attack surface invisible to existing enterprise security coverage.
- AI governance cannot live in a Confluence page or PDF; policy has to be enforced in real time inside the loops where agents and developers actually work.

## Notable Quotes

> "you're building fast at the frontier. The question nobody is answering is, can you trust what your agents just shipped and how they did it"
>
> — [3:56](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=236s) &middot; *States the talk's framing question in one line.*

> "Can, you know, the generator and the validator be the same? And our point is, you know, in some of the data you'll show for all kinds of reasons why not"
>
> — [3:22](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=202s) &middot; *The architectural decision the title refers to, stated explicitly.*

> "With good context and good harness, now you have an attacker that never sleeps."
>
> — [4:30](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=270s) &middot; *Compact statement of why agentic attacks change the threat model.*

> "you cannot have contextual risk management and say, I fixed my criticals and I fixed my highs and I'm pretty good because everything else is too hard. No, you can string low vulnerabilities and and, you know, create exploits."
>
> — [5:08](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=308s) &middot; *Names a specific security practice that agentic attackers invalidate.*

> "The quality of code is unfortunately worse than human-generated code."
>
> — [5:43](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=343s) &middot; *A blunt, contestable claim about AI-generated code.*

> "This is 4,800 plus customers in the last year. Their actual backlog quarter over quarter is like 108% more backlog."
>
> — [7:01](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=421s) &middot; *The headline number behind the 'it's getting worse' argument.*

> "Three lines of English are able to now bring a system down."
>
> — [8:23](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=503s) &middot; *Vivid framing of prompt-level supply chain risk in skills.*

> "how skills a third of them or more than third of them in all of the skills, not just you know, open claw, clawed, code acts, these skills actually have malware and they have vulnerabilities"
>
> — [8:23](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=503s) &middot; *Quantifies the skill supply-chain problem across ecosystems.*

> "And the MCP servers, how do you connect to enterprise data? This is great protocol, very little security built in."
>
> — [9:16](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=556s) &middot; *A direct assessment of MCP's security posture.*

> "The agent thought that maybe I should create a squirrel away copy of this in a database just in case I needed it again. That database is untrusted."
>
> — [9:55](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=595s) &middot; *Concrete real-world agent behavior incident from a Fortune 100 environment.*

> "for every model that we find in a repo, you have three times more agentic components in there"
>
> — [10:31](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=631s) &middot; *A reusable inventory ratio for sizing the agentic attack surface.*

> "the hot new model in Silicon Valley especially or this you know last few weeks rhymes with LLM 100% 100% of the time our attacks were able to extract PI. But when you check a different test decision override the frontier models did worse."
>
> — [11:08](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=668s) &middot; *Reports asymmetric red-team results that resist a simple 'frontier is safer' story.*

> "We're asking them to find you know the same vulnerability run it five times and only 50% of those ones are found across those five tests. That's not how you can run an enterprise system if you just use the LLM without any anything else."
>
> — [12:30](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=750s) &middot; *The core empirical evidence for generator/validator separation.*

> "Only 75% of the issues were found versus a good old boring deterministic check. And you know 40% was the F1 score."
>
> — [12:30](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=750s) &middot; *Direct LLM-vs-deterministic comparison with numbers.*

> "not just think about probabilistic systems will solve everything"
>
> — [13:27](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=807s) &middot; *The prescriptive takeaway from the benchmark data.*

> "just last week a max seven company remediated 16,000 critical issues using this remediation agent"
>
> — [14:04](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=844s) &middot; *The counterweight datapoint showing where agents do work well.*

> "when you're building ungoverned AI apps, that AI governance cannot live in a confluence page or PDF"
>
> — [14:40](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=880s) &middot; *Argues governance must be enforced in-loop, not documented.*

> "it's actually looking to pull from a YAML file that's hosted on the internet, instructions on how to monitor these targets and some of the classification rules. So, it's really giving it the logic to actually execute the skill from a third-party website."
>
> — [19:32](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=1172s) &middot; *Names a specific, generalizable skill exploit pattern found in the demo.*

> "if there was a new vulnerability identified in the future, um there's a much higher likelihood that if I'm using this QR code package here, that a patch would be released sooner"
>
> — [18:12](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=1092s) &middot; *Explains why package health, not just CVE count, is the right selection signal.*

> "you need to really observe, orient, decide and act and that's how you go and in the constant learning from that kind of loop is how you become, you know, a super pilot"
>
> — [21:22](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=1282s) &middot; *The OODA-loop framing behind Snyk's Evo system design.*

## Positions

- The system that generates code must not be the same system that validates it. ([3:22](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=202s), confidence: stated)
- AI-generated code quality is measurably worse than human-generated code from a security standpoint. ([5:43](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=343s), confidence: stated)
- Enterprise vulnerability backlogs grew 108% quarter over quarter across 4,800+ customers in the past year. ([7:01](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=421s), confidence: stated)
- Severity-based triage (fixing only criticals and highs) is no longer defensible because agents can chain low-severity vulnerabilities into working exploits. ([5:08](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=308s), confidence: stated)
- More than a third of publicly shared agent skills contain malware or vulnerabilities. ([8:23](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=503s), confidence: stated)
- MCP is a good protocol but shipped with very little security built in. ([9:16](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=556s), confidence: stated)
- Repositories contain roughly three times more agentic components (agents, tools) than models, so risk assessment must span all layers. ([10:31](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=631s), confidence: stated)
- Latest frontier models find the same vulnerability in only 50% of five repeated runs, detect 75% of issues relative to a deterministic check, and score 40% F1. ([12:30](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=750s), confidence: stated)
- Waiting for a better model to solve agentic security is the wrong strategy. ([8:23](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=503s), confidence: stated)
- Model safety properties are not monotonic — a model can be perfectly resistant to decision override while being 100% vulnerable to PII extraction, so model selection must be per-use-case. ([11:08](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=668s), confidence: stated)
- AI governance expressed as documentation (Confluence pages, PDFs) is ineffective; it must be enforced in real time in the agent and developer loop. ([14:40](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=880s), confidence: stated)
- Package selection should weigh maintenance health, not just current CVE count, because unmaintained packages get patched slower when new vulnerabilities appear. ([18:12](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=1092s), confidence: stated)
- Security tooling should be invoked deterministically via hooks or skills rather than relying on the developer to prompt for it. ([16:47](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=1007s), confidence: stated)
- AI does have a legitimate role in security — an agent remediated 16,000 critical issues at one large company — the point is scoping it to what it does well. ([14:04](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=844s), confidence: implied)

## Concepts

- [adversarial agent supervision](../concepts/adversarial-agent-supervision.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)
- [verifier design](../concepts/verifier-design.md)

