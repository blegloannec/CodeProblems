#!/usr/bin/env python3

import sys, re

I = [L.strip() for L in sys.stdin.readlines()]


# Part 1
Alle = {}
for i in range(len(I)):
    MO = re.match(r'^(.+) \(contains (.+)\)$', I[i])
    I[i] = MO.group(1).split()
    for a in MO.group(2).split(', '):
        if a in Alle: Alle[a] &= set(I[i])
        else:         Alle[a]  = set(I[i])

PosAll = set()
for P in Alle.values():
    PosAll |= P

part1 = 0
for ingr in I:
    for i in ingr:
        if i not in PosAll:
            part1 += 1
print(part1)


# Part 2 - Solving by leaf elimination (recycled from Day 16)
Sol = {}
Q = [a for a,P in Alle.items() if len(P)==1]
while Q:
    a0 = Q.pop()
    i = Alle[a0].pop()
    Sol[i] = a0
    del Alle[a0]
    for a,P in Alle.items():
        try:
            P.remove(i)
            if len(P)==1:
                Q.append(a)
        except KeyError:
            pass

print(','.join(sorted(Sol.keys(), key=(lambda i: Sol[i]))))
