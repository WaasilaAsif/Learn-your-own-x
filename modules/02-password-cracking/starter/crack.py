"""
Checkpoint 2: crack the handed-out unsalted MD5 hashes with a wordlist.

AUTHORIZED TARGETS ONLY. The hashes in hashes.txt were generated for this
workshop. Only ever run this against hashes you were handed or hashes of your
own passwords (see make_your_own.py). Never against anyone else's account,
system, or data.

Finish the crack() function where marked TODO, then run:

    python crack.py

It should recover all 5 passwords. Then run `python check.py` to verify.
"""
import hashlib
import sys


def load(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def crack(hashes, words, algo="md5"):
    """Return {hash: plaintext or None}.

    The attack: hash every word in the wordlist and see which target hashes
    match. Because an unsalted hash is identical for everyone, one pass over
    the wordlist cracks every matching hash at once.
    """
    results = {h: None for h in hashes}

    # TODO: for each word, compute hashlib.new(algo, word.encode()).hexdigest()
    #       and if that digest is one of the target hashes, record the word:
    #           results[digest] = word
    #
    # Hint — turn the target list into a set for fast lookups:
    #           targets = set(hashes)

    return results


if __name__ == "__main__":
    hashes = load(sys.argv[1] if len(sys.argv) > 1 else "hashes.txt")
    words = load(sys.argv[2] if len(sys.argv) > 2 else "wordlist.txt")

    cracked = crack(hashes, words)
    for h, w in cracked.items():
        print(f"{h}  {w if w else '[not found]'}")
    found = sum(1 for w in cracked.values() if w)
    print(f"\ncracked {found}/{len(hashes)}")
