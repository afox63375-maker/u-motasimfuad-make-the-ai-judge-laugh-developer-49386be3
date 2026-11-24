"""Entry for make.fun: "Make the AI Judge Laugh — Developer Excuses".

The program carries exactly one line of text: a developer's excuse for
production breaking. Running it writes that line, unchanged, to the
output file the competition's scorer reads.
"""

import os
import sys

# The excuse itself. The gate wants a single line of 1..200 characters,
# so this string holds no newline and stays well under the ceiling.
EXCUSE = (
    "Production isn't down; it just reached the code path I labeled "
    "'this can never happen' and decided to fact-check me."
)

CHAR_FLOOR = 1
CHAR_CEILING = 200


def check_line(text):
    """Refuse to ship anything the scorer would mark invalid."""
    if "\n" in text or "\r" in text:
        raise ValueError("the entry must be a single line")
    if not text.strip():
        raise ValueError("the entry cannot be only whitespace")
    if not CHAR_FLOOR <= len(text) <= CHAR_CEILING:
        raise ValueError(
            "the entry must be %d..%d characters, got %d"
            % (CHAR_FLOOR, CHAR_CEILING, len(text))
        )
    text.encode("utf-8")  # raises if the text cannot be stored as UTF-8


def destination():
    """Where the scorer looks: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(folder, "entry.txt")


def main():
    check_line(EXCUSE)
    path = destination()
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    # Bytes go out exactly as held: no trailing newline is appended.
    payload = EXCUSE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    # Read the file back and compare byte for byte; a short or garbled
    # write is worse than a loud failure, so refuse to exit cleanly.
    with open(path, "rb") as handle:
        stored = handle.read()
    if stored != payload:
        raise IOError("written entry does not match the excuse held in code")
    return 0


if __name__ == "__main__":
    sys.exit(main())
