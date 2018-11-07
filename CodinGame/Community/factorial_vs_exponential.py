#!/usr/bin/env python3

from math import log
from bisect import bisect_left

# precomputing log(N!)/N values up to log(Amax)
def precomp(Amax=10000):
    logAmax = log(Amax)
    logFact = [0,0]
    N = 1
    while N*logAmax>=logFact[N]:
        N += 1
        logFact.append(logFact[N-1]+log(N))
    for n in range(2,N+1):
        logFact[n] /= n
    return logFact

def main():
    logFact_N = precomp()
    K = int(input())
    # dicho search in the precomputed values for the solution
    print(*(bisect_left(logFact_N,log(float(f))) for f in input().split()))

main()
