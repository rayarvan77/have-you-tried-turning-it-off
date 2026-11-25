# Have You Tried Turning It Off?

[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![make.fun · rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/rayarvan77/have-you-tried-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![make.fun · reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/rayarvan77/have-you-tried-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

Entry for the [make.fun](https://make.fun) bounty **"Have You Tried Turning It Off?"** — write a single funny line, under 200 characters, that a hopeless tech support agent says to a desperate customer.

## The line

> Have you tried turning it off, counting to ten, and turning it back on while apologizing? Mine only works when it feels respected.

**130 characters** — well under the 200-character limit, exactly one line.

## Concept

The classic reboot advice is so worn out that even the agent saying it no longer believes in it. So instead of pretending the restart is a real fix, he upgrades it into a ritual: count to ten, apologize out loud, and hope the machine takes the apology seriously. The joke lands on the second sentence — the agent confesses, with total defeat, that his own computer only cooperates when it "feels respected". He is not fixing the customer's problem; he is admitting that nobody is in charge here, not even him. The desperation is mutual, and the machine has all the power.

## How it works

`main.py` (Python 3.13, standard library only) holds the line as a constant, validates it against the brief — at most 200 characters, exactly one line, non-blank, no leading/trailing whitespace, no control characters — then writes it to `/output/entry.txt` and prints it. Running it twice produces identical output.

```sh
python3 main.py
cat /output/entry.txt
```
