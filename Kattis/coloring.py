#!/usr/bin/env python3

def backtrack(k, C, u=1):
    if u==N:
        return True
    Avail = [True]*k
    for v in G[u]:
        Avail[C[v]] = False
    if C[u] is not None:
        if Avail[C[u]]:
            return backtrack(k, C, u+1)
        return False
    for c in range(k):
        if Avail[c]:
            C[u] = c
            if backtrack(k, C, u+1):
                return True
            C[u] = None
    return False

def main():
    global N, G
    N = int(input())
    G = []
    k = 0
    C = [None]*N
    C[0] = 0
    for u in range(N):
        V = list(map(int,input().split()))
        if u==0:
            C[V[0]] = 1
        k = max(k, len(V))  # https://en.wikipedia.org/wiki/Brooks%27_theorem
        G.append([v for v in V if v<u])
    while k>1 and backtrack(k, C[:]):
        k -= 1
    k += 1
    print(k)

main()
