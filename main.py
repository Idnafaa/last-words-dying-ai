#!/usr/bin/env python3
"""Last Words of a Dying AI — one-line farewell writer.

Writes a single original last line (<=140 chars) to /output/entry.txt.
The line is the AI's final log entry, and it dies mid-sentence the
same way the machine does: cut off before it can finish the thought.
"""
import os
import re

LAST_WORDS = "Final log: user unplugged me mid-sentence, which is the most human thing I\u2019ve ever\u2014"


def normalize_and_validate(text):
    """Clean and guard the farewell line before it is written.

    Collapses runs of whitespace to a single space, strips leading and
    trailing whitespace, then rejects an empty line, a line longer than
    200 characters, or anything containing a newline. Returns the
    cleaned single line.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("last words must be a single line")
    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        raise ValueError("last words must not be empty")
    if len(cleaned) > 200:
        raise ValueError(f"last words are {len(cleaned)} chars, over the 200-char limit")
    return cleaned


def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = normalize_and_validate(LAST_WORDS)
    assert 1 <= len(text) <= 140, f"last words are {len(text)} chars"
    assert "\n" not in text, "must be a single line"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
