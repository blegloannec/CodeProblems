#!/usr/bin/env python

## Data
K,V = 12,10
X = raw_input().strip()
if X=='':
    N = int(raw_input())
else:
    N = int(X)
G = []
C0 = []
for _ in xrange(N):
    A,B = raw_input().split()
    G.append(A)
    C0.append(int(B))

## Aux
def getC(C,i):
    return (C>>(2*i))&3

def decrC(C,i):
    # on retire 1 au ieme chiffre (suppose >0)
    # en base 4
    return C - (1<<(2*i))

# representation de C en base 4
def encodeC(C):
    res = 0
    for i in xrange(len(C)-1,-1,-1):
        res = 4*res + C[i]
    return res

def initLC(G,LC):
    for c in xrange(len(G)):
        for i in xrange(K):
            LC[i][G[c][i]].append(c)


## Init
G = map((lambda s: map(int,list(s))), G)
N = len(G)
LC = [[[] for _ in xrange(V)] for _ in xrange(K)]
initLC(G,LC)
C0 = encodeC(C0)


## Backtracking
memo = {}
def backtrack_first_half(C1,i=0,S=[]):
    if i==K/2:
        # on en memorise qu'un pour economiser la memoire
        # car on sait qu'il n'y aura qu'une unique solution
        if C1 not in memo:
            memo[C1] = tuple(S[:])
        else:
            memo[C1] = None
        return
    for a in xrange(V):
        avail = True
        for c in LC[i][a]:
            if getC(C1,c)==0:
                avail = False
                break
        if avail:
            C = C1
            for c in LC[i][a]:
                C = decrC(C,c)
            S.append(a)
            backtrack_first_half(C,i+1,S)
            S.pop()

def backtrack_second_half(C1,i=K/2,S=[]):
    if i==K:
        # on cherche une premiere moitie complementaire
        # complement de C1 obtenu par simple soustraction
        # car les chiffres en base 4 de C0 sont supposes
        # >= a ceux de C1
        C = C0-C1
        if C in memo:
            return list(memo[C])+S
        return None
    for a in xrange(V):
        avail = True
        for c in LC[i][a]:
            if getC(C1,c)==0:
                avail = False
                break
        if avail:
            C = C1
            for c in LC[i][a]:
                C = decrC(C,c)
            S.append(a)
            X = backtrack_second_half(C,i+1,S)
            if X!=None:
                return X
            S.pop()
    return None

## MAIN
def main():
    backtrack_first_half(C0)
    print ''.join(map(str,backtrack_second_half(C0)))

main()
