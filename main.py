"""FridgeLight: pitch for the worst app idea ever pitched.

Entry for make.fun's "The Worst App Idea Ever Pitched" bounty.
The program writes exactly one sentence (237 characters) to
<output>/entry.txt: a deadpan pitch for an app nobody needs.
"""

import os
import sys

# Why this pitch: a named product, a function nobody asked for
# (live fridge-door surveillance), and a founder who states it with
# total confidence. One sentence, no padding, no second idea.
PITCH = (
    "FridgeLight is the app that pings your phone every time someone "
    "opens your fridge, logs exactly how long the door stayed open, "
    "and ranks your whole household by midnight-snack discipline, "
    "because your leftovers deserve 24/7 surveillance."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"wrote {path} ({len(PITCH)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
