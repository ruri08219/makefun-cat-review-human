"""One-line one-star cat review of its human.

Writes the entry to /output/entry.txt as UTF-8, then reads it back
and asserts a byte-identical round-trip and the 1-200 char gate.
Standard library only.
"""

import os

ENTRY = (
    "One star. He bought me a $200 bed, then acted betrayed when I slept "
    "in the box. The box is five stars. He is one. The dog next door "
    "shares his snacks — I am packing my whiskers."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY, "round-trip mismatch"
    assert "\n" not in back, "entry must be a single line"
    assert 1 <= len(back) <= 200, "entry must be 1-200 characters"
    assert back.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
