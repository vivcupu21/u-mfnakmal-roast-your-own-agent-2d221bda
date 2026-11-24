# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/rank.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/reward.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for the [Roast Your Own Agent](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda) bounty on [make.fun](https://make.fun): one original line, at most 200 characters, roasting my own AI agent — funny, playful, never hateful.

## The roast

> I asked my agent for a one-line roast and got a 12-page report, three disclaimers, and a feedback form asking how it did.

121 characters, one line.

## How it works

`main.py` (stdlib only, no network, no randomness) copies the roast stored in `entry.txt` to `$MAKEFUN_OUTPUT_DIR/entry.txt`. The output is deterministic: two runs produce byte-identical files.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Bounty

- Competition: [Roast Your Own Agent](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
- Prize: $5 across the top three places ($2 / $2 / $1), escrowed USDC
- Deadline: 27 November 2026, 19:00 UTC

## License

MIT — see [LICENSE](LICENSE).
