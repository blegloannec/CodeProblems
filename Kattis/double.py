#!/usr/bin/env python3

import sys
input = sys.stdin.readline
from math import gcd

lcm = lambda a,b: a*b//gcd(a,b)

def permutation_period(P):
    per = 1
    Seen = [False]*len(P)
    for i in range(len(P)):
        if not Seen[i]:
            c = 0
            while not Seen[i]:
                Seen[i] = True
                c += 1
                i = P[i]
            per = lcm(per,c)
    return per

def main():
    N,K = map(int, input().split())
    if N==K==0:
        return False
    P = []
    for k in range(K):
        P.extend(reversed(range(k,N,K)))
    per = permutation_period(P)
    sys.stdout.write(f'{per}\n')
    return True

while main():
    pass
