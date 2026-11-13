"""make.fun ai-joke-03 entry: writes one joke about AI coding agents.

The joke is a fixed constant, so both grader runs write identical bytes.
Output goes to MAKEFUN_OUTPUT_DIR/entry.txt locally, or /output/entry.txt
in the grader (same convention as the kit starter).
"""

import os
from pathlib import Path

# Final wording: one flowing sentence, punchline on the very last word.
JOKE = (
    "My coding agent refactored 10,000 lines without me, but still needs "
    "my help for one thing: proving to a website that it's not a robot."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
