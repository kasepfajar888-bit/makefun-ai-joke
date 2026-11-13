"""make.fun ai-joke-03 entry: writes one joke about AI coding agents.

The joke is a fixed constant, so both grader runs write identical bytes.
Output goes to MAKEFUN_OUTPUT_DIR/entry.txt locally, or /output/entry.txt
in the grader (same convention as the kit starter).
"""

import os
from pathlib import Path

# Iteration 3, candidate #7 from my brainstorm: the agent explains my
# own code back to me flawlessly, then silently fixes my naming shame.
JOKE = (
    "I asked my agent to explain my own code. It did, perfectly, then quietly "
    "renamed my variables like a disappointed parent."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
