#!/usr/bin/env python3

def digsum(n):
    s = 0
    while n>0:
        n,c = divmod(n,10)
        s += c
    return s

# reverse river, returns the largest acceptable predecessor
def riverse(n):
    for m in range(n-1,0,-1):
        if m+digsum(m)==n:
            return m
    return 0  # no solution

r = int(input())
print('YES' if riverse(r) else 'NO')
