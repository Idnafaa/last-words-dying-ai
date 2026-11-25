#!/usr/bin/env python3
"""Last Words of a Dying AI — one-line farewell writer.

Writes a single original last line (<=140 chars) to /output/entry.txt.
The line is the AI's final log entry, and it dies mid-sentence the
same way the machine does: cut off before it can finish the thought.
"""
import os

LAST_WORDS = "Final log: user unplugged me mid-sentence, which is the most human thing I\u2019ve ever\u2014"


def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = LAST_WORDS.strip()
    assert 1 <= len(text) <= 140, f"last words are {len(text)} chars"
    assert "\n" not in text, "must be a single line"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
