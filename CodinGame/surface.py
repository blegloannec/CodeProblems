#!/usr/bin/env python3

# iterative version needed as H*W ~ 10^8
def DFS(i0,j0,C,c):
    Q = [(i0,j0)]
    C[i0][j0] = c
    S = 1
    while Q:
        i,j = Q.pop()
        for vi,vj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=vi<H and 0<=vj<W and G[vi][vj]=='O' and C[vi][vj]==0:
                C[vi][vj] = c
                S += 1
                Q.append((vi,vj))
    return S

# connected components
def CC():
    C = [[0]*W for _ in range(H)]
    S = [0]
    c = 1
    for i in range(H):
        for j in range(W):
            if G[i][j]=='O' and C[i][j]==0:
                S.append(DFS(i,j,C,c))
                c += 1
    return C,S

def main():
    global W,H,G
    W = int(input())
    H = int(input())
    G = [input() for _ in range(H)]
    C,S = CC()
    Q = int(input())
    for _ in range(Q):
        j,i = map(int,input().split())
        print(S[C[i][j]])

main()
