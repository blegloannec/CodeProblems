#!/usr/bin/env python3

def LCS(u,v):
    m,n = len(u),len(v)
    T = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if u[i-1]==v[j-1]:
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = max(T[i-1][j],T[i][j-1])
    # construction de la solution par remontee
    sol = []
    i,j = m,n
    while i>0 and j>0:
        if u[i-1]==v[j-1]:
            sol.append(u[i-1])
            i -= 1
            j -= 1
        elif T[i][j]==T[i-1][j]:
            i -= 1
        else:
            j -= 1
    return sol[::-1]

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print(' '.join(map(str,LCS(A,B))))

main()
