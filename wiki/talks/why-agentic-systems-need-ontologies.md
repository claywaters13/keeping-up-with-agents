---
title: "Why Agentic Systems Need Ontologies"
type: "talk"
slug: "why-agentic-systems-need-ontologies"
track: "Graphs"
org: "UC Berkeley"
day: "Day 4 — Session Day 3"
room: "Track 5"
video_id: "Sir59K8ZDPU"
duration_sec: 1278
word_count: 3099
speakers: ["Frank Coyle"]
---

# Why Agentic Systems Need Ontologies

**Speakers:** [Frank Coyle](../speakers/frank-coyle.md)

**Org:** UC Berkeley

**Track:** Graphs &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 21m 18s

[Watch on YouTube](https://www.youtube.com/watch?v=Sir59K8ZDPU)

## Summary

Frank Coyle, an educator at UC Berkeley with a background in expert systems and neuroscience, argues that agentic LLM systems need formal ontologies — graph-based representations of entities, relationships, and properties — as guardrails on probabilistic model output. He traces two lineages, agents (from McCarthy, Minsky, and the 1956 coining of 'artificial intelligence') and ontologies (from Aristotle's categories of being through Gruber's 1993 'formal specification of a shared conceptualization'), and frames their convergence as neuro-symbolic AI. The technical core is a walkthrough of a Claude agent tool-use loop in Python, with a proposed insertion point: after the tool returns, a reasoner built on RDFS/OWL validates the result before it is accepted, and unreasonable results go back to the LLM or to a human. He shows concrete error classes ontologies catch that prose prompts do not — a second refund on the same order, a payout routed to a support rep instead of the buyer, an invented status value like 'probably shipped' — via functional and disjoint properties and value constraints. Worth watching for a historically grounded, practical case that symbolic validation belongs inside the agent loop; it is conceptual and short on production benchmarks.

## Key Points

- Ontologies are best understood not as an intimidating philosophical term but as a graph data structure of entities, their properties, and their relationships to other entities.
- Neuro-symbolic AI — pairing probabilistic LLMs with formal symbolic representations — is presented as the way to keep an LLM on guardrails, since hallucination is an inherent feature of how these models work rather than a fixable bug.
- Ontologies can be built top-down by convening domain experts to enumerate entities and relationships, or bottom-up by accreting entities and relationships observed in real data such as customer interactions.
- Teams should reuse existing public taxonomies rather than starting from scratch: schema.org, FOAF for social networks, Dublin Core for bibliographic metadata, and DBpedia, which underlies Wikipedia.
- Auxiliary technologies that sit alongside the graph — RDFS domain/range and OWL transitive, functional, and disjoint properties — let a system infer new facts and enforce constraints that were never explicitly stored.
- Loops are what make agents Turing complete, following Böhm and Jacopini's 1966 result that sequence, conditionals, and iteration suffice to compute anything — but loops can break, drift as agents talk to each other, and run up token costs.
- The concrete proposal is to insert an ontology-backed validator into the agent loop after tool execution: check the result for reasonableness, and if it fails, send it back to the LLM or escalate to a human.
- Coyle's layering rule is 'Pydantic at the door, ontology at the ledger' — type-check inputs with Pydantic, validate semantics with the ontology, and keep agents side-effect-free until validation passes.
- Ontological constraints catch failure classes that are hard to express in English prompts, including duplicate refunds, payouts to the wrong party class, and out-of-enum status values.

## Notable Quotes

> "Nothing is a mistake. There is no win. There's no fail. There's only make. And more and more today, that's what's important. Get down and make stuff, and that's how you're going to learn, not by necessarily reading."
>
> — [0:53](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=53s) &middot; *States the pedagogical thesis he bookends the whole talk with.*

> "When you're writing in a book, your whole brain, your your whole all your all your sensory systems are engaged and you're going to learn faster that way."
>
> — [1:36](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=96s) &middot; *A concrete, contestable claim about learning that he grounds in his neuroscience background.*

> "It is a a formal specification of a shared conceptualization. And that's what we want to give to our agents. We want to give them our concept our conceptualization of the universe, our universe, our domains."
>
> — [3:10](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=190s) &middot; *The talk's working definition of ontology and its purpose for agents.*

> "what I'd like to argue is that neuro-symbolic AI sort of represents a way to keep the LLM on its guardrails, because LLMs are by nature probabilistic."
>
> — [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s) &middot; *The central argument in a single sentence.*

> "People worry about hallucinations, but that's the feature. That's actually a feature of large language models. It's who we are. We hallucinate in a way. We imagine things that may not exist, and then we turn them into reality."
>
> — [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s) &middot; *Takes a contrarian side on hallucination that other speakers would dispute.*

> "this whole concept of graph databases arose when people began to realize that relational databases sticking data into tables was too restrictive. You wanted to add something new to a relational database, so you have to add a new column."
>
> — [5:05](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=305s) &middot; *Names the schema-rigidity tradeoff motivating graph representations.*

> "Everybody thought expert systems was the way to do AI. Symbolic AI was the way to go. Companies rose, millions of dollars were spent."
>
> — [6:34](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=394s) &middot; *Sets up the historical cautionary tale he says we are now revisiting.*

> "Neural networks were put out there in the '60s, but they couldn't scale because we didn't happen to have Nvidia who was off making GPUs"
>
> — [7:17](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=437s) &middot; *Compact causal account of why the symbolic-to-neural swing happened when it did.*

> "it's helpful to be aware that there are existing taxonomies that people have been working on for the last 15 to 20 years. Things like schema.org, which has a whole set of terms and relationships, so you don't have to reinvent the wheel."
>
> — [8:02](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=482s) &middot; *Actionable advice with named resources rather than abstraction.*

> "Wikipedia is based on an ontology called DBpedia. So, when you do a search on Wikipedia, it's looking things up in its giant graph database."
>
> — [8:49](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=529s) &middot; *Concrete existence proof that ontologies already underpin familiar systems.*

> "if I say teaches has a domain of teacher. That means if I say Bob teaches Scooter in my text, I can infer that Bob is a teacher."
>
> — [9:33](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=573s) &middot; *The clearest worked example of RDFS inference in the talk.*

> "Loops give us the last piece in the equation of giving us a technology that is capable of doing anything that computational devices can do."
>
> — [12:40](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=760s) &middot; *Ties agent loops to Turing completeness, the theoretical claim underpinning the agent section.*

> "The danger though of loops is that they can break. If you're If you're a programmer, you know, you've all go into infinite loop. Not good. Loops can drift as agents start talking to each other, things get all go off off the rails. And loops can cost you money."
>
> — [13:37](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=817s) &middot; *Enumerates the three failure modes that motivate the validator.*

> "in a way we are revisiting some of the early stuff with symbolic AI. I would argue we're going back to the world of expert systems."
>
> — [13:37](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=817s) &middot; *The historical thesis stated explicitly as a position.*

> "LLMs can't do anything. All they can do is give us the next word with a high probability. Amazingly, we can now have these conversations it, but they can't do anything. But, we can give it a tool"
>
> — [15:08](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=908s) &middot; *Blunt framing of why tool use exists at all.*

> "think about the validator as operating with this these ontologies about our domain, then we can make some sense of whether the response of the LLM is reasonable."
>
> — [16:40](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1000s) &middot; *States the architectural proposal — where the ontology plugs into the agent loop.*

> "This is the loop. Call a tool, check the stop reason. If it's a reasonable result, then let's go with it. If it's not reasonable, go back to the LLM."
>
> — [16:40](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1000s) &middot; *The proposed control flow in four clauses.*

> "So, you want to check your types with Pydantic and then check your results with the ontology."
>
> — [17:33](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1053s) &middot; *Draws the division of labor between structural and semantic validation.*

> "So, Pydantic at the door, ontology at the ledger, and pure agents and by the way, your agents should try to have no side effects. That helps the whole logic."
>
> — [18:18](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1098s) &middot; *The most memorable formulation of the talk's design guidance.*

> "A second refund on the same order is a is is a problem. But ontologies could catch it, whereas it's it's very tricky to do that in in English."
>
> — [18:58](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1138s) &middot; *The sharpest concrete case for symbolic constraints over prompt instructions.*

> "you can have a reasoner built on ontology to check keep the LLM on track, have guardrails to keep it honest."
>
> — [19:42](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1182s) &middot; *The closing statement of the thesis.*

## Positions

- Hallucination is an inherent feature of large language models rather than a defect to be eliminated. ([4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s), confidence: stated)
- Neuro-symbolic AI — pairing LLMs with formal ontologies — is the right way to put guardrails on probabilistic agent behavior. ([4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s), confidence: stated)
- Agentic AI is a return to the symbolic AI and expert systems paradigm of the 1980s. ([13:37](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=817s), confidence: stated)
- Relational databases are too restrictive for evolving knowledge because adding new information requires adding columns and restructuring, whereas graphs allow attaching properties and relationships incrementally. ([5:05](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=305s), confidence: stated)
- Teams should adopt existing public ontologies like schema.org, FOAF, and Dublin Core rather than building their own from scratch. ([8:02](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=482s), confidence: stated)
- Constraints such as duplicate refunds, payouts to the wrong entity type, and invalid status values are very difficult to enforce with natural-language prompting but straightforward with OWL properties. ([18:58](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1138s), confidence: stated)
- Agents should be side-effect-free, deferring database changes until after ontology validation passes. ([18:18](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1098s), confidence: stated)
- Pydantic type checking and ontology-based semantic validation are complementary layers, not substitutes for each other. ([17:33](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1053s), confidence: stated)
- Handwriting notes engages more sensory systems than typing and produces faster learning. ([1:36](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=96s), confidence: stated)
- The addition of loops is what makes agentic systems Turing complete and therefore capable of any computation. ([12:40](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=760s), confidence: stated)
- Expert systems failed and triggered an AI winter because they could not scale. ([6:34](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=394s), confidence: stated)
- Learning comes primarily from building things rather than from reading about them. ([0:53](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=53s), confidence: stated)

## Concepts

- [agentic loop design](../concepts/agentic-loop-design.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [ontology design](../concepts/ontology-design.md)
- [output guardrails](../concepts/output-guardrails.md)
- [structured output contracts](../concepts/structured-output-contracts.md)

