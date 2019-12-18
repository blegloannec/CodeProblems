#!/usr/bin/env python3

# purely technical but not hard

P = 10**9+7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    S = 1  # size
    X = 0  # diameter
    D = 0  # sum of all distances
    F = 0  # sum of distances to a foot
    for n in range(N):
        S1  = 4*S + 2
        X1  = 2*X + 3*A[n]
        F1  = F
        F1 +=      F + (2*A[n]+X)*S
        F1 += 2 * (F + (3*A[n]+X)*S)
        F1 += X +   A[n]
        F1 += X + 2*A[n]
        D1  = 4*D
        D1 += 4 * (2*F*S + 3*A[n]*S**2)
        D1 += 2 * (2*F*S + 2*A[n]*S**2)
        D1 += 4 * (F +   A[n]*S)
        D1 += 4 * (F + 2*A[n]*S)
        D1 += A[n]
        S, X, D, F = S1%P, X1%P, D1%P, F1%P
    print(D)

main()
