# 01: Shell and scripting

**You'll build:** a shell script that reads a server log and prints a summary report
**You'll understand:** how the shell, pipes, and the standard Unix tools compose into a data-processing pipeline — the "glue" every developer reaches for
**Time:** one in-person workshop (about 2 hours)
**Format:** in person, bring a laptop

The shell is the oldest and most reusable tool you'll learn. Once you can chain `grep`, `sort`, and `awk` with a pipe, you can answer questions about any text file — logs, CSVs, code — in seconds, without writing a program. This module adapts the shell and scripting lectures from MIT's [**Missing Semester**](https://missing.csail.mit.edu/) into a hands-on sandbox.

You work in the [`starter/`](starter/) folder — a safe sandbox with a sample web-server log and nothing you can break. Everything is text files; experiment freely.

## Prerequisites

Before the workshop:

- **A Unix-style shell.**
  - **Windows:** use **Git Bash** (it came with Git from module 00). Not PowerShell, not CMD — the commands below are bash.
  - **macOS / Linux:** the built-in **Terminal** is already bash or zsh; either works.
- Confirm you have the standard tools — run this and expect no errors:
  ```bash
  echo "shell ok"; grep --version | head -1; awk --version 2>/dev/null | head -1 || echo awk present
  ```
- A code editor (VS Code is fine) to edit the script.

## Setup

Clone this repo (or `git pull` if you cloned it for module 00), then:

```bash
cd modules/01-shell-and-scripting/starter
ls -la            # see what's here
head logs/access.log
```

You're set up when `head logs/access.log` prints lines that look like web requests (an IP, a date, a `"GET /path"`, and a status code like `200` or `404`).

## The mental model (read once)

Three ideas carry the whole module:

1. **Everything is text, and the shell streams it.** A program reads from **stdin** and writes to **stdout**. 
2. **A pipe `|` connects them:** `A | B` sends A's output straight into B's input. You build a pipeline left to right, each stage doing one small transformation.
3. **Each tool does one thing.** `grep` filters lines, `sort` orders them, `uniq` collapses duplicates, `wc` counts, `cut`/`awk` pick out columns. Combined, they're a query engine.

So "how many 404s are in this log?" becomes: *filter to 404 lines, then count them.*

## Checkpoint 1: Move around and look

**Goal:** read files and navigate without a mouse.

In `starter/`, try each and notice what the flags change:

```bash
ls -l            # long listing: permissions, size, date
ls -la            # also show hidden (dotfiles)
wc -l logs/access.log      # how many lines (requests) total?
head -5 logs/access.log    # first 5 lines
tail -5 logs/access.log    # last 5 lines
less logs/access.log       # scroll (q to quit) — for files too big for the screen
man wc                     # the manual. On Git Bash, 'wc --help' if man is missing
```

**Check it:** `wc -l logs/access.log` prints `120`. That's your request count.

## Checkpoint 2: Pipes and filters

**Goal:** answer real questions by chaining tools with `|`.

A log line looks like:

```
203.0.113.7 - - [10/Oct/2026:13:02:00 +0000] "GET / HTTP/1.1" 200 1024
```

The **status code** is the number right after the `"..."` request (e.g. `200`, `404`). Work these out:

```bash
# How many requests returned 404 (not found)?
grep -c '" 404 ' logs/access.log

# How many were errors — any 4xx or 5xx code? (-E turns on extended regex)
grep -cE '" [45][0-9][0-9] ' logs/access.log

# The first field of each line is the client IP. Pull it out with awk:
awk '{print $1}' logs/access.log | head

# Now the classic pipeline: who made the most requests?
awk '{print $1}' logs/access.log | sort | uniq -c | sort -rn | head
```

That last line is the one to understand deeply: **pick the column → sort so identical values are adjacent → `uniq -c` counts runs → sort by that count, descending.** This five-stage pattern answers a huge fraction of real log questions.

**Check it:** your numbers match these exactly:

| Question | Answer |
|---|---|
| 404s | `25` |
| Errors (4xx + 5xx) | `48` |
| Busiest client IP | `203.0.113.7` (46 requests) |
| Unique client IPs | `4` |

(Unique IPs: `awk '{print $1}' logs/access.log | sort -u | wc -l`.)

## Checkpoint 3: Variables, a loop, a conditional

**Goal:** the three building blocks of any script.

Type these straight into the shell (they work interactively too):

```bash
# a variable (no spaces around =), and using it:
name="access"
echo "reading ${name}.log"

# a loop over the status codes you care about:
for code in 200 404 500; do
  n=$(grep -cE "\" $code " logs/access.log)
  echo "$code -> $n"
done

# a conditional: warn if there are too many errors
errors=$(grep -cE '" [45][0-9][0-9] ' logs/access.log)
if [ "$errors" -gt 20 ]; then
  echo "WARNING: $errors error responses"
else
  echo "errors look normal ($errors)"
fi
```

Note `$(...)` — **command substitution** — captures a command's output into a variable. That's the bridge between the pipelines from checkpoint 2 and the logic here.

**Check it:** the loop prints `200 -> 53`, `404 -> 25`, `500 -> 9`; the conditional prints the WARNING line (there are 48 errors).

## Checkpoint 4: Write the report script

**Goal:** save your work as a reusable, robust script.

Open [`starter/report.sh`](starter/report.sh). It's a skeleton with three `TODO`s. Fill each one using what you built above, so that:

```bash
bash report.sh logs/access.log
```

prints exactly:

```
Total requests: 120
Error responses: 48
Top client: 203.0.113.7
```

Three details that make it a *real* script, not just pasted commands — they're already in the skeleton, make sure you understand them:

- **`#!/usr/bin/env bash`** (the *shebang*) — the first line tells the system which interpreter to run. With it and `chmod +x report.sh`, you can run `./report.sh` directly.
- **`set -euo pipefail`** — exit on the first error, on an unset variable, or on a failed command inside a pipe. Without it, a script sails past failures and produces garbage. Put it at the top of every script you write.
- **`"${1:?usage: ...}"`** — `$1` is the first argument (the log file). The `:?` prints your usage message and exits if it's missing.

**Check it:**

```bash
bash check.sh
```

It runs your script against the sample log and verifies all three lines. You want:

```
PASS — checkpoint 4 complete ✅
```

## Going further

- **Make it executable:** `chmod +x report.sh`, then `./report.sh logs/access.log`. Check `ls -l` — see the `x` permission bits appear.
- **`find` + `xargs`:** `find . -name '*.log' | xargs wc -l` counts lines across every log file at once.
- **A function and an alias:** add `alias ll='ls -la'` to your `~/.bashrc` (your *dotfile*), open a new shell, and `ll` works everywhere. Dotfiles are how you carry your setup between machines.
- **`sed` / `awk` as mini-languages:** `awk '{sum+=$NF} END {print sum}' logs/access.log` sums the last column (bytes sent). `awk` alone can do most of what the pipeline above does.
- Do the Missing Semester [shell](https://missing.csail.mit.edu/2026/course-shell/) and [command-line environment](https://missing.csail.mit.edu/2026/command-line-environment/) exercises — `marco`/`polo`, a retry loop, `pidwait`. They're excellent and build straight on this.

## This module is one slice of a larger source

Missing Semester is a whole course, and every lecture is a candidate module in this spirit. Good next ones to adapt into this sandbox format:

- **Debugging and profiling** — `gdb`/`pdb`, `strace`, `perf`, flame graphs, `hyperfine` ([lecture](https://missing.csail.mit.edu/2026/debugging-profiling/)).
- **The development environment** — editors, `tmux`, dotfiles as a tracked repo ([lecture](https://missing.csail.mit.edu/2026/development-environment/)).
- **Data wrangling** — `sed`, `awk`, regex at scale ([2020 lecture](https://missing.csail.mit.edu/2020/data-wrangling/)).

If you adapt one, follow [`modules/_template/`](../_template/) and the [contributing guide](../../CONTRIBUTING.md). Don't just replay a lecture — turn it into checkpoints with a sandbox and a `check` step, the way this one did.

## Further reading

- [Missing Semester](https://missing.csail.mit.edu/) — the source course, free, CC BY-NC-SA. Watch the [shell lecture](https://missing.csail.mit.edu/2026/course-shell/).
- [ExplainShell](https://explainshell.com/) — paste any command, see what every flag means.
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) — a dense, respected one-page reference.
- [ShellCheck](https://www.shellcheck.net/) — paste a script, get your bugs found. Install it and run `shellcheck report.sh`.
- [Shell cheatsheet](shell-cheatsheet.md) — the commands and flags from this module in one place.

## Done? Make it count

Post your `bash check.sh` output (the `PASS` line) in the module 01 thread on the Discord to earn the module role.

Your **real** next contribution: the pipelines you learned here are exactly how you'll explore an unfamiliar codebase. Try them on this repo — `grep -rn "checkpoint" modules/ | wc -l`.

---

## For facilitators

- Send the prerequisites 3 days ahead. The one blocker is Windows users on PowerShell instead of Git Bash — check this first thing.
- The sample log is deterministic (seeded), so every expected number in the README is exact and the same on every machine. If you edit `starter/logs/access.log`, recompute the four answers and the `check.sh` expected lines.
- Demo checkpoint 2's five-stage pipeline live, adding one stage at a time (`awk` → `| sort` → `| uniq -c` → `| sort -rn` → `| head`) so the room sees the output change at each `|`. That one pattern is the whole point.
- Keep one helper per 8–10 people. Most questions are quoting and spaces-around-`=`.
