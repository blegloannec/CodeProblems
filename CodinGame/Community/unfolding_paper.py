#!/usr/bin/env python3

N = int(input())
W,H = map(int,input().split())
G = [input() for _ in range(H)]

# connected components
CC = [[None]*W for _ in range(H)]

def dfs(i,j,c):
    CC[i][j] = c
    for vi,vj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=vi<H and 0<=vj<W and G[vi][vj]=='#' and CC[vi][vj]==None:
            dfs(vi,vj,c)

C = 0
for i in range(H):
    for j in range(W):
        if G[i][j]=='#' and CC[i][j]==None:
            dfs(i,j,C)
            C += 1

# Top, Bottom, Left, Right components and intersections
T = set(CC[0][j] for j in range(W) if CC[0][j]!=None)
B = set(CC[H-1][j] for j in range(W) if CC[H-1][j]!=None)
L = set(CC[i][0] for i in range(H) if CC[i][0]!=None)
R = set(CC[i][W-1] for i in range(H) if CC[i][W-1]!=None)
TL,TR,BL,BR = len(T&L),len(T&R),len(B&L),len(B&R)
T,B,L,R = map(len,[T,B,L,R])

# unfolding
for _ in range(N):
    # unfold bottom to top
    C = 2*C-T
    L,R = 2*L-TL,2*R-TR
    T,TL,TR = B,BL,BR
    # unfold right to left
    C = 2*C-L
    T,B = 2*T-TL,2*B-BL
    L,TL,BL = R,TR,BR
print(C)
