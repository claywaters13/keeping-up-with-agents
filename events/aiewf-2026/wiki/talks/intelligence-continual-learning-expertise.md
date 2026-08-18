---
title: "Intelligence + Continual Learning = Expertise"
type: "talk"
slug: "intelligence-continual-learning-expertise"
track: "Memory & Continual Learning"
org: "NeoCognition"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "I6aiEf3aEFQ"
duration_sec: 1183
word_count: 2714
speakers: ["Yu Su"]
---

# Intelligence + Continual Learning = Expertise

**Speakers:** [Yu Su](../speakers/yu-su.md)

**Org:** NeoCognition

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 19m 43s

[Watch on YouTube](https://www.youtube.com/watch?v=I6aiEf3aEFQ)

## Summary

Yu Su argues that the striking gap between agents' success at coding and their brittleness everywhere else is a modern Moravec's paradox: frontier models have plenty of raw intelligence but almost no expertise. He distinguishes intelligence — reasoning through unfamiliar problems from available context, episode by episode — from expertise, the accumulated, situated competence that lets an expert see a domain's deep structure, know which context matters, and compress the search space instead of brute-forcing it. Because the digital world is millions of idiosyncratic 'microworlds' rather than one uniform environment, no monolithic pretrained model can encode the needed expertise; agents must learn continually on the job. He defines continual learning as 'adaptive compression of experience into reusable structures for future behavior,' plots intelligence and expertise as orthogonal axes where the CL algorithm sets the slope, and floats the provocative goal of 'unbounded expertise from bounded intelligence' — the idea that past some intelligence threshold, better learning algorithms matter more than bigger models. Worth watching as a conceptual frame for why agent deployments stall outside coding, though it is a position talk with no benchmarks or system details.

## Key Points

- Coding became the first mass market for language agents because code is a language-native world where state, structure, and rewards (tests) are already symbolic — a privileged environment that does not generalize to most digital work.
- The failures of agents outside coding are a modern Moravec's paradox: symbolic tasks once seen as the crown jewel of intelligence are now easy, while ordinary everyday digital work remains hard because it needs different cognitive competencies.
- Modern work is not one world but millions of microworlds — each domain, profession, company, and even each configuration of the same software has its own local physics — which is too heterogeneous and dynamic to compress into one static model.
- Intelligence is the capacity to reason through unfamiliar problems from available context, with episodes independent of one another; expertise is accumulated, situated competence that acts reliably and efficiently with judgment in a particular domain.
- Expertise is not knowing more facts: it is different pattern recognition, seeing deep structure (a meeting request is a constraint optimization over authority and priorities), knowing when rules can be bent, and knowing when output is good enough — together amounting to a world model of the microworld.
- Intelligence expands the search (brute-forcing with parallel attempts) while expertise compresses it via learned shortcuts, which is why current agents are so token-inefficient that companies are scrambling to curb spend.
- Continual learning is defined as adaptive compression of experience into reusable structures for future behavior, with four axes — what experience, how compressed, into what structures, used for what — whose many instantiations explain why the field is terminologically confused.
- Plotting raw intelligence against expertise as orthogonal axes, scaling alone yields 'the world's smartest novice'; the continual learning algorithm sets the slope, opening the possibility of 'escape intelligence' where unbounded expertise comes from bounded intelligence.
- Open problems he flags: defining and measuring expertise per environment, the reliability-versus-plasticity tradeoff (humans as the existence proof), synergizing parametric and non-parametric learning, and whether specialization can feed back into better generalization.
- With public training data exhausted, the next internet-scale data opportunity is in-situ learning inside private worlds, channeled back to general models.

## Notable Quotes

> "why we are so successful at the coding agents, but they're so terrible at anything else"
>
> — [0:01](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=1s) &middot; *states the motivating puzzle the whole talk is built to answer*

> "In just under 2 years, their revenue has grown 400 times"
>
> — [2:57](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=177s) &middot; *the concrete number anchoring his claim that coding was the first mass market*

> "Coding is the really the ideal market for these language agents because code is already a language-native world. Everything is already represented symbolically"
>
> — [2:57](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=177s) &middot; *explains coding's success as an environment property, not a model property*

> "it's not going to be the year of agents, it's going to be the decade of agents because they they cannot do computer use, they don't have continual learning"
>
> — [3:46](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=226s) &middot; *invokes Andrew Ng's timeline claim and endorses it as still largely accurate*

> "I think we are actually witnessing a modern version of the Moravec's paradox"
>
> — [4:41](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=281s) &middot; *the talk's central diagnostic frame*

> "But then we still struggle with this everyday digital work because they really require quite different set of cognitive competencies to excel at them"
>
> — [4:41](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=281s) &middot; *argues the gap is a difference in kind, not a matter of more scaling*

> "I think modern society is really not just one unified world. It's millions of these micro worlds"
>
> — [5:27](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=327s) &middot; *the structural premise behind the need for per-environment learning*

> "It's just like too heterogeneous and dynamic for any monolithic model to try to compress it into one static representation"
>
> — [5:27](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=327s) &middot; *a direct argument against the bigger-pretrained-model path*

> "For intelligence, it's the capacity to reason through unfamiliar problems from available context"
>
> — [6:17](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=377s) &middot; *the working definition the rest of the talk contrasts against*

> "Expertise is really accumulated and situated competence. It's the ability to act reliably, efficiently, and with judgment"
>
> — [6:17](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=377s) &middot; *the counterpart definition, naming reliability and efficiency as expertise properties*

> "experts don't just know more facts. They actually see the world differently"
>
> — [7:16](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=436s) &middot; *compresses the cognitive-science claim underpinning his notion of expertise*

> "I think experts effectively has have built a world model of their environments"
>
> — [8:19](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=499s) &middot; *connects expertise to the world-model framing agent builders already use*

> "intelligence tend to expand our search. Like every problem solving is a search problem. So, intelligence tend to brute force it"
>
> — [9:17](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=557s) &middot; *names the tradeoff that explains agent token inefficiency*

> "Well, expertise will actually try to compress the search space because expertise has constructed this has learned this essential shortcuts for the problem space"
>
> — [10:05](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=605s) &middot; *the efficiency payoff he claims from expertise*

> "I think continual learning is adaptive compression of experience into reusable structures for future behavior"
>
> — [10:05](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=605s) &middot; *his crisp, reusable definition of a term he calls confusing*

> "what we will get is what I call the world's smartest novice"
>
> — [12:30](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=750s) &middot; *memorable label for scaling intelligence without continual learning*

> "I think we'll find that they are largely orthogonal to each other"
>
> — [12:30](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=750s) &middot; *the orthogonality claim is the talk's key and most contestable structural assertion*

> "which I call the unbounded expertise from bounded intelligence"
>
> — [13:24](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=804s) &middot; *names the future he considers most interesting*

> "Once the raw intelligence has across a certain threshold, we don't need a stronger intelligence anymore"
>
> — [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s) &middot; *a strong, checkable prediction with direct implications for frontier scaling*

> "Reliable systems or stable systems, they resist the change. But the plastic systems likes change. So, how do we reconcile that?"
>
> — [15:56](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=956s) &middot; *states the core open tension in continual learning for agents*

> "If we can make these specialized agent work, they can learn in situ and channel back the learning to the general model"
>
> — [16:44](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=1004s) &middot; *links specialization to the post-public-data training data problem*

> "This will be a new dimension for us to scale because intelligence is already becoming abundance. The frontier models they are probably smarter than average humans. But expertise is still scarce."
>
> — [17:33](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=1053s) &middot; *the closing thesis in economic terms: scale expertise, not intelligence*

## Positions

- Coding agents succeed primarily because code is a language-native, symbolically represented environment with built-in rewards and tests, not because agents have general competence. ([2:57](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=177s), confidence: stated)
- Anthropic's revenue grew roughly 400x in under two years to about $40B, with the newest number around $60B annualized, driven largely by coding. ([2:57](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=177s), confidence: stated)
- The difficulties with computer use and continual learning that prompted Andrew Ng's 'decade of agents' remark are still largely unchanged today. ([3:46](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=226s), confidence: stated)
- No monolithic model can compress the idiosyncratic 'local physics' of millions of microworlds into one static representation, so agents must learn on the job. ([5:27](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=327s), confidence: stated)
- Intelligence and expertise are largely orthogonal capabilities, so scaling model intelligence alone does not accumulate expertise. ([12:30](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=750s), confidence: stated)
- The choice of continual learning algorithm sets the slope at which intelligence converts into expertise; weak in-context-learning approaches yield only marginal gains. ([13:24](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=804s), confidence: stated)
- Past a certain threshold of raw intelligence, further intelligence gains become unnecessary and better continual learning algorithms become the binding constraint — current frontier models may already be good enough. ([14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s), confidence: stated)
- Both parametric and non-parametric learning are required for continual learning to actually work; neither alone suffices. ([15:56](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=956s), confidence: stated)
- Public data for LLM pretraining is exhausted, and the next internet-scale data opportunity lies in private, in-situ learning within specialized environments. ([16:44](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=1004s), confidence: stated)
- Current agents' token inefficiency is a symptom of lacking expertise — without learned shortcuts they brute-force the search space. ([9:17](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=557s), confidence: implied)
- Making expertise abundant will lower friction enough to make new categories of economically unviable work worth doing. ([18:36](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=1116s), confidence: stated)

## Concepts

- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [context engineering](../concepts/context-engineering.md)
- [continual learning](../concepts/continual-learning.md)
- [small language models](../concepts/small-language-models.md)
- [token efficiency](../concepts/token-efficiency.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)
- [world models](../concepts/world-models.md)

