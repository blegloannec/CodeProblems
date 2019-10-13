#!/usr/bin/env python3

from functools import lru_cache

V = ((-1,-2),(-2,-1),(1,-2),(-2,1),(1,2),(2,1),(-1,2),(2,-1))

Target = 'ICPCASIASG'
Layers = {}
for l,c in enumerate(Target):
    if c in Layers:
        Layers[c].append(l)
    else:
        Layers[c] = [l]

def build_layered_dag():
    global DAG
    DAG = {}
    for i in range(S):
        for j in range(S):
            if G[i][j] in Layers:
                L = Layers[G[i][j]]
                for l in L:
                    DAG[l,i,j] = []
                for di,dj in V:
                    vi,vj = i+di,j+dj
                    if 0<=vi<S and 0<=vj<S:
                        for l in L:
                            if l+1<len(Target) and Target[l+1]==G[vi][vj]:
                                DAG[l,i,j].append((l+1,vi,vj))

@lru_cache(maxsize=None)
def length(u):
    l = 1
    if DAG[u]:
        l += max(length(v) for v in DAG[u])
    return l

def main():
    global S,G
    S = int(input())
    I = input()
    G = [I[i:i+S] for i in range(0,S*S,S)]
    build_layered_dag()
    found = any(length(u)==len(Target) for u in DAG if u[0]==0)
    print('YES' if found else 'NO')

main()
