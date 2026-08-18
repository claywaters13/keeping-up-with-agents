---
title: "Can Oncology Workflows Run Without Human Touch?"
type: "talk"
slug: "can-oncology-workflows-run-without-human-touch"
track: "AI in Healthcare"
org: "Risa Labs"
video_id: "_cVfz88_j7A"
duration_sec: 1001
word_count: 2362
speakers: ["Anant Shankhdhar"]
---

# Can Oncology Workflows Run Without Human Touch?

**Speakers:** [Anant Shankhdhar](../speakers/anant-shankhdhar.md)

**Org:** Risa Labs

**Track:** AI in Healthcare &nbsp;|&nbsp; **Duration:** 16m 41s

[Watch on YouTube](https://www.youtube.com/watch?v=_cVfz88_j7A)

## Summary

Anant Shankhdhar, an AI engineer at Risa Labs, walks through how his team removed the human reviewer from oncology prior-authorization workflows — the process of getting insurers to approve cancer drugs. The system is a four-agent chain (eligibility & benefits verification, auth-status determination, medical necessity, and submission) layered on top of deterministic checks, so that agents are only invoked where rules cannot decide. The central engineering argument is that a single LLM extraction is too indeterminate to trust without review, so confidence must be manufactured by reconciling multiple independent evidence sources — patient notes, prior authorization letters, and a payer rule knowledge base built from portal checks and document extraction. Practical infrastructure details include an LLM-generated RPA config layer over a repository of reusable portal actions to avoid hand-built integrations, plus a self-healing loop that repairs broken automations during production hours. Worth watching if you care about how to stage automation in a high-stakes regulated domain: it is a concrete case study in expanding the no-touch share of a workflow rather than trying to automate it wholesale.

## Key Points

- The prior-authorization workflow decomposes into order intake, eligibility and benefits verification, drug auth-status classification (no auth required, auth on file, or auth required), and submission back to the payer.
- The team built four agents — EV, auth, medical necessity, and submission — with the medical necessity agent acting as the 'clinical brain' that reasons over patient data.
- Insurance data is scattered across dozens of portals, APIs, and documents, so a unified coverage service normalizes payer sources into a single coverage result format before a deterministic engine decides whether to continue or stop the order.
- A single LLM extraction over patient notes could not eliminate the human reviewer because notes often lacked sufficient data and LLM extraction is non-deterministic, so its outputs could not be blindly trusted.
- Confidence was raised by cross-checking the LLM's claim against independent sources: prior authorization letters for 'auth on file' cases, and a SQL-backed payer rule knowledge base for 'no auth required' cases; only concurring evidence is accepted.
- Some orders became fully no-touch because every drug on them was either already authorized or did not require authorization at all.
- Rather than hand-building custom integrations per portal, the team maintains a repository of RPA actions and uses LLM-based config generation to assemble automations, cutting development time significantly.
- Browser automations are fragile, so a self-healing loop detects and mitigates breakages during production hours to prevent run failures.
- The medical necessity agent reads patient notes and policy criteria, queries a patient medical graph of extracted biomarkers, and returns an answered questionnaire with both supportive and contradictory facts plus a confidence score — escalating only low-confidence cases to a clinician.
- The agents were generalized beyond prior authorization and now serve multiple oncology workflows.

## Notable Quotes

> "I was tasked with the with the problem to run some of these orders without any sort of human touch directly towards submission. Which means I need to confidently identify which all orders can be proceeded without any human verification and then build the entire flow for them as well."
>
> — [1:33](https://www.youtube.com/watch?v=_cVfz88_j7A&t=93s) &middot; *States the exact problem framing — confident selection of which orders qualify, not blanket automation.*

> "So, confidence is a key metric that we were working towards."
>
> — [1:33](https://www.youtube.com/watch?v=_cVfz88_j7A&t=93s) &middot; *Names the single metric the whole architecture optimizes for.*

> "one of the problems that we have here is that insurance details, insurance documents, everything is a scattered across dozens of portals, APIs, and documents. And it is difficult to find that information at one place."
>
> — [2:30](https://www.youtube.com/watch?v=_cVfz88_j7A&t=150s) &middot; *Identifies the data-fragmentation constraint that motivates the unified coverage service.*

> "we built a unified service that connects to different payer sources and gives the output in a normalized uniform format, which we can use for processing further. And we also added a deterministic decision engine to flag the cases which would not move forward"
>
> — [3:22](https://www.youtube.com/watch?v=_cVfz88_j7A&t=202s) &middot; *The core design move: normalize inputs, then let deterministic rules gate the pipeline.*

> "if we have to build this, then we will need to make custom integrations for different sorts of portals, which is not not a very scalable uh process."
>
> — [4:18](https://www.youtube.com/watch?v=_cVfz88_j7A&t=258s) &middot; *Names the scaling tradeoff that justifies LLM-generated RPA configs.*

> "we built a LLM-based config generation which performs these actions and builds the config for for a portal to run on."
>
> — [5:05](https://www.youtube.com/watch?v=_cVfz88_j7A&t=305s) &middot; *Concrete pattern — LLMs used at build time to author automation configs rather than at run time.*

> "these automations are fragile, so it may happen that they break during the run time. For this, we have a self-healing loop which identifies these cases during production hours and then mitigates them."
>
> — [5:05](https://www.youtube.com/watch?v=_cVfz88_j7A&t=305s) &middot; *Acknowledges RPA brittleness and gives the operational answer to it.*

> "LLM uh extraction is sort of an indis- uh indeter- deterministic process. That means that whatever outputs we get from here cannot be blindly tested. So, we still need a human to review all these things. It might improve the efficiency, but it will not eliminate the human."
>
> — [6:43](https://www.youtube.com/watch?v=_cVfz88_j7A&t=403s) &middot; *The pivotal negative result: single-source LLM extraction improves efficiency but cannot remove the reviewer.*

> "instead of just having one source, I have two sources that give me the same information and wherever they conquer, I can say with confidence that this drug is already been authorized."
>
> — [7:34](https://www.youtube.com/watch?v=_cVfz88_j7A&t=454s) &middot; *States the multi-source concurrence principle that underpins the no-touch decision.*

> "we use that information to build a payer rule knowledge base, which is basically a SQL database uh which was made from portal checks as well as LLM extractions."
>
> — [8:18](https://www.youtube.com/watch?v=_cVfz88_j7A&t=498s) &middot; *Specifies the second evidence source concretely, including its storage substrate.*

> "we use all this information, we reconcile the evidence, and we only extract the auth auth statuses with a higher confidence."
>
> — [8:18](https://www.youtube.com/watch?v=_cVfz88_j7A&t=498s) &middot; *Compresses the evidence-reconciliation strategy into one line.*

> "we noticed that certain orders were completely eliminate We could eliminate certain orders completely from these two type of drugs. Because it may happen that an order does not actually require require authorization at all."
>
> — [9:10](https://www.youtube.com/watch?v=_cVfz88_j7A&t=550s) &middot; *Reports the emergent win — whole orders, not just drugs, dropping out of the review queue.*

> "some decisions do actually need clinical reasoning."
>
> — [10:46](https://www.youtube.com/watch?v=_cVfz88_j7A&t=646s) &middot; *Marks the boundary where lookup and rules stop and reasoning must begin.*

> "the medical necessity agent answers simple and complex clinical questions per patient uh and attaches confidence score to any answer. So, we escalate only the ones that actually need a clinician."
>
> — [11:39](https://www.youtube.com/watch?v=_cVfz88_j7A&t=699s) &middot; *Defines the escalation policy: confidence score as the routing signal to a human expert.*

> "we query the patient medical graph, which is a graph of biomarkers that are extracted for a patient."
>
> — [12:31](https://www.youtube.com/watch?v=_cVfz88_j7A&t=751s) &middot; *Names the structured clinical representation the reasoning layer runs against.*

> "we use this thing these this information and pass it to an LLM to get an answered questioner with all the supportive and contradictory facts."
>
> — [13:13](https://www.youtube.com/watch?v=_cVfz88_j7A&t=793s) &middot; *Surfacing contradictory evidence alongside supportive is an unusual and auditable output design.*

> "for the cases we do not have this enough information, we move keep that for human escalation."
>
> — [13:13](https://www.youtube.com/watch?v=_cVfz88_j7A&t=793s) &middot; *Confirms insufficient evidence defaults to a human rather than a guess.*

> "the no touch is growing on the share of every order. So, we started with deterministic checks. Agents only for the rules that where what rules can't decide."
>
> — [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s) &middot; *The talk's thesis in one line — automation share grows incrementally, and agents are the fallback, not the default.*

> "We used multi-source of evidence to beat the single source of evidence to add confidence to our cases. We added itself healing in order to scale our RPS. And finally, we added the reasoning layer in order to deal with the cases where actually authentic authorization is required."
>
> — [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s) &middot; *Closing summary of the three techniques, useful as a portable recipe.*

## Positions

- A single LLM extraction over patient notes cannot eliminate human review — it improves efficiency but its non-deterministic outputs cannot be blindly trusted. ([6:43](https://www.youtube.com/watch?v=_cVfz88_j7A&t=403s), confidence: stated)
- Two independent sources agreeing on the same fact is sufficient grounds to proceed without human verification. ([7:34](https://www.youtube.com/watch?v=_cVfz88_j7A&t=454s), confidence: stated)
- Deterministic checks should come first, with agents reserved only for cases rules cannot decide. ([16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s), confidence: stated)
- Hand-built custom integrations per insurance portal do not scale; LLM-generated configs over a shared action repository significantly reduce development time. ([4:18](https://www.youtube.com/watch?v=_cVfz88_j7A&t=258s), confidence: stated)
- RPA automations are inherently fragile and will break at runtime, so a self-healing loop is a prerequisite for scaling them. ([5:05](https://www.youtube.com/watch?v=_cVfz88_j7A&t=305s), confidence: stated)
- Cases with insufficient evidence or low confidence should default to human escalation rather than an automated decision. ([13:13](https://www.youtube.com/watch?v=_cVfz88_j7A&t=793s), confidence: stated)
- Full no-touch automation of oncology prior authorization is achievable incrementally — the no-touch share of orders grows over time rather than arriving all at once. ([16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s), confidence: stated)
- Agents built for one workflow can be generalized to serve multiple oncology workflows without redesign. ([15:00](https://www.youtube.com/watch?v=_cVfz88_j7A&t=900s), confidence: stated)
- Presenting contradictory facts alongside supportive ones makes clinical LLM answers more trustworthy for downstream review. ([13:13](https://www.youtube.com/watch?v=_cVfz88_j7A&t=793s), confidence: implied)

## Concepts

- [citation and grounding](../concepts/citation-and-grounding.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

