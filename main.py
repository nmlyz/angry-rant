#!/usr/bin/env python3
"""Write one short, funny rant about an everyday annoyance to /output/entry.txt.

The rant is fixed text: the same bytes on every run, with no input,
no network access and no third-party packages.
"""
import os

RANT = (
    "My car won't stop dinging because the bag of groceries in the passenger "
    "seat isn't wearing a seatbelt. So I buckled in the oranges. The oranges "
    "are safer than I am now. The car is satisfied. I am not."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(RANT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
