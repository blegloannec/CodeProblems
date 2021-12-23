#!/usr/bin/env python3

T = int(input())
for t in range(1, T+1):
    N1,D1,D2 = input().split()
    B1 = len(D1)
    x = 0
    for d in N1:
        x = B1*x + D1.index(d)
    B2 = len(D2)
    N2 = []
    while x:
        x,d = divmod(x, B2)
        N2.append(D2[d])
    N2 = ''.join(reversed(N2))
    print(f'Case #{t}: {N2}')
