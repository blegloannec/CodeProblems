#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    while True:
        N = int(input())
        if N==0:
            break
        res = 0
        # k (a + a+k-1) / 2 = N
        N *= 2
        k = 1
        while k*k<=N:
            if N%k==0:
                a = N//k-k+1
                if a%2==0:
                    a //= 2
                    if a>=2:
                        res += 1
                    else:
                        break
            k += 1
        sys.stdout.write(f'{res}\n')

main()
