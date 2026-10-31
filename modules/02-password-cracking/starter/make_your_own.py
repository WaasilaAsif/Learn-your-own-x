"""
Checkpoint 1: hash a password yourself and see what cracking is up against.

AUTHORIZED TARGETS ONLY: hash passwords that are YOURS or made up for practice.
Don't type a password you actually use anywhere — invent one.

    python make_your_own.py correcthorse
    python make_your_own.py correcthorse letmein 123456

Each password is printed with its MD5 hash. Notice two things:
  1. Hashing is one-way: you can't read the password back out of the hash.
  2. The SAME password always gives the SAME hash — that sameness is exactly
     the weakness checkpoints 2 and 3 exploit (and salting removes).

Append a hash to hashes.txt to practice cracking your own:
    python make_your_own.py mypassword >> my_hashes.txt   # the hash + word
"""
import hashlib
import sys

if len(sys.argv) < 2:
    print("usage: python make_your_own.py <password> [more ...]")
    raise SystemExit(1)

for pw in sys.argv[1:]:
    digest = hashlib.md5(pw.encode()).hexdigest()
    print(f"{digest}  (md5 of {pw!r})")
