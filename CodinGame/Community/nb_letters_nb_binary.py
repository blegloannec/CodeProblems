#!/usr/bin/env python3

import sys

# n <= 10^18 < 2^60 s'ecrit sur au plus 60 bits
# donc S(n) <= 60*4-1 = 243
# en une etape on tombe directement sur un nombre <= 243
# on remarque alors que tous ces nb aboutissent a un pt fixe
# qui est 13 ou 18

def S(u):
    res = 0
    while u>0:
        res += 4-(u&1)
        u >>= 1
    return res

def main():
    u,n = map(int,sys.stdin.readline().split())
    while n>0 and S(u)!=u:
        u = S(u)
        n -= 1
    print(u)

main()
