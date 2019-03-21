#!/usr/bin/env python3

def dfs(i0, j0, c):
    size = borders = 0
    Q = [(i0,j0)]
    G[i0][j0] = c
    while Q:
        i,j = Q.pop()
        size += 1
        for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=vi<L and 0<=vj<L:
                if G[vi][vj]=='.':
                    Q.append((vi,vj))
                    G[vi][vj] = c
                elif G[vi][vj]=='B':
                    borders |= 1
                elif G[vi][vj]=='W':
                    borders |= 2
    return borders,size

if __name__=='__main__':
    L = int(input())
    G = [list(input()) for _ in range(L)]
    C = 0
    B,W = 0,6
    for i in range(L):
        for j in range(L):
            if G[i][j]=='.':
                b,s = dfs(i,j,C)
                if b==1:
                    B += s
                elif b==2:
                    W += s
                C += 1
            elif G[i][j]=='B':
                B += 1
            elif G[i][j]=='W':
                W += 1
    print('BLACK : %d' % B)
    print('WHITE : %d.5' % W)
    print(('BLACK' if B>W else 'WHITE'),'WINS')
