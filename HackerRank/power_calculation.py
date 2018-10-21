#!/usr/bin/env python3

M = 100

# sum(i^N, i=1..K) mod M
def somme(K,N):
    S = [0]*(M+1)
    for i in range(1,M+1):
        S[i] = (S[i-1] + pow(i,N,M)) % M
        # NB: as mentionned in the editorial, the pow calculations above
        #     could be optimized by pre-computation taking into account
        #     the multiplicative order (or even better exponent) mod M
        #     (phi(100) = 40 or even better lambda(100) = 20)
    q,r = divmod(K,M)
    res = (S[M]*q + S[r]) % M
    return res

def main():
    T = int(input())
    for _ in range(T):
        K,N = map(int,input().split())
        print('%02d' % somme(K,N))

main()
