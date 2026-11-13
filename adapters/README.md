# Using the skill with different tools

The rules live in two source files:

- `SKILL.md` + `references/`: the full skill, for tools that load skill folders.
- `PROMPT.md` / `PROMPT-short.md`: self-contained prompts for anything else.

The files in `adapters/` (except this README and `claude-code/`) are generated from `PROMPT.md` by `scripts/build_adapters.py`. Do not edit them by hand.

Tool file formats change. The paths below were checked against each tool's documentation on 2026-11-13 except where marked; confirm them against your tool's current docs.

| Tool | What to use | Where it goes |
| --- | --- | --- |
| Claude Code | The whole repository as a skill | `~/.claude/skills/ececs-academic-english/` (personal) or `.claude/skills/ececs-academic-english/` (project). See [claude-code/README.md](claude-code/README.md). |
| OpenAI Codex | The whole repository as a skill (`SKILL.md` + `agents/openai.yaml`) | Current docs list `~/.agents/skills/` (user) and `.agents/skills/` (repository). Older versions used `~/.codex/skills/`. |
| Any agent that reads `AGENTS.md` | [agents-md/AGENTS.md](agents-md/AGENTS.md) | Copy to your project root as `AGENTS.md`, or append its content to an existing one. |
| Gemini CLI | [gemini/GEMINI.md](gemini/GEMINI.md) | `~/.gemini/GEMINI.md` (all projects) or `GEMINI.md` in a project. Gemini CLI can also be configured to read `AGENTS.md`. |
| GitHub Copilot | [copilot/copilot-instructions.md](copilot/copilot-instructions.md), or the path-specific [copilot/academic-english.instructions.md](copilot/academic-english.instructions.md) | `.github/copilot-instructions.md`, or `.github/instructions/academic-english.instructions.md` (applies to `.md`, `.txt`, `.tex` and `.rst` files) |
| Cursor | [cursor/academic-english.mdc](cursor/academic-english.mdc) | `.cursor/rules/academic-english.mdc`. *Not verified against current Cursor docs; check the rules page if it is not picked up.* |
| Chat apps (ChatGPT, Claude.ai, Gemini, DeepSeek, Kimi, Qwen, …) | `PROMPT.md` or `PROMPT-short.md` | Paste into custom instructions, project instructions or a custom GPT/Gem, or at the start of a chat. Apps that accept uploaded skills can use the repository folder instead. |
| API / own scripts | `PROMPT.md` | Use as the system prompt. |
