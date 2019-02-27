#!/usr/bin/env python3

inf = float('inf')

memo = {1: (0,None)}
def dp(n):
    if n not in memo:
        res, pred = inf, None
        for s in S:
            if s>n: break
            if n%s==0:
                res0 = 1 + dp(n//s)[0]
                if res0<=res:
                    res, pred = res0, n//s
        memo[n] = (res,pred)
    return memo[n]

if __name__ == '__main__':
    N,M = map(int,input().split())
    S = sorted(map(int,input().split()))
    l,_ = dp(N)
    if l==inf:
        print(-1)
    else:
        L = []
        while N is not None:
            L.append(N)
            _,N = memo[N]
        L.reverse()
        print(*L)
