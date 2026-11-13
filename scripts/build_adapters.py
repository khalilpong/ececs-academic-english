#!/usr/bin/env python3
"""Generate tool-specific adapter files from PROMPT.md.

PROMPT.md is the single source for every adapter that embeds the rules, so the
adapters cannot drift from it. Edit PROMPT.md (and SKILL.md), then run:

    python3 scripts/build_adapters.py          # write adapters
    python3 scripts/build_adapters.py --check  # exit 1 if any adapter is stale
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTICE = "<!-- Generated from PROMPT.md by scripts/build_adapters.py. Edit PROMPT.md, not this file. -->"
DESCRIPTION = "Academic English editing for coursework reports and assignments in any discipline"

ADAPTERS = {
    "adapters/agents-md/AGENTS.md": "",
    "adapters/gemini/GEMINI.md": "",
    "adapters/copilot/copilot-instructions.md": "",
    "adapters/copilot/academic-english.instructions.md": (
        "---\n"
        'applyTo: "**/*.md,**/*.txt,**/*.tex,**/*.rst"\n'
        "---\n"
    ),
    "adapters/cursor/academic-english.mdc": (
        "---\n"
        f"description: {DESCRIPTION}\n"
        "globs:\n"
        "alwaysApply: false\n"
        "---\n"
    ),
}


def render(frontmatter: str, prompt: str) -> str:
    return f"{frontmatter}{NOTICE}\n\n{prompt.rstrip()}\n"


def main() -> int:
    check = "--check" in sys.argv[1:]
    prompt = (ROOT / "PROMPT.md").read_text(encoding="utf-8")
    stale = []
    for rel, frontmatter in ADAPTERS.items():
        path = ROOT / rel
        content = render(frontmatter, prompt)
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue
        if check:
            stale.append(rel)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"wrote {rel}")
    if stale:
        print("Stale adapters (run scripts/build_adapters.py):", *stale, sep="\n  ")
        return 1
    if check:
        print("All adapters are up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
