#!/usr/bin/env python3

# DFS backtracking
# NB: An Held-Karp-like DP would also be possible
#     (to benefit from memoization), but cases are
#     very weak anyways.
def dfs(i,j):
    p = Map[i][j].lower()
    w = 1 if Map[i][j]==p else 0
    res = w
    Seen[i][j] = True
    for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
        if 0<=vi<N and 0<=vj<N and not Seen[vi][vj] and Map[vi][vj].lower()==p:
            res = max(res, w+dfs(vi,vj))
    Seen[i][j] = False
    return res

def main():
    global N,Map,Seen
    N = int(input())
    Map = [input() for _ in range(N)]
    Seen = [[c=='#' for c in L] for L in Map]
    res = 0
    for i in range(N):
        for j in range(N):
            if not Seen[i][j]:
                l = dfs(i,j)
                if l>=5 and l>res:
                    res = l
                    win = Map[i][j].upper()
    print(f'{win} {res}' if res else '0')

main()
