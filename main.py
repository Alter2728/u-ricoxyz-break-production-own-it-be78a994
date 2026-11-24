"""Entry for make.fun's "Break Production, Own It" bounty.

Writes one brutally honest one-line error message / postmortem
excuse to entry.txt in the output directory (1-200 UTF-8
characters). The same bytes are written on every run.
"""

import os

# Draft: "I dropped the production database at 3 a.m. and my only
# backup was a screenshot of the dashboard."
# Revised: name the actual command (DROP TABLE) and the cause
# (staging and prod looked identical) instead of the vague verb
# "dropped"; the specific mistake is more honest and more quotable,
# and the screenshot punchline still lands last.
LINE = (
    "I ran DROP TABLE on production at 3 a.m. because staging "
    "and prod looked identical, and my only backup was a screenshot."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
