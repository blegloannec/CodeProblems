#!/usr/bin/env python3

Q,M,S,L = map(int, input().split())
q,r = divmod(L,M)
t = q*Q
if r>0:
    t += Q
    S -= (M-r)*Q
if S>0:
    t += (S+M-1)//M
print(t)
