#!/usr/bin/env python3

import sys

I = [L.rstrip('\n') for L in sys.stdin.readlines()]
S = len(I)
A0 = [[int(c=='#') for c in L] for L in I]


# Part 1
def step(A):
    B = [[0]*S for L in range(S)]
    for x in range(S):
        for y in range(S):
            s = 0
            for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0<=vx<S and 0<=vy<S:
                    s += A[vx][vy]
            B[x][y] = int(s==1 if A[x][y] else 1<=s<=2)
    return B

def mask(A):
    m = 0
    for i in range(S-1,-1,-1):
        for j in range(S-1,-1,-1):
            m = (m<<1) | A[i][j]
    return m

Seen = set()
A = A0
M = mask(A)
while M not in Seen:
    Seen.add(M)
    A = step(A)
    M = mask(A)
print(M)


# Part 2
M = S//2
assert A0[M][M]==0

def step_rec(Adown, A, Aup):
    B = [[0]*S for _ in range(S)]
    if Adown is not None:
        AdU = sum(Adown[0])
        AdD = sum(Adown[-1])
        AdL = sum(Adown[i][0] for i in range(S))
        AdR = sum(Adown[i][-1] for i in range(S))
    else:
        AdU = AdD = AdL = AdR = 0
    for x in range(S):
        for y in range(S):
            if x==y==M:
                continue
            s = 0
            for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if vx==vy==M:
                    if y==M:
                        s += AdU if x==M-1 else AdD
                    else: # x==M
                        s += AdL if y==M-1 else AdR
                elif 0<=vx<S and 0<=vy<S:
                    s += A[vx][vy]
                elif Aup is not None:
                    if vx==-1:
                        s += Aup[M-1][M]
                    elif vx==S:
                        s += Aup[M+1][M]
                    elif vy==-1:
                        s += Aup[M][M-1]
                    else: # vy==S
                        s += Aup[M][M+1]
            B[x][y] = int(s==1 if A[x][y] else 1<=s<=2)
    return B

Z = [[0]*S for _ in range(S)]
L = [None,Z,A0,Z,None]
for t in range(200):
    L = [None,Z] + [step_rec(L[l-1],L[l],L[l+1]) for l in range(1,len(L)-1)] + [Z,None]
print(sum(sum(sum(a) for a in L[i]) for i in range(1,len(L)-1)))
