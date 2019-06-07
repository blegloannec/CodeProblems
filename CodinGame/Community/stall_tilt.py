#!/usr/bin/env python3

from math import *

G = 9.81
Alim = pi/3.

N = int(input())
B = int(input())
S = [int(input()) for _ in range(N)]
R = [int(input()) for _ in range(B)]

Slim = int(sqrt(tan(Alim)*min(R)*G))
Ranking = [(B,Slim,'y')]
for i in range(N):
    try:
        b = next(j for j in range(B) if atan(S[i]*S[i]/R[j]/G) > Alim)
    except StopIteration:
        b = B
    Ranking.append((b, S[i], chr(i+ord('a'))))
Ranking.sort(reverse=True)

print(Slim)
print('\n'.join(a for _,_,a in Ranking))
