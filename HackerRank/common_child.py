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
    return T[m][n]

def main():
    A = input()
    B = input()
    print(LCS(A,B))

main()
