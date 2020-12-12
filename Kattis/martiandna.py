#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N,K,R = map(int, input().split())
    DNA = list(map(int, input().split()))
    Req = {}
    for _ in range(R):
        B,Q = map(int, input().split())
        Req[B] = Q
    # O(N) 2-pointer approach
    # In the following:
    #  - Req stores the count of missing letters
    #    in the current [l,r[ interval
    #    (with possibly Req[c] < 0 if c in excess)
    #  - R counts the number of still missing letters
    #    (i.e. nb of c such that Req[c] > 0)
    r = 0
    res = N+1
    for l in range(N):
        while r<N and R>0:
            c = DNA[r]
            r += 1
            if c in Req:
                Req[c] -= 1
                if Req[c]==0:
                    R -= 1
                    if R==0:
                        res = min(res, r-l)
        c = DNA[l]
        if c in Req:
            Req[c] += 1
            if Req[c]==1:
                R += 1
        if R==0:
            res = min(res, r-l-1)
    print('impossible' if res>N else res)

main()
