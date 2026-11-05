# Buildathon: The Most Inconvenient Feature

> A Learn Your Own X buildathon. Build something that **works perfectly** and is
> **miserable to use.** The engineering is real; the UX is a crime.

**You'll build:** a feature that does its job correctly but is maximally tedious, confusing, or absurd to actually use
**You'll understand:** that good UX is *invisible* — the fastest way to learn what makes an interface good is to deliberately make it terrible and watch people suffer
**Format:** solo or teams of up to 3 · one evening of building · demo + vote at the end
**Submission:** add a row to the [submissions table](#submissions) with links (see [How to submit](#how-to-submit))

---

## The one rule that matters

**It has to actually work.** An inconvenient feature is still a *working* feature — you must be able to complete the task with it, start to finish. A thing that's broken isn't inconvenient, it's just broken, and it won't score.

Pick any ordinary task — set a timer, pick a date, enter a password, choose a volume, agree to terms — and implement it so it *functions correctly* but is agony to use.

### What scores

| Criterion | What judges look for |
|-----------|----------------------|
| **It works** | The task can be completed every time. No crashes, no dead ends. |
| **Inventive cruelty** | The inconvenience is *creative*, not just slow. Make us groan, then laugh. |
| **Commitment** | It's polished enough that the awfulness feels intentional, not accidental. |
| **The reveal** | A 30-second live demo where the room collectively winces. |

### What's out of bounds

- Anything that doesn't complete the task (broken ≠ inconvenient).
- Dark patterns that actually harm someone (stealing data, charging money, tricking real consent). Inconvenient is funny; malicious is not. Keep it a sandbox.
- Shock content. Keep it demo-able to the whole room.

## Need inspiration?

The genre is real and glorious: [r/badUIbattles](https://www.reddit.com/r/badUIbattles/), the [User Inyerface](https://userinyerface.com/) game, [The Password Game](https://neal.fun/password-game/), and the classic "set the volume with a maze" entries. The point of all of them: the feature **works** — that's what makes it torture.

A worked, runnable example lives in [`example/`](example/) — **The Inconvenient Timer**. It's a real countdown timer; you just can't set it without losing your mind. Read its [README](example/README.md) to see the exact format your own entry can follow, including how it still passes a "does it work?" check.

## How to submit

1. Build your feature. A single self-contained `index.html` is perfect (no build step, opens anywhere), but any runnable project is fine.
2. Put it somewhere with a link — a GitHub repo, a Gist, a GitHub Pages URL, a CodePen, or a short screen-recording.
3. **Add one row to the [submissions table](#submissions) below** via a pull request. Keep the description to one line. Fill every column.
4. Open the PR to the `buildathon` branch. Title it `Submit: <your feature name>`.

That PR *is* your entry. (Bonus: for many of you this is also real practice of the module 00 fork → branch → PR workflow.)

## Submissions

Add your entry as a new row. Newest at the bottom. Keep the example row at the top as the format reference.

| Feature name | What it does (and why it's torture) | Team | Link |
|--------------|-------------------------------------|------|------|
| The Inconvenient Timer (example) | A working countdown timer you can only set by clicking "+1 second" — and the button runs away | Maintainers | [example/](example/) |
| _Your feature_ | _one line_ | _you_ | _repo / demo / video_ |

---

## For facilitators

- **Say the one rule loudly and often: it must still work.** Most entries drift toward "broken." Judge a quick does-it-complete-the-task check before the vote.
- Timebox hard: ~90 min to build, 30 sec/team to demo, then a show-of-hands vote. The demo is the whole event — keep it moving.
- Hand out `example/` at the start so nobody stalls on setup; it doubles as the submission-format reference.
- Keep it kind. The target is *interfaces*, never people. Shut down anything that crosses into real dark patterns or shock content.
- A projector + one laptop per team is enough. No internet required if entries are single-file HTML.
