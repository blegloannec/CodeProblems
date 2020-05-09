#!/usr/bin/env python3

from math import *

inside = lambda l,r,a: l<=a<=r or l<=a-tau<=r

def main():
    T = int(input())
    for _ in range(T):
        N,D = map(int,input().split())
        I = []
        for _ in range(N):
            x,y = map(int,input().split())
            da = asin(D/hypot(x,y))
            l = atan2(y,x) - da
            r = l + 2*da
            I.append((l,r))
        I.sort()
        res = N
        for i0 in range(N):
            a = I[i0][1]
            cnt = 1
            for i in range(1,N):
                l,r = I[(i0+i)%N]
                if not inside(l,r,a):
                    a = r
                    cnt += 1
            res = min(res, cnt)
        print(res)

main()
