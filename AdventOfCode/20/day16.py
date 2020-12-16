#!/usr/bin/env python3

import re

# Parsing rules
Fields = {}
L = input()
while L:
    L = re.match(r'(.+?): (\d+)-(\d+) or (\d+)-(\d+)$', L)
    Fields[L.group(1)] = tuple(int(L.group(k)) for k in range(2,6))
    L = input()

# My ticket
input()
Mine = list(map(int, input().split(',')))
input()
input()

# Part 1 - Marking acceptable values
Values = [False]*1000
for l1,r1,l2,r2 in Fields.values():
    for v in range(l1,r1+1): Values[v] = True
    for v in range(l2,r2+1): Values[v] = True

# Part 1 - Parsing tickets and keeping valid ones
Tickets = []
part1 = 0
while True:
    try:
        T = list(map(int, input().split(',')))
    except EOFError:
        break
    err = [x for x in T if not Values[x]]
    if err:
        part1 += sum(err)
    else:
        Tickets.append(T)
print(part1)


# Part 2 - Computing possible indices for each field
PosIdx = {f:[] for f in Fields}
for name,(l1,r1,l2,r2) in Fields.items():
    for i in range(len(Fields)):
        if all(l1<=T[i]<=r1 or l2<=T[i]<=r2 for T in Tickets):
            PosIdx[name].append(i)

# Part 2 - Solving by leaf elimination
Idx = [None]*len(Fields)
Q = [f for f,I in PosIdx.items() if len(I)==1]
while Q:
    f0 = Q.pop()
    i = PosIdx[f0][0]
    Idx[i] = f0
    del PosIdx[f0]
    for f,I in PosIdx.items():
        try:
            I.remove(i)
            if len(I)==1:
                Q.append(f)
        except ValueError:
            pass

# Part 2 - Result
part2 = 1
for i,f in enumerate(Idx):
    if f.startswith('departure'):
        part2 *= Mine[i]
print(part2)
