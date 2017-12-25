#!/usr/bin/env python3

# yet another Turing machine...

import sys

def parse_input():
    L = [l[:-2].split() for l in sys.stdin.readlines()]
    T = {}
    q0 = L[0][-1]
    t = int(L[1][-2])
    for i in range(3,len(L),10):
        q = L[i][-1]
        for j in [i+1,i+5]:
            a = int(L[j][-1])
            b = int(L[j+1][-1])
            d = 1 if L[j+2][-1]=='right' else -1
            r = L[j+3][-1]
            T[q,a] = (b,d,r)
    return T,q0,t

def simu(T,q,n):
    O = set()  # Ones
    p = 0
    for _ in range(n):
        a = int(p in O)
        b,d,q = T[q,a]
        if b!=a:
            if a:
                O.remove(p)
            else:
                O.add(p)
        p += d
    return len(O)

print(simu(*parse_input()))
