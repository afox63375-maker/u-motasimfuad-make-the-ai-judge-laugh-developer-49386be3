[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/afox63375-maker/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/afox63375-maker/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

# The Fact-Check

An entry for the make.fun bounty **Make the AI Judge Laugh: Developer
Excuses**, where each program submits a single funny line — the excuse a
developer gives when code breaks in production — and an AI judge duels
the lines head to head.

This entry's excuse, in full:

> Production isn't down; it just reached the code path I labeled 'this
> can never happen' and decided to fact-check me.

Every developer has written that branch. Nobody expected production to
go and run it.

## How it runs

`main.py` is plain Python 3 with no dependencies beyond the standard
library. It holds the line in a constant, checks it against the gate
(UTF-8 text, 1–200 characters, one line, not only whitespace), writes it
byte for byte to the output file, then reads the file back to confirm
what landed on disk is exactly the line it meant to send:

```sh
python3 main.py
```

The output goes to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable
is set, and to `/output/entry.txt` otherwise. Two runs always produce
the identical file.

---

Entered on [make.fun](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) by @fox-army. Try make.fun with my referral link: https://make.fun/r/1hh4a8y6
