# Example: The Useless Machine

**You'll build:** a digital version of the classic Useless Machine — a switch whose only purpose is to turn itself back off, so you can never leave it on
**You'll understand:** what makes a feature *valuable*, by building the purest possible absence of value and then defending it
**Time:** about an hour
**Format:** one self-contained `index.html`, opens in any browser, no install

This is the reference entry for the [Most Useless Feature](../) buildathon. It shows the format your own submission can follow: a small thing that **works reliably**, a README that explains the pointlessness, and the "prove it's useless" step that keeps it submittable.

## The idea

The [Useless Machine](https://en.wikipedia.org/wiki/Useless_machine) is a toy with exactly one behavior: you flip its switch ON, and a little arm reaches out and flips it back OFF. That's it. It produces nothing, stores nothing, tells you nothing. It is the canonical useless feature — and it *works perfectly*, every single time.

We build the digital version. Flip the switch; after a dramatic pause, a hand slides out and flips it back. A counter tallies how many times you've tried, purely to mock you. **Remove the whole thing and nothing of value is lost** — which is exactly the point.

## Setup

```bash
# from this folder — just open the file, no server, no dependencies
```

Open [`index.html`](index.html) in any browser (double-click, or drag it into a tab).

You're set up when you see a switch in the OFF position and a smug status line daring you to turn it on.

## Checkpoint 1: A switch that works

**Goal:** before it defies you, it has to function. A plain toggle: click it, it goes ON; click again, OFF.

Build (or read, in `index.html`) an honest toggle first — a button or checkbox that flips a boolean and updates the on-screen state. This is the baseline you're about to make pointless.

**Check it:** clicking toggles the switch between ON and OFF, and the label reflects it.

## Checkpoint 2: Give it a will of its own

**Goal:** whenever the switch goes ON, it returns itself to OFF after a short, theatrical pause.

When state becomes ON, start a timer (~700ms). When it fires, set state back to OFF. The user's click is honored (it *does* turn on) — the machine just refuses to stay that way.

**Check it:** turn it on and let go. Within a second it's OFF again, by itself. You cannot leave it on no matter how fast you are.

## Checkpoint 3: Commit to the bit

**Goal:** sell the uselessness. Animate a little "hand" that slides out to flip the switch, and add a counter + a smug status message.

Add the arm (a CSS slide), a `Times you tried: N` tally, and rotating dismissive messages ("Nice try.", "No.", "It is not your destiny."). None of it does anything useful — it just makes the nothing *land*.

**Check it:** turning it on visibly triggers the hand animation, the counter increments, and the status line taunts you.

## Checkpoint 4: Prove it's useless (the submittable check)

**Goal:** confirm your entry passes the one rule — *if it fixes a problem, it's not submittable.*

In one sentence, try to name a real problem this solves. You can't:

> This solves no problem. You cannot leave the switch on, so it stores no setting, triggers no action, and informs you of nothing. Removing it loses nothing of value.

That sentence is your defense at judging. If you *can* honestly finish "this is handy because…", your feature is too useful — add more pointlessness.

**Check it:** you cannot name a genuine problem it fixes. (The click counter doesn't count — it measures only your futility, which helps no one.)

## How this maps to a submission

That's a complete buildathon entry. To submit your own:

1. Make your `index.html` (or any runnable project) do its pointless thing reliably.
2. Write the one-sentence "this is useless because…" defense (checkpoint 4).
3. Add a row to the [submissions table](../#submissions) with a link, via a pull request.

## Going further (deeper into the void)

- A "fullscreen" button that exits fullscreen the instant you enter it.
- A progress bar that fills to 99% and then slowly drains back to 0, forever.
- A "copy" button that copies the words `nothing to copy` to your clipboard.
- A leaderboard of how many times people have tried the switch — a ranking of wasted effort, informing no decision.

## Further reading

- [Useless Machine (Wikipedia)](https://en.wikipedia.org/wiki/Useless_machine) — the history of the thing you just rebuilt.
- [The Useless Web](https://theuselessweb.com/) — a directory of the state of the art.
- [Simone Giertz](https://www.youtube.com/@simonegiertz) — the patron saint of things that work and help no one.
- John Maeda, *The Laws of Simplicity* — after a night of pointlessness, read what value and simplicity actually are.

## Done? Make it count

Demo it live, land the joke, then post your submission link in the buildathon thread on the Discord.

---

## For facilitators

- Single-page HTML, zero dependencies — hand it out as the format reference; it runs offline.
- The judging gate is checkpoint 4: ask "what problem does it solve?" If a team can answer sincerely, it's disqualified. Lean into that — the funniest entries are the ones straining hardest to stay useless.
- The counter is a good teaching example of the line: it looks like a feature, but it measures only futility, so it stays useless. Use it to discuss where utility actually begins.
