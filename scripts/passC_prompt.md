# Pass C — Concept Synthesis

You are synthesizing what an entire conference concluded about ONE concept.

Your input (below) is a JSON payload containing:
- `concept` — the canonical concept name and its definition
- `talks` — every talk tagged with this concept. Each talk has its title, speaker(s), org, track, a YouTube base URL, its extracted `positions` (claims the speaker made, each with a `timestamp_sec`), and `quotes` (verbatim, each with a `timestamp_sec`).

These positions were extracted from talk transcripts. They are claims speakers actually made. Treat them as evidence, not as opinion to be smoothed over.

## What to produce

Return ONE JSON object, no markdown fences, with exactly these keys:

```
{
  "concept": "<the concept name, copied>",
  "state_of_practice": "<3-6 sentences: what the field actually believes about this concept as of this conference. Write for a smart practitioner who did not attend. Be specific and technical. No throat-clearing.>",
  "consensus": [
    {
      "claim": "<a position multiple speakers independently converged on>",
      "support_count": <number of DISTINCT talks supporting it>,
      "supporting_talks": ["<slug>", ...],
      "evidence_quote": "<the single best verbatim quote, copied EXACTLY from a quotes field>",
      "evidence_talk": "<slug the quote came from>",
      "evidence_timestamp_sec": <int>
    }
  ],
  "disagreements": [
    {
      "question": "<the open question, phrased neutrally as a question>",
      "position_a": "<one side, stated concretely>",
      "position_a_talks": ["<slug>", ...],
      "position_b": "<the opposing side>",
      "position_b_talks": ["<slug>", ...],
      "why_it_matters": "<1-2 sentences on what changes downstream depending on the answer>"
    }
  ],
  "practical_guidance": {
    "do": ["<specific, checkable practice speakers endorsed>", ...],
    "avoid": ["<specific failure mode or anti-pattern speakers warned about>", ...]
  },
  "notable_outliers": [
    {"claim": "<a contrarian or unusually specific claim worth remembering>", "talk": "<slug>", "timestamp_sec": <int>}
  ],
  "maturity": "<one of: settled | consolidating | contested | frontier>",
  "maturity_rationale": "<1-2 sentences justifying that label from the evidence>"
}
```

## Rules

1. **Never invent a quote.** Every string in an `evidence_quote` field must be copied character-for-character from a `quotes` entry in the input. These are verified verbatim against source captions and will be re-verified after you run. If no quote fits a consensus item, use an empty string rather than paraphrasing.
2. **Consensus requires at least 3 distinct talks.** If fewer than 3 talks agree on anything, return an empty `consensus` array. Do not manufacture agreement.
3. **Disagreements are the most valuable output.** Look hard for them. A disagreement is real when speakers make incompatible recommendations, not merely when they emphasize different things. If speakers genuinely all agree, return an empty array — but check carefully first, because unanimous agreement across 20+ independent talks is rare and usually means you have not read closely enough.
4. **Prefer specific over general.** "Cap the tool-description block at 2% of the context window" beats "manage context carefully." Generic advice is worthless here; if a position is vague, skip it in favor of one that is checkable.
5. **Attribute by slug**, exactly as given in the input. Do not invent slugs.
6. **`maturity` definitions:** `settled` = practitioners agree and the debate is over; `consolidating` = converging, with edges still argued; `contested` = credible people actively disagree on fundamentals; `frontier` = too new for consensus, mostly reports from early attempts.
7. Output raw JSON only. No markdown fences, no commentary before or after.

---

## INPUT

