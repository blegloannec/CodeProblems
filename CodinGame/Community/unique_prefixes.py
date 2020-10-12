#!/usr/bin/env python3

from collections import Counter
from itertools import chain

# hash-based approach
PMOD = 10**14+99
BASE = 131
def prefix_hash(word):
    h = 0
    for c in word:
        h = (h*BASE + ord(c)) % PMOD
        yield h

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    Cnt = Counter(chain(*map(prefix_hash, set(W))))
    for w in W:
        l = 1
        for h in prefix_hash(w):
            if Cnt[h]<2: break
            l += 1
        print(w[:l])

main()
