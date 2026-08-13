---
title: "Your LLM Stack Is a 2008 Database With Better Marketing"
type: "talk"
slug: "your-llm-stack-is-a-2008-database-with-better-marketing"
track: "Security"
org: "NVIDIA"
day: "Day 2 — Session Day 1"
room: "Track 5"
video_id: "XjI-AR4pt7Y"
duration_sec: 1236
word_count: 2770
speakers: ["Lovina Dmello"]
---

# Your LLM Stack Is a 2008 Database With Better Marketing

*Program title: Your LLM Stack Is a 2008 Database With Better Marketing: Why ML Security Is Dominated by Misconfiguration, Not Missing Features*

**Speakers:** [Lovina Dmello](../speakers/lovina-dmello.md)

**Org:** NVIDIA

**Track:** Security &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 20m 36s

[Watch on YouTube](https://www.youtube.com/watch?v=XjI-AR4pt7Y)

## Summary

Lovina Dmello, a senior software developer on NVIDIA's deep learning infrastructure team, argues that production ML security failures are overwhelmingly ordinary infrastructure mistakes rather than exotic AI attacks — the same misconfigurations the industry supposedly solved years ago. She anchors the argument in the 2023 Ray cluster exposure (thousands of dashboards and job APIs open because authentication was off by default) and an audit of 50 production ML setups where 78% had at least one critical security mistake. The talk offers three organizing ideas: misconfiguration beats missing features as the top failure mode; the defenses in research papers rarely survive contact with latency and throughput SLAs; and ML must be secured like infrastructure, not like a model. She gives a four-tier defense-in-depth map, a NIST-AI-RMF-aligned maturity model where each level is tied to an overhead budget, and a fix list covering over-privileged accounts, flat networks, and exposed secrets. Worth watching if you own ML platform or deployment security and want a prioritization argument rather than a new attack taxonomy.

## Key Points

- The 2023 Ray cluster exposure — thousands of clusters with open dashboards and job APIs, over a billion dollars of exposure — happened because authentication was off by default and nobody turned it on, not because of any novel attack.
- Moving to ML quietly broke three assumptions of the classic 2008 application model: deterministic behavior became probabilistic, fixed parameters became copyable weights that leak through the serving API, and single tenancy became shared multi-tenant GPUs.
- An audit of 50 real production ML setups found at least one critical security mistake in 78% of them, with the same three problems recurring: wide-open access controls, no separation between system components, and passwords and trained models sitting in reachable storage.
- Misconfigurations persist because protections are built by security experts for security experts and then handed to ML teams whose job is model accuracy, not infrastructure configuration.
- Security controls have measurable performance costs that determine whether they ship: basic controls like logins and input checking run under ~8% overhead, heavier workload isolation 10–20%, and real-time malicious-input detection 15–30% — the last being what researchers love most and what teams can least afford to run on every request.
- The real question for teams is not whether to apply a control but how to implement it without slowing everything down, since the same check done sloppily can double response time.
- Three gaps make the ecosystem non-production-ready: ML security tooling lags general software tooling by years, expertise is siloed between security, ML, and operations teams, and research defends against invisible perturbations while real breaches involve stolen credentials and misused access across dozens of models on shared systems.
- Dmello's maturity model ties each level to an overhead budget — under 5% is test-only, 5–10% is the production baseline, level three adds controls for regulated industries — and she claims most teams believe they are at level three while actually sitting at level one or two.
- Her forward-looking watch list is prompt injection, RAG corpus poisoning, GPU side channels from multi-tenant packing, and unverified model and add-on supply chains, offered explicitly as direction rather than settled guidance.

## Notable Quotes

> "almost everything that is breaking in the production ML security isn't some exotic AI attack. It's the same boring infrastructure mistakes that we supposedly fixed years ago."
>
> — [0:01](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1s) &middot; *The thesis of the talk, stated in one sentence.*

> "what they found out over there was there were thousands of clusters that were sitting open on the internet. What that means is the dashboards were open and there were job APIs that were open."
>
> — [0:59](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=59s) &middot; *Concrete scale of the Ray incident that anchors the argument.*

> "So, what happened was somebody just forgot to turn the default setting on while putting them into the production environment."
>
> — [2:00](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=120s) &middot; *Reduces a billion-dollar exposure to a config default.*

> "We changed everything about the stack when we moved to machine learning, but we forgot to change the security assumptions. So we are running a 2028 playbook on a 2026 system."
>
> — [4:27](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=267s) &middot; *The framing device behind the talk's title (the year is a verbal slip for 2008).*

> "if we have a perfect access control policy, it's just a decoration if the cluster underneath is wide open."
>
> — [5:56](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=356s) &middot; *States the layering priority: infrastructure failures cascade upward.*

> "the green ones, infrastructure compromise and insiders, those are exactly where the real breaches keep landing. And they are the cheapest to get wrong by accident"
>
> — [7:41](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=461s) &middot; *Names where budget should go, against the research field's focus.*

> "In 78% of them, what the researchers found out was at least one critical security mistake."
>
> — [8:32](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=512s) &middot; *The single hardest number in the talk.*

> "this production protections are built by security experts for security experts and then they get handed to the ML teams."
>
> — [9:27](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=567s) &middot; *Explains the organizational root cause rather than blaming engineers.*

> "Every control costs us something. And in ML that something is latency and throughput. The two things that SLA is made up of."
>
> — [10:15](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=615s) &middot; *Frames security as a performance-budget tradeoff, the talk's second core idea.*

> "the purple ones is catching malicious input in real time. So, this is the most expensive one. Over here, it can cost like I don't know, 15 to 30% and it's one of the thing that researchers love the most."
>
> — [11:13](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=673s) &middot; *Direct tension between what research favors and what production can afford.*

> "the guidance team actually need isn't should I do this, it's like how do I do it without slowing everything down."
>
> — [12:01](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=721s) &middot; *Reframes the practitioner question from whether to how.*

> "The security tooling for ML is years behind the rest of the software."
>
> — [12:01](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=721s) &middot; *Checkable claim about ecosystem maturity.*

> "security team don't speak ML, ML teams don't speak security, and the operation teams don't know how the model behaves."
>
> — [13:00](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=780s) &middot; *Crisp statement of the expertise-silo gap.*

> "most of teams teams believe that they are at level three, but uh they are actually either at level one or two"
>
> — [14:48](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=888s) &middot; *A self-assessment gap teams can test themselves against.*

> "the model can't reliably tell the difference between our instructions and someone else's input. So, a cleverly worded message can quickly hijack the whole system."
>
> — [17:17](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1037s) &middot; *Compact statement of why prompt injection is structural, not a bug.*

> "where we can pack multiple customers on one GPU in order to save money. That time information can leak from one customer to the other."
>
> — [18:11](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1091s) &middot; *Names the cost-driven origin of multi-tenant GPU side channels.*

> "the field has enough defenses. It just need deployable ones. The frontier isn't a new attack defense pair. It's making the existing controls run with proper production overhead."
>
> — [18:54](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1134s) &middot; *The clearest contrarian position: deployment, not discovery, is the frontier.*

> "your LLM stack really is a 2008 database with better marketing. So, secure it like a database, lock down accesses, segment the network, and protect the data at rest."
>
> — [19:45](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1185s) &middot; *The title paid off as an actionable prescription.*

## Positions

- Production ML breaches are caused overwhelmingly by ordinary infrastructure misconfiguration, not by novel adversarial or model-specific attacks. ([0:01](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1s), confidence: stated)
- The Ray cluster exposure resulted from authentication being off by default and represented over a billion dollars of exposure. ([2:00](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=120s), confidence: stated)
- An audit of 50 real production ML setups found at least one critical security mistake in 78% of them. ([8:32](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=512s), confidence: stated)
- Access control policy is worthless if the underlying cluster is exposed, so infrastructure security must be secured first. ([5:56](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=356s), confidence: stated)
- Basic security controls cost under about 8% overhead, workload isolation 10–20%, and real-time malicious input detection 15–30%. ([10:15](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=615s), confidence: stated)
- Real-time malicious-input detection is a non-starter as a blanket control because you cannot slow every request down; it should be reserved for higher-risk systems. ([11:13](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=673s), confidence: stated)
- A security control's overhead depends almost entirely on implementation quality — the same check done sloppily can double response time. ([12:01](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=721s), confidence: stated)
- ML security tooling is years behind mainstream software security tooling, which solved scanning and secrets management decades ago. ([12:01](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=721s), confidence: stated)
- Academic ML security research is misaligned with reality: it studies imperceptible input perturbations on single models while real attacks use stolen credentials and existing access against fleets on shared infrastructure. ([13:00](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=780s), confidence: stated)
- 5–10% security overhead is the minimum acceptable bar for production; under 5% is only appropriate for test environments. ([14:48](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=888s), confidence: stated)
- Most teams overestimate their security maturity, believing they are at level three when they are at level one or two. ([14:48](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=888s), confidence: stated)
- Services should require verified identity between each other rather than relying on network access as the trust boundary. ([16:30](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=990s), confidence: stated)
- Models cannot reliably distinguish operator instructions from third-party input, so prompt injection is not solvable at the model layer alone. ([17:17](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1037s), confidence: stated)
- The field already has enough defenses; the open problem is engineering them to run within acceptable production overhead. ([18:54](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1134s), confidence: stated)
- Security budget should be allocated to infrastructure compromise and insider threats rather than model-level attack research. ([18:54](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1134s), confidence: stated)
- Current defenses against prompt injection, RAG poisoning, GPU side channels, and model supply chain risk are immature and should not be treated as settled. ([18:11](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=1091s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)

