# Academic English for Coursework

**English** · [中文](#中文说明)

A writing skill for students' assignments and reports in **any course and discipline**, usable with **any LLM or agent**. It reviews, polishes, trims and explains academic English. The target is clear, natural undergraduate prose (default about IELTS 6.5–7.5 / CEFR C1), and the skill preserves your meaning, data, citations and the strength of your claims.

It is a user-made skill, not an official university or IELTS standard, and not a tool for evading AI detection. Your assignment's own rules always come first.

## Quick start

| You use | Do this |
| --- | --- |
| A chat app (ChatGPT, Claude.ai, Gemini, DeepSeek, Kimi, Qwen, …) | Paste [PROMPT.md](PROMPT.md), or the compact [PROMPT-short.md](PROMPT-short.md), into custom or project instructions, or at the start of a chat. |
| Claude Code | Clone this repository into `~/.claude/skills/ececs-academic-english/`. |
| OpenAI Codex | Install the repository folder as a skill (see [adapters](adapters/README.md) for current paths). |
| Gemini CLI, GitHub Copilot, Cursor, or any tool that reads `AGENTS.md` | Copy the matching file from [adapters/](adapters/README.md). |
| An API | Use [PROMPT.md](PROMPT.md) as the system prompt. |

Then ask, for example:

- "Polish this lab report paragraph; keep all numbers and citations."
- "Review my essay introduction only; don't rewrite it."
- "Trim this section to 800 words. Headings count, references don't."
- "Make these four group-report sections consistent."
- "Explain your changes in Chinese."

## What it does

- **Follows your brief first:** word limits and what counts, citation style, headings and language rules.
- **Modes:** light polish (default), review only, trim to a word limit, full rewrite (only on request), group-report consistency, explanation.
- **Assignment types:** lab and technical reports, design and project reports, essays, literature reviews, case-study and problem-question answers, reflections, proposals, abstracts, thesis chapters, posters.
- **Discipline-aware:** STEM, business, law, humanities, social sciences, health.
- **Protects content:** numbers, units, equations, quotations, citations, technical terms and claim strength ("must", "may", estimates, plans, conditions).
- **Never invents sources;** flags possible factual or citation problems instead of silently fixing them.
- **Output:** the revised text, a table of key changes and reasons, content flags, and word counts.

## Repository layout

```
SKILL.md            canonical, tool-neutral rules (agent skill format)
PROMPT.md           full self-contained prompt
PROMPT-short.md     compact prompt
references/         level descriptors, assignment types, disciplines, citations,
                    hedging, word limits, common errors, examples, provenance
adapters/           Claude Code, Codex, AGENTS.md, Gemini CLI, Copilot, Cursor
agents/openai.yaml  Codex interface metadata
scripts/            build_adapters.py (generates adapters from PROMPT.md)
tests/              cross-model behaviour cases
```

## Settings you can change

Say them in your request, for example "use American spelling", "target CEFR B2" or "explain in English":

- Target level (default IELTS 6.5–7.5 / CEFR C1)
- English variety (default: keep the text's own; British if none)
- Edit depth (default: light polish)
- Explanation language (default: the language you write in)
- Citation style (default: keep the text's own)

## Maintaining

1. Edit `SKILL.md` and `PROMPT.md` together so that they agree.
2. Run `python3 scripts/build_adapters.py` to regenerate adapters; `--check` reports stale ones.
3. Run the cases in [tests/](tests/README.md) on at least one model.
4. Record the change in [CHANGELOG.md](CHANGELOG.md).

## Licence

[MIT](LICENSE). You may use, adapt and share the skill, keeping the copyright notice.

---

## 中文说明

这是一个通用的学术英语写作技能，适用于**所有课程、所有学科**的书面作业和报告，并且能在**任何大模型或智能体**中使用。它可以审阅、润色、压缩和讲解学术英语，目标是清楚自然的本科学术英语（默认约 IELTS 6.5–7.5 / CEFR C1），同时保留原意、数据、引用和论断强度。

这是用户自建的技能，不是学校或 IELTS 的官方标准，也不用于规避 AI 检测。每份作业自身的要求始终优先。

### 怎么用

- **聊天应用**（ChatGPT、Claude.ai、Gemini、DeepSeek、Kimi、通义千问等）：把 [PROMPT.md](PROMPT.md) 或精简版 [PROMPT-short.md](PROMPT-short.md) 粘贴到自定义指令、项目指令或对话开头。
- **Claude Code**：把本仓库克隆到 `~/.claude/skills/ececs-academic-english/`。
- **Codex、Gemini CLI、GitHub Copilot、Cursor 及读取 `AGENTS.md` 的工具**：见 [adapters/README.md](adapters/README.md)。
- **API**：用 [PROMPT.md](PROMPT.md) 作系统提示词。

### 主要功能

- 先读作业要求：字数上限及计入范围、引用格式、标题和语言要求。
- 多种模式：轻度润色（默认）、只审阅不改写、压缩到字数上限、全面改写（需明确要求）、小组报告统一风格、讲解修改原因。
- 覆盖实验报告、设计报告、议论文、文献综述、案例分析和法律问题题、反思写作、研究计划、摘要、论文章节、海报等常见作业类型，以及理工、商科、法律、人文社科和医学健康等学科的写作惯例。
- 保留数字、单位、公式、引文、引用、专业术语和论断强度；不编造文献；对可能的事实或引用问题单独提示，而不是悄悄修改。
- 输出包括修改后的文本、主要修改及原因表、内容提示和字数统计。修改说明默认使用你提问时的语言，也可以指定。

### 可调整的设置

在请求里直接说明即可，例如“用美式拼写”“目标 CEFR B2”“用英文解释”。可以调整的有：目标水平、英语变体、修改深度、解释语言和引用格式。

### 许可协议

采用 [MIT](LICENSE) 许可：可以自由使用、修改和分享，需保留版权声明。
