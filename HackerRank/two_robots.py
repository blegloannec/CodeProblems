#!/usr/bin/env pypy

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N,Q = map(int,raw_input().split())
        for q in xrange(Q):
            a,b = map(int,raw_input().split())
            a -= 1
            b -= 1
            d = abs(b-a)
            if q==0:
                DP = [d]*N
            else:
                DP, DP0 = [float('inf')]*N, DP
                for p2 in xrange(N):
                    DP[p1] = min(DP[p1], DP0[p2]+abs(a-p2)+d)
                    DP[p2] = min(DP[p2], DP0[p2]+abs(a-p1)+d)
            p1 = b
        print(min(DP))

main()
