#!/usr/bin/env python3

G = [' *** ',
     ' * * ',
     ' * * ',
     '*****']

n = int(input())
h = 1
while n>=h:
    n -= h
    h += 1
h -= 1

for i in range(h):
    B = ' '*(3*(h-1-i))
    for L in G:
        print(B+' '.join(L for _ in range(i+1))+B)
