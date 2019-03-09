#!/usr/bin/env python3

# NB: we use a simple DFS here as "It is guaranteed that there is only one path..."
def dfs():
    u0 = next((i,j) for i in range(H) for j in range(W) if G[i][j]=='M')
    Q = [u0]
    Dist = {u0: 0}
    while Q:
        u = i,j = Q.pop()
        if G[i][j]=='*':
            return Dist[u]
        V = [(vi,vj) for vi,vj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]  \
             if 0<=vi<H and 0<=vj<W and G[vi][vj]!='X']
        w = int(len(V)>2 or (G[i][j]=='M' and len(V)>1))
        for v in V:
            if v not in Dist:
                Dist[v] = Dist[u] + w
                Q.append(v)

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        H,W = map(int,input().split())
        G = [input() for _ in range(H)]
        K = int(input())
        print('Impressed' if dfs()==K else 'Oops!')
