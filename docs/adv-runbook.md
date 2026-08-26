# adv — runbook

Adversarial difficulty loop, many problems at once.

The loop: GPT-5.5 medium tries the problem blind. The Sol chat that authored it
checks the attempt. Solver right → too easy → Sol hardens → try again. Solver
wrong → PASS.

Both models stay in ChatGPT web and you drive them, so it runs on free Plus chat
quota. `adv` never touches chatgpt.com — it moves text through your clipboard,
routes each reply to the right problem, and rewrites the files.

---

## 0. One-time check

```bash
cd ~/workspace/freelance/hd-techlabs-math-skills-copy
python3 --version          # 3.9+
which powershell.exe       # WSL clipboard bridge
./scripts/adv --help
```

---

## 1. Start the watcher

One terminal, left running all day:

```bash
./scripts/adv watch
```

Every capture is reported there. Keep it visible. Everything else happens in a
second terminal.

---

## 2. Register problems

A problem needs `problem.md` and `solution.md` already written — `adv` hardens
existing problems, it does not create them.

```bash
./scripts/adv add problem09 problem12 problem17
```

Prefixes work when unambiguous. `problem9` matching both `problem90-...` and
`problem91-...` is refused — type more characters.

---

## 3. Name the Sol chats

Rename each authoring chat to its problem slug, e.g.
`problem09-dynamical-systems`. For your eyes only — routing uses a tag inside
the message, not the chat title — but with several chats open you need it.

---

## 4. Send the problem to the solver

```bash
./scripts/adv next problem09
```

Open a **new** chat, GPT-5.5 Thinking/medium, `Ctrl+V`, Enter.

The problem text is embedded in the prompt and the solver is told **not** to use
the GitHub connector. That matters: `solution.md` sits in the same folder as
`problem.md`, so a solver allowed to browse the repo would just read the answer.

Do not wait — fire off the others too:

```bash
./scripts/adv next problem12
./scripts/adv next problem17
```

---

## 5. Copy each answer as it lands

Click ChatGPT's **Copy** button. The watcher picks it up:

```
[adv] problem12-...: solver attempt captured (round 1)
      → next: paste into the Sol chat  [adv next problem12-...]
```

Any order, any number of chats. Each reply carries its own
`=== PROBLEM: <slug> ===` tag, so nothing gets mixed up.

---

## 6. Send the attempt to the author

```bash
./scripts/adv next problem12
```

Paste into the **existing Sol chat for that problem** — continue that
conversation, do not open a new one. It remembers which routes it already
blocked.

Copy Sol's reply. Two outcomes:

```
[adv] problem12-...: TOO_EASY → hardened, now round 2, committed a1b2c3d, pushed
[adv] problem12-...: PASS after 2 round(s) — solver never established the...
```

---

## 7. The board

```bash
./scripts/adv status
```

```
SLUG                              ROUND  WAITING FOR   LAST
problem09-dynamical-systems           2  5.5 solve     just now
problem12-generating-functions        1  Sol check     3m ago
problem17-linear-transformations      2  PASS ✓        1m ago
```

---

## 8. GitHub mode vs embedded mode

The author step has two modes, chosen automatically.

**GitHub mode** — used when `adv` can push. The prompt is ~15 lines: it tells Sol
to read `problem.md`, `solution.md`, and `skills/math-harder/SKILL.md` straight
from the repo at a named commit. `adv` commits and pushes before generating the
prompt, so the repo always has the current version.

Because a connector can serve a cached copy, the prompt also asks Sol to echo

```
=== READ-CHECK: <last non-empty line of problem.md> ===
```

If that line does not match the local file, `adv` refuses the verdict:

```
[adv] refused: STALE READ — the author read an older problem.md.
```

Ask Sol to re-read from GitHub, then copy again. Override with
`adv catch <slug> --force` only if you are certain.

**Embedded mode** — used automatically when the push fails:

```
[adv] push failed (Permission ... denied to <user>) — embedding the files in the
      prompt instead of pointing at GitHub
```

The prompt then carries the full problem and solution (~290 lines) and drops the
READ-CHECK, since there is no repo read to verify. Correct either way, just a
longer paste.

Force embedded mode regardless: `ADV_EMBED=1 ./scripts/adv next <slug>`.

### Enabling GitHub mode

GitHub mode needs push rights on `vohavinhtan/hd-skill-problem`. Check:

```bash
git push --dry-run origin main
```

A `403 ... denied to <someone-else>` means the stored credential belongs to
another account. Fix the credential (or switch the remote to SSH), then GitHub
mode turns on by itself.

---

## 9. When something goes sideways

**Reply came back without the `=== PROBLEM: ... ===` tag.**

```bash
./scripts/adv catch problem12
```

**The authoring Sol chat is gone.**

```bash
./scripts/adv reseed problem12
```

The next author prompt embeds everything a fresh Sol chat needs.

This is now mostly automatic. `adv` fingerprints `problem.md` + `solution.md`
every time it hands them to a chat, and any author prompt built while the chat
cannot be shown to hold that exact pair carries the current files with it —
after `adv add`, after a reviewer pass done in another conversation, after a
hand edit, a `git pull`, or a merged PR. `adv reseed` only forces the same thing
by hand.

**`adv add` refuses: a newer version exists on the remote.**

```
[adv] error: problem70-generating-functions: a newer version of this problem
      exists on the remote, not in your working tree:
          origin/problem70-clean-redesign  (2 commit(s) this folder does not have)
```

Every read in `adv` goes to the working tree, so a problem revised in another
clone — or sitting on a PR branch that was never merged into the checked-out
branch — would run the whole loop against the superseded copy. `adv add` fetches
origin and refuses instead. Pull or check the branch out, then add. `--force`
registers the working-tree copy anyway.

The check is on `add` only, because that is where a problem enters the loop. It
compares the folder against every remote ref, not just the current branch, and a
fetch failure downgrades to a warning rather than a refusal.

**`STALE` after the current files were pasted.**

```
[adv] refused: the current problem.md and solution.md were pasted into that chat
      with this attempt, so STALE cannot mean the repo is behind
```

Nothing is written. `STALE` is only believed for a bare-attempt paste, where the
chat is the only holder of the current version; when the files travelled with
the attempt, a `STALE` reply is the chat answering from an older memory, and
adopting it would revert whatever last changed the folder. Open a fresh Sol chat
and re-send: `adv reseed <slug> && adv next <slug>`.

**`TOO_EASY` but the reply was truncated.**

```
[adv] refused: TOO_EASY but the reply carried ['problem.md']
```

Nothing was written. Ask Sol to resend both files complete, then copy again.

**Wrong stage.**

```
[adv] refused: problem09-... awaits the author verdict, not a solver attempt
```

Check `adv status` and send what it is actually waiting for.

---

## 10. Artifacts

```
.tmp/adv/<slug>/
  attempt.md                 latest solver attempt
  round01-attempt.md         per-round solver attempts
  round01-verdict.md         per-round author verdicts
  versions/problem.r1.md     the problem before each hardening
  versions/solution.r1.md
.tmp/adv/state.json          the board
```

Delete `state.json` to reset the board; problem folders are untouched.

Each hardening is also a git commit, so `git log -- <problem folder>` is the
evolution history of that problem.

---

## Commands

| Command | What it does |
|---|---|
| `adv watch [secs]` | daemon; capture replies, apply them, advance state |
| `adv add [--force] <slug>...` | register problems — fetches origin first and refuses a working-tree copy the remote has moved past |
| `adv next <slug>` | load that problem's next prompt into the clipboard |
| `adv status` | board of every registered problem |
| `adv catch <slug> [--force]` | force-route the current clipboard to that problem |
| `adv show <slug>` | state and per-round history |
| `adv reseed <slug>` | embed problem+solution in the next author prompt |
| `adv drop <slug>...` | unregister (files and artifacts kept) |

## Safety

`adv` refuses rather than guesses. It ignores untagged clipboard content, its own
prompts, unregistered slugs, replies for the wrong stage, and duplicate copies;
it rejects a verdict written against a stale read; and it never overwrites
`problem.md` unless the reply carried **both** complete files.
