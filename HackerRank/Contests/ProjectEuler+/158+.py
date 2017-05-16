#!/usr/bin/env python3

# Eulerian numbers
# http://oeis.org/A008292
# see also PE pb 602
# a(n,i) = (i+1)*a(n-1,i) + (n-i)*a(n-1,i-1)

def main():
    N,q = map(int,input().split())
    M = list(map(int,input().split()))
    B = [[int(k==0) for k in range(N+1)] for _ in range(N+1)]
    P = [[int(k==0) for k in range(N+1)] for _ in range(N+1)]
    for n in range(1,N+1):
        for i in range(1,n+1):
            # coefficients binomiaux
            B[n][i] = B[n-1][i-1] + B[n-1][i]
            # nombres euleriens
            P[n][i] = (i+1)*P[n-1][i] + (n-i)*P[n-1][i-1]
    res = sum(max(B[N][n]*P[n][m] for n in range(1,N+1)) for m in M)
    print(res)

main()
