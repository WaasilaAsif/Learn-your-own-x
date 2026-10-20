# Git on the command line (for beginners)

GitHub is the website. **Git** is the tool on your computer that actually tracks your changes and talks to GitHub. This guide installs it, sets it up, and teaches the handful of commands you'll use 95% of the time.

Work through it with a terminal open. Do this **before** the workshop.

---

## 1. Install Git

**Windows:** download from [git-scm.com/downloads](https://git-scm.com/downloads) and run the installer. Accept the defaults. This also gives you **Git Bash**, a terminal you'll use for commands.

**macOS:** open Terminal and type `git --version`. If Git isn't installed, macOS offers to install it. Or install [Homebrew](https://brew.sh) and run `brew install git`.

**Linux (Debian/Ubuntu):**
```bash
sudo apt update && sudo apt install git
```

**Check it worked** — in your terminal:
```bash
git --version
```
You should see something like `git version 2.43.0`. If you do, Git is installed.

## 2. Tell Git who you are

Git stamps every change with your name and email. Set them once:

```bash
git config --global user.name "Your Name"
git config --global user.email "the-email-on-your-github-account"
```

> ⚠️ **Use the same email as your GitHub account.** If it doesn't match, your commits won't link to your profile and won't count on your contribution graph. This is the single most common beginner mistake.

Check it:
```bash
git config --global --list
```

## 3. The mental model (read this once)

Git has three places your work lives:

1. **Working directory** — your actual files, as you edit them.
2. **Staging area** — a holding zone for changes you're about to save. You `add` files here.
3. **Commit** — a permanent snapshot of the staged changes, with a message.

And then there's the **remote** — the copy on GitHub. You `push` your commits up to it and `pull` others' changes down.

So the flow is: **edit → `add` → `commit` → `push`.**

## 4. The commands you'll actually use

| Command | What it does |
|---------|--------------|
| `git init` | Start tracking a new folder with Git |
| `git clone <url>` | Download a copy of a repo from GitHub |
| `git status` | Show what's changed and what's staged — **use this constantly** |
| `git add <file>` | Stage a file (`git add .` stages everything) |
| `git commit -m "message"` | Save a snapshot of staged changes |
| `git log --oneline` | See the history of commits |
| `git branch` | List branches (the `*` is where you are) |
| `git switch -c <name>` | Create a new branch and move to it |
| `git switch <name>` | Move to an existing branch |
| `git push` | Send your commits up to GitHub |
| `git pull` | Bring GitHub's latest changes down |
| `git diff` | See exactly what you changed, line by line |
| `git remote -v` | Show which GitHub repos this folder is linked to |

## 5. Connecting to GitHub (the part that confuses everyone)

When you `push`, GitHub needs to know it's really you. A password won't work — GitHub turned that off. Pick **one** of these:

**Option A — GitHub CLI (easiest).** Install the [GitHub CLI](https://cli.github.com), then:
```bash
gh auth login
```
Follow the prompts (choose HTTPS, log in through the browser). Done — pushing just works after this.

**Option B — Personal Access Token (PAT).** When Git asks for a password during `push`, you paste a token instead:
1. GitHub → Settings → Developer settings → Personal access tokens → **Tokens (classic)** → Generate new token.
2. Give it `repo` scope, generate it, and **copy it immediately** (you won't see it again).
3. When `git push` asks for a password, paste the token.

**Option C — SSH keys** (most permanent, slightly more setup): follow GitHub's guide at [docs.github.com → connecting with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

For the workshop, **Option A is the least painful.** Set it up beforehand.

## 6. The full contribution flow (what you'll do in the workshop)

```bash
# 1. Fork the repo on GitHub (button, top right), then clone YOUR fork:
git clone https://github.com/<your-username>/git-practice.git
cd git-practice

# 2. Make a branch for your change:
git switch -c add-<your-username>

# 3. Make your change (create or edit a file), then:
git status                       # see what changed
git add .                        # stage it
git commit -m "Add me to contributors"

# 4. Push your branch to your fork:
git push -u origin add-<your-username>

# 5. Go to GitHub and open a Pull Request from your branch.
```

## 7. When something goes wrong

| Problem | Fix |
|---------|-----|
| `git: command not found` | Git isn't installed, or restart your terminal after installing |
| Push asks for a password and rejects it | You need a token or `gh auth login` — see section 5 |
| `fatal: not a git repository` | You're not inside a repo folder — `cd` into it, or you forgot `git clone` |
| Your commits don't show on your profile | Your git email doesn't match your GitHub email — fix section 2 |
| `rejected ... fetch first` | Someone pushed before you — run `git pull`, then push again |
| You committed to the wrong branch | Ask a facilitator; it's fixable and a good thing to learn |

## 8. Keep this handy

[Pro Git](https://git-scm.com/book/en/v2) (free book) chapters 2–3 cover everything above in depth. The [GitHub Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf) is a one-page PDF worth printing.

---

## You're ready for the workshop when…

- [ ] `git --version` shows a version
- [ ] `git config --global --list` shows your name and your GitHub email
- [ ] You can authenticate with GitHub (CLI, token, or SSH)
- [ ] You've read the flow in section 6 — you don't need to memorize it, just recognize it