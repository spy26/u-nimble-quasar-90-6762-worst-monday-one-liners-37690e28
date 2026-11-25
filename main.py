"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = "My Monday deploy failed at 9:03. The post-mortem was scheduled for 9:05."


def main() -> None:
    entry = ENTRY
    if not entry or not entry.strip():
        raise SystemExit("entry is empty")
    if len(entry) > 140:
        raise SystemExit(f"entry is {len(entry)} characters, over the 140 limit")
    entry.encode("utf-8")  # must be valid UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
