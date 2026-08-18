---
title: "State of Data"
type: "talk"
slug: "state-of-data"
track: "Posttraining & Midtraining"
org: "Independent / State of Data"
day: "Day 3 — Session Day 2"
room: "Track 9"
video_id: "ZyIoTOAbRfs"
duration_sec: 1102
word_count: 3365
speakers: ["Sean Cai"]
---

# State of Data

**Speakers:** [Sean Cai](../speakers/sean-cai.md)

**Org:** Independent / State of Data

**Track:** Posttraining & Midtraining &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 18m 22s

[Watch on YouTube](https://www.youtube.com/watch?v=ZyIoTOAbRfs)

## Summary

Sean Cai, an independent analyst who writes the 'State of Data' newsletter, argues that data — not compute or talent — is the underfunded leg of model improvement, and that the data supply chain is permanently unbundling from vertically integrated giants like Scale, Surge, and Remarque into specialists. He offers a vocabulary for reasoning about it: state-based versus process-based data, and 'type one' (real captured workflows) versus 'type two' (contrived, expert-manufactured examples), with the industry's dirty secret being that everyone sells type two as type one. He then gives a three-axis model of verifiability (asymmetry, veracity, proliferation) that explains why coding matured first — GitHub solved all three — and predicts which domains mature next, plus a scathing account of how contrived benchmarks are built and sold to hill-climb themselves. He shows private finance-task benchmarking where Opus 4.8 scores worse than 4.7 on some rubrics and GPT 5.5 and Opus 4.8 land within three points while failing in opposite directions. Worth watching for anyone buying eval or RL-environment data, or trying to read data-market spend as a leading indicator of lab product launches.

## Key Points

- Model improvement is a function of compute, data, and talent, and data is the underfunded leg — the imbalance shows up as exponentially rising CapEx against lagging AI revenue.
- The data supply chain is unbundling permanently rather than transitionally: specialists now beat vertically integrated giants at sourcing people, building environments, designing rewards, and running evals, and labs hedge by mandating 20-30 vendors.
- The valuable data is process-based (trajectories, reasoning traces, decision sequences), not state-based rows in an ERP, and 'type one' captured real workflows are what take a model from 20 to 80 percent while contrived 'type two' data only bootstraps early competence.
- Because the frontier moves, the only durable supply of frontier data is a live business you partner with, not a dead startup's code base.
- Verifiability decomposes into three axes — asymmetry (can the task be split into checkable steps), veracity (is there consensus on what correct means), and proliferation (does the world hand you fresh verified examples) — and GitHub scored high on all three, which is why coding matured first.
- The standard benchmark business is Goodhart's law with a profit motive: vendors cherry-pick tasks where models diverge, package them as a North Star benchmark, then sell the data to hill-climb that same benchmark.
- A single benchmark number under a single scaffold is one sample from an unmeasured distribution; cross-harness and cross-infrastructure differences drive much of the observed divergence between reported model scores.
- Data-market purchasing is a leading indicator of lab product launches — Anthropic's cybersecurity data spend in January and biological data spend in March/April preceded corresponding product releases two to three months later.
- No pioneer of an infrastructure technology has held more than 10% of the market long-run; models differ on efficiency and modality so they aren't fungible like electricity, meaning neither nationalization nor durable lock-in is the likely endgame.
- Successful data companies are quietly pivoting to enterprise and becoming 'neo labs', because once enterprises own rather than rent intelligence they need an abstraction layer — model routing, RL dataset management across base-model migrations — that does not yet exist.

## Notable Quotes

> "Data is to the white collar revolution what coal and iron basically is to the Victorian age and the information age right now."
>
> — [0:53](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=53s) &middot; *the talk's central framing in one line*

> "Specialists outcompete the giants at a lot of steps sourcing the people, building environments, designing rewards, running evals. The fragmentation I would say, is pretty permanent. It's not transitional."
>
> — [1:38](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=98s) &middot; *the load-bearing structural claim about the data supply chain*

> "vendor diversification on the scale of like 20 to 30 different vendors because they inherently distrust their ability to scale quality with quantity"
>
> — [1:38](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=98s) &middot; *a concrete number describing how labs actually behave*

> "But type one is what gets you from 20 to 80% so to say cuz the real the realism is inherited from the work itself"
>
> — [5:07](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=307s) &middot; *quantifies the payoff difference between contrived and captured data*

> "the only durable supply of it technically is a live business you partner with, not a dead startup's code bases like so many data companies out there are buying today"
>
> — [5:07](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=307s) &middot; *a direct swipe at a common data-acquisition strategy*

> "The dirty secret of the industry though is that everybody sells um type two and bills it as type one."
>
> — [5:41](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=341s) &middot; *the talk's sharpest accusation about vendor behavior*

> "The ease of training a model to do a task is proportional to how verifiable the task is."
>
> — [5:41](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=341s) &middot; *states Verifier's Law, the organizing principle for the middle of the talk*

> "let's cherry-pick the ones where the model diverged, and let's package them as a hard North Star benchmark. And then, this is the perverse part, let's sell the data to hill climb that same benchmark."
>
> — [8:11](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=491s) &middot; *names the exact mechanism behind benchmark-and-data bundling*

> "It's Goodhart's law with a profit motive. Basically, the moment your measure like becomes a target, and then the target is set by people who aren't true domain experts, it stops sort of measuring anything real."
>
> — [8:11](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=491s) &middot; *the memorable compression of the benchmark critique*

> "cross-harness differencing and cross-infrastructure differencing is the primary cause for a lot of benchmark divergences in performance"
>
> — [8:46](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=526s) &middot; *a specific technical attribution for reported score disagreements*

> "a single benchmark number under a single scaffold is like basically one sample from a distribution who's basically with nobody measured. And that's why there's so much what I call benchmark psychosis today."
>
> — [9:26](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=566s) &middot; *coins the term and states the statistical objection*

> "when you actually run these, I think you'll you'll notice very clearly Opus 4.8 is worse than 4.7 on a lot of these rubrics"
>
> — [10:13](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=613s) &middot; *a falsifiable claim about a specific model regression*

> "GPT 5.5 and Opus 4.08 score within three points on the same task."
>
> — [10:13](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=613s) &middot; *reports a number, and sets up the point that equal scores hide opposite failure modes*

> "it's basically like taking a Swiss Army knife and using the screwdriver bit to cut cheese and like concluding the knife is broken"
>
> — [10:59](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=659s) &middot; *the best analogy in the talk for single-benchmark evaluation*

> "In in January, uh Anthropic was spending a lot on cybersecurity data from new vendors."
>
> — [11:34](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=694s) &middot; *the concrete evidence for data spend as a leading indicator*

> "no pioneer of an infrastructure technology has actually held more than 10% of the market in the long run"
>
> — [14:49](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=889s) &middot; *a contestable historical claim applied to today's labs*

> "because models differ on efficiency and modality, they're not fungible like electricity. So, it's not it's not exactly leading to nationalization, but it's definitely not heading to durable lock-in either."
>
> — [15:25](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=925s) &middot; *stakes out a middle position in the model-commoditization debate*

> "I came here to give a talk on data markets. I'm here to tell you that that successful data companies nowadays are all pivoting to enterprise."
>
> — [16:05](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=965s) &middot; *the industry-structure prediction the talk builds toward*

> "if you're a researcher, stop outsourcing your definition of realism to the same vendors you buy your eval's and tasks from"
>
> — [16:48](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=1008s) &middot; *the actionable takeaway for practitioners*

> "if you're a builder, your moat's not the data, it's the sort of pipeline into real-world work"
>
> — [17:21](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=1041s) &middot; *reframes where defensibility lives in the data business*

## Positions

- Data, not compute or talent, is the underfunded input to model improvement, and the imbalance explains rising CapEx against lagging AI revenue. ([3:40](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=220s), confidence: stated)
- The fragmentation of the data supply chain away from vertically integrated giants is permanent, not a transitional phase. ([1:38](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=98s), confidence: stated)
- Essentially all data vendors sell contrived type two data while marketing it as captured type one data. ([5:41](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=341s), confidence: stated)
- The only durable source of frontier data is an ongoing partnership with a live business; buying defunct startups' codebases does not work. ([5:07](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=307s), confidence: stated)
- Coding matured as the first AI application market because GitHub happened to score high on all three verifiability axes at once. ([6:20](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=380s), confidence: stated)
- Domain maturation order is predictable from verifiability: code, then search, finance, healthcare and law, then cyber, biology, and scientific discovery, with taste last. ([7:34](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=454s), confidence: stated)
- Contrived benchmarks structurally cannot test whether a model sustains correct reasoning across a long dependent episode. ([8:46](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=526s), confidence: stated)
- Opus 4.8 performs worse than 4.7 on long-horizon finance rubrics due to over-engineered self-reflection introduced in post-training. ([10:13](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=613s), confidence: stated)
- GPT 5.5 and Opus 4.8 score within three points on the same finance task but fail in opposite directions — GPT gets arithmetic right and methodology wrong, Opus the reverse. ([10:59](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=659s), confidence: stated)
- A lab's data purchasing can be used as a two-to-three-month leading indicator of its upcoming product launches. ([12:18](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=738s), confidence: stated)
- Robotics data vendors are broadly unsophisticated and the modality question (ego vs teleop vs UMI) is unsettled, so buying there entangles you with an unsolved research problem. ([13:00](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=780s), confidence: stated)
- RL environment companies are research accelerators and a boutique industry; they are only venture-scalable via agnostic infrastructure that serves enterprise application use cases. ([13:44](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=824s), confidence: stated)
- Foundation model labs will not achieve durable lock-in, because no infrastructure pioneer has historically held more than 10% of its market long-run. ([14:49](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=889s), confidence: implied)
- Open models such as GLM 5.2 already surpass GPT on many real-world rubrics, proving application-layer companies can decouple from the model layer. ([15:25](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=925s), confidence: stated)
- Data businesses do not remain data businesses; durable value accrues to the services and application layer, so successful data companies become neo labs. ([16:48](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=1008s), confidence: stated)
- Researchers should not buy their evals and their definition of task realism from the same vendor, since that is letting the test writer grade the test. ([17:21](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=1041s), confidence: stated)

## Concepts

- [benchmark saturation](../concepts/benchmark-saturation.md)
- [model portability](../concepts/model-portability.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rubric design](../concepts/rubric-design.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)
- [verifier design](../concepts/verifier-design.md)

