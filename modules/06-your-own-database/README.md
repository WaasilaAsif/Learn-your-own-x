---
status: proposed
proposed-by: Waasila Asif
domain: Systems
type: build-your-own
---

# 06: Build your own database (PROPOSAL)

> **This is a module proposal, not a finished module.** No `starter/` code exists yet.
> Approve the scope here and the starter sandbox + checker get built next, in the
> same format as modules 00–03. See the **Build plan** at the bottom.

**You'll build:** a tiny persistent key–value database in pure Python — an append-only log, an in-memory index, crash recovery, and compaction
**You'll understand:** how real databases survive a power cut, why "just write to a file" isn't enough, and the log-structured design behind Bitcask, LevelDB, and Kafka
**Time:** one workshop (about 2 hours) plus a weekend
**Format:** self-paced or in person, bring a laptop

## Why this module

"A database is just a file" is the illusion this module breaks. By the end you can pull the plug mid-write (the checker simulates exactly that) and your data is still there and still consistent. That moment — *durability you built yourself* — is what systems people eat up. It fills the Systems gap in a curriculum that otherwise skips straight from shell to AI, and it uses nothing but the standard library.

## Prerequisites

- **Python 3.10+** (`python --version`). Standard library only.
- You've opened a file in Python before. That's the bar.

## Draft checkpoints

1. **get / set to disk.** Append each `set` as a record to a log file; `get` scans for the latest value of a key. *Check it:* set then get survives restarting the process — the value is read back from the file, not memory.
2. **An index makes it fast.** Keep an in-memory map of key → byte-offset in the log, so `get` is one `seek`, not a full scan. *Check it:* the checker writes 10,000 keys and asserts a `get` reads exactly one record.
3. **Crash recovery.** On startup, rebuild the index by replaying the log. *Check it:* the checker kills the process mid-run, reopens the DB, and asserts every committed key is intact and no half-written record corrupts it.
4. **Compaction.** Old versions pile up in an append-only log; write a compactor that keeps only the latest value per key. *Check it:* after rewriting a key 1,000 times then compacting, the file holds one record for it and all data still reads correctly.

## Build plan (what ships when approved)

- `starter/kvdb.py` — the file framing, record (de)serialization, and CLI done for you; `get()`, `set()`, `_load_index()`, and `compact()` left as `TODO`s.
- `starter/check.py` — deterministic workload (seeded keys/values); simulates a crash by writing a truncated final record and asserting recovery. Fails on the skeleton, passes when complete.
- Crash simulation is done in-process (write a partial record, reopen) so it needs no OS tricks and runs identically on Windows/macOS/Linux.
- Deterministic data; ASCII-only output.

## Going further

- Add a `delete` (tombstone records) and make compaction drop them.
- Add a hash of each record and verify it on read — detect bit-rot.
- Benchmark: how many writes/second? Then add a write buffer and measure again.
- Swap the flat index for a sorted structure and support range scans (the road to an LSM-tree / B-tree).

## Further reading

- *Designing Data-Intensive Applications* (Kleppmann), Ch. 3 — the log-structured vs page-oriented storage chapter this module is a hands-on version of.
- [Bitcask paper](https://riak.com/assets/bitcask-intro.pdf) — the exact "log + in-memory hash index" design we build.
- [Build Your Own Database (CodeCrafters)](https://codecrafters.io/) — a longer SQLite-shaped take, if you want the next step.

## Open questions for review

- Key–value log (this proposal) vs a mini-SQL/B-tree engine? Recommended: key–value. The B-tree version is a great *advanced* follow-up but blows the one-weekend budget.
- Store values as length-prefixed bytes (binary) or newline-delimited JSON? Leaning length-prefixed binary so checkpoint 1 teaches real framing, with a JSON mode noted in "Going further".
