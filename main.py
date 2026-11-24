"""Write the One-Line Laugh entry to /output/entry.txt.

The joke: a fitness tracker congratulates the narrator on reaching
10,000 steps, and only at the very end does the reader learn every
step was earned looking for the fitness tracker itself. A different
angle from our earlier smart-fridge line: no smart home, no review
stars — the surprise is a self-defeating loop: the achievement and
the failure are the same walk, which everyone who has ever lost a
wearable recognises instantly.

Gate (from RULES.txt): /output/entry.txt is UTF-8 text of 1 to 200
characters, not only white space, one single sentence.
"""

import os

PARTS = (
    "My fitness tracker congratulated me on 10,000 steps today — ",
    "every single one of them earned ",
    "looking for my fitness tracker.",
)


def entry_line():
    return "".join(PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
