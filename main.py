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
"""

import os

LINE = "My printer only jams on urgent documents, which is how I know it can read."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
