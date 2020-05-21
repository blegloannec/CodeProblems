#!/usr/bin/env python3

# "functional" graph, each connected component is made of some trees
# leading to a cycle
# taking the whole cycle is mandatory if one picks anyone from the component
# but all tree vertices are optional
# hence each component can contribute with any value from the interval
# [cycle size, full component size]

def get_comp(u):
    if Comp[u] is None:
        Comp[u] = get_comp(Succ[u])
    return Comp[u]

def main():
    global Succ, Comp
    N,K = map(int, input().split())
    Succ = [int(i)-1 for i in input().split()]
    # 1. identify components & their cycles
    Pred = [0]*N
    for v in Succ:
        Pred[v] += 1
    Q = [u for u in range(N) if Pred[u]==0]
    InACycle = [True]*N
    while Q:
        u = Q.pop()
        InACycle[u] = False
        v = Succ[u]
        Pred[v] -= 1
        if Pred[v]==0:
            Q.append(v)
    Comp = [None]*N
    C = 0
    for u in range(N):
        if InACycle[u] and Comp[u] is None:
            Comp[u] = C
            v = Succ[u]
            while v!=u:
                Comp[v] = C
                v = Succ[v]
            C += 1
    CompSize = [0]*C
    CycleSize = [0]*C
    for u in range(N):
        c = get_comp(u)
        CompSize[c] += 1
        if InACycle[u]:
            CycleSize[c] += 1
    # 2. solving actual problem
    DP = [-1]*(K+1)
    DP[0] = 0
    # DP[k] = max size of any subset of components such that their
    #         cycle sizes sum up to k
    for siz, cyc in zip(CompSize, CycleSize):
        for k in range(K-cyc,-1,-1):
            if DP[k]>=0:
                DP[k+cyc] = max(DP[k+cyc], DP[k]+siz)
    res = min(K, max(DP))
    print(res)

main()
