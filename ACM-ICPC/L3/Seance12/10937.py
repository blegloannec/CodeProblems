#!/usr/bin/env python3

from collections import deque

inf = float('inf')

def bfs(i0,j0):
    Q = deque([(i0,j0)])
    D = [[inf]*w for _ in range(h)]
    D[i0][j0] = 0
    while Q:
        i,j = Q.popleft()
        for (vi,vj) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=vi<h and 0<=vj<w and G[vi][vj]=='.' and D[vi][vj]==inf:
                D[vi][vj] = D[i][j]+1
                Q.append((vi,vj))
    return D

# bitmask Held-Karp
memo = {}
def tsp(used,u):
    if used==0:
        return 0 if u==0 else inf
    if (used,u) in memo:
        return memo[used,u]
    res = inf
    for v in range(len(T)):
        if (used>>v)&1:
            res = min(res,tsp(used^(1<<v),v)+D[v][T[u][0]][T[u][1]])
    memo[used,u] = res
    return res

def cycle_tsp():
    memo.clear()
    full = (1<<len(T))-1
    return min(tsp(full^(1<<v),v)+D[v][T[0][0]][T[0][1]] for v in range(1,len(T)))

def main():
    global G,h,w,T,D
    while True:
        h,w = map(int,input().split())
        if h==w==0:
            break
        G = [list(input()) for _ in range(h)]
        T = []
        imp = False
        for i in range(h):
            for j in range(w):
                if G[i][j]=='~':
                    G[i][j] = '#'
                elif G[i][j]=='!':
                    T.append((i,j))
                    G[i][j] = '.'
                elif G[i][j]=='@':
                    i0,j0 = i,j
                    G[i][j] = '.'
                elif G[i][j]=='*':
                    G[i][j] = '#'
                    for vi in range(i-1,i+2):
                        for vj in range(j-1,j+2):
                            if 0<=vi<h and 0<=vj<w:
                                if G[vi][vj]=='@' or G[vi][vj]=='!':
                                    imp = True
                                elif G[vi][vj]!='*':
                                    G[vi][vj] = '#'
        if len(T)==0:
            print(0)
        elif imp:
            print(-1)
        else:
            T = [(i0,j0)]+T
            D = [bfs(T[u][0],T[u][1]) for u in range(len(T))]
            res = cycle_tsp()
            print(-1 if res==inf else res)

main()
