# Changelog

## 2.0.0 — 2026-11-13

Generalised the skill for written assignments and reports in any course, and for any LLM or agent.

- `SKILL.md` rewritten as tool-neutral rules, with settings, order of authority (brief → user → discipline → defaults), workflow, modes, a fixed output format and a self-check.
- New `PROMPT.md` and `PROMPT-short.md` for chat apps and APIs without skill support.
- New `adapters/` for Claude Code, Codex, AGENTS.md, Gemini CLI, GitHub Copilot and Cursor. Generated adapters are built from `PROMPT.md` by `scripts/build_adapters.py` (`--check` detects drift).
- New references: level descriptors, assignment types, discipline conventions, citations and mechanics, hedging and claim strength, word limits, common errors (including Chinese-L1 patterns) and examples.
- `references/basis-and-examples.md` split into `references/provenance.md` and `references/examples.md`.
- New `tests/` with ten cross-discipline behaviour cases.
- Explanation language now defaults to the user's language; English variety keeps the text's existing variety (British if none).
- Skill name `ececs-academic-english` kept for compatibility with existing installs.

## 1.0.0 — 2026-10-19

Initial Codex skill based on the ECECS Pro language brief.
