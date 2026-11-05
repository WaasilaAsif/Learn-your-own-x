---
status: proposed
proposed-by: Waasila Asif
domain: Graphics
type: build-your-own
---

# 04: Build your own ray tracer (PROPOSAL)

> **This is a module proposal, not a finished module.** No `starter/` code exists yet.
> Approve the scope here and the starter sandbox + checker get built next, in the
> same format as modules 00–03. See the **Build plan** at the bottom for exactly what
> will ship.

**You'll build:** a tiny ray tracer in pure Python (no libraries) that renders a scene of shaded, reflecting spheres to an image file
**You'll understand:** how every rendered frame you've ever seen is just rays, vectors, and a bit of trigonometry — and why ray tracing is "embarrassingly parallel"
**Time:** one workshop (about 2 hours) plus a weekend
**Format:** self-paced or in person, bring a laptop

## Why this module

It is the single most *shareable* thing on this list. You run a script, a `render.png` appears, and it looks like real 3D. That payoff is why Peter Shirley's [*Ray Tracing in One Weekend*](https://raytracing.github.io/) is one of the most-finished graphics tutorials ever written — we build a trimmed, Python version of the same idea. It also diversifies the curriculum: modules 00–03 are tooling, security, and AI; this is graphics and math-you-can-see.

No dependencies. It writes a [PPM](https://en.wikipedia.org/wiki/Netpbm) image with plain text, which the checker converts to PNG — so it runs on the locked-down lab machines too.

## Prerequisites

- **Python 3.10+** (`python --version`).
- Comfort with basic vectors (add, subtract, dot product) — the first checkpoint re-teaches these, so rusty is fine.

## Draft checkpoints

Each ends with a concrete **Check it**, same as every module.

1. **An image is just numbers.** Write a gradient PPM by hand (loop over pixels, write RGB). *Check it:* `render.ppm` opens and shows a smooth gradient.
2. **Fire one ray, hit one sphere.** Implement a `Vec3`, a ray, and the ray–sphere intersection. Color a hit red. *Check it:* a red circle on a background.
3. **Make it look 3D (diffuse shading).** Surface normals + a light direction. Add a ground plane. *Check it:* the sphere now has light and shadow falloff; the checker compares your pixels to a seeded reference within tolerance.
4. **Reflections + a scene.** Recursive rays for mirror spheres; three spheres of different materials. *Check it:* `render.png` shows reflections; `python check.py` passes.

## Build plan (what ships when approved)

- `starter/ray.py` — `Vec3` done for you; `hit_sphere()` and the shading loop left as `TODO`s.
- `starter/scene.py` — a fixed, seeded scene so every learner's reference image is identical.
- `starter/check.py` — renders the scene and compares pixel values against a committed reference within a tolerance (floating-point render, so exact-match won't do). Fails on the skeleton, passes when complete.
- `starter/ppm_to_png.py` — tiny converter (stdlib `zlib`-based PNG writer) so output is shareable without Pillow.
- All Python output ASCII-only (Windows cp1252 console constraint).

## Going further

- Anti-aliasing (multiple rays per pixel), then a defocus/depth-of-field camera.
- Triangles instead of spheres → load a simple `.obj` model.
- Time it, then multiprocess it across cores to *feel* why render farms exist.

## Further reading

- [*Ray Tracing in One Weekend*](https://raytracing.github.io/) — the canonical gentle version (C++, maps directly onto ours).
- [Scratchapixel](https://www.scratchapixel.com/) — the math, from scratch, with pictures.

## Open questions for review

- Lock scope at **4 checkpoints** (spheres + reflections) and push anti-aliasing to "Going further"? Recommended, to keep it one weekend.
- Reference-image tolerance: ship one reference PNG and a per-pixel tolerance, or a hash of a downsampled render? (Leaning: tolerance on a small 200×150 render.)
