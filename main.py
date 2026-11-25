#!/usr/bin/env python3
"""One Star for Monday.

Writes a single one-line, one-star review of Monday — written as though
Monday were a restaurant — to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The program is fully deterministic: it always writes the same line, so
two runs produce byte-identical output.

Why this line: it reads like a genuine diner's complaint (a waiter, an
order, a dish served) and the joke only works on Monday — you order a
fresh start, the week's first day, and what arrives is the whole week
of work, served up as the Monday special.
"""

import os

LINE = (
    "One star. The waiter took my order for a fresh start and served "
    "me a full week of work, calling it the Monday special."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, and the line
    # itself is the whole entry.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
