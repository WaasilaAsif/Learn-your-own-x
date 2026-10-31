"""
Checkpoints 3 & 4: why salting and slow KDFs defeat the wordlist attack.

AUTHORIZED TARGETS ONLY: everything here hashes a throwaway practice password.

This script shows, with numbers from YOUR machine:
  - salt: the same password gets a different hash every time, so a precomputed
    table (checkpoint 2's trick) is worthless.
  - slow KDF: bcrypt is deliberately thousands of times slower than MD5, so a
    wordlist that cracks MD5 instantly would take effectively forever.

Run:  python slow_hash_demo.py
Needs: pip install -r requirements.txt   (bcrypt, argon2-cffi)
"""
import hashlib
import time

import bcrypt
from argon2 import PasswordHasher

PASSWORD = b"correcthorse"   # a throwaway practice password

print("=== 1. Salt: same password, different hash every time ===")
for i in range(2):
    h = bcrypt.hashpw(PASSWORD, bcrypt.gensalt(rounds=10))
    print(f"  hash {i + 1}: {h.decode()}")
print("  Both verify against the original password, but they're different")
print("  strings -- so a precomputed hash->word table can't match either.\n")

print("=== 2. Speed: how many guesses per second? ===")
N = 20000
t = time.perf_counter()
for _ in range(N):
    hashlib.md5(b"x").hexdigest()
md5_rate = N / (time.perf_counter() - t)

t = time.perf_counter()
bcrypt.hashpw(b"x", bcrypt.gensalt(rounds=10))
bcrypt_one = time.perf_counter() - t

print(f"  MD5:    ~{md5_rate:,.0f} guesses/second")
print(f"  bcrypt: 1 guess took {bcrypt_one * 1000:.1f} ms "
      f"(~{1 / bcrypt_one:,.0f} guesses/second)")
print(f"  bcrypt is ~{md5_rate * bcrypt_one:,.0f}x slower PER GUESS.\n")

print("=== 3. Put it in attacker terms ===")
guesses = 1_000_000_000   # a modest 1-billion-word list
print(f"  A {guesses:,}-word list against this one password:")
print(f"    MD5:    {guesses / md5_rate / 60:,.1f} minutes")
print(f"    bcrypt: {guesses * bcrypt_one / 86400:,.0f} days")
print("  That gap is the entire point of a slow KDF.\n")

print("=== 4. Argon2 (today's recommended default) ===")
ph = PasswordHasher()
h = ph.hash("correcthorse")
print(f"  argon2 hash: {h}")
print(f"  verify ok:   {ph.verify(h, 'correcthorse')}")
