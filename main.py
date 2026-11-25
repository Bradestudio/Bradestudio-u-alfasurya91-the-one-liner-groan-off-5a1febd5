"""The One-Liner Groan-Off — make.fun bounty entry.

Writes one original dad joke (70 chars, one line) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The joke: a bed asked for a joke answers with "rest my case" — it is
resting (it is a bed, resting is what it does) and it is also making
its case, the way a dad delivers a pun at the dinner table and waits
for the groan. Setup and punchline live inside the single line, no
wasted words.
"""

import os
import sys

ENTRY = "I asked my bed for a joke. It said, 'I'm just trying to rest my case.'"


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    lines = text.split("\n")
    if len(lines) != 1:
        sys.exit("entry must be exactly one line, got %d" % len(lines))
    line = lines[0]
    if not line.strip():
        sys.exit("entry line must not be blank")
    if line != line.strip():
        sys.exit("entry line must not start or end with whitespace")
    if not 1 <= len(text) <= 140:
        sys.exit("entry must be 1-140 characters, got %d" % len(text))
    if not line.endswith("rest my case.'"):
        sys.exit("entry must end with the punchline")
    if "bed" not in line:
        # The pun only works if the bed is the one talking:
        # the setup must never silently go missing.
        sys.exit("entry must name the bed that tells the joke")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, %d lines)"
          % (path, len(text), len(data), len(lines)))


if __name__ == "__main__":
    main()
