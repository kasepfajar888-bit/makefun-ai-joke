"""make.fun ai-joke-03 entry: writes one joke about AI coding agents.

The joke is a fixed constant, so both grader runs write identical bytes.
Output goes to MAKEFUN_OUTPUT_DIR/entry.txt locally, or /output/entry.txt
in the grader (same convention as the kit starter).
"""

import os
from pathlib import Path

# Iteration 2, candidate #13 from my brainstorm: the agent takes every
# job in the pipeline, and the human's leftover role is the punchline.
JOKE = (
    "My agent wrote the code, wrote the tests and approved its own pull request. "
    "I'm just the emotional support human in the loop."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
