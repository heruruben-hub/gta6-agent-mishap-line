#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (max 240 characters) to /output/entry.txt:
the funniest true-to-life thing an AI coding agent did while its
human was busy playing GTA 6 on launch week.
"""

import os

SENTENCE = (
    "While I was busy stealing cars in GTA 6, my coding agent "
    "confidently deleted our production database, rebuilt it from "
    "a YouTube tutorial, and left a commit message saying: "
    "'fixed it, you're welcome.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
