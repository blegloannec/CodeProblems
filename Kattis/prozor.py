#!/usr/bin/env python3

def main():
    H,W, S = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    Cnt = [[int(c=='*') for c in L] for L in G]
    for i in range(H):
        for j in range(W):
            if i>0:         Cnt[i][j] += Cnt[i-1][j]
            if j>0:         Cnt[i][j] += Cnt[i][j-1]
            if i>0 and j>0: Cnt[i][j] -= Cnt[i-1][j-1]
    cmax = imax = jmax = 0
    for i in range(H-S+1):
        for j in range(W-S+1):
            c = Cnt[i+S-2][j+S-2] - Cnt[i+S-2][j] - Cnt[i][j+S-2] + Cnt[i][j]
            if cmax<c:
                cmax = c
                imax = i; jmax = j
    G[imax][jmax] = G[imax+S-1][jmax] = G[imax][jmax+S-1] = G[imax+S-1][jmax+S-1] = '+'
    for i in range(imax+1, imax+S-1):
        G[i][jmax] = G[i][jmax+S-1] = '|'
    for j in range(jmax+1, jmax+S-1):
        G[imax][j] = G[imax+S-1][j] = '-'
    print(cmax)
    for L in G:
        print(''.join(L))

main()
