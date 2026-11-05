---
status: proposed
proposed-by: Waasila Asif
domain: AI/ML
type: build-your-own
---

# 05: Build your own neural network from scratch (PROPOSAL)

> **This is a module proposal, not a finished module.** No `starter/` code exists yet.
> Approve the scope here and the starter sandbox + checker get built next, in the
> same format as modules 00–03. See the **Build plan** at the bottom.

**You'll build:** a 2-layer neural network in pure NumPy — no PyTorch, no TensorFlow — that learns to recognize handwritten digits, then recognizes one you draw yourself
**You'll understand:** what "training" actually is: forward pass, loss, backpropagation, and gradient descent, with no framework hiding the math
**Time:** one workshop (about 2 hours) plus a weekend
**Format:** self-paced or in person, bring a laptop

## Why this module

Everyone in the club has *used* a model (module 03 wires one up over MCP). Almost nobody has seen the thirty lines of arithmetic that make one *learn*. Writing backprop by hand once — watching the loss drop and accuracy climb on your own machine — permanently demystifies deep learning. "From scratch" is the hook that makes technical students actually finish it.

It pairs with module 03 (MCP/using models) as the other half of the AI track: **03 uses a model, 05 builds one.**

## Prerequisites

- **Python 3.10+** and `pip install numpy`.
- You multiply matrices in the module; a 5-minute refresher on "rows × columns" is enough. No calculus required — the chain rule is derived as array operations, not symbols.

## Draft checkpoints

1. **See the data.** Load a small, committed MNIST subset (seeded, ~2000 images) and render one digit as ASCII in the terminal. *Check it:* you print a `7` and the label says `7`.
2. **Forward pass.** Implement `relu`, a linear layer, and `softmax`; push one image through to get 10 class scores. *Check it:* output is a probability vector summing to 1.0 (checker asserts shape + sum).
3. **Backprop by hand.** Implement the gradients and one gradient-descent step. *Check it:* the loss on a single batch *decreases* after an update — the checker asserts loss(after) < loss(before).
4. **Train + predict your own digit.** Run the training loop; hit a target accuracy; then draw a digit in a provided 28×28 grid script and classify it. *Check it:* `python check.py` reports test accuracy ≥ a fixed threshold (~90% on the subset).

## Build plan (what ships when approved)

- `starter/nn.py` — data loading, the training loop, and the ASCII renderer done for you; `forward()`, `backward()`, and `step()` left as `TODO`s with the shapes documented.
- `starter/data/` — a **committed, seeded** MNIST subset (small `.npz`), so accuracy numbers in the README are exact and reproducible, and nothing is downloaded at the venue.
- `starter/check.py` — trains with a fixed seed and asserts the accuracy threshold; fails on the skeleton, passes when complete.
- `starter/draw_digit.py` — terminal 28×28 drawing grid so learners can test the net on their own input.
- Deterministic: fixed `np.random.seed`, so "≥90%" is a promise, not a hope. ASCII-only output.

## Going further

- Add a second hidden layer, or swap ReLU for tanh, and see accuracy move.
- Mini-batch vs full-batch gradient descent — time both.
- Rewrite the exact same network in ~15 lines of PyTorch and see what the framework was doing for you.

## Further reading

- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) (Michael Nielsen) — free, builds the same digit classifier.
- [3Blue1Brown: Neural networks](https://www.3blue1brown.com/topics/neural-networks) — the visual intuition for backprop.
- [Andrej Karpathy, micrograd](https://github.com/karpathy/micrograd) — backprop in ~100 lines, the inspiration for "from scratch".

## Open questions for review

- Ship the MNIST subset as `.npz` in-repo (adds ~1–2 MB) vs a tiny generator script? Recommended: commit the `.npz` so it's deterministic and offline.
- Accuracy threshold: 90% is comfortable on a 2k-image subset in a few seconds of CPU training; confirm that's the bar.
