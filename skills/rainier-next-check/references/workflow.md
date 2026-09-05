# Rainier Next Check Workflow

## State model

For `problem103` use:

- submission branch: `main`
- local design branch: `adversary/problem103`
- immutable run record: `solver-results/problem103/<blob-prefix>.json`
- latest handoff: `solver-results/problem103/latest.json`
- web-chat binding: `solver-results/problem103/chat-binding.json` on the adversary branch only
- terminal marker: `solver-results/problem103/terminal.json` on the adversary branch only
- local WSL window binding: `.tmp/codex-adversary/problem103-window.json`
- Windows runtime binding: `%LOCALAPPDATA%\Rainier\window-bindings\problem103.json`

`main` is frozen/submission state. All local hardening happens on `adversary/problemNN`.

## First invocation

Invocation form:

`/rainier-next-check problemNN https://chatgpt.com/c/<conversation-id>`

1. Validate the ChatGPT conversation URL and extract the conversation ID from `/c/<id>` when possible.
2. Resolve exactly one `workspace/rainier-problem/problemNN-*/problem.md` and matching `solution.md` on `main`.
3. Ensure `adversary/problemNN` exists. Create it from current `main` only if absent. Never reset an existing adversary branch.
4. Upsert `solver-results/problemNN/chat-binding.json` on the adversary branch immediately. Store `problem`, `conversation_id` when extractable, and `chat_url`. Never copy this file to `main`.
5. On WSL2, make the next user action:

   `python scripts/rainier-bind-window.py problemNN`

   The binder waits until the user clicks the Chrome window/account that owns this chat, captures the foreground HWND/PID, verifies the process is Chrome, and stores only local window metadata. It does not inspect or store account email, Chrome profile credentials, cookies, or browser secrets.
6. The binder also installs the per-user Windows `rainier-chat://` protocol handler. Toast clicks route through this handler so the exact Chrome HWND is focused before the exact ChatGPT URL is opened.
7. The handler must use focus-only behavior (`BringWindowToTop` + `SetForegroundWindow`). Do not use `ShowWindowAsync(..., SW_RESTORE)` because that can move or unsnap the user's Chrome window.
8. If the saved HWND/PID is stale or no longer points to Chrome, fail closed and ask for rebinding. Never fall back to another Chrome window, browser profile, default browser, or GitHub URL.
9. After window binding, use:

   `python scripts/codex-adversary-watch-chat.py problemNN --watch`

The wrapper defaults to GPT-5.5 Medium and a 2100-second timeout.

## Window binding and notification routing

Window binding is local-only and is not part of the adversary Git history.

The WSL mirror has the shape:

```json
{
  "problem": "problem103",
  "hwnd": 458894,
  "pid": 11988,
  "process_name": "chrome",
  "title": "Problem - problem103 - Google Chrome",
  "bound_at": "<UTC timestamp>"
}
```

The Windows runtime copy under `%LOCALAPPDATA%\Rainier\window-bindings\` is consumed by `scripts/rainier-window-handler.ps1`, which the binder installs under `%LOCALAPPDATA%\Rainier\`.

Notification routing is:

```text
solver finishes
-> wrapper refreshes exact chat-binding.json from origin/adversary/problemNN
-> wrapper encodes that ChatGPT URL into rainier-chat://problemNN/<payload>
-> Windows toast click invokes the local protocol handler
-> handler validates problem + ChatGPT host + /c/ path
-> handler validates HWND still exists and belongs to the saved Chrome PID
-> handler focuses only that HWND
-> handler navigates that Chrome window to the exact conversation
-> clipboard becomes: next
```

`--notify-test` may be used after binding:

`python scripts/codex-adversary-watch-chat.py problemNN --notify-test`

A watcher process already running before new code is pulled does not hot-reload. Restart the process after pulling when testing new notification behavior, but never use `--force` to re-solve an already measured blob.

## Candidate measurement

For each unseen adversary `problem.md` blob:

- exactly one cold GPT-5.5 Medium solve
- timeout 2100 seconds unless explicitly overridden
- solver receives only the normalized problem statement
- `status=success` means text returned, not mathematical correctness

If `latest.json.problem_blob_sha` does not equal the current adversary problem blob, the current candidate is unmeasured. Return `WAIT_CODEX`.

## `next` after a solver result

On bare `next`:

1. Read `solver-results/problemNN/latest.json` on `adversary/problemNN`.
2. Verify its `problem_blob_sha` equals the current adversary candidate blob.
3. Follow `result_file` when needed.
4. Fetch the exact matching adversary `solution.md`.
5. Compare solver mathematics against that solution.

If the solver is correct, identify the earliest robust shortcut, harden structurally, independently verify the new solution, then update `solution.md` first and `problem.md` second on the adversary branch. The new problem blob must receive a fresh cold solve.

If the solver is wrong or materially incomplete, mark it locally stumped, stop hardening, run promotion preflight, and promote the exact tested pair.

If the solver timed out, require the expected timeout metadata, normally:

```text
local_verdict = LOCAL_STUMPED_BY_TIMEOUT
recommended_action = PROMOTE_TO_MAIN_FOR_RAINIER
promotion_ready = true
requested_model = gpt-5.5
requested_reasoning_effort = medium
timeout_seconds = 2100
```

Never promote on `SOLVER_ERROR` or infrastructure failure.

## Promotion preflight

Before writing to `main`, require at least:

- prompt nonempty and at most 2000 characters
- standalone Answer nonempty, at most 102 characters, no `\\boxed`
- consecutive `Step 1:`, `Step 2:`, ...
- final non-whitespace line of the last step exactly `Final Answer: $\\boxed{...}$`
- 1 to 5 Solution Concepts, each under 100 characters
- Domain, Sub-domain, Domain Explanation, Problem Type, Answer Type present and compatible
- Problem Type and Answer Type agree between problem and solution

Formatting-only solution repairs do not require another solver run because the measured statement blob is unchanged.

## Promotion and terminal marker

1. Capture the exact adversary solution/problem pair.
2. Update `main` solution first.
3. Update `main` problem second.
4. Re-fetch both and verify exact equality with the selected adversary pair.
5. Upsert `solver-results/problemNN/terminal.json` on the adversary branch for the exact promoted problem blob:

```json
{
  "problem": "problemNN",
  "state": "MAIN_READY_FOR_RAINIER",
  "problem_blob_sha": "<exact adversary problem blob>",
  "main_problem_blob_sha": "<verified matching main problem blob>",
  "main_solution_blob_sha": "<verified matching main solution blob>",
  "main_commit_sha": "<main commit containing promoted problem.md>",
  "reason": "LOCAL_STUMPED_PROMOTED_TO_MAIN"
}
```

6. Never copy `terminal.json`, `chat-binding.json`, or solver result/control files to `main` unless explicitly requested.

The ChatGPT-linked watcher treats the marker as terminal only when its `problem_blob_sha` exactly equals the current adversary problem blob. On a match it exits successfully. A later statement edit changes the blob and automatically invalidates the old marker.

## Official Rainier feedback

Official portal evidence outranks local evidence.

- difficulty PASS -> freeze the exact `main` statement
- difficulty FAIL/borderline -> continue on the existing adversary branch using the portal trace/JSON as stronger evidence
- any statement edit invalidates all earlier portal percentages

## Compact states

Use one of:

- `RAINIER CHECK: WAIT_CODEX`
- `RAINIER CHECK: HARDENED_WAIT_CODEX`
- `RAINIER CHECK: MAIN_READY_FOR_RAINIER`
- `RAINIER CHECK: BLOCKED_RUNNER`
