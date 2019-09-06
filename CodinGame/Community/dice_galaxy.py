#!/usr/bin/env python3

Dirs = ((-1,0),(1,0),(0,-1),(0,1))

def dfs_tree(i,j, disti,distj, i0,j0, di0,dj0):
    if 0<=i<H and 0<=j<W and G[i][j]=='#':
        if disti*di0 + distj*dj0 == 2:
            G[i][j] = '6'
        else:
            for di,dj in Dirs:
                if (i+di,j+dj)!=(i0,j0):
                    dfs_tree(i+di,j+dj, disti+di,distj+dj, i,j, di0,dj0)

if __name__=='__main__':
    W = int(input())
    H = int(input())
    G = [list(input().replace('6','#')) for _ in range(H)]
    Ones = [(i,j) for i in range(H) for j in range(W) if G[i][j]=='1']
    for i0,j0 in Ones:
        for di,dj in Dirs:
            dfs_tree(i0+di,j0+dj, di,dj, i0,j0, di,dj)
    print('\n'.join(''.join(L) for L in G))
