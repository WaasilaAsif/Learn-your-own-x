# Contributing

## Small fixes

Typos, broken links, unclear explanations: open a pull request directly.

## Proposing a new module

1. Open an issue using the **Module proposal** template.
2. Once a maintainer approves it, copy `modules/_template/` to `modules/NN-your-module-name/`.
3. Build it on a branch and open a pull request when every checkpoint works from a fresh clone.

## What a module must have

- **Starter code that runs on day one.** Nobody should lose a workshop to setup.
- **Staged checkpoints**, each with a way to check it's done: a test command, an expected output, or a merged PR.
- **Honest scope:** finishable in one workshop plus a weekend. A toy version that teaches the core idea beats an ambitious one nobody finishes.
- **Further reading** for anyone who wants the real-world version.

## Review process

1. Your domain director reviews the PR first.
2. The maintainer does a final review and merges.

Expect at least one round of changes. That's normal, and it's how real open source works.

## Commit messages

Use the imperative and keep the first line under 72 characters: `Add checkpoint 3 tests to port scanner`, not `added stuff`.
