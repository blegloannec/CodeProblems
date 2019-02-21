#!/usr/bin/env python3

from collections import defaultdict

# This is a kinda classical problem related to the task of computing
# a longest eulerian (without edge repetition, seeing dominoes as edges) chain
# or a longest hamiltonian (without vertex repetition, seeing dominoes as
# vertices) chain.
# These problems have no efficient solution, one valid approach would be
# a O(n*2^n) DP a la Held-Karp (method 1 below).
# However here we are only interested in the decision problem,
# which is polynomial (method 0 below, eulerian path criterion).


# Method 0: eulerian path testing in linear-time
def eulerian(Domi):
    G = defaultdict(list)
    Deg = defaultdict(int)
    for a,b in Domi:
        G[a].append(b)
        G[b].append(a)
        Deg[a] += 1
        Deg[b] += 1
    odd = sum(Deg[a]%2 for a in G)
    if odd not in [0,2]:
        return False
    Q = [a]
    seen = set()
    while Q:
        a = Q.pop()
        for b in G[a]:
            if b not in seen:
                seen.add(b)
                Q.append(b)
    connected = len(seen)==len(G)
    return connected

def main0():
    N = int(input())
    Domi = [tuple(map(int,input().split())) for _ in range(N)]
    print(str(eulerian(Domi)).lower())

main0()


# Method 1: O(n*2^n) DP for the longest eulerian chain
def forward_dp():  # similar to a dfs
    full = (1<<N)-1
    Possible = set()
    Q = [(1<<i,Domi[i][1]) for i in range(N)]
    while Q:
        used,last = Q.pop()
        if used==full:
            return True
        for i,col in Left[last]:
            if used&(1<<i)==0:
                v = (used|(1<<i),col)
                if v not in Possible:
                    Possible.add(v)
                    Q.append(v)
    return False

def main1():
    global N,Domi,Left
    N = int(input())
    Domi = [tuple(map(int,input().split())) for _ in range(N)]
    Left = defaultdict(list)
    for i,(a,b) in enumerate(Domi):
        Left[a].append((i,b))
        Left[b].append((i,a))  # reversed
    print(str(forward_dp()).lower())

#main1()
