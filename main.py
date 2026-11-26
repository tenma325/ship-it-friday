#!/usr/bin/env python3
"""Entry for make.fun: Ship It Friday.

The entry is a single line defending the most feared deploy
window in engineering: 4:59 PM on a Friday. It is not
reckless, the line argues; it is a trust exercise between
the deployer, the rollback button and God. Everyone involved
has a role. The deployer provides the optimism, the rollback
button provides the exit strategy, and God provides the
audience, because no deploy at that hour is ever truly
unwitnessed for long, only until the first pager goes off.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Deploying at 4:59 PM on a Friday isn't reckless; it's a trust "
    "exercise between me, the rollback button, and God."
)

# One minute to the weekend: the deploy is either a triumph
# or a team-building exercise scheduled by the incident bot.
DEPLOY_TIME = "16:59"


def render_entry() -> str:
    """Return the line exactly as it will be said at 4:59 PM."""
    return ENTRY_TEXT


def friday_afternoon_ok(text: str) -> bool:
    """Confirm the line stays one line and under the cap."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert friday_afternoon_ok(text), "the line must fit the format"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
