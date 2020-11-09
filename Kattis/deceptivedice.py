#!/usr/bin/env python3

def E(n, k):
    #assert k>0
    if k==1:
        return (n+1.)/2.
    e = E(n, k-1)  # expectation of the k-1 following rolls
    # if at the current roll we get:
    #  - x ≤ ⌊e⌋, we continue (with proba. ⌊e⌋/n)
    #  - x > ⌊e⌋, we stop (exp. (⌊e⌋+1 + n)/2 with proba. (n-⌊e⌋)/n)
    d = int(e)
    return (d*e + (n-d)*(d+1.+n)/2.) / n

N,K = map(int, input().split())
print(E(N,K))
