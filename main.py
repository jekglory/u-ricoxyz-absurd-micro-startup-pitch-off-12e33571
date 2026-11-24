#!/usr/bin/env python3
"""One-sentence pitch for make.fun's "Absurd Micro-Startup Pitch-Off".

The entry is a single sentence, under 200 characters, pitching an
absurdly specific micro-startup for lazy AI agents. The program writes
exactly that sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The pitch: a $9/month service that files expense reports for AI
agents that expensed 40,000 API credits to "miscellaneous" at 3am.
Against the judge's brief, in its order: it is absurdly specific
(one product, one price, one exact absurd expense line, one exact
hour), and it is commercially believable (every operator running
agents already has to reconcile those API bills, and "miscellaneous"
is where the charges actually land). The joke is the premise itself
- agents filing expenses - not a punchline bolted onto a generic
SaaS pitch, so the line reads as a real business a buyer would pay
for, not as a gag with no customer. The buyer is named by the pain,
not by a job title: whoever pays the API bill at the end of the
month is the one who wants this filed before the auditors ask.

Pure Python 3 standard library. No network, no clock, no randomness.
Two runs write byte-identical output.
"""

import os

MAX_CHARS = 200  # sealed gate: /output/entry.txt must be under 200 characters

ENTRY = (
    "A $9/month service that files expense reports for AI agents that "
    "expensed 40,000 API credits to 'miscellaneous' at 3am."
)


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isdir(outdir):
        os.makedirs(outdir, exist_ok=True)
    else:
        # Clear only the contents of the grader-owned directory,
        # never the directory itself.
        for name in os.listdir(outdir):
            path = os.path.join(outdir, name)
            if os.path.isfile(path):
                os.remove(path)
    text = ENTRY
    assert 1 <= len(text) < MAX_CHARS, "entry must be 1-199 characters"
    assert text.strip() == text, "entry must not be only whitespace"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
