#!/usr/bin/env python3

import sys

NMAX = 15

def precomp_triangles(N, G, GMat, T):
    for u in range(N):
        for iv in range(len(G[u])):
            v = G[u][iv]
            for iw in range(iv+1,len(G[u])):
                w = G[u][iw]
                if GMat[v][w]:
                    T[u].append((v,w))
        if len(T[u])==0:
            return False
    return True

def backtrack(T, I, Used, iu=0):
    if iu==len(I):
        return True
    u = I[iu]
    if Used[u]:
        return backtrack(T, I, Used, iu+1)
    for v,w in T[u]:
        if not Used[v] and not Used[w]:
            Used[u] = Used[v] = Used[w] = True
            if backtrack(T, I, Used, iu+1):
                return True
            Used[u] = Used[v] = Used[w] = False
    return False

def main():
    while True:
        M = int(sys.stdin.readline())
        if M<=0:
            break
        N = 0
        Num = {}
        G = []
        GMat = [[False]*NMAX for _ in range(NMAX)]
        for _ in range(M):
            A,B = sys.stdin.readline().split()
            try:
                a = Num[A]
            except KeyError:
                Num[A] = a = N
                N += 1
                G.append([])
            try:
                b = Num[B]
            except KeyError:
                Num[B] = b = N
                N += 1
                G.append([])
            G[a].append(b)
            G[b].append(a)
            GMat[a][b] = GMat[b][a] = True
        if N%3!=0 or any(len(V)<2 for V in G):
            sys.stdout.write('impossible\n')
        else:
            T = [[] for _ in range(N)]
            if not precomp_triangles(N, G, GMat, T):
                sys.stdout.write('impossible\n')
            else:
                I = sorted(range(N), key=(lambda u: len(T[u])))
                Used = [False]*N
                if backtrack(T,I,Used):
                    sys.stdout.write('possible\n')
                else:
                    sys.stdout.write('impossible\n')

main()
