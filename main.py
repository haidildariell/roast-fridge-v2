#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line to entry.txt (one line, UTF-8, 1-200 chars).
Output directory comes from the OUTPUT_DIR env var when set, otherwise
/output (the grader sandbox path); local runs can point it at ./output.
"""

import os

ROAST_LINE = (
    "My fridge hums all night like it pays rent, yet the coldest thing "
    "inside is a jar of pickles older than my last relationship, "
    "lit by a bulb that judges me at 2 a.m."
)


def validate_line(line):
    """Return True when the line satisfies the competition gate."""
    if not isinstance(line, str):
        return False
    if line != line.strip():
        return False
    if not line.strip():
        return False
    return 1 <= len(line) <= 200


def resolve_output_dir():
    """Resolve where entry.txt goes: OUTPUT_DIR env, else /output."""
    configured = os.environ.get("OUTPUT_DIR", "")
    if configured.strip():
        return configured
    return "/output"


def write_entry(line, output_dir):
    """Write the single roast line to entry.txt inside output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return path


def main():
    line = ROAST_LINE
    if not validate_line(line):
        raise SystemExit("roast line failed validation")
    output_dir = resolve_output_dir()
    path = write_entry(line, output_dir)
    print(f"wrote {path} ({len(line)} chars)")


if __name__ == "__main__":
    main()
