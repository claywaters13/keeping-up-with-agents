You are building the canonical concept vocabulary for a linked wiki of 228 AI Engineer World's Fair 2026 talks.

Pass A extracted concepts from each talk independently, so the raw list below has heavy duplication: lexical variants ("llm-as-a-judge" / "llm as a judge" / "llm-as-judge"), near-synonyms ("agent harness design" / "harness engineering"), and over-specific one-offs ("how we evaluated our retriever at $COMPANY"). 91% of these strings appear in exactly one talk.

Your job is to propose the canonical vocabulary that every raw string will later be mapped onto. This vocabulary IS the wiki's graph: each canonical concept becomes a page linking the talks that engage it. Too many concepts and you get hundreds of stub pages and a useless graph. Too few and distinct ideas collapse into mush.

Return ONLY a JSON object, no prose before or after:

{
  "canonical": [
    {
      "concept": "lowercase noun phrase, the page title",
      "definition": "one sentence, precise enough that someone assigning a raw string to this concept knows whether it belongs",
      "aliases": ["3-8 raw strings from the list below that should map here"],
      "est_talks": 12,
      "tier": "core | supporting"
    }
  ],
  "drop_guidance": ["3-6 rules describing which raw strings should be dropped rather than mapped, with examples from the list"],
  "notes": "anything the assignment pass needs to know: ambiguous boundaries, concepts you deliberately kept separate, concepts you deliberately merged"
}

Rules:
- Target **about 120 canonical concepts**. 100-150 is acceptable. Optimize for a good graph, not for hitting a number exactly.
- A canonical concept must plausibly cover **3 or more talks**. If it can't, it belongs in the tail and should be dropped or folded into a broader parent.
- Mark `tier: "core"` for the roughly 30-40 concepts that are genuinely central to this conference — the ones a reader would browse first. Everything else is `"supporting"`.
- Concepts must be **reusable across talks**, not descriptions of one talk's work. Prefer "retrieval evaluation" over "how we evaluated our retriever".
- Keep concepts that represent a real **distinction** separate even when related. "context compaction" and "context window management" are different ideas; do not merge them just because both contain "context".
- Do NOT merge a specific technique into its parent category when the technique itself spans several talks. "llm-as-a-judge" should survive as its own concept, not dissolve into "evaluation".
- Avoid vendor and product names as concepts unless the product is genuinely the subject across multiple talks. A talk mentioning it is not the same as a talk about it.
- `est_talks` is your estimate of how many of the 228 talks will map to this concept. Use the frequency counts as a floor, not a ceiling — most singletons are variants that will fold into a head concept.
- `aliases` must be strings copied exactly from the raw list. They are examples to guide assignment, not the complete mapping.

The raw concept list follows, as `count<TAB>concept`, sorted by frequency descending. `count` is the number of talks that produced that exact string.

---

