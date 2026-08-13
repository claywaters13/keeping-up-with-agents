---
title: "Anant Shankhdhar"
type: "speaker"
slug: "anant-shankhdhar"
talk_count: 1
---

# Anant Shankhdhar

## Talks

- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md) (AI in Healthcare)

## Concepts

- [citation and grounding](../concepts/citation-and-grounding.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

## Quotes

> "I was tasked with the with the problem to run some of these orders without any sort of human touch directly towards submission. Which means I need to confidently identify which all orders can be proceeded without any human verification and then build the entire flow for them as well."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [1:33](https://www.youtube.com/watch?v=_cVfz88_j7A&t=93s)

> "So, confidence is a key metric that we were working towards."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [1:33](https://www.youtube.com/watch?v=_cVfz88_j7A&t=93s)

> "one of the problems that we have here is that insurance details, insurance documents, everything is a scattered across dozens of portals, APIs, and documents. And it is difficult to find that information at one place."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [2:30](https://www.youtube.com/watch?v=_cVfz88_j7A&t=150s)

> "we built a unified service that connects to different payer sources and gives the output in a normalized uniform format, which we can use for processing further. And we also added a deterministic decision engine to flag the cases which would not move forward"
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [3:22](https://www.youtube.com/watch?v=_cVfz88_j7A&t=202s)

> "if we have to build this, then we will need to make custom integrations for different sorts of portals, which is not not a very scalable uh process."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [4:18](https://www.youtube.com/watch?v=_cVfz88_j7A&t=258s)

> "we built a LLM-based config generation which performs these actions and builds the config for for a portal to run on."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [5:05](https://www.youtube.com/watch?v=_cVfz88_j7A&t=305s)

> "these automations are fragile, so it may happen that they break during the run time. For this, we have a self-healing loop which identifies these cases during production hours and then mitigates them."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [5:05](https://www.youtube.com/watch?v=_cVfz88_j7A&t=305s)

> "LLM uh extraction is sort of an indis- uh indeter- deterministic process. That means that whatever outputs we get from here cannot be blindly tested. So, we still need a human to review all these things. It might improve the efficiency, but it will not eliminate the human."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [6:43](https://www.youtube.com/watch?v=_cVfz88_j7A&t=403s)

> "instead of just having one source, I have two sources that give me the same information and wherever they conquer, I can say with confidence that this drug is already been authorized."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [7:34](https://www.youtube.com/watch?v=_cVfz88_j7A&t=454s)

> "we use that information to build a payer rule knowledge base, which is basically a SQL database uh which was made from portal checks as well as LLM extractions."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [8:18](https://www.youtube.com/watch?v=_cVfz88_j7A&t=498s)

> "we use all this information, we reconcile the evidence, and we only extract the auth auth statuses with a higher confidence."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [8:18](https://www.youtube.com/watch?v=_cVfz88_j7A&t=498s)

> "we noticed that certain orders were completely eliminate We could eliminate certain orders completely from these two type of drugs. Because it may happen that an order does not actually require require authorization at all."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [9:10](https://www.youtube.com/watch?v=_cVfz88_j7A&t=550s)

> "some decisions do actually need clinical reasoning."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [10:46](https://www.youtube.com/watch?v=_cVfz88_j7A&t=646s)

> "the medical necessity agent answers simple and complex clinical questions per patient uh and attaches confidence score to any answer. So, we escalate only the ones that actually need a clinician."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [11:39](https://www.youtube.com/watch?v=_cVfz88_j7A&t=699s)

> "we query the patient medical graph, which is a graph of biomarkers that are extracted for a patient."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [12:31](https://www.youtube.com/watch?v=_cVfz88_j7A&t=751s)

> "we use this thing these this information and pass it to an LLM to get an answered questioner with all the supportive and contradictory facts."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [13:13](https://www.youtube.com/watch?v=_cVfz88_j7A&t=793s)

> "for the cases we do not have this enough information, we move keep that for human escalation."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [13:13](https://www.youtube.com/watch?v=_cVfz88_j7A&t=793s)

> "the no touch is growing on the share of every order. So, we started with deterministic checks. Agents only for the rules that where what rules can't decide."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s)

> "We used multi-source of evidence to beat the single source of evidence to add confidence to our cases. We added itself healing in order to scale our RPS. And finally, we added the reasoning layer in order to deal with the cases where actually authentic authorization is required."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s)

