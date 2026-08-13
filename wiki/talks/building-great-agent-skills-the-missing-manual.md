---
title: "Building Great Agent Skills: The Missing Manual"
type: "talk"
slug: "building-great-agent-skills-the-missing-manual"
video_id: "UNzCG3lw6O0"
duration_sec: 1243
word_count: 4204
speakers: []
---

# Building Great Agent Skills: The Missing Manual

**Speakers:** unknown / not credited

**Duration:** 20m 43s

[Watch on YouTube](https://www.youtube.com/watch?v=UNzCG3lw6O0)

## Summary

Matt Pocock (author of the popular 'Matt Pocock skills' repo) delivers a remote talk arguing that the AI coding community has entered 'skill hell': plenty of freely available agent skills, but no shared rubric for telling a good one from a bad one. He offers a four-part checklist — trigger, structure, steering, and pruning — for writing and auditing skills. The most transferable ideas are the tradeoff between model-invoked skills (context load on the agent, plus unpredictability that forces you to eval whether skills fire) and user-invoked skills (cognitive load on the user), and the 'leading words' technique, where a dense, prior-triggering phrase like 'vertical slice' is repeated through a skill and then verified by watching it appear in the agent's reasoning traces. He also explains splitting a skill into sequential skills to increase legwork by hiding future steps from the agent, and names concrete bloat failure modes: duplication, sediment, and no-ops. Practical and opinionated; worth watching if you maintain skills for yourself or an organization.

## Key Points

- There is no shared rubric for evaluating agent skills, and the talk proposes one as a four-item checklist: trigger, structure, steering, pruning.
- Every skill can be user-invoked, but only skills with a description exposed to the model are model-invocable; setting 'disable model invocation: true' hides the description from the agent.
- Model-invoked skills add context load — one description per skill in every request — while user-invoked skills add cognitive load on the operator, so neither choice is free.
- The speaker deliberately prefers user-invoked skills because model invocation is unpredictable and forces you to eval whether skills are being called at the right time, a class of problem he'd rather delete than solve.
- Skills decompose into two units — steps (the procedure) and reference (supporting material) — and the main skill.md should be kept as small as possible for maintenance, auditability, and token cost.
- Reference material used only in one branch of a skill should be moved out of skill.md and hidden behind a context pointer to an external file bundled with the skill.
- 'Leading words' — dense phrases like 'vertical slice' that trigger the model's priors — steer agent behavior better than plain instructions, and you can verify they worked by watching the agent repeat them in its thinking traces.
- Splitting a multi-step process into separate sequential skills increases legwork on the current step by hiding the future goal, which is the speaker's fix for plan mode's tendency to rush clarifying questions.
- Oversized skills are a symptom of three specific failure modes: duplication (no single source of truth), sediment (accreted contributions nobody dares delete), and no-ops (text that passes a deletion test because the agent would do it anyway).

## Notable Quotes

> "Skill hell is where you have all of these skills available, freely available, that you can download, contribute to, you can figure out on your own, but you don't really know how the pieces all work together."
>
> — [0:38](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=38s) &middot; *Names the problem the whole talk is organized around.*

> "Organizations have no way or no understanding on how to build good skills, how to take their operating procedures and turn them into things that an agent can do."
>
> — [1:07](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=67s) &middot; *Extends the problem from individual developers to org-level adoption.*

> "the thing that we're missing is we don't know what makes a skill great. We can't yet look at a skill and go, "Okay, this skill is doing these good things and these bad things." There's no shared rubric, no framework for looking at a skill and making it better."
>
> — [1:44](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=104s) &middot; *The thesis: the gap is evaluative, not technical.*

> "So, this description serves as a kind of context pointer. It sits in the agent's context pointing to another file where the agent can go if it wants more context."
>
> — [4:03](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=243s) &middot; *Defines the core mechanism reused throughout the talk.*

> "every time you add a model invoked skill into your agent's environment, it increases what I'm going to call the context load on that agent."
>
> — [5:09](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=309s) &middot; *Introduces the cost term for model invocation.*

> "So, if you have a hundred model invoked skills, that's going to be a hundred descriptions inside the context for your agent."
>
> — [5:09](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=309s) &middot; *Concretizes the scaling cost with a number.*

> "user invoked skills have a different load, which is the more user invoked skills you have, the higher cognitive load on the user."
>
> — [5:45](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=345s) &middot; *States the symmetric cost, making this a genuine tradeoff rather than a rule.*

> "Superpowers is primarily model invoked skills. It gives the agent superpowers. Whereas my skills, I much prefer to be in full control."
>
> — [5:45](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=345s) &middot; *Direct comparison to the other major skills repo, positioning both designs.*

> "every time you have a context pointer pointing from one resource to another, the model may just choose not to follow it, you know, even if it's absolutely perfect for the task, it may just choose not to invoke the skill."
>
> — [6:25](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=385s) &middot; *The reliability argument against model invocation.*

> "this unpredictability leaves people to need to eval their skills to make sure they're being called at the right time, which is really nasty and it's a problem I prefer to avoid."
>
> — [7:04](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=424s) &middot; *Frames eval burden as a design consequence you can architect away.*

> "The steps are the step-by-step procedure that the skill is going to walk through and the reference is any supporting information that helps it walk through those steps."
>
> — [7:37](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=457s) &middot; *The structural primitive the rest of the structure section builds on.*

> "Smaller skills are just easier to maintain, easier to audit, fewer words to think about. And every time you shave off a word, that is a token shaved, that multiple tokens shaved from your skills cost."
>
> — [8:54](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=534s) &middot; *Gives both the human and economic reason for minimizing skill.md.*

> "if you have reference material that's only used in one branch, then that's a candidate for being removed from the main skill.md."
>
> — [9:33](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=573s) &middot; *The actionable rule for branch-based pruning.*

> "The idea of leading words, or light vert if you like literary theory, I suppose, is that there are certain words that pack in a bunch of meaning into a very small space."
>
> — [11:57](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=717s) &middot; *Defines the talk's central steering technique.*

> "you put the leading word in the skill itself in the text, and then the agent will repeat the leading word back to itself as part of its operations, as part of its thinking tokens, and as part of its output to you."
>
> — [12:32](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=752s) &middot; *Explains the mechanism by which leading words change behavior.*

> "if you give them a big tranche of work to do, they will generally code up all of the database layer, then all of the schemas, then all of the API endpoints, then all of the front end."
>
> — [12:32](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=752s) &middot; *The concrete failure mode motivating the 'vertical slice' example.*

> "The cool thing about this technique is you can know if it's worked because you say vertical slice in your skill, and then you'll notice in the reasoning traces that it's saying, "Okay, we're going to do this as a thin vertical slice.""
>
> — [13:13](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=793s) &middot; *Offers a cheap verification signal instead of a formal eval.*

> "English is a pretty wide API in terms of different functions you can call, different things you can experiment with, and there are many leading word candidates out there."
>
> — [14:33](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=873s) &middot; *Memorable framing of prompt wording as an interface surface.*

> "what I have found in every single implementation of plan mode I've tried is that ask clarifying questions just, you know, it doesn't ever do enough legwork."
>
> — [15:12](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=912s) &middot; *A strong, checkable claim about a widely used agent feature.*

> "we have step one and step two, but the agent only sees one step at a time. So, this is a really cool technique for increasing legwork on the step that you're on by hiding the future goal, hiding the future steps."
>
> — [15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s) &middot; *States the skill-splitting technique and the reason it works.*

> "Let's imagine we have an implement skill and we have an entire paragraph of the skill that tells the agent to write a long detailed commit message. What would happen if you just deleted that paragraph? Well, the agent would probably still write a decent like long commit message."
>
> — [18:12](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=1092s) &middot; *The deletion test for no-ops, made concrete.*

> "And sediment is just a classic thing when people are working on the same set of docs, really, which is that everyone starts contributing to a shared markdown file. People add their own stuff. They don't feel brave enough to delete and modify anyone else's."
>
> — [17:38](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=1058s) &middot; *Names an org-level bloat dynamic that maintainers will recognize.*

## Positions

- There is currently no shared rubric or framework for judging whether an agent skill is good. ([1:44](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=104s), confidence: stated)
- Each model-invoked skill costs tokens on every request because its description sits permanently in the agent's context. ([5:09](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=309s), confidence: stated)
- Model-invoked and user-invoked skills have comparable costs, so choosing between them is not an easy decision. ([7:04](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=424s), confidence: stated)
- The speaker prefers user-invoked skills, accepting higher user cognitive load in exchange for eliminating invocation unpredictability. ([6:25](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=385s), confidence: stated)
- Model-invoked skills force you to run evals to confirm they fire at the right times; user-invoked skills remove that class of problem entirely. ([7:04](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=424s), confidence: stated)
- The Superpowers skill set is primarily model-invoked, whereas Matt Pocock skills are primarily user-invoked. ([5:45](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=345s), confidence: stated)
- Most skills should be composed of exactly two unit types: steps and reference material. ([7:37](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=457s), confidence: stated)
- The main skill.md file should be made as small as possible, for maintainability, auditability, and token cost. ([8:54](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=534s), confidence: stated)
- Reference material relevant to only one branch of a skill should live in an external file behind a context pointer rather than in skill.md. ([11:24](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=684s), confidence: stated)
- Agents fail to follow instructions mainly because the skill isn't using leading words consistently. ([11:57](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=717s), confidence: stated)
- A leading word is working if you can see the agent repeating it in its reasoning traces. ([13:13](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=793s), confidence: stated)
- Agents default to building layer by layer rather than seeking early feedback via a thin vertical slice. ([12:32](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=752s), confidence: stated)
- Every implementation of plan mode the speaker has tried under-invests in the clarifying-questions step because the agent can see that its goal is to produce a plan. ([15:12](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=912s), confidence: stated)
- Splitting a process into separate skills so the agent sees only one step at a time increases the legwork it does on the current step. ([15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s), confidence: stated)
- Massive skills are always a symptom of another failure mode — duplication, sediment, or no-ops — rather than a problem in themselves. ([16:23](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=983s), confidence: stated)
- Every part of a skill should have a single source of truth, with no duplication across steps or reference material. ([17:04](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=1024s), confidence: stated)
- No-ops are especially common when an agent writes your skills. ([18:12](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=1092s), confidence: stated)
- Instructions that the agent would follow anyway if deleted are no-ops and should be removed. ([18:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=1126s), confidence: implied)
- Community-authored skills should be audited with this framework before you pull them in, because they may not be any good. ([20:00](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=1200s), confidence: stated)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [context rot](../concepts/context-rot.md)
- [mechanistic interpretability](../concepts/mechanistic-interpretability.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [token efficiency](../concepts/token-efficiency.md)

