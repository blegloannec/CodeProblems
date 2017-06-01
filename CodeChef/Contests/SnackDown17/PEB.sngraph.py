#!/usr/bin/env python3

def find(T,x):
    if T[x]<0:
        return x
    T[x] = find(T,T[x])
    return T[x]

def union(T,x,y):
    x0,y0 = find(T,x),find(T,y)
    T[y0] = x0

def main():
    t = int(input())
    for _ in range(t):
        n,m = map(int,input().split())
        G = [[] for _ in range(n)]
        for _ in range(m):
            u,v = map(int,input().split())
            u -= 1
            v -= 1
            G[u].append(v)
            G[v].append(u)
        # sommets par degre
        D = [[] for _ in range(n)]
        for u in range(n):
            D[len(G[u])].append(u)
        T = [-1]*n  # union-find pour les composantes connexes
        compo = n   # nb de composantes connexes
        L = [0]*n
        # on reconstruit le graphe a l'envers
        for d in range(n-1,-1,-1):
            L[d] = compo-1  # liens a ajouter apres l'etape d
            for u in D[d]:
                for v in G[u]:
                    if len(G[v])>=d:
                        if find(T,u)!=find(T,v):
                            union(T,u,v)
                            compo -= 1
        print(' '.join(map(str,L)))

main()
