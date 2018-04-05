#!/usr/bin/env python3

from math import *

l2 = log(2.)
lpi = log(pi)

LF = [0.]*2
for i in range(2,10**5+1):
    LF.append(LF[-1] + log(i))

def log_stirling(n):
    ln = log(n)
    return (l2+lpi+ln)/2. + n*(ln-1.)

def main():
    while True:
        n = int(input())
        if n==0:
            break
        print(exp(LF[n]-log_stirling(n)))

main()
