#!/usr/bin/env python3

n = int(input())
P = [int(p)-1 for p in input().split()]  # permutation
seen = [False]*n
res = m0 = m1 = 0
for i in range(n):
    if not seen[i]:
        seen[i] = True
        j = P[i]
        c = 1  # taille du cycle
        while j!=i:
            seen[j] = True
            j = P[j]
            c += 1
        res += c*c
        if c>m0:
            m0,m1 = c,m0
        elif c>m1:
            m1 = c
# on fusionne les 2 plus grands cycles
res += (m0+m1)*(m0+m1)-m0*m0-m1*m1
print(res)
