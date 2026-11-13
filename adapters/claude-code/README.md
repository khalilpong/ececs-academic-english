# Claude Code

The repository root is already a valid skill folder (`SKILL.md` with `name` and `description` frontmatter, plus `references/`).

Personal install (all projects):

```bash
git clone https://github.com/khalilpong/ececs-academic-english ~/.claude/skills/ececs-academic-english
```

Project install (shared with collaborators): clone or copy into `.claude/skills/ececs-academic-english/` in the project.

Claude Code loads the skill automatically when a request matches its description, for example "polish this lab report paragraph" or "trim my essay to 2,000 words". You can also name the skill in your request. Update it with `git pull` in the skill folder.
