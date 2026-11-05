---
status: proposed
proposed-by: Waasila Asif
domain: Data (All)
type: build-your-own
---

# 07: Build your own "Wrapped" (PROPOSAL)

> **This is a module proposal, not a finished module.** No `starter/` code exists yet.
> Approve the scope here and the starter sandbox + checker get built next, in the
> same format as modules 00–03. See the **Build plan** at the bottom.

**You'll build:** your own Spotify-Wrapped-style report from a data export (messages, listening history, or step count) — the top lists, the by-hour activity chart, and one shareable "insight" image
**You'll understand:** the whole small-data pipeline — parse a messy export, count and group it, and turn numbers into a picture that tells a story — plus why "it's just your own data" is a privacy feature, not a limitation
**Time:** one workshop (about 2 hours) plus a weekend
**Format:** self-paced or in person, bring a laptop

## Why this module (the crossover one)

This is the module that gets the **non-technical** people in the room. Everyone wants to know their own patterns — when do I text the most, who do I reply to fastest, what's my most-played track. The payoff is personal and instantly shareable, so design-minded and non-CS students stay engaged, while the CS students get a real parse-group-visualize pipeline. Mixed-audience data workshops consistently work when people bring (or are handed) their *own* data and end on a picture — that's exactly this.

**Privacy by design:** it ships with a committed, synthetic `sample_data/` so nobody is required to upload anything personal. Everything runs locally; no data leaves the laptop. Using your real export is an opt-in "Going further".

## Prerequisites

- **Python 3.10+**; `pip install matplotlib` for the chart (checkpoints 1–2 are stdlib only).
- No prior data experience. The sample data and parser skeleton carry beginners through.

## Draft checkpoints

1. **Load the export.** Parse the provided `sample_data/` (a WhatsApp-style chat export format) into a list of records. *Check it:* `python check.py` reports the exact expected row count from the seeded sample.
2. **Top lists.** Count messages per person and find the busiest day. *Check it:* checker asserts the known top sender and count from the sample.
3. **Activity by hour.** Bucket activity into 24 hours and plot it. *Check it:* `activity.png` is written and the peak hour matches the seeded expected value.
4. **Your insight card.** Compose one shareable image: a headline stat + the chart + a caption. *Check it:* `wrapped.png` exists and contains your top-3 lists (checker verifies the data behind it).

## Build plan (what ships when approved)

- `starter/sample_data/` — a **seeded, synthetic** chat export (no real people), so every expected number in the README is exact.
- `starter/wrapped.py` — the file reader and plotting scaffold done; `parse()`, `top_senders()`, `by_hour()` left as `TODO`s.
- `starter/check.py` — asserts the deterministic counts and that the images are produced. Fails on the skeleton, passes when complete.
- A one-page `FORMATS.md` showing how to export your *own* WhatsApp / Spotify / Google Takeout / Apple Health data and map it to the same parser (opt-in).
- Deterministic sample; ASCII-only console output; charts rendered to file (no GUI needed on lab machines).

## Going further

- Point it at your **real** export (instructions in `FORMATS.md`) — same code, your life.
- Add a word-frequency "most-used emoji / word" (watch out for stop-words).
- Reply-time analysis: median seconds to first reply per contact.
- Make it a little static HTML page instead of a PNG, and host it with what you learned in module 00.

## Further reading

- [Spotify: Understanding Wrapped](https://newsroom.spotify.com/) — what makes the format land (story, not dashboard).
- [Storytelling with Data](https://www.storytellingwithdata.com/) — choosing the *one* chart that makes a point.
- [pandas 10-minute intro](https://pandas.pydata.org/docs/user_guide/10min.html) — the grown-up version of the counting you did by hand.

## Open questions for review

- Default sample format: WhatsApp chat export (recommended — most universal and text-only) vs Spotify JSON? Could ship both; start with chat export.
- Allow `matplotlib`, or keep it stdlib and render a bar chart as an HTML/SVG file? Leaning matplotlib for the payoff, with an SVG fallback noted for dependency-locked machines.
