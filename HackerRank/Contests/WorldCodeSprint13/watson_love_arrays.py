#!/usr/bin/env python3

from collections import defaultdict

def inv(x):
    return pow(x,M-2,M)

def main():
    global M
    T = int(input())
    for _ in range(T):
        N,M,K = map(int,input().split())
        A = list(map(int,input().split()))
        for i in range(N):
            A[i] %= M
        res = 0
        if K==0:
            z = None
            for i in range(N):
                if A[i]==0:
                    z = i
                if z!=None:
                    res += z+1
        else:
            P = 1
            D = defaultdict(int)
            D[1] = 1
            for i in range(N):
                if A[i]==0:  # reset
                    P = 1
                    D.clear()
                    D[1] = 1
                else:
                    P = (P*A[i])%M
                    Q = inv((K*inv(P))%M)
                    res += D[Q]
                    D[P] += 1
        print(res)

main()
