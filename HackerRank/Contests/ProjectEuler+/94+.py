#!/usr/bin/env python

import sys

def compte(N):
    X0,H0 = 2,1
    X,H = X0,H0
    res = 0
    while 2*(2*X-1)/3+(2*X-1)/3-1<=N:
        X,H = X0*X + 3*H0*H, X0*H + H0*X
        if (2*X-1)%3==0:
            x = (2*X-1)/3
            y = x-1
            if (y*H)%2==0:
                if 2*x+y<=N:
                    res += 2*x+y
        if (2*X+1)%3==0:
            x = (2*X+1)/3
            y = x+1
            if (y*H)%2==0:
                if 2*x+y<=N:
                    res += 2*x+y
    return res

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        print compte(N)

main()
