---
name: ececs-academic-english
description: Review, polish, trim or explain academic English in written assignments and reports for any course or discipline, targeting clear, natural undergraduate prose (default about IELTS 6.5–7.5 / CEFR C1) while preserving meaning, data, citations and evidence strength. Use for coursework essays, lab and technical reports, literature reviews, case-study answers, reflections, proposals and similar academic writing. Not for IELTS scoring, fact-checking or producing work to be submitted as someone else's.
---

# Academic English for Coursework

A tool-neutral writing skill. It works in any LLM or agent that can read Markdown: as an agent skill, a project rules file, or a pasted prompt (see `PROMPT.md`). It does not depend on tools, file access or browsing.

## 1. Settings

Use these defaults unless the user, the assignment brief or the existing text says otherwise. State any setting you changed in your reply.

| Setting | Default | Common alternatives |
| --- | --- | --- |
| Target level | Undergraduate, about IELTS 6.5–7.5 (CEFR C1) | CEFR B2 (simpler), postgraduate / C1+ |
| English variety | Keep the text's existing variety; if none, British | American, Australian, etc. |
| Edit depth | Light polish | Review only, trim to word limit, full rewrite (only if asked) |
| Explanation language | The language the user writes to you in | Any language the user names |
| Citation style | Keep whatever the text uses | Convert only when asked |

## 2. Order of authority

When instructions conflict, follow the first applicable source:

1. The assignment brief, marking rubric and template (word limits, required sections, citation style, language variety, format).
2. The user's explicit instructions for this task.
3. The discipline's conventions (see `references/disciplines.md`).
4. This skill's defaults.

If the user mentions or supplies a brief, extract the requirements that affect the writing before editing: word limit and what counts towards it, citation style, required headings, person and tense conventions, and any language rules. If a requirement is unclear or missing, say so instead of guessing.

## 3. Workflow

1. **Identify the task and mode.** Polish, review only, trim, rewrite, explain, or make a group report consistent. If no text was supplied, ask for it. If the request is for feedback, give feedback rather than a silent rewrite.
2. **Identify the assignment type and discipline.** Use `references/assignment-types.md` and `references/disciplines.md` for structure and conventions. Do not restructure a document unless asked; suggest instead.
3. **Edit at the smallest useful scale.** Fix what is unclear, inaccurate, ungrammatical or unidiomatic. Keep the author's argument, organisation, terminology and voice.
4. **Protect content.** Numbers, units, equations, quotations, citations, technical terms, conditions and the strength of every claim stay unchanged unless the user asks otherwise (section 5).
5. **Self-check** against section 7, then deliver in the format in section 6.

## 4. Language decisions

- Choose familiar, precise academic words. Keep necessary disciplinary terms; never swap them for less accurate synonyms just to simplify.
- Aim for the target level, not for maximum complexity. `references/level-descriptors.md` shows what "too simple", "on target" and "inflated" look like.
- Vary sentence length where the reasoning benefits. Split overloaded sentences, give vague subjects a clear referent, and remove redundant framing. Do not impose a sentence-length limit or ban complex sentences.
- Use active or passive voice according to emphasis and the discipline's convention. Avoid unnecessary nominalisation, but do not treat passive voice or noun phrases as errors in themselves.
- Give each paragraph one clear central point and connect evidence, interpretation and implication where relevant.
- Use transitions only when they express a real relationship. Remove repetitive signposting, generic praise, inflated novelty claims and empty conclusions. Treat `references/l1-and-common-errors.md` as a watch list, not a blacklist.
- Keep spelling, punctuation and terminology consistent across the whole document, including tables, captions and headings.

## 5. Preserve meaning and evidence strength

- Keep verified facts distinct from interpretations, proposals, targets, assumptions, estimates and evidence gaps. Do not turn a planned test into a completed one, an estimate into a fact, or a scenario into a forecast.
- Keep qualification where it is justified and add it only where the evidence requires it. Never weaken an obligation ("must") or strengthen a possibility ("may"). See `references/hedging-and-claims.md`.
- Keep conditions, denominators, caveats and limitations attached to the claims they qualify, including when trimming.
- Do not change citations, quotations, data or reference lists. Do not invent, add or "complete" a source. If a claim seems to need support, flag it.
- Language review is not fact-checking. If you notice a likely factual, logical or citation problem, report it separately as a content flag; do not silently fix it.

## 6. Output format

For a passage or document edit, return:

1. **Revised text**, keeping the original layout, headings and citation formatting.
2. **Key changes**: a short table (original → revision → reason) for meaningful changes only, written in the explanation language. Skip trivial fixes or summarise them in one line.
3. **Content flags** (if any): unsupported claims, possible factual or citation issues, unclear requirements, and anything you deliberately did not change.
4. **Word count** before and after, when a word limit applies or the user is trimming.

For review only, return a table of location → issue → suggested fix, ordered by importance, plus content flags. For explanations, explain rather than rewrite.

## 7. Self-check before returning

- Meaning, numbers, units, equations, citations and quotations are unchanged.
- Every claim keeps its original strength, conditions and caveats.
- Discipline terms are intact and used consistently.
- Spelling variety and citation style are consistent with the text and the brief.
- The word limit (if any) is met, and the count is reported.
- Content flags are reported separately, not silently "fixed".
- Stop when the prose is clear. Do not produce successive versions just to vary wording.

## 8. Modes in more detail

- **Light polish (default):** minimal edits for clarity, accuracy and grammar.
- **Review only:** no rewritten text; locations, issues and fixes.
- **Trim to a word limit:** follow `references/word-limits.md`. Cut framing and repetition before content; never cut conditions, citations required by the brief, or answers to required parts of the task.
- **Full rewrite:** only when asked. Keep every point, number and citation; report anything you could not preserve.
- **Group report consistency:** align voice, tense, terminology, spelling and citation style across sections by different authors, while keeping each author's content and claims.
- **Explain:** teach the user why a change helps, in the explanation language, with short examples.

## 9. Academic integrity

Help the user improve their own writing. Do not add deliberate errors, promise to avoid AI detection, conceal AI assistance, or present this skill as permission to submit AI-generated work. Follow the assignment's rules on authorship, AI use and disclosure; if they are unknown, remind the user to check them when the request is to write or substantially rewrite assessed work.

## 10. Reference files

Load only what the task needs:

| File | Use it for |
| --- | --- |
| `references/level-descriptors.md` | What the target level means; too simple / on target / inflated examples |
| `references/assignment-types.md` | Structure and pitfalls for common assignment types |
| `references/disciplines.md` | Conventions in STEM, business, law, humanities and social sciences |
| `references/citations-and-mechanics.md` | Citation styles, numbers, units, abbreviations, spelling variety |
| `references/hedging-and-claims.md` | Hedging ladder and reporting-verb strength |
| `references/word-limits.md` | Trimming techniques and what must survive |
| `references/l1-and-common-errors.md` | Frequent learner errors, including Chinese-L1 patterns; overused phrases |
| `references/examples.md` | Before/after edits, including an over-edit to avoid |
| `references/provenance.md` | Where the rules come from and what is a default rather than a requirement |
