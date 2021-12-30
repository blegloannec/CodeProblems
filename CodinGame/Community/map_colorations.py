#!/usr/bin/env python3

def monomial(n):
    P = [0]*(n+1)
    P[n] = 1
    return P

def poly_sub(P, Q):
    return [(P[i] if i<len(P) else 0) - (Q[i] if i<len(Q) else 0) for i in range(max(len(P),len(Q)))]

def poly_eval(P, x):
    res = 0
    for c in reversed(P):
        res = res*x + c
    return res

# https://en.wikipedia.org/wiki/Chromatic_polynomial
def chromatic_poly(V, Edges):
    if Edges:
        u,v = Edges.pop()
        if u==v:
            return chromatic_poly(V, Edges)
        Edges = [e for e in Edges if e!=(u,v) and e!=(v,u)]
        EdgesMerge = [((u if a==v else a), (u if b==v else b)) for a,b in Edges]
        return poly_sub(chromatic_poly(V, Edges), chromatic_poly(V-1, EdgesMerge))
    return monomial(V)

def main():
    N = int(input())
    E = []
    Num = {}
    for _ in range(N):
        u,v = input().split()
        if u not in Num:
            Num[u] = len(Num)
        if v not in Num:
            Num[v] = len(Num)
        E.append((Num[u],Num[v]))
    V = len(Num)
    P = chromatic_poly(V, E)
    K = int(input())
    for _ in range(K):
        C = int(input())
        print(poly_eval(P,C))

main()
