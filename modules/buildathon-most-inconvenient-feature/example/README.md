# Example: The Inconvenient Timer

**You'll build:** a countdown timer that works perfectly and is miserable to set — no typing, no presets, just a "+1 second" button that runs away from your cursor
**You'll understand:** how much invisible design work goes into a plain number input, by removing all of it on purpose
**Time:** about an hour
**Format:** one self-contained `index.html`, opens in any browser, no install

This is the reference entry for the [Most Inconvenient Feature](../) buildathon. It shows the format your own submission can follow: a small thing that **works**, a README that explains the cruelty, and a simple way to confirm it still does its job.

## The idea

A countdown timer is a solved problem: type `5:00`, hit start. So we solve it *again*, badly. To set the duration you may only click a **+1 second** button, one second at a time. No text field. No presets. No holding the key. And after every click the button **jumps to a random spot**, so you have to chase it. Setting five minutes is 300 clicks and a cardio workout.

Crucially, it is a *real timer*: the count is accurate, Start actually counts down, and it alarms at zero. That's the whole genre — **it works, it's just torture.**

## Setup

```bash
# from this folder
# just open the file — no server, no dependencies
```

Open [`index.html`](index.html) in any browser (double-click it, or drag it into a tab).

You're set up when you see the timer at `00:00`, a lonely **+1 second** button, and a disabled **Start** button.

## Checkpoint 1: A timer that works the *convenient* way

**Goal:** before you make it awful, make it correct. A normal timer: set seconds, start, it counts down to zero and alarms.

Build (or read, in `index.html`) the honest version first: a number input, a Start button, a `setInterval` that ticks down once a second, and an alert/beep at zero. This is the baseline you will deliberately ruin.

**Check it:** set it to 3 seconds, press Start, and it reaches `00:00` and alarms within ~3 seconds.

## Checkpoint 2: Remove every convenience

**Goal:** the *only* way to add time is a single **+1 second** button.

Delete the number input and the presets. Replace them with one button that increments the target by exactly one second per click. Typing, pasting, arrow keys — all gone.

**Check it:** there is no way to reach `02:00` except by clicking the button 120 times. (Go on. Or trust us.)

## Checkpoint 3: Make it hurt — the dodging button

**Goal:** after each click, the +1 button teleports to a random position inside the window.

On every `click`, move the button to random `top`/`left` coordinates, clamped so it's always fully on-screen and always clickable. The inconvenience must never tip into *impossible* — that would break the one rule.

**Check it:** each click both adds a second *and* moves the button, and you can always still reach it (it never lands off-screen or under another element).

## Checkpoint 4: Keep it honest — it must still finish the job

**Goal:** prove it's inconvenient, not broken.

Start must still run an accurate countdown and alarm at zero, no matter how painfully the time was entered.

**Check it:** laboriously click to `00:05`, press Start, and confirm it counts `05 → 00` in five real seconds and alarms. If it does, it's a valid entry. If it can't complete the task, it's disqualified — broken isn't inconvenient.

## How this maps to a submission

That's a complete buildathon entry. To submit your own:

1. Make your `index.html` (or any runnable project) do its task correctly but awfully.
2. Confirm checkpoint 4 for *your* task — it must complete every time.
3. Add a row to the [submissions table](../#submissions) with a link, via a pull request.

## Going further (crank the cruelty)

- The button shrinks by 2px every click, so late clicks are pixel-hunting.
- A "confirm" modal after Start asking "Are you sure?" with the Yes button disabled for 3 seconds.
- Display the remaining time in words, in a language picked at random each second.
- Replace the alarm's "stop" button with checkpoint 3's dodging behavior.

## Further reading

- [User Inyerface](https://userinyerface.com/) — the masterclass in working-but-hostile UI.
- [The Password Game](https://neal.fun/password-game/) — escalating rules, each one works, all of them torture.
- [r/badUIbattles](https://www.reddit.com/r/badUIbattles/) — the community, for ideas and for posting yours.
- Don Norman, *The Design of Everyday Things* — read it to understand exactly which affordances you just vandalized.

## Done? Make it count

Demo it live and watch the room wince, then post your submission link in the buildathon thread on the Discord.

---

## For facilitators

- This file is single-page HTML with zero dependencies — hand it out as the format reference. It opens offline.
- The dodging button is clamped to the viewport on purpose; if someone's entry has an unreachable control, that's the "it must still work" rule failing — coach them to clamp it.
- Good teaching beat: show the convenient checkpoint-1 timer, then the finished one, back to back. The gap *is* the lesson about invisible design.
