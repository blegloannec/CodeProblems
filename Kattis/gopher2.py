#!/usr/bin/env python3

# same as UVa 10080

### max bipartite matching from tryalgo ###
def augment(u, bigraph, visit, match):
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v], bigraph, visit, match):
                match[v] = u
                return True
    return False

def bip_match(bigraph, nU, nV):
    match = [None]*nV
    for u in range(nU):
        augment(u, bigraph, [False]*nV, match)
    return match
### ===== ###

dist2 = lambda P,Q: (P[0]-Q[0])**2 + (P[1]-Q[1])**2

def case():
    n,m,s,v = map(int,input().split())
    A = [tuple(map(float,input().split())) for _ in range(n)]
    B = [tuple(map(float,input().split())) for _ in range(m)]
    dist2_max = (v*s)**2
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if dist2(A[i],B[j]) <= dist2_max:
                G[i].append(j)
    match = bip_match(G, n, m)
    size = m-match.count(None)
    print(n-size)

def main():
    while True:
        try:
            case()
        except:
            break

main()
