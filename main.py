"""Entry for make.fun bounty u-puan-one-letter-for-your-day-e54e9c36.

Writes exactly one character, "U", to entry.txt (in $MAKEFUN_OUTPUT_DIR,
or /output when the harness does not set it). No trailing newline: the
gate requires UTF-8 text of exactly 1 character, so even one extra byte
would make the entry invalid.

Why "U": the judge sees only the letter and imagines the word behind it.
"U" stands for "unhinged" — a day gone off the rails. It is the one
day-word in the field that is BOTH a sharp picture (criterion 2) AND
funny/surprising/repeatable (criterion 3): "today was unhinged" is a line
you repeat to a friend. Its rivals split the two — exhausted / hectic /
stressful are vivid but earnest, wild / chaotic are fun but generic or
clichéd — while the vague-positive letters (A for amazing, F for
fantastic) lose on vividness outright. U also fits its word (criterion 5:
the initial matches the sound and shape of "unhinged") and is a sharper
pick than the obvious ones the brief penalises. And U's whole distribution
of plausible words is strong (unhinged, underwhelmed, unbelievable), so
the pick does not depend on one lucky inference.

The letter won a head-to-head tournament judged with the competition's
own brief (see CANDIDATES.md): 7-0 in an 8-letter round robin (28 games)
plus 5-0 against challengers (O, F, B, D, R) — 12-0 overall. Closest
rival: Z (zonked), 6-1, beaten by U at margin 2.

Deterministic, stdlib-only, no network, no input. The letter is a fixed
literal.
"""

import os

LETTER = "U"


def main() -> None:
    # Gate: exactly 1 character, no newline, no whitespace.
    if len(LETTER) != 1 or LETTER.isspace():
        raise SystemExit(f"entry must be exactly 1 letter, got {LETTER!r}")
    if not ("A" <= LETTER <= "Z"):
        raise SystemExit(f"entry must be a letter A-Z, got {LETTER!r}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Read back: the gate counts bytes, so verify the file on disk is
    # exactly the one letter — a stray newline here would be fatal.
    with open(path, "rb") as f:
        written = f.read()
    if written != LETTER.encode("utf-8"):
        raise SystemExit(f"entry.txt must be exactly {LETTER!r}, got {written!r}")


if __name__ == "__main__":
    main()
