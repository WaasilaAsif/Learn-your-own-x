# Shell Cheatsheet 🐚

The commands, flags, and pipelines from module 01, plus the ones you'll reach for next. Keep it open in a tab.

> **stdin / stdout / pipe:** a command reads **stdin** and writes **stdout**. `A | B` feeds A's stdout into B's stdin. Build a pipeline left to right; each stage does one job.

---

## Navigate and look

| Command | What it does |
|---|---|
| `pwd` | Print the directory you're in |
| `ls -l` / `ls -la` | Long listing / also hidden dotfiles |
| `cd <dir>` / `cd ..` / `cd` | Move into / up one / to home |
| `cat <file>` | Dump a whole file |
| `head -n 5` / `tail -n 5` | First / last 5 lines |
| `tail -f <file>` | Follow a file as it grows (live logs) |
| `less <file>` | Scroll a big file (`q` quits, `/` searches) |
| `wc -l` / `wc -w` | Count lines / words |
| `man <cmd>` / `<cmd> --help` | The manual / quick help |

## Filter, sort, count

| Command | What it does |
|---|---|
| `grep 'pat' f` | Lines matching `pat` |
| `grep -c 'pat' f` | **C**ount matching lines |
| `grep -i` / `-v` / `-n` | Case-**i**nsensitive / in**v**ert / show line **n**umbers |
| `grep -E 'a|b'` | **E**xtended regex (alternation, `[45][0-9][0-9]`, …) |
| `grep -r 'pat' dir/` | **R**ecursive, search a whole tree |
| `sort` / `sort -r` / `sort -n` | Order lines / reverse / numeric |
| `sort -u` | Sort and drop duplicates |
| `uniq -c` | Collapse **adjacent** duplicate lines, prefix a count |
| `cut -d',' -f2` | Field 2, splitting on `,` |
| `tr 'a-z' 'A-Z'` | Translate/replace characters |

> **The counting pipeline** — memorize this one:
> ```bash
> awk '{print $1}' file | sort | uniq -c | sort -rn | head
> ```
> Pick a column → sort so equals are adjacent → `uniq -c` counts → sort by count desc → top N. `uniq` only sees *adjacent* lines, so the `sort` before it is mandatory.

## awk and sed (mini-languages)

| Command | What it does |
|---|---|
| `awk '{print $1}'` | Print field 1 (whitespace-separated) |
| `awk '{print $NF}'` | Print the **last** field (`NF` = number of fields) |
| `awk '$9 == 404'` | Print lines where field 9 equals 404 |
| `awk '{s+=$NF} END{print s}'` | Sum the last column |
| `sed 's/old/new/g'` | Replace `old` with `new` on every line |
| `sed -n '5,10p'` | Print only lines 5–10 |

## Redirection and pipes

| Syntax | What it does |
|---|---|
| `cmd > file` | Send stdout to `file` (**overwrite**) |
| `cmd >> file` | **Append** stdout to `file` |
| `cmd 2> file` | Send stderr (errors) to `file` |
| `cmd > out 2>&1` | stdout **and** stderr to `out` |
| `cmd < file` | Feed `file` as stdin |
| `A | B` | A's stdout → B's stdin |
| `cmd1 && cmd2` | Run `cmd2` only if `cmd1` succeeded |
| `cmd1 || cmd2` | Run `cmd2` only if `cmd1` failed |

## Scripting building blocks

```bash
#!/usr/bin/env bash           # shebang: which interpreter runs this file
set -euo pipefail             # exit on error / unset var / failed pipe stage

name="access"                 # NO spaces around =
echo "file is ${name}.log"    # ${...} to use a variable

count=$(wc -l < "$1")         # $(...) captures a command's output; $1 = first arg

for code in 200 404 500; do   # loop
  echo "$code"
done

if [ "$count" -gt 100 ]; then # conditional ( -gt -lt -eq ; use [[ ]] in bash )
  echo "big"
else
  echo "small"
fi

greet() { echo "hi $1"; }     # a function
greet world
```

> **Quote your variables.** Always `"$var"`, not `$var` — an unquoted value with a space or `*` in it gets split or glob-expanded and breaks your script in ways that are miserable to debug.

## Find files and fan out

| Command | What it does |
|---|---|
| `find . -name '*.log'` | Every `.log` file under here |
| `find . -type f -mtime -1` | Files modified in the last day |
| `find . -name '*.log' | xargs wc -l` | Run `wc -l` on all of them |
| `which <cmd>` | Where a command lives on `$PATH` |

## Permissions and running scripts

| Command | What it does |
|---|---|
| `chmod +x script.sh` | Make it executable |
| `./script.sh` | Run an executable script in this folder |
| `bash script.sh` | Run it with bash without `+x` |

---

## Keyboard survival

| Keys | Does |
|---|---|
| `Tab` | Autocomplete a path or command |
| `↑` / `↓` | Previous / next command |
| `Ctrl-R` | Search command history (type, `Ctrl-R` again to cycle) |
| `Ctrl-C` | Kill the running command |
| `Ctrl-L` | Clear the screen |
| `Ctrl-A` / `Ctrl-E` | Jump to start / end of the line |

## Go deeper

- [Missing Semester](https://missing.csail.mit.edu/) — the source course ⭐
- [ExplainShell](https://explainshell.com/) — decode any command
- [ShellCheck](https://www.shellcheck.net/) — lint your scripts
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
