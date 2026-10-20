# Git Cheatsheet 🧾

Everyday commands, the flags that actually matter, and a "flex" section for when you want to look like you've been doing this for years. Keep it open in a tab.

> **Flag vs argument:** a *flag* (also called an option or directive) changes how a command behaves. Short flags start with one dash (`-m`), long ones with two (`--message`). Many short flags can be stacked: `git commit -am "msg"` = `-a` + `-m`.

---

## Setup (once per machine)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"   # must match GitHub
git config --global init.defaultBranch main         # new repos start on 'main'
git config --global --list                          # see your config
```

## Start a repo

| Command | What it does |
|---------|--------------|
| `git init` | Start tracking the current folder |
| `git clone <url>` | Copy a GitHub repo to your machine |
| `git clone <url> myfolder` | Clone into a folder named `myfolder` |

## The everyday loop

| Command | What it does |
|---------|--------------|
| `git status` | What's changed / staged — run this constantly |
| `git add <file>` | Stage one file |
| `git add .` | Stage everything in the current folder |
| `git commit -m "msg"` | Commit staged changes with a message |
| `git commit -am "msg"` | Stage **tracked** files **and** commit, in one step (`-a` + `-m`) |
| `git diff` | See unstaged changes, line by line |
| `git diff --staged` | See what's staged (about to be committed) |
| `git log --oneline` | Compact history, one line per commit |

## Branching

| Command | What it does |
|---------|--------------|
| `git branch` | List branches (`*` = current) |
| `git switch <name>` | Move to an existing branch |
| `git switch -c <name>` | **C**reate a branch and move to it |
| `git branch -d <name>` | **D**elete a merged branch (safe) |
| `git branch -D <name>` | Force-delete a branch, even if unmerged ⚠️ |
| `git merge <name>` | Merge `<name>` into your current branch |

## Working with GitHub (remotes)

| Command | What it does |
|---------|--------------|
| `git remote -v` | Show linked remotes (`origin` = your fork) |
| `git remote add upstream <url>` | Add the original repo as `upstream` |
| `git push` | Send commits to the remote |
| `git push -u origin <branch>` | Push **and** set the branch to track it (`-u`). First push of a branch. |
| `git pull` | Fetch + merge the remote's changes |
| `git fetch` | Download changes **without** merging them yet |

## Undoing things (handle with care)

| Command | What it does |
|---------|--------------|
| `git restore <file>` | Discard unstaged changes to a file |
| `git restore --staged <file>` | Unstage a file (keep the edits) |
| `git commit --amend` | Edit the **last** commit (message or contents) |
| `git reset --soft HEAD~1` | Undo last commit, **keep** changes staged |
| `git reset --mixed HEAD~1` | Undo last commit, keep changes **unstaged** (default) |
| `git reset --hard HEAD~1` | Undo last commit and **delete** the changes ⚠️ |
| `git revert <commit>` | Make a **new** commit that undoes an old one (safe for shared history) |

> **`reset` vs `revert`:** `reset` rewrites history (dangerous on branches others use). `revert` adds a new commit, so it's safe to push. On a shared branch, prefer `revert`.

## The flags worth knowing

| Flag | Means | Example |
|------|-------|---------|
| `-m` | message | `git commit -m "fix"` |
| `-a` | all tracked files | `git commit -am "fix"` |
| `-u` | set upstream (track) | `git push -u origin main` |
| `-b` | branch | `git checkout -b feature` |
| `-f` / `--force` | **force** — override Git's safety checks ⚠️ | `git push -f` |
| `--amend` | change the last commit | `git commit --amend` |
| `-d` / `-D` | delete / force-delete branch | `git branch -d old` |
| `--oneline` | compact one-line output | `git log --oneline` |
| `-p` | patch (pick changes interactively) | `git add -p` |

> ⚠️ **`-f` / `--force` is the one to respect.** `git push -f` overwrites what's on GitHub with your version — it can erase other people's commits. On a shared branch, use `--force-with-lease` instead: it refuses to overwrite if someone else pushed since you last pulled. Never force-push to `main`.

## Stashing (park work without committing)

| Command | What it does |
|---------|--------------|
| `git stash` | Shelve your changes, clean the working directory |
| `git stash pop` | Bring the shelved changes back |
| `git stash list` | See all stashes |

---

## 🥷 Flex your Git knowledge

The commands that separate "I can commit" from "I actually understand Git."

### Visualize the commit tree
```bash
git log --oneline --graph --all --decorate
```
Draws the branch/merge structure as an ASCII tree, right in your terminal. Make it an alias (below) and you'll use it every day.

### Tag releases
```bash
git tag v1.0.0                      # lightweight tag on the current commit
git tag -a v1.0.0 -m "First release"  # annotated tag (has author + message + date)
git push origin v1.0.0              # tags don't push automatically — push them
git tag                             # list tags
```
> Annotated tags (`-a`) are what you use for real releases; they store who, when, and why. GitHub turns pushed tags into Releases.

### Find who changed a line, and when
```bash
git blame <file>        # line-by-line: which commit (and who) last touched each line
```

### Find the commit that broke something (binary search)
```bash
git bisect start
git bisect bad          # current version is broken
git bisect good <commit> # this old one worked
# Git checks out the midpoint; you test and mark good/bad until it finds the culprit
git bisect reset
```

### Rescue "lost" commits
```bash
git reflog              # a log of EVERYWHERE HEAD has been — even after a bad reset
```
> `reflog` is your safety net. Did a `reset --hard` and panicked? Your commit is almost always still in the reflog. Copy its hash and `git checkout` or `git reset` back to it.

### Copy one commit onto another branch
```bash
git cherry-pick <commit>   # apply a single commit from elsewhere onto your branch
```

### Rewrite history interactively (squash, reorder, reword)
```bash
git rebase -i HEAD~3    # edit the last 3 commits: squash, reword, drop, reorder
```
> Powerful and a little dangerous — only rebase commits you **haven't pushed/shared**.

### Make your own shortcuts
```bash
git config --global alias.tree "log --oneline --graph --all --decorate"
git config --global alias.st "status -s"
# now: git tree   and   git st
```

### Clean up junk files
```bash
git clean -n       # preview what would be deleted (dry run)
git clean -fd      # actually delete untracked files and folders 
```

---

## Go deeper

- [W3Schools Git](https://www.w3schools.com/git/) — beginner-friendly ⭐
- [Learn Git Branching](https://learngitbranching.js.org/) — interactive, visual
- [Pro Git](https://git-scm.com/book/en/v2) — the free, complete reference
- [GitHub cheat sheet PDF](https://education.github.com/git-cheat-sheet-education.pdf)