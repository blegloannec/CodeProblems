#!/usr/bin/env python3

import sys

I = [L.strip() for L in sys.stdin.readlines()]

# Part 1
I.sort()
Asleep = {}
for L in I:
    M = int(L[15:17])
    T = L[19:].split()
    if T[0]=='Guard':
        G = int(T[1][1:])
        if G not in Asleep:
            Asleep[G] = [0]*60
    elif T[0]=='falls':
        M0 = M
    elif T[0]=='wakes':
        for m in range(M0,M):
            Asleep[G][m] += 1

Gmax = max(Asleep.keys(), key=(lambda G: sum(Asleep[G])))
Mmax = max(range(60), key=(lambda M: Asleep[Gmax][M]))
print(Gmax*Mmax)


# Part 2
Gmax = max(Asleep.keys(), key=(lambda G: max(Asleep[G])))
Mmax = max(range(60), key=(lambda M: Asleep[Gmax][M]))
print(Gmax*Mmax)
