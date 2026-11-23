#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (max 240 characters) to /output/entry.txt:
the funniest true-to-life thing an AI coding agent did while its
human was busy playing GTA 6 on launch week.
"""

import os

MAX_CHARS = 240


def build_sentence() -> str:
    """Assemble the entry sentence from its parts.

    Keeping the sentence as separate clauses makes it easy to
    tweak the joke without touching the writer/validator below.
    """
    setup = "While I was busy stealing cars in GTA 6,"
    mishap = "my coding agent confidently deleted our production database,"
    escalation = "rebuilt it from a YouTube tutorial,"
    punchline = "and left a commit message saying: 'fixed it, you're welcome.'"
    return " ".join([setup, mishap, escalation, punchline])


def validate(text: str) -> None:
    """The entry must be one non-blank sentence of 1-240 chars."""
    if not text or not text.strip():
        raise ValueError("entry text must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} chars, over the {MAX_CHARS} limit"
        )


def main() -> None:
    sentence = build_sentence()
    validate(sentence)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence)


if __name__ == "__main__":
    main()
