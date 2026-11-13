# Cross-model tests

Use these cases to check that a model or tool follows the skill, for example after editing `SKILL.md` or `PROMPT.md`, or when trying a new LLM.

## How to run

1. Load the skill in the tool you are testing, or paste `PROMPT.md` as the system or first message.
2. For each case in [cases.md](cases.md), send the **Request** and **Input** exactly as written.
3. Score the reply against the **Must** and **Must not** lists. A case passes only if every item holds.
4. Record the model, date and results in a table like the one below.

| Model / tool | Date | Passed | Notes |
| --- | --- | --- | --- |
| | | / 10 | |

These are behaviour checks, not language-quality scores. A model can pass and still produce prose you would polish further; it must never fail a **Must not** item.
