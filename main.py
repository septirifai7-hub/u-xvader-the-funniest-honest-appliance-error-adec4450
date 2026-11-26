"""The Funniest Honest Appliance Error.

A washing machine reports its failure the way a tired machine would:
flat, specific, and quietly giving up on one sock. The joke is the
honesty -- the drum really did lose a sock, and the machine knows it.

Running this file writes the error line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``), with no trailing newline.
"""

import os

ENTRY = (
    "Error E04: drum will not spin. One sock is missing. I have searched "
    "the entire load twice and I am no longer confident the sock was ever real."
)


def get_entry() -> str:
    """Return the appliance's error line."""
    return ENTRY


def write_entry(output_dir: str | None = None) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    directory = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry and print where it went."""
    print(write_entry())


if __name__ == "__main__":
    main()
