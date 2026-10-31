"""
Checkpoint 2 checker. Imports your crack() and confirms it recovers all five
handed-out passwords. Run:  python check.py
"""
import sys

from crack import crack, load

EXPECTED = {
    "e10adc3949ba59abbe56e057f20f883e": "123456",
    "5f4dcc3b5aa765d61d8327deb882cf99": "password",
    "d8578edf8458ce06fbc5bb76a58c5ca4": "qwerty",
    "f25a2fc72690b780b2a14e140ef6a9e0": "iloveyou",
    "8621ffdbc5698829397d97767ac13db3": "dragon",
}

hashes = load("hashes.txt")
words = load("wordlist.txt")
got = crack(hashes, words)

ok = True
for h, want in EXPECTED.items():
    if got.get(h) == want:
        print(f"ok   {h} -> {want}")
    else:
        print(f"MISS {h} -> expected {want!r}, got {got.get(h)!r}")
        ok = False

print()
if ok:
    print("PASS - checkpoint 2 complete")
else:
    print("Not yet. Finish crack() in crack.py (the TODO), then rerun.")
    sys.exit(1)
