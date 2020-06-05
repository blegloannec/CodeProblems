#!/usr/bin/env python3

S = 16

res = 0
L = ' '*S
for _ in range(S):
    L, L0 = input(), L
    inside = False
    for j,c in enumerate(L):
        if c=='|' or (c=='+' and L0[j] in '|+'):
            # "Crossing number" technique for the point-in-polygon problem.
            # When meeting a +, we only flip inside/outside if the corresponding
            # edge is above (arbitrarily), and ignore it when it is below.
            # That way, we properly deal with all situations:
            #      | |   |       |
            # ~~>  +-+   +-+   +-+   +-+  ~~>
            #              |   |     | |
            #     0110  0111  0001  0000
            inside = not inside
        elif c=='o' and inside:
            res += 1
print(res)
