#!/usr/bin/env python3

S,N = map(int, input().split())
P = [(i+1,0) for i in range(N)]
p = 0
while len(P) > 1:
    p = (p+S-1) % len(P)
    i,c = P[p]
    if c == 0:
        P = P[:p] + [(i,1), (i,1)] + P[p+1:]
    elif c == 1:
        P[p] = (i,2)
        p += 1
    else:
        P = P[:p] + P[p+1:]
print(P[0][0])
