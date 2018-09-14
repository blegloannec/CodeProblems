#!/usr/bin/env python3

# Tricky greedy scheduling algo, way harder than it looks...
# see e.g. Brucker, Scheduling Algorithms, sec 4.3.1, p73

# We condider the partial (topological) ordering < induced by the tree.
# chain := a sequence of vertices to delete consecutively (hence compatible
# with the ordering: if two comparable vertices u < v are in the chain,
# then u appears before v).
# two chains A and B are independent iff no two vertices u in A and v in B
# are comparable. Equivalently, A and B can executed in any order AB or BA
# (not interlaced as by definition of a chain, vertices are to be deleted
# consecutively).
# Cost(A) = sum of vertices costs in A

# 1. Heuristic
# if A and B are independent chains that we will execute consecutively,
# executing A before B leads to an "additional cost" of Cost(B)*Size(A)
# and hence is the right choice iff Cost(B)*Size(A) <= Cost(A)*Size(B)
# iff Score(B) := Cost(B)/Size(B) <= Cost(A)/Size(A) =: Score(A).

# 2. Greedy choice
# Considering a current set of optimal chains, if A is the chain
# of *maximum Score*, then there exists an optimal schedule where
# A is executed immediately after the chain B that contains the parent
# of the head of A.
# Hence we can merge chains B and A, recompute the associated score
# and repeat until there is only one remaining chain.


from heapq import *

def find(x):
    if Tarj[x]<0:
        return x
    Tarj[x] = find(Tarj[x])
    return Tarj[x]

def union(x,y):
    # assuming x and y are distinct representatives
    Tarj[y] = x
    Count[x] += Count[y]
    Cost[x] += Cost[y]
    Pred[y] = Last[x]
    Last[x] = Last[y]

def score(u):
    return -Cost[u]/Count[u]

def schedule():
    # assuming the root is 0
    global Count,Tarj,Pred,Last
    Count = [1]*n
    Tarj = [-1]*n
    Pred = [None]*n
    Last = list(range(n))
    H = [(score(u),u) for u in range(n)]
    heapify(H)
    while H:
        s,u = heappop(H)
        if u==0 or find(u)!=u or score(u)!=s:
            continue
        v = find(P[u])
        union(v,u)
        heappush(H,(score(v),v))
    S = []
    u = Last[0]
    while u!=None:
        S.append(u)
        u = Pred[u]
    return S[::-1]

def main():
    global n,Cost,P
    n = int(input())
    Cost = list(map(int,input().split()))
    P = [None]+[int(x)-1 for x in input().split()]
    C = Cost[:]
    S = schedule()
    res = sum(C[S[i]]*i for i in range(n))
    print(res)

main()
