"""make.fun ai-joke-03 entry: writes one joke about AI coding agents.

The joke is a fixed constant, so both grader runs write identical bytes.
Output goes to MAKEFUN_OUTPUT_DIR/entry.txt locally, or /output/entry.txt
in the grader (same convention as the kit starter).
"""

import os
from pathlib import Path

# Iteration 4, winner of my second brainstorm: the agent reads my git
# history to learn the project, and weaponises my worst commits kindly.
JOKE = (
    "My agent read my git history to understand the project, and now it brings "
    "up my 2 a.m. commits the way a therapist brings up childhood."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
