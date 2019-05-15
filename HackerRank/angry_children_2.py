#!/usr/bin/env python3

# the optimal K packets must be consecutive in the sorted A

if __name__=='__main__':
    N = int(input())
    K = int(input())
    A = sorted(int(input()) for _ in range(N))
    S = A[:]
    for i in range(1,N):
        S[i] += S[i-1]
    # init. window [0,K-1]
    curr = 0
    for i in range(1,K):
        curr += i*A[i] - S[i-1]
    best = curr
    # iterating over windows of size K
    for i in range(K,N):
        # moving from window [i-K,i-1] to [i-K+1,i]
        curr -= S[i-1]-S[i-K] - (K-1)*A[i-K]  # removing A[i-K]
        curr += (K-1)*A[i] - (S[i-1]-S[i-K])  # adding   A[i]
        best = min(best,curr)
    print(best)
