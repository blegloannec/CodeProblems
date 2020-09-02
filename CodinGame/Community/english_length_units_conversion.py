#!/usr/bin/env python3

import re
from fractions import Fraction
from collections import defaultdict, deque

def conv_bfs(ConvGrph, u0, uf):
    Q = deque([u0])
    Rate = {u0: Fraction(1)}
    while Q:
        u = Q.popleft()
        if u==uf:
            return Rate[uf]
        for v,r in ConvGrph[u]:
            if v not in Rate:
                Rate[v] = Rate[u]*r
                Q.append(v)

def main():
    from_unit, to_unit = input().split(' in ')
    ConvGrph = defaultdict(list)
    N = int(input())
    for _ in range(N):
        rel = re.match(r'(\d+) (.+) = (\d+) (.+)$', input())
        f = Fraction(int(rel.group(1)), int(rel.group(3)))
        u1 = rel.group(2); u2 = rel.group(4)
        ConvGrph[u1].append((u2, f))
        ConvGrph[u2].append((u1, 1/f))
    rate = conv_bfs(ConvGrph, from_unit, to_unit)
    print(f'{rate.numerator} {from_unit} = {rate.denominator} {to_unit}')

main()
