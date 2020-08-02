#!/usr/bin/env python3

OP = '+-*/'

N = int(input())
E = []
for c in input().split():
    if c in OP:
        b,pb = E.pop()
        a,pa = E.pop()
        pc = OP.index(c)
        if pc>>1 > pa>>1:
            a = f'({a})'
        if pc>pb or (pc==pb and pc&1):
            b = f'({b})'
        E.append((f'{a} {c} {b}', pc))
    else:
        E.append((c, len(OP)))
print(E[0][0])
