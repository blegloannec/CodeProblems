#!/usr/bin/env python3

import sys

num = lambda c: ord(c)-ord('a')
P = 10**4+9
B = [1,29]
for _ in range(2,80):
    B.append((B[-1]*B[1])%P)

def deg(s):
    s = [num(c) for c in s]
    l = 1
    while l<len(s):
        h = 0
        H = [-1,P]
        for i in range(len(s)):
            h = (B[1]*h + s[i]) % P
            if i>=l:
                h = (h - B[l]*s[i-l]) % P
            if i>=l-1:
                H.append(h)
        H.sort()
        if any(H[i-1]<H[i]<H[i+1] for i in range(1,len(H)-1)):
            break
        l += 1
    return l-1

def main():
    for s in sys.stdin.readlines():
        print(deg(s.strip()))

main()
