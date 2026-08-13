---
title: "Autonomous Agents for Scientific Tasks"
type: "talk"
slug: "autonomous-agents-for-scientific-tasks"
org: "Radicait"
video_id: "XLEYtv3cMlw"
duration_sec: 1162
word_count: 3185
speakers: ["Sina Shahandeh"]
---

# Autonomous Agents for Scientific Tasks

**Speakers:** [Sina Shahandeh](../speakers/sina-shahandeh.md)

**Org:** Radicait

**Duration:** 19m 22s

[Watch on YouTube](https://www.youtube.com/watch?v=XLEYtv3cMlw)

## Summary

Sina Shahandeh argues that today's coding agents are already good enough at implementation but hit a hard ceiling on open-ended, long-horizon scientific problems because they run out of ideas — what he calls research taste. Using his company's work generating synthetic PET scans from CT scans, he shows how a plain Karpathy-style 'optimize this metric' loop saturates after a handful of iterations, while a human researcher would propose a structurally radical change (e.g. moving from 2.5D stacked-slice convolutions to 3D). His fix is an explicit decomposition step: have the coding agent generate a linked hierarchy of documents describing every component of the system (data, architecture, loss, metrics, scripts), then ask it to generate improvement hypotheses per component, optionally reviewed adversarially or collaboratively by a second, stronger reasoning model. He frames this as the hypothesis-generation analogue of chain-of-thought — a scaffolding trick that scales test-time compute and that better post-trained models should eventually make unnecessary. He closes by naming multimodal scientific perception as the real remaining bottleneck: no current model can reliably spot a lung nodule or judge scan registration quality, so a human still has to close the observation loop.

## Key Points

- Coding agents perform well on hill-climbing code optimization but plateau on open-ended scientific problems, whereas good and top-1% human researchers keep improving past that point.
- The bottleneck is not implementation or memory — which Shahandeh considers largely solved by organizing patterns and learning from mistakes — but generating good hypotheses.
- His concrete testbed is 'in-silico PET': training an encoder-decoder GAN to translate lung-nodule CT patches into synthetic PET scans, avoiding a slow and expensive real PET scan.
- Left to itself, an agent tweaks hyperparameters and known knobs; it will not propose a radical restructuring like switching from 2.5D channel-stacked slices to 3D convolutions.
- The core technique is an explicit decomposition step: prompt the coding agent to crawl the codebase and emit a linked multi-level document hierarchy (data, architecture, training loss, ops, metrics, peripheral scripts), viewable as an Obsidian graph.
- Given that scaffold, the agent can enumerate on the order of 100 candidate solutions by systematically modifying each component, producing a far more comprehensive search than an unstructured prompt.
- Loops should be equipped with additional skills and second models: a stronger multimodal model (e.g. Gemini) to visually QC lung masks and scan registration, and a stronger reasoning model (GPT-5.x Pro via Peter Steinberger's Oracle CLI) to generate hypotheses and critique whether each implemented change actually worked.
- The biggest remaining barrier to an autonomous 'scientist in a data center' is observation: multimodal models are not trained on scientific imagery and cannot reliably detect features like a small lung nodule.
- Shahandeh expects these hierarchy tricks to be temporary — analogous to chain-of-thought on GPT-4-era models — and to fade as models are post-trained to decompose problems themselves.

## Notable Quotes

> "for many of these coding tasks um this works very well but when the problems become very much open-ended and um sometimes a long horizon like most of the scientific task you have this case where AI agents uh usually kind of saturate to a certain level"
>
> — [0:00](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=0s) &middot; *states the central failure mode the whole talk is organized around*

> "the problem is they ran out of ideas uh or you know what people call them research taste"
>
> — [0:00](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=0s) &middot; *names the specific deficit — ideas, not execution*

> "I think what is much more difficult is it coming up with a hypothesis so how can we come up with a good hypothesis good ideas for our uh coding agents to keep improving better uh the process"
>
> — [1:19](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=79s) &middot; *explicitly ranks hypothesis generation above memory and implementation as the bottleneck*

> "we're building uh insilicopet meaning you have a CT and we want to generate um a PET PET image um a PET scan from the CT scan"
>
> — [2:56](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=176s) &middot; *grounds the abstract method in the concrete problem being solved*

> "like any other scientific task the problem is decomposing the problem entire long-term horizon two years 10 years research process into steps and each of those steps is really fundamentally are the goal are a loop"
>
> — [3:43](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=223s) &middot; *frames long-horizon science as nested loops, the structural premise of the approach*

> "if you give this to a typical ML model they would not think about it as you know go through hyperparameters or you know some sort of you know playing around with problems that it knows but it wouldn't do a very radical change"
>
> — [5:50](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=350s) &middot; *sharp characterization of the timidity of agent-proposed changes*

> "First is to decompose the problem into its subcomponents but it's an explicit act um um action."
>
> — [6:56](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=416s) &middot; *the method in one line — decomposition must be a separate explicit step*

> "coding agents can itself go in with this prompt of go in through this codebase and create this series of hyper um documents that are linked to each other"
>
> — [7:44](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=464s) &middot; *the hierarchy is cheap to produce — the agent bootstraps its own scaffold*

> "before if I just say say here's our code base and here's my objective Google optimized this process similar to what originally Carpathy's readme file in this program MD it would not it would not generate it would saturate after a while"
>
> — [9:55](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=595s) &middot; *direct comparison against the naive baseline he's arguing improves on*

> "it becomes a very much more comprehensive search because you have a scaffold that are reasoning LLM can go in and make a decision around improving each of these"
>
> — [10:45](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=645s) &middot; *explains the mechanism — the hierarchy defines a search space*

> "this loop can go much faster and much better because here we create a better hypothesis"
>
> — [11:38](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=698s) &middot; *compact statement of the claimed payoff*

> "as part of the metrics uh you can kind of call in another model that has a better multimodal capability uh to review the image"
>
> — [14:33](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=873s) &middot; *names a concrete multi-model pattern: vision model as qualitative metric*

> "to use GP5 and pro that's something we really like is Peter Spinberger's Oracle CLI which packages the code and package the data and send them to API"
>
> — [15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s) &middot; *specific tooling recommendation for routing hard reasoning to a stronger model*

> "you have the ability to go through this loop of scientific discovery with much more rigor in terms of hypothesis and and I think implementation is already quite a bit solved"
>
> — [15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s) &middot; *takes a side on which half of the research loop is still open*

> "the big thing in science is um better observations the multimodal model currently they lack very much understanding of these components"
>
> — [15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s) &middot; *identifies perception, not reasoning, as the frontier gap for science agents*

> "no LLM today is able to identify these very well because they're just not simply trained on scientific images and scientific data"
>
> — [15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s) &middot; *a falsifiable claim about current model capability with a stated cause*

> "that's I think one of the biggest bottlenecks for uh for not having a full you know scientist in a in a in a data center"
>
> — [15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s) &middot; *connects the perception gap to the broader autonomous-scientist goal*

> "going forward with the newer models that are much better post-trained to compartmentalize the problems and break down the problems. Uh we probably get need less and less of these tricks down the road"
>
> — [18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s) &middot; *unusually candid about the technique's expected shelf life*

> "that allows a very uh structured way to scale the test time compute to to generate more and more tokens on this problem"
>
> — [18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s) &middot; *reframes hierarchical decomposition as a test-time compute scaling lever*

## Positions

- Coding agents saturate at a fixed performance level on open-ended long-horizon scientific tasks, while good human researchers keep improving. ([0:00](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=0s), confidence: stated)
- The bottleneck for autonomous research is hypothesis generation, not implementation — implementation is largely solved. ([1:19](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=79s), confidence: stated)
- Memory and learning-from-mistakes limitations in coding agents are largely solved by simply organizing patterns and activity. ([1:19](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=79s), confidence: stated)
- Without explicit scaffolding, agents make incremental changes (hyperparameter tweaks) rather than radical architectural ones like moving from 2.5D to 3D convolutions. ([5:50](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=350s), confidence: stated)
- Making decomposition an explicit, separate action — producing a linked hierarchy of component documents — measurably widens the space of improvements an agent will propose. ([6:56](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=416s), confidence: stated)
- A Karpathy-style 'here's the codebase, here's the objective, optimize' prompt will saturate after a while, whereas the hierarchy-based hypothesis process does not. ([9:55](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=595s), confidence: stated)
- Routing hypothesis generation and post-implementation critique to a stronger reasoning model (GPT-5.x Pro via Oracle CLI) produces much better improvements. ([15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s), confidence: stated)
- No LLM today can reliably identify small scientific image features such as a lung nodule, because they are not trained on scientific images and data. ([15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s), confidence: stated)
- Weak scientific observation is one of the biggest barriers to a fully autonomous 'scientist in a data center'. ([15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s), confidence: stated)
- Hierarchical decomposition prompting is a temporary scaffold, analogous to chain-of-thought on GPT-4-era models, and will be needed less as models are post-trained to decompose problems themselves. ([18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s), confidence: stated)
- Fine-tuning multimodal models on scientific imagery is a major open opportunity for model builders. ([15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s), confidence: implied)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [agentic science](../concepts/agentic-science.md)
- [cross-model verification](../concepts/cross-model-verification.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [task decomposition](../concepts/task-decomposition.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)

