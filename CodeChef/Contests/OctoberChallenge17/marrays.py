#!/usr/bin/env python3

# the "trick" is abs(x-y) = max(x-y,y-x)
# so that everything naturally falls into a DP
# computing some global max (see below)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = []
        for _ in range(N):
            A.append(list(map(int,input().split()[1:])))
        P = M = 0
        for i in range(N):
            li = len(A[i])
            P0 = max(max(P-i*A[i][j]+((i+1)%N)*A[i][(j-1)%li],M+i*A[i][j]+((i+1)%N)*A[i][(j-1)%li]) for j in range(li))
            M0 = max(max(P-i*A[i][j]-((i+1)%N)*A[i][(j-1)%li],M+i*A[i][j]-((i+1)%N)*A[i][(j-1)%li]) for j in range(li))
            P,M = P0,M0
        print(P)  # as P = M in the end

main()
