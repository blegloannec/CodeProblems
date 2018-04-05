#!/usr/bin/env python3

import sys

def aug(u,G,M,seen):
    for v in G[u]:
        if not seen[v]:
            seen[v] = True
            if M[v]==None or aug(M[v],G,M,seen):
                M[v] = u
                return True
    return False

def bip_match(G,Us,Vs):
    M = [None]*Vs
    for u in range(Us):
        aug(u,G,M,[False]*Vs)
    return M

def main():
    I = sys.stdin.readlines()
    l = 0
    while l<len(I):
        N = int(I[l])
        G = []
        L = C = 0
        Cc = [None]*N
        for i in range(l+1,l+1+N):
            Lc = None
            for j in range(N):
                if I[i][j]=='.':
                    if Lc==None:
                        Lc = L
                        L += 1
                        G.append([])
                    if Cc[j]==None:
                        Cc[j] = C
                        C += 1
                    G[Lc].append(Cc[j])
                else:
                    Lc = Cc[j] = None
        M = bip_match(G,L,C)
        print(sum(int(x!=None) for x in M))
        l += N+1

main()
