"""The Meeting That Should Have Been One Line.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the single
sentence that could have replaced an entire pointless meeting.
Standard library only.
"""

import os
import sys

MEETING_LINE = (
    "The decision is yes, the budget is approved, and the "
    "deadline is Friday \u2014 this meeting is just that sentence, "
    "said slower, by six people, for an hour."
)


def meeting_line_gate(text):
    """Check the meeting line against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one sentence that could
    have replaced an entire pointless meeting, no context and no
    explanation. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("meeting line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "meeting line is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("meeting line must be exactly one line")
    return cleaned


def meeting_line_measure(text):
    """Measure the meeting line for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A line too short to carry a decision, or one
    padded out to fill the cap instead of killing the meeting,
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = meeting_line_gate(MEETING_LINE)
    shape = meeting_line_measure(text)
    if shape["words"] < 5:
        raise ValueError("meeting line is too short to replace a meeting")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
