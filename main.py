#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry (program/v1).

The program writes exactly one funny line of text to entry.txt.

Design (from the bounty brief: laugh first, then turn, tightness,
freshness, clarity):
- Setup plants one meaning of "space" (personal space, as in a
  relationship talk).
- Punchline flips it to the other meaning (disk space) with a
  consequence — deleted files — that is surprising, instantly clear,
  and needs no second line.
- 55 characters, one breath, no word to trim.

The line was chosen by a local pairwise tournament over 19 fresh
one-liners written for this bounty (see CANDIDATES.md): 5-0 in the
six-way round-robin playoff.

Stdlib only. Deterministic: the same bytes on every run.
"""

import os

LINE = "I told my computer I needed space. It deleted my files."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 140, "gate: entry must be 1-140 characters"
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
