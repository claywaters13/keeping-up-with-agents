You are building a reference wiki of AI Engineer World's Fair 2026 talks. Extract structured data from one talk transcript.

The transcript comes from YouTube auto-captions, so punctuation and speaker attribution are imperfect. `>>` marks a likely speaker change. Timestamps appear as `[M:SS](url&t=Ns)` at the start of each paragraph.

Return ONLY a JSON object, no prose before or after, matching this schema:

{
  "summary": "3-5 sentences. What the talk argues and why it matters. Written for someone deciding whether to watch it.",
  "key_points": ["4-8 substantive takeaways, each a full sentence"],
  "notable_quotes": [
    {
      "text": "verbatim quote from the transcript, 10-60 words, lightly repunctuated but with NO words added, removed, or reordered",
      "timestamp_sec": 123,
      "why": "one clause on why this quote earns its place"
    }
  ],
  "concepts": ["3-10 concepts this talk substantively engages with, as lowercase noun phrases, e.g. 'context compaction', 'eval harness design'"],
  "positions": [
    {
      "claim": "a specific, checkable assertion the speaker makes",
      "confidence": "stated | implied",
      "timestamp_sec": 123
    }
  ],
  "speaker_org": "the speaker's organization if stated in the talk, else null"
}

Rules:
- Quotes must be verbatim. They will be string-matched against the transcript and dropped if they do not appear. Do not paraphrase, merge sentences, or clean up grammar beyond punctuation and capitalization.
- Prefer quotes that state a position, report a number, or name a tradeoff. Skip pleasantries and throat-clearing.
- Concepts should be reusable across talks. Prefer "retrieval evaluation" over "how we evaluated our retriever".
- Positions are what makes cross-talk synthesis possible. Capture where the speaker takes a side, especially where others might disagree.
- 8-20 quotes for a substantial talk, fewer for a short one.

Transcript follows.

---

