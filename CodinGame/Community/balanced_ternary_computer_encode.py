#!/usr/bin/env python3

D = 'T01'
def dec2tern(n):
    T = []
    while n:
        n,r = divmod(n+1,3)
        T.append(D[r])
    res = ''.join(reversed(T))
    return res if res else '0'

print(dec2tern(int(input())))
