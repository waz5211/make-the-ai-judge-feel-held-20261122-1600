"""Write a short original text to /output/entry.txt.

Deterministic, no network access. The output directory is created
if it does not exist.
"""

import os
from pathlib import Path

ENTRY = (
    "The kitchen light is on, low and amber. Your coat finds its hook. "
    "A mug from this morning sits on the table, its tea cold now. "
    "You rinse it; the water runs warm over your hands. "
    "Outside, rain settles on the window. You sit. "
    "The chair is where you left it."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
