#!/usr/bin/env python3

# width of an order reduced to maximum bipartite matching via
# https://en.wikipedia.org/wiki/Dilworth's_theorem

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
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        V = list(map(int,input().split()))
        Order = [[] for _ in range(N)]
        for u in range(N):
            for v in range(u+1,N):
                if abs(V[u]-V[v])>=K:
                    Order[u].append(v)
        M = bip_match(Order,N,N)
        Ms = sum(1 for u in M if u is None)  # endpoints of chains
        print(Ms)

main()
