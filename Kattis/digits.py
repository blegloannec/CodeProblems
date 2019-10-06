#!/usr/bin/env python3

from math import log10
size10 = lambda n: int(log10(n))+1  # or len(str(n))

def dig_fix(n):
    i = 1
    while n!=1:
        n = size10(n)
        i += 1
    return i

while True:
    L = input()
    if L=='END':
        break
    n = len(L)
    print(1 if L=='1' else dig_fix(n)+1)
