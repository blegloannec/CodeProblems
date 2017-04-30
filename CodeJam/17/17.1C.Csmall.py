#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1,T+1):
        N,K = map(int,input().split())
        assert(N==K)
        U = float(input())
        P = list(map(float,input().split()))
        P.sort(reverse=True)
        res = 1.
        for i in range(len(P)):
            M = (sum(P[i:])+U)/(len(P)-i) # moyenne sur ce qui reste
            if P[i]<M:
                p0 = min(M,P[i]+U)
                U -= p0-P[i]
            else:
                p0 = P[i]
            res *= p0
        print('Case #%d: %f' % (t,res))

main()
