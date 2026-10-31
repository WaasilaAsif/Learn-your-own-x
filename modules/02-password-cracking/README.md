# 02: Password cracking with wordlists

**You'll build:** a wordlist cracker that breaks weak unsalted hashes — then watch properly salted, slow-hashed passwords resist it
**You'll understand:** why hashing, salting, and slow KDFs (bcrypt, Argon2) exist, and how to reason about password storage as a *defender*
**Time:** one in-person workshop (about 2 hours)
**Format:** in person, bring a laptop

> ## ⚠️ Authorized targets only — read before anything else
>
> This is a **defensive** security module. You crack **only** hashes we hand you in this repo, or hashes of passwords **you made up yourself**. Never run any of this against a real account, a password you actually use, a system you don't own, or anyone else's data. Cracking hashes you aren't authorized to touch is illegal in most places and against this community's code of conduct. The whole point here is to understand attacks so you can **defend** against them — the same way [pwn.college](https://pwn.college/) and [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) teach with deliberately provided targets.
>
> This warning is repeated at the top of every checkpoint and every script. That repetition is the point.

Everything runs in the [`starter/`](starter/) folder, a self-contained sandbox: the hashes, the wordlist, and the tools are all right there. No internet, no real targets, nothing you can point at the outside world.

## Prerequisites

Before the workshop:

- **Python 3.10+** — `python --version` shows 3.10 or higher.
- Install the defense libraries (checkpoint 2 needs nothing but the standard library; 3–4 need these):
  ```bash
  cd modules/02-password-cracking/starter
  pip install -r requirements.txt
  ```
- A terminal and a code editor.

## Setup

```bash
cd modules/02-password-cracking/starter
ls
python make_your_own.py correcthorse
```

You're set up when the last command prints `correcthorse` next to a 32-character MD5 hash.

## The mental model (read once)

- A **hash** is a one-way function: easy to go password → hash, infeasible to go hash → password by reversing it.
- So how are passwords ever cracked? **Guessing.** An attacker hashes millions of candidate guesses (a **wordlist** of leaked/common passwords) and checks which hash matches. They don't reverse the hash — they out-guess it.
- Three things decide whether guessing wins:
  1. **Password strength** — is it in the wordlist at all?
  2. **Salt** — a random value mixed in per password, so identical passwords get different hashes and precomputed tables are useless.
  3. **Speed** — a *fast* hash (MD5, SHA-1) lets an attacker try billions of guesses an hour. A *slow* KDF (bcrypt, Argon2) is deliberately expensive, so the same wordlist would take years.

This module walks each one.

## Checkpoint 1: Hashing is one-way — and that's not enough

> ⚠️ Authorized targets only: use a password you **invent**, never a real one.

**Goal:** see what a hash is, and spot its built-in weakness.

```bash
python make_your_own.py hunter2
python make_your_own.py hunter2        # run it twice
python make_your_own.py apple banana
```

Notice:

- You can't read the password out of the hash — it really is one-way.
- The **same input always produces the same hash.** Run `hunter2` twice: identical output. That determinism is what makes the next checkpoint possible — and what salting (checkpoint 3) destroys.

**Check it:** both runs of `hunter2` print the exact same hash, `2ab96390c7dbe3439de74d0c9b0b1767`.

## Checkpoint 2: Crack the weak hashes

> ⚠️ Authorized targets only: `hashes.txt` was generated for this workshop. These are the only hashes you're cleared to crack (plus your own).

**Goal:** recover 5 plaintext passwords from their MD5 hashes using the wordlist.

Open [`starter/crack.py`](starter/crack.py). The `crack()` function has one `TODO`: hash each word in the wordlist and match it against the target hashes. Fill it in, then:

```bash
python crack.py
```

It should recover all five. The attack is brutal in its simplicity: **hash every common word once, compare to the targets.** Because the hashes are unsalted, one pass over the wordlist cracks every matching hash at the same time — and a real attacker's wordlist (`rockyou.txt`) has 14 million entries.

**Check it:**

```bash
python check.py
```

Expect `PASS - checkpoint 2 complete`. (Under the hood it recovers `123456`, `password`, `qwerty`, `iloveyou`, `dragon` — every one a perennial "worst passwords" list entry. That's why they fall instantly.)

> **The real tools.** Professionals use [`hashcat`](https://hashcat.net/hashcat/) and [John the Ripper](https://www.openwall.com/john/) — GPU-accelerated, billions of guesses per second, with rule engines that mutate words (`password` → `P@ssw0rd!`). Your Python does the same thing slower. Install one later and try `hashcat -m 0 hashes.txt wordlist.txt` **on this folder's files only.**

## Checkpoint 3: Salt breaks the attack

> ⚠️ Authorized targets only — still working with throwaway practice passwords.

**Goal:** understand why a **salt** makes checkpoint 2's one-pass trick worthless.

```bash
python slow_hash_demo.py
```

Look at section 1 of the output: the **same** password hashed twice gives **two different** hashes. That's the salt — a random value stored alongside each hash and mixed in before hashing.

Why it matters: in checkpoint 2, one hash of `password` cracked it for *everyone* who used it. With a unique salt per user, the attacker must re-run the entire wordlist **separately for every single hash**. Precomputed tables ("rainbow tables") become useless. Salt doesn't make a weak password strong — it makes the attack *scale badly*, which buys enormous time.

**Check it:** in the output, the two `hash 1` / `hash 2` lines under section 1 are different strings, yet the script confirms both verify against the original password.

## Checkpoint 4: Slow hashing makes guessing hopeless

> ⚠️ Authorized targets only.

**Goal:** measure, on your own machine, why bcrypt/Argon2 beat MD5 for storing passwords.

Same script, sections 2–4. It times MD5 vs bcrypt on *your* hardware and extrapolates:

- MD5 does **~1,000,000+ guesses/second**. bcrypt does a few **dozen**. bcrypt is tens of thousands of times slower *on purpose*.
- A billion-word list against one password: **minutes** with MD5, **years** with bcrypt.

That's the entire design goal of a **KDF** (key derivation function): be slow enough that online-scale guessing is futile, tunable so you can crank the cost as hardware improves. [**Argon2**](https://en.wikipedia.org/wiki/Argon2) (section 4) is the current recommended default; bcrypt is the well-tested older standard. Either is correct; **a bare MD5/SHA-256 of a password is a vulnerability.**

**Check it:** the script prints bcrypt as thousands of times slower per guess than MD5, and the billion-word-list estimate shows MD5 in minutes vs bcrypt in hundreds of days.

## The defender's takeaways (the real lesson)

You attacked so you can defend. When you store passwords:

1. **Never store them reversibly, and never with a fast hash.** Use **Argon2** (or bcrypt/scrypt). Most frameworks have this built in — use it, don't invent your own.
2. **Salting is automatic** in those libraries — the salt is baked into the output string. Don't hand-roll it.
3. **Length beats complexity.** A 4-word passphrase (`correct horse battery staple`) has more entropy than `P@ss1!` and is easier to remember. Encourage length and a password manager, not forced symbols.
4. **The best defense is not being in the wordlist.** Checkpoint 2 only worked because the passwords were common. Unique, long, random passwords (from a manager) aren't in any list.

## Going further

- **Rules/mutations:** extend `crack.py` to also try each word capitalized, reversed, and with `123`/`!` appended. See how many *more* you'd catch — this is what real crackers do.
- **Estimate entropy:** install [`zxcvbn`](https://pypi.org/project/zxcvbn/) (the strength meter Dropbox open-sourced) and score your practice passwords. It predicts guess counts, not naive "has a symbol" rules.
- **SHA vs MD5:** change `algo="md5"` to `"sha256"` in `crack.py` — still instantly cracked, because the problem was never the algorithm's strength, it was speed and no salt.
- **Try `hashcat`/`John`** on this folder's `hashes.txt` only, to feel real cracking speed.

## Further reading

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — the authoritative "how to store passwords" reference. Read this one.
- [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html) — the modern guidance (length over forced complexity; drop periodic resets).
- [How Dropbox stores passwords](https://dropbox.tech/security/how-dropbox-securely-stores-your-passwords) — a real production design.
- [Troy Hunt: Have I Been Pwned](https://haveibeenpwned.com/Passwords) — check whether a hash is in a known breach (k-anonymity API; it never sends the full password).
- [pwn.college](https://pwn.college/) · [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) — authorized, deliberately vulnerable practice environments.

## Done? Make it count

Post your `python check.py` output (the `PASS` line) **and** one sentence on what you'll change about how you store or choose passwords, in the module 02 thread on the Discord, to earn the module role.

---

## For facilitators

- **State the authorization rule out loud at the start and at every checkpoint.** If anyone points a tool at a real target, the session stops. This is non-negotiable and it's what keeps the module teachable.
- The hashes and wordlist are fixed and committed, so every expected value in the README is exact. If you regenerate them, update `check.py`'s `EXPECTED` map, checkpoint 2's named passwords, and checkpoint 1's `hunter2` hash.
- All Python output is deliberately ASCII — Windows' default console (cp1252) crashes on emoji/dashes. Keep it that way if you edit the scripts.
- bcrypt timing in checkpoint 4 varies by machine; the *ratio* (tens of thousands×) is the point, not the absolute numbers. On a fast laptop bcrypt may show ~15 guesses/s, on a slow one ~5 — both prove the lesson.
- Good moment for a live demo: run `hashcat` on the projector against `hashes.txt` so the room sees GPU speed, then against a bcrypt hash so they see it crawl.
