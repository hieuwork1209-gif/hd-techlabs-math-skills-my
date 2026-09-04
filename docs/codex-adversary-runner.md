# Codex adversary runner

This runner is the local solver half of the Rainier hardening loop.

It watches `origin/adversary/problem81`. Whenever that branch gets a new
`problem.md` blob, it extracts only the normalized problem statement and runs
exactly one fresh Codex solve using GPT-5.4 with reasoning effort `high`.

The solve happens in a temporary directory, not inside the Rainier repository,
so the solver cannot read `solution.md` or other repository context. The result
is committed back to:

`solver-results/problem81/<problem-blob-sha>.json`

A result commit does not trigger another solve because deduplication is keyed on
the `problem.md` blob SHA.

## First setup

From the local clone that already has your Codex CLI login:

```bash
git fetch origin adversary/problem81
git switch adversary/problem81
codex --version
python scripts/codex-adversary-watch.py problem81
```

The last command is a one-shot calibration run against the current problem81.
If it succeeds, it pushes one JSON result to the adversary branch.

## Continuous mode

After the one-shot run is verified:

```bash
python scripts/codex-adversary-watch.py problem81 --watch
```

Leave that process running. It polls every 45 seconds by default.

## Solver configuration

Defaults are intentionally fixed to one run per candidate:

```text
model = gpt-5.4
reasoning effort = high
runs = 1
sandbox = read-only
session persistence = ephemeral
```

The runner uses the Codex CLI authentication already present on the machine. It
does not require a Make scenario and does not use Make credits.

## Stop

Press `Ctrl+C` in the watcher terminal.

## Troubleshooting

If the CLI says GPT-5.4 is unavailable, verify that the same signed-in Codex
account still exposes GPT-5.4 in the Codex model picker.

If `codex` is not found, open the shell/environment where Codex CLI is installed
or add it to `PATH`.

If pushing the result fails, make sure the local clone's `origin` can push to
`hieuwork1209-gif/hd-techlabs-math-skills-my`.
