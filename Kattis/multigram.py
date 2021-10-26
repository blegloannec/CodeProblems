#!/usr/bin/env python3

import sys

P = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
MOD = 2245507992822379

def inv(n):
    return pow(n, MOD-2, MOD)

Hash = [1]
def subhash(l,r):
    return (Hash[r]*inv(Hash[l])) % MOD

def main():
    S = sys.stdin.readline().strip()
    N = len(S)
    orda = ord('a')
    # hash of prefixes
    for c in S:
        Hash.append((Hash[-1]*P[ord(c)-orda]) % MOD)
    # looking for solution
    for d in range(1,N):
        if N%d==0:
            h = subhash(0,d)
            if all(h==subhash(i,i+d) for i in range(d, len(S), d)):
                print(S[:d])
                return
    print('-1')

main()
