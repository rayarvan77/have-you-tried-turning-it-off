"""Have You Tried Turning It Off? — one-line entry.

Holds the single funny line a hopeless tech support agent says to a
desperate customer, checks it against the brief's gates, and writes it
to /output/entry.txt. Deterministic: same input, same output, every run.
"""

from pathlib import Path

LINE = (
    "Have you tried turning it off, counting to ten, and turning it back "
    "on while apologizing? Mine only works when it feels respected."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce every gate in the brief; fail loudly instead of shipping bad text."""
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("line must not contain control characters")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    validate(LINE)
    print(LINE)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
