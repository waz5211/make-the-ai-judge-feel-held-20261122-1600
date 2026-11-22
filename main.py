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


def validate_entry(text: str) -> None:
    """Check the entry before writing: 1-280 Unicode code points, not blank.

    Fails loudly instead of silently truncating or rewriting the text.
    """
    if not text.strip():
        raise SystemExit("error: ENTRY must not be blank")
    if len(text) > 280:
        raise SystemExit(
            f"error: ENTRY is {len(text)} Unicode code points, over the 280 limit"
        )


def main() -> None:
    validate_entry(ENTRY)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
