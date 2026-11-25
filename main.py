"""One Line, Big Laugh — entry program.

Writes exactly one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Gate: UTF-8 text, 1-200 characters.

DECISION RECORD — Pass 1 (candidates weighed against the judge brief:
genuinely hilarious real joke first, then an unexpected turn, then
tightness, freshness, memorability; exact ties go to the smaller text,
so shorter is better):

A. "My smart fridge ordered milk, my smart speaker cancelled it, and my
   smart TV is now showing me divorce lawyer ads." (~118 chars)
   REJECTED: three-beat escalation is fine, but "smart home turns on its
   owner" is a well-worn premise and the line spends words setting up
   three devices before the payoff.

B. "I told my therapist I talk to my plants. She said that's healthy.
   I didn't tell her they answer back in my voice." (~124 chars)
   REJECTED: the turn at the end is good and it is memorable, but
   therapist jokes are a crowded lane and it runs long for its one twist.

C. "The printer only jams when the document is urgent, which is how I
   know it reads." (80 chars)
   CHOSEN: a real joke with a setup and a twist, not a mere observation.
   The premise is fresh (a printer with intent, not just a broken
   machine), the turn lands in the last four words, and it is short
   enough to win a size tie-break. Absurdly specific detail (urgent
   documents) does the work.

D. "My phone autocorrected 'I'm on my way' to 'I'm on my whey', so now
   my trainer thinks I'm committed and my boss thinks I'm lost."
   REJECTED: autocorrect was already the subject of one of our earlier
   submitted entries — no reuse.

E. "I bought a standing desk to be healthier. Now I just sit on the
   floor next to it, which doctors agree is technically
   standing-adjacent." (~140 chars)
   REJECTED: self-defeating and specific, but the payoff ("standing-
   adjacent") is a wink at the reader rather than a turn, and it is
   nearly twice as long as C for the same single laugh.

F. "My Roomba got stuck under the couch for three days. When I freed
   it, it cleaned the same spot for an hour, like it was telling me
   about the trip." (~145 chars)
   REJECTED: charming and memorable, and the "telling me about the trip"
   turn is strong — but Roomba-with-feelings is a familiar bit, and at
   145 chars it loses a size tie-break to C while carrying the same
   one-twist payload.

Pass 2 — two genuine revisions of the chosen line C:
1. "My printer only jams on urgent documents, which is how I know it
   can read." — cut "The printer" -> "My printer" (ownership makes the
   grievance personal), dropped "when the document is" (dead weight),
   "it can read" punches harder than "it reads" because the ability,
   not the act, is the accusation. 80 -> 74 chars.
2. Considered "My printer only jams when it matters, which is how I
   know it reads." (67 chars) — shorter, but "when it matters" is
   vaguer than "on urgent documents" and the judge rewards absurdly
   specific detail; kept revision 1. Final line is 74 characters.

Pass 3 — a fresh look before locking the entry (this pass):
Before touching the code I re-opened the line itself, because a
structural pass that never questions the payload is just tidying.
Two new phrasings of the same joke were drafted and weighed:

G. "My printer waits until the document is urgent to jam, which tells
   me it can read." (82 chars)
   REJECTED: same joke, worse rhythm. Front-loading "waits until"
   delays the verb, and "which tells me" is softer than "which is
   how I know" — the chosen line's confidence is part of the laugh.

H. "It only jams on urgent documents, which is how I know my printer
   can read." (75 chars)
   REJECTED: moving "my printer" to the end buries the subject and
   makes the first clause float without an owner; the grievance
   needs a named culprit up front. Also one char longer.

Conclusion: the 74-char line survives both challenges unchanged.
The rest of this pass therefore worked on the code around it: the
gate (1-200 chars, single line) was previously only described in
prose, so the program now checks it itself via validate_line()
before writing, and the output path resolution lives in its own
output_path() function so the env-var fallback is stated in
exactly one place. Behaviour is otherwise identical: the same
line, the same file, the same trailing newline.
"""

import os

LINE = "My printer only jams on urgent documents, which is how I know it can read."

# The bounty's hard gate: one line of UTF-8 text, 1-200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def validate_line(line: str) -> None:
    """Fail loudly if the entry line ever drifts outside the gate.

    The line is a fixed constant today, but the check is cheap
    insurance: if a future edit makes it empty, over-long, or
    multi-line, the program should refuse to write a bad entry
    rather than submit one silently.
    """
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars; gate is {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")


def output_path() -> str:
    """Where the entry file goes.

    $MAKEFUN_OUTPUT_DIR/entry.txt when the harness sets the variable,
    otherwise /output/entry.txt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    validate_line(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
