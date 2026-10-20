# 00: Git and GitHub

**You'll build:** your first merged pull request, into a practice repo
**You'll understand:** commits, branches, forks, and the pull request workflow every open source project runs on
**Time:** one in-person workshop (about 2 hours)
**Format:** in person, bring a laptop

You practice the whole workflow in a safe sandbox — the [**git-practice**](https://github.com/WaasilaAsif/git-practice) repo — where nothing can break. It follows the same idea as [first-contributions](https://github.com/firstcontributions/first-contributions): the best way to learn the open source workflow is to go through it once for real.

## Prerequisites

Before the workshop, have these ready. Setup at the venue eats the whole session.

**New to GitHub?** Walk through these two guides first — they take ~30 min total:
-[Setting up GitHub (complete beginners)](setup-github-account.md) — account, 2FA, profile
-[Git on the command line](git-cli-basics.md) — install Git, configure it, learn the commands


**Already set up?** Just confirm:
- Git installed: run `git --version` and see a version number
- A GitHub account with 2FA on
- A code editor (VS Code is fine)


## Checkpoint 1: Git knows who you are

**Goal:** your commits carry your name and email.

```bash
git config --global user.name "Your Name"
git config --global user.email "the-email-on-your-github-account"
```

Use the same email as your GitHub account, or your commits won't link to your profile.

**Check it:** `git config --global --list` shows both values.

## Checkpoint 2: Commits on your own machine

**Goal:** understand what a commit actually is before touching GitHub.

1. Make an empty folder, run `git init` in it.
2. Create a file, then run `git status`. Notice the file is untracked.
3. `git add` it, then `git status` again. It's now staged.
4. `git commit -m "Add first file"`.
5. Change the file and make a second commit.

Concepts to understand here: working directory, staging area, commit. Read [Git basics: recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) if any of those feel fuzzy.

**Check it:** `git log --oneline` shows your two commits.

## Checkpoint 3: Fork, clone, branch

**Goal:** your own copy of the practice repo to change.

1. Open the [**git-practice**](https://github.com/WaasilaAsif/git-practice) repo and click **Fork** (top right).
2. Clone **your fork**, not the original:
   ```bash
   git clone https://github.com/<your-username>/git-practice.git
   cd git-practice
   ```
3. Add the original as `upstream` (you'll need it for the bonus round, and it's good habit):
   ```bash
   git remote add upstream https://github.com/WaasilaAsif/git-practice.git
   ```
4. Make a branch for your change:
   ```bash
   git switch -c add-<your-username>
   ```

Why a fork and a branch: you can't push to someone else's repo, and branches keep each change separate so it can be reviewed on its own.

**Check it:** `git branch` shows your new branch with a `*`, and `git remote -v` shows both `origin` (your fork) and `upstream`.

## Checkpoint 4: Your pull request

**Goal:** a pull request open against the practice repo.

1. Create `contributors/<your-username>.md` using the format in the practice repo's `contributors/README.md`.
2. Commit it: `git commit -m "Add <your-username> to contributors"`.
3. Push your branch to your fork:
   ```bash
   git push -u origin add-<your-username>
   ```
4. On GitHub, open a pull request from your branch to **git-practice**'s `main`. Fill in the template.

**Check it:** your PR shows up in the practice repo's Pull requests tab.

## Checkpoint 5: Respond to review

**Goal:** get through one round of code review, the way real projects work.

A facilitator will leave at least one comment on your PR. Make the change on the same branch, commit, and push again. The PR updates by itself; you don't open a new one.

**Check it:** your PR is merged and your file is in `contributors/` on `main`. Your name's on the wall. 🎉

## Going further: a merge conflict

Pair with someone. Both of you add a line to the **same spot** in the practice repo's `guestbook.md` on separate branches, and open PRs. Whoever merges second gets a conflict. Resolve it locally: `git merge main`, fix the `<<<<` `====` `>>>>` markers, keep both lines, commit, push. Merge conflicts look scary until you've fixed one.

## Further reading

- [Pro Git](https://git-scm.com/book/en/v2), free, chapters 2 and 3 cover everything you used today
- [first-contributions](https://github.com/firstcontributions/first-contributions)
- [Good first issues](https://goodfirstissue.dev), when you're ready for a real project
- [Git cheatsheet](git-cheatsheet.md) — commands, flags, and advanced tricks

## Done? Make it count

The practice repo is a sandbox — it gets reset each semester. Your **real** first contribution is adding yourself to the [Learn Your Own X](https://github.com/WaasilaAsif/learn-your-own-x) repo once you finish a module. Same workflow, a repo that sticks.

Post your merged practice PR link in the module 00 thread on the Discord. That merged PR earns your **First PR 🎉** badge — your first one is the hardest, and you just did it.

---

## For facilitators

- Send the prerequisites at least 3 days before, and again the day before.
- Keep one helper per 8 to 10 people walking the room. Most blockers are setup, not concepts.
- Review PRs live on the projector during checkpoint 5, so the room sees what review looks like. Leave a real, kind comment on each PR so everyone does a review round.
- Branch protection on the practice repo's `main` (require one approval) makes the review step real.
- Reset the practice repo between cohorts: delete merged `contributors/*` files and reset `guestbook.md`, or just re-create the repo from a clean template.
