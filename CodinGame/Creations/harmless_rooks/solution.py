#!/usr/bin/env python3

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
    N = int(input())
    B = [input() for _ in range(N)]
    G = []
    L = C = 0
    Cc = [None]*N
    for i in range(N):
        Lc = None
        for j in range(N):
            if B[i][j]=='.':
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
    S = len(M) - M.count(None)
    print(S)

main()
