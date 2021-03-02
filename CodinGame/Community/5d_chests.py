#!/usr/bin/env python3

import itertools

D = 5

def prod(X):
    p = 1
    for x in X:
        p *= x
    return p

def sieve(n):
    P = [True]*n
    P[0] = P[1] = False
    for p in range(2, n):
        if P[p]:
            for k in range(p*p, n, p):
                P[k] = False
    return P


class UnionFind:
    def __init__(self):
        self.Repr = []
        self.Size = []
    
    def incr(self):
        self.Repr.append(None)
        self.Size.append(1)
        return len(self.Repr)-1
    
    def find(self, x):
        if self.Repr[x] is None:
            return x
        x0 = self.Repr[x] = self.find(self.Repr[x])
        return x0
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self.Repr[y] = x
        self.Size[x] += self.Size[y]
        return True


def main():
    N = int(input())
    C = int(input())
    P = sieve(C+1)
    UF = UnionFind()
    Gold = {}
    for X in itertools.combinations_with_replacement(range(1,N+1), D):
        if P[1+prod(X)%C]:
            for Y in itertools.permutations(X):
                if Y not in Gold:
                    Gold[Y] = UF.incr()
    for X,xid in Gold.items():
        X = list(X)
        for i in range(D):
            X[i] += 1
            Y = tuple(X)
            X[i] -= 1
            if Y in Gold:
                UF.union(xid, Gold[Y])
    print(len(Gold))
    print(UF.Repr.count(None))
    print(max(UF.Size))

main()
