#!/usr/bin/env python3

N = 16

def perm2str(P):
    return ''.join(chr(i+ord('a')) for i in P)

def num(c):
    return ord(c)-ord('a')

## Part 1
def dance(I, P=None):
    if P==None:
        P = list(range(N))
    index = lambda c: P.index(num(c))
    for C in I:
        if C[0]=='s':
            X = int(C[1:])
            P = P[-X:]+P[:-X]
        else:
            if C[0]=='x':
                A,B = map(int,C[1:].split('/'))
            else:
                A,B = map(index,C[1:].split('/'))
            P[A],P[B] = P[B],P[A]
    return P

I = input().split(',')
print(perm2str(dance(I)))


## Part 2
n = 10**9

# Method 0: naive "global" eventual periodicity (as on day 6)
# ~0.4s with python3 (for a short cycle)
def iter_cycle(I,n):
    P = list(range(N))
    K = tuple(P)
    V,S,t = [],{},0
    while K not in S:
        V.append(K)
        S[K] = t
        P = dance(I,P)
        K = tuple(P)
        t += 1
    pre,per = S[K],t-S[K]
    if n<pre:
        return V[n]
    else:
        return V[pre+(n-pre)%per]
    
#print(perm2str(iter_cycle(I,n)))


# Method 1: the dance is the "composition" of two completely independent
# permutations (that "commute"), one on the positions and one on the values
# we compute those permutations in O(dance size)
# and their iterations in O(1) via cycle decomposition
def perm_dance(I):
    P = list(range(N))  # positions permutation
    Q = P[:]            # values permutation
    for C in I:
        if C[0]=='s':
            X = int(C[1:])
            P = P[-X:]+P[:-X]
        elif C[0]=='x':
            A,B = map(int,C[1:].split('/'))
            P[A],P[B] = P[B],P[A]
        else:
            A,B = map(num,C[1:].split('/'))
            Q[A],Q[B] = Q[B],Q[A]
    return P,Q

def cycle_decomp(P):
    C = []
    seen = [False]*len(P)
    for i in range(len(P)):
        if not seen[i]:
            C0 = [i]
            j = P[i]
            while j!=i:
                C0.append(j)
                j = P[j]
            C.append(C0)
    return C

def iter_perm(D,n):
    P = [0]*N
    for C in D:
        for i in range(len(C)):
            P[C[(i+n)%len(C)]] = C[i]
    return P

P,Q = perm_dance(I)
P = iter_perm(cycle_decomp(P),n)
Q = iter_perm(cycle_decomp(Q),n)
R = [0]*N  # result
for i in range(N):
    R[P[i]] = Q[i]
print(perm2str(R))
