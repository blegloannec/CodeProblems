#!/usr/bin/env python3

import sys
from fractions import Fraction
input = sys.stdin.readline

def Tbounds(F):
    if not Fmin <= F <= Fmax:
        return (-1,-1)
    # incr. temp. pass for min temp.
    f = F - Fmin
    X = [a for _,a,_ in Tap]
    i = 0
    while f>0:
        _,a,b = Tap[i]
        df = min(f, b-a)
        X[i] += df
        f -= df
        i += 1
    tmin_num = sum(x*t for x,(t,_,_) in zip(X,Tap))
    # decr. temp. pass for max temp.
    f = F - Fmin
    X = [a for _,a,_ in Tap]
    i = len(Tap)-1
    while f>0:
        _,a,b = Tap[i]
        df = min(f, b-a)
        X[i] += df
        f -= df
        i -= 1
    tmax_num = sum(x*t for x,(t,_,_) in zip(X,Tap))
    return (tmin_num, tmax_num)

def main():
    global Tap, Fmin, Fmax
    K = int(input())
    Tap = sorted(tuple(map(int, input().split())) for _ in range(K))
    Fmin = sum(a for _,a,_ in Tap)
    Fmax = sum(b for _,_,b in Tap)
    R = int(input())
    for _ in range(R):
        t,f = map(int, input().split())
        ftmin,ftmax = Tbounds(f)
        sys.stdout.write('yes\n' if ftmin<=f*t<=ftmax else 'no\n')

main()
