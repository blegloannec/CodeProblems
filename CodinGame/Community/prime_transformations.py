#!/usr/bin/env python3

from collections import defaultdict

P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def decomp(n):
    D = []
    for p in P:
        m = 0
        while n%p==0:
            m += 1
            n //= p
        if m>0:
            D.append((p,m))
    return D

def main():
    X = int(input())
    C = int(input())
    # construction des associations possibles (via les exposants)
    Sol = {}
    for _ in range(C):
        A,B = map(int,input().split())
        IB = defaultdict(list)
        for p,m in decomp(B):
            IB[m].append(p)
        for p,m in decomp(A):
            sp = set(IB[m])
            if p in Sol:
                Sol[p] &= sp
            else:
                Sol[p] = sp
    # deductions
    RevSol = defaultdict(list)
    for p in Sol:
        for q in Sol[p]:
            RevSol[q].append(p)
    Sub = {}
    Q = [p for p in Sol if len(Sol[p])==1]
    while Q:
        p = Q.pop()
        Sub[p] = Sol[p].pop()
        for q in RevSol[Sub[p]]:   # on elimine les associations obsoletes
            if q!=p:
                Sol[q].remove(Sub[p])
                if len(Sol[q])==1:
                    Q.append(q)
    # calcul du resultat
    Y = 1
    for p,m in decomp(X):
        Y *= Sub[p]**m
    print(Y)

main()
