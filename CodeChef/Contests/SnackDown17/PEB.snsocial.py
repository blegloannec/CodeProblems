#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        n,m = map(int,input().split())
        A = [list(map(int,input().split())) for _ in range(n)]
        wmax,P = -1,[]
        for i in range(n):
            for j in range(m):
                if A[i][j]>wmax:
                    wmax = A[i][j]
                    P = [(i,j)]
                elif A[i][j]==wmax:
                    P.append((i,j))
        # simulation en O(n*m)
        t,c = 0,len(P)
        while c<n*m:
            Q = []
            for (i,j) in P:
                for di in [-1,0,1]:
                    for dj in [-1,0,1]:
                        x,y = i+di,j+dj
                        if 0<=x<n and 0<=y<m and A[x][y]!=wmax:
                            A[x][y] = wmax
                            Q.append((x,y))
            P = Q
            c += len(P)
            t += 1
        print(t)

main()
