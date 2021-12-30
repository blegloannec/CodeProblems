#!/usr/bin/env python3

from math import sqrt

# X = G^x mod P
# x = q * S + r
# X * G^(-S)^q = G^r
def baby_step_giant_step(G,P,X):
    S = int(sqrt(P-1)) + 1
    D = {}
    Gr = 1
    for r in range(S):
        D[Gr] = r
        Gr = (Gr*G) % P
    GSinv = pow(G,(P-2)*S,P)
    Y = X
    for q in range(S):
        if Y in D:
            return q*S + D[Y]
        Y = (Y*GSinv) % P
    return -1

if __name__=='__main__':
    G,X,P = map(int,input().split())
    print(baby_step_giant_step(G,P,X))
