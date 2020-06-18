#!/usr/bin/env python3

def backtrack(k=0):
    if k==N*N:
        return True
    i,j = divmod(k,N)
    if Sol[i][j]>0:
        return backtrack(k+1)
    l,r = 1,N
    if i>0:
        if   G[2*i-1][2*j]=='v': r = min(r, Sol[i-1][j]-1)
        elif G[2*i-1][2*j]=='^': l = max(l, Sol[i-1][j]+1)
    if i+1<N and Sol[i+1][j]>0:
        if   G[2*i+1][2*j]=='^': r = min(r, Sol[i+1][j]-1)
        elif G[2*i+1][2*j]=='v': l = max(l, Sol[i+1][j]+1)
    if j>0:
        if   G[2*i][2*j-1]=='>': r = min(r, Sol[i][j-1]-1)
        elif G[2*i][2*j-1]=='<': l = max(l, Sol[i][j-1]+1)
    if j+1<N and Sol[i][j+1]>0:
        if   G[2*i][2*j+1]=='<': r = min(r, Sol[i][j+1]-1)
        elif G[2*i][2*j+1]=='>': l = max(l, Sol[i][j+1]+1)
    for x in range(l,r+1):
        if not (RowUsed[i][x] or ColUsed[j][x]):
            Sol[i][j] = x
            RowUsed[i][x] = ColUsed[j][x] = True
            if backtrack(k+1):
                return True
            Sol[i][j] = 0
            RowUsed[i][x] = ColUsed[j][x] = False
    return False

def main():
    global N, G, Sol, RowUsed, ColUsed
    S = int(input())
    N = (S+1)//2
    G = [input() for _ in range(S)]
    Sol = [[0]*N for _  in range(N)]
    RowUsed = [[False]*(N+1) for _ in range(N)]
    ColUsed = [[False]*(N+1) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            x = int(G[2*i][2*j])
            if x!=0:
                Sol[i][j] = x
                RowUsed[i][x] = ColUsed[j][x] = True
    assert backtrack()
    print('\n'.join(''.join(map(str,L)) for L in Sol))

main()
