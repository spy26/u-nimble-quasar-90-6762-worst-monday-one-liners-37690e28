"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = "My Monday deploy failed at 9:03. The post-mortem was scheduled for 9:05."


def validate_entry(text: str) -> str:
    """Refuse to write anything unless the entry is exactly one line of
    plain text: non-empty, not whitespace-only, no newline or control
    characters, and within the 1-to-140 character competition limit."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main() -> None:
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
