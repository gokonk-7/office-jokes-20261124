"""Office-jokes entry for make.fun.

Writes one line about office life to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.
The line is a fixed, hand-written joke: no network, no randomness, no
clock reads, so every run produces byte-identical output.
"""

import os

JOKE = (
    "The fire drill was the only meeting this quarter where everyone "
    "arrived on time, left early, and nobody asked to circle back."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
    # not only white space, and exactly one line.
    assert 1 <= len(text) <= 199, f"entry is {len(text)} chars, must be 1-199"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back: what the grader will judge must be exactly this line.
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "written entry does not match the joke"


if __name__ == "__main__":
    main()
