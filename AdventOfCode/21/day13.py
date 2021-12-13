#!/usr/bin/env python3

import sys


# Parsing input
Pts = []
Instr = []
read_pt = True
for L in sys.stdin.readlines():
    L = L.strip()
    if L=='':
        read_pt = False
    elif read_pt:
        Pts.append(tuple(map(int, L.split(','))))
    else:
        a,p = L.split('=')
        Instr.append((a[-1], int(p)))


# Folding
part1 = True
for a,p in Instr:
    Pts1 = set()
    for x,y in Pts:
        if   a=='x' and x>p:
            Pts1.add((p-(x-p), y))
        elif a=='y' and y>p:
            Pts1.add((x, p-(y-p)))
        else:
            Pts1.add((x, y))
    Pts = Pts1
    if part1:
        print(len(Pts))  # Part 1
        part1 = False


# Output
W = max(x for x,_ in Pts)+1
H = max(y for _,y in Pts)+1
Out = [['  ']*W for _ in range(H)]
for x,y in Pts:
    Out[y][x] = '##'
print('\n'.join(''.join(L) for L in Out))
