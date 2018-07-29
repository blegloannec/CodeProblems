#!/usr/bin/env python3

def decomp(N,X):
    S = [set(),set()]
    for i in range(N):
        S[X&1].add(i)
        X >>= 1
    return S

def main():
    N,C = map(int,input().split())
    P = [set(range(N)) for _ in range(N)]
    for _ in range(C):
        X,Y = (decomp(N,int(X)) for X in input().split())
        for b in range(2):
            for x in X[b]:
                P[x] &= Y[b]
    Q = [i for i in range(N) if len(P[i])==1]
    R = set(range(N))-set(Q)
    while Q:
        i = Q.pop()
        P[i] = P[i].pop()
        for j in list(R):
            P[j].discard(P[i])
            if len(P[j])==1:
                Q.append(j)
                R.remove(j)
    print(*(1<<P[i] for i in range(N)))

main()
