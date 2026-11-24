"""Entry for make.fun's "Break Production, Own It" bounty.

Writes one brutally honest one-line error message / postmortem
excuse to entry.txt in the output directory (1-200 UTF-8
characters). The same bytes are written on every run.
"""

import os

# Draft: "Error 500: I deleted the production database, and the only
# backup I had was a screenshot of the dashboard."
# Revised: "Error 500:" is generic sysadmin boilerplate and "deleted"
# is vaguer than the concrete verb; drop the label, name the hour,
# and let the punchline land on the screenshot backup.
LINE = (
    "I dropped the production database at 3 a.m. and my only "
    "backup was a screenshot of the dashboard."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
