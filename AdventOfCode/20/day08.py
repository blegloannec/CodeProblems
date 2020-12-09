#!/usr/bin/env python3

import sys
from collections import namedtuple

Conf = namedtuple('Conf', ('term', 'acc'))

def interpret(P):
    N = len(P)
    acc = p = 0
    term = True
    Seen = [False]*N
    while 0 <= p < N:
        if Seen[p]:
            term = False
            break
        Seen[p] = True
        o,a = P[p]
        if o=='acc':
            acc += a
            p += 1
        elif o=='jmp':
            p += a
        else:  # nop
            p += 1
    return Conf(term, acc)


# Input
I = [L.strip() for L in sys.stdin.readlines()]
P = []
for L in I:
    c,v = L.split()
    P.append((c, int(v)))


# Part 1
print(interpret(P).acc)


# Part 2
for i,(c,v) in enumerate(P):
    if c!='acc':
        P[i] = (('nop' if c=='jmp' else 'jmp'), v)
        res = interpret(P)
        if res.term:
            print(res.acc)
        P[i] = (c, v)
