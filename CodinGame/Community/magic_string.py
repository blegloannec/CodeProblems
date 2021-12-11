#!/usr/bin/env python3

n = int(input())
l,r = sorted(input() for _ in range(n))[n//2-1:n//2+1]

magic = []
for a,b in zip(l,r):
    if a==b:
        magic.append(a)
    else:
        magic.append(chr(ord(a)+1))
        break
magic = ''.join(magic)

if len(magic)==len(l) or magic==r:
    magic = l
print(magic)
