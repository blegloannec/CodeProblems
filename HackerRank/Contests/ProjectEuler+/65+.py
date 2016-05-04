#!/usr/bin/env python

import sys

def sumdig10(n):
    s = 0
    while n>0:
        s += n%10
        n /= 10
    return s

def main():
    N = int(sys.stdin.readline())
    f = [2]
    for i in range(N/3+1):
        f += [1,2*(i+1),1]
    # rationnels de la fraction continue
    p0,p1 = 0,1
    #q0,q1 = 1,0
    for i in range(N):
        p1,p0 = p1*f[i]+p0,p1
        #q1,q0 = q1*f[i]+q0,q1
    print sumdig10(p1)

main()
