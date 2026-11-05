# Buildathon: The Most Useless Feature

> A Learn Your Own X buildathon. Build something that works flawlessly and is
> **completely, gloriously pointless.** If it's useful, it's disqualified.

**You'll build:** a feature that does *something*, does it reliably, and accomplishes absolutely *nothing* of value
**You'll understand:** what "value" in software actually means — by building the purest possible absence of it, and defending why it's useless
**Format:** solo or teams of up to 3 · one evening of building · demo + vote at the end
**Submission:** add a row to the [submissions table](#submissions) with links (see [How to submit](#how-to-submit))

---

## The one rule that matters

**If it fixes a problem, it is not submittable.**

Your feature must not solve anything. It cannot save time, inform, organize, communicate, automate, or produce anything a person would actually want. The test: *remove it, and nothing of value is lost.* If you can finish the sentence "this is handy because…", you've failed — go make it more pointless.

It must still **work**, though. A useless feature is reliably, confidently useless. It runs every time and does its nothing on command. Broken is not the same as useless.

### What scores

| Criterion | What judges look for |
|-----------|----------------------|
| **Genuinely useless** | Passes the "remove it, nothing is lost" test. No sneaky utility. |
| **It works** | It performs its pointless act reliably and on purpose. |
| **Commitment to the bit** | Polished, confident, straight-faced. The more serious the packaging, the funnier the void inside. |
| **The defense** | You can argue, convincingly, that it solves no problem. (This is checkpoint 4 in the example.) |

### Where's the line? (useless vs useful)

- A button that counts how many times you clicked it → **useless.** ✅
- A button that counts your water intake for the day → useful (health tracking). ❌
- A clock showing the time on Mars you'll never visit → **useless.** ✅
- A clock showing your next class → useful. ❌
- "But it's *entertaining*!" → mild amusement is an allowed *side effect* of the bit, but it can't be the point. A real game or meme generator people actually enjoy using has crossed into useful. Aim for pointless-that-happens-to-be-funny, not fun-that-happens-to-be-silly.

### Out of bounds

- Anything that secretly *is* useful (that's the whole disqualifier).
- Wasting shared resources for real (crypto mining, spamming an API, hammering someone's server). Useless, not harmful.
- Shock content. Keep it demo-able to the whole room.

## Need inspiration?

This is a celebrated art form: the [Useless Machine](https://en.wikipedia.org/wiki/Useless_machine) (a box whose only function is to switch itself off), [The Useless Web](https://theuselessweb.com/), Simone Giertz's [shitty robots](https://www.youtube.com/@simonegiertz), and a hundred "button that does nothing" projects. Every one *works*. None of them *help*.

A worked, runnable example lives in [`example/`](example/) — **The Useless Machine**: a switch that always turns itself back off, so you can never leave it on. Read its [README](example/README.md) for the exact format your entry can follow, including the "prove it's useless" step.

## How to submit

1. Build your pointless feature. A single self-contained `index.html` is perfect, but any runnable project is fine.
2. Put it somewhere with a link — a GitHub repo, a Gist, a GitHub Pages URL, a CodePen, or a short screen-recording.
3. **Add one row to the [submissions table](#submissions) below** via a pull request. One-line description, and one line defending its uselessness.
4. Open the PR to the `buildathon` branch. Title it `Submit: <your useless thing>`.

That PR *is* your entry. (For many of you it's also real practice of the module 00 fork → branch → PR workflow.)

## Submissions

Add your entry as a new row. Newest at the bottom. Keep the example row at the top as the format reference.

| Feature name | What it does | Why it's useless | Team | Link |
|--------------|--------------|------------------|------|------|
| The Useless Machine (example) | A switch that flips itself back off every time you turn it on | You can never leave it on, so it achieves nothing | Maintainers | [example/](example/) |
| _Your feature_ | _one line_ | _one line_ | _you_ | _repo / demo / video_ |

---

## For facilitators

- **The judging gate is the uselessness rule, not polish.** Before the vote, ask each team "what problem does this solve?" If they can answer honestly, it's disqualified. The best entries make the room laugh at *how hard* it is to defend as useless.
- Timebox: ~90 min build, 30 sec/team demo, show-of-hands vote.
- Hand out `example/` at the start as the format reference; it opens offline, no install.
- Keep it harmless: useless must not mean resource-abusing or offensive. Shut those down early.
- Great closing discussion: now that they've built pure uselessness, ask what *does* make a feature valuable. The void teaches the shape of the thing.
