#!/usr/bin/env python3

from fractions import gcd

def main():
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        S = input()
        C = c1 = j = 0
        for i in range(N):
            while j<N and j-i<=K:
                if S[j]=='1':
                    c1 += 1
                j += 1
            if S[i]=='1':
                c1 -= 1
                C += 1+2*c1
        D = N*N
        g = gcd(C,D)
        print('%d/%d' % (C//g,D//g))

main()
