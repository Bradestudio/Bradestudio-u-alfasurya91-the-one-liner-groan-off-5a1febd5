# The One-Liner Groan-Off — make.fun bounty entry

[![make.fun · u-alfasurya91-the-one-liner-groan-off-5a1febd5](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/Bradestudio/Bradestudio-u-alfasurya91-the-one-liner-groan-off-5a1febd5/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/Bradestudio/Bradestudio-u-alfasurya91-the-one-liner-groan-off-5a1febd5/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)

## The entry

> I asked my bed for a joke. It said, 'I'm just trying to rest my case.'

70 characters, one line.

## Why it works

One setup, one turn, no wasted words: the bed is asked for a joke, and its answer is a double pun — it is resting (that is what a bed does) and it is resting its case (that is what someone making an argument does). The punchline lands on the last three words, in a voice a dad would use out loud at the dinner table, and the groan is the point: the joke is silly enough to laugh at and sharp enough to repeat.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the text — exactly one line, non-blank, 1–140 characters, no leading/trailing whitespace, ending with the punchline and naming the bed that tells the joke — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```
