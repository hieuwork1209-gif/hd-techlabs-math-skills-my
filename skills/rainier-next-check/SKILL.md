---
name: rainier-next-check
description: Run the Rainier local adversarial difficulty loop for an existing problem. Use for `/rainier-next-check problemNN <chat_url>`, requests to create or continue `adversary/problemNN`, and bare `next` follow-ups in an active loop. Keep hardening off `main`, use one cold GPT-5.5 Medium solve per unseen statement blob with a 2100-second timeout, route WSL2 desktop notifications to the locally bound Chrome window, and promote the exact tested pair when the solver is wrong or times out.
user-invocable: true
disable-model-invocation: false
argument-hint: problemNN plus ChatGPT conversation URL on first use; later `next` continues the active check
---

# Rainier Next Check

Use this skill as the local adversarial preflight layer **after** the normal Rainier authoring/repair flow. Do not replace or alter `/rainier-next`.

Read `references/workflow.md` before acting.

## Core contract

- Treat `main` as the portal-submission/frozen branch.
- Treat `adversary/problemNN` as the only branch for local difficulty hardening.
- On first use, accept the ChatGPT web conversation URL supplied with the command, e.g. `/rainier-next-check problem89 https://chatgpt.com/c/<conversation-id>`.
- Immediately upsert that URL into `solver-results/problemNN/chat-binding.json` on `adversary/problemNN`. Never copy it to `main`.
- On WSL2, after the chat binding exists, make the next user action `python scripts/rainier-bind-window.py problemNN`. The user clicks the Chrome window/account that owns this chat. The binder stores only local HWND/PID/window metadata; it never reads or stores account email/profile credentials.
- Window bindings live only in `.tmp/codex-adversary/problemNN-window.json` plus the Windows runtime copy under `%LOCALAPPDATA%\Rainier\window-bindings\`. They are never committed.
- After a valid window binding, use `python scripts/codex-adversary-watch-chat.py problemNN --watch` as the independent local solver harness.
- The wrapper supplies GPT-5.5 Medium and a 2100-second timeout unless explicitly overridden.
- One unseen `problem.md` blob gets exactly one GPT-5.5 Medium solve. Do not use `--force` in the normal loop.
- A watcher `success` means only that text was returned. Compare it mathematically with the matching `solution.md` before deciding.
- If the solver is correct, diagnose its earliest robust shortcut, structurally harden, verify the new ground truth, then update `solution.md` first and `problem.md` second on the adversary branch.
- If the solver is wrong/materially incomplete or the watcher records `LOCAL_STUMPED_BY_TIMEOUT`, stop local hardening, pass submission gates, and promote the exact matching `solution.md` then `problem.md` to `main`.
- Never promote on `SOLVER_ERROR` or an infrastructure failure.
- Never call a local stump or timeout an official Rainier difficulty pass.
- After promotion to `MAIN_READY_FOR_RAINIER`, upsert `solver-results/problemNN/terminal.json` on the adversary branch for the exact promoted problem blob. A matching marker makes the watcher exit successfully instead of repeating `already tested`.
- PowerShell notifications must route through the exact locally bound Chrome HWND. If that binding is missing or stale, do not fall back to another browser/account.

## Follow-up `next`

In a conversation already using this skill, interpret a bare `next` as: read `solver-results/problemNN/latest.json` from `adversary/problemNN`, follow its `result_file` when needed, compare against the exact candidate solution, and continue the state machine without asking the user to restate the problem.

## User boundary

The web chat cannot wake itself when GitHub changes. After a watcher attempt finishes, the only user handoff needed is `next`. The user supplies the web-chat URL on first invocation and performs the one-time local Chrome-window binding. Later turns reuse both bindings until the user explicitly rebinds or the Chrome HWND becomes stale.
