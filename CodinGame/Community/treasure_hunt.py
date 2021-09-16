#!/usr/bin/env python3

def dfs_backtrack(i,j):
    res = 0
    if not Seen[i][j]:
        Seen[i][j] = True
        for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=vi<H and 0<=vj<W:
                res = max(res, dfs_backtrack(vi,vj))
        res += Map[i][j]
        Seen[i][j] = False
    return res

def main():
    global H,W,Map,Seen
    H,W = map(int, input().split())
    Map = [list(input()) for _ in range(H)]
    Seen = [[False]*W for _ in range(H)]
    for i,L in enumerate(Map):
        for j,c in enumerate(L):
            if c=='X':
                i0,j0 = i,j
                L[j] = 0
            elif c==' ':
                L[j] = 0
            elif c=='#':
                Seen[i][j] = True
            else:
                L[j] = ord(c)-ord('0')
    print(dfs_backtrack(i0,j0))

main()
