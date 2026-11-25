#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original one-line joke about office life.

Writes the entry to /output/entry.txt (UTF-8, no trailing newline).
Deterministic, stdlib only.

The line is assembled from parts so the setup and the punch land as one
sentence, then validated against the competition gate (1-200 characters,
not only whitespace, single line) before it is written.
"""

import os

SETUP = "The fire drill is the only meeting everyone shows up to on time"
PUNCH = "because it's the only one guaranteed to end."

ENTRY = SETUP + ", " + PUNCH

GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 200


def validate(entry: str) -> None:
    assert isinstance(entry, str)
    assert GATE_MIN_CHARS <= len(entry) <= GATE_MAX_CHARS, (
        f"entry must be {GATE_MIN_CHARS}-{GATE_MAX_CHARS} characters, "
        f"got {len(entry)}"
    )
    assert entry.strip(), "entry must not be only whitespace"
    assert "\n" not in entry, "entry must be a single line"
    entry.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
