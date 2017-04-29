#!/usr/bin/env python3

# see Project Euler 419 for a real problem...

def looknsay(s):
    t  = []
    i = 0
    while i<len(s):
        c = 1
        while i+c<len(s) and s[i+c]==s[i]:
            c += 1
        t.append(c)
        t.append(s[i])
        i += c
    return t

def main():
    R = list(map(int,input().split()))
    L = int(input())
    for _ in range(L-1):
        R = looknsay(R)
    print(' '.join(map(str,R)))

main()
