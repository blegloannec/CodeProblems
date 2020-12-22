#!/usr/bin/env python3

import sys
from collections import *

I = [L.strip() for L in sys.stdin.readlines()]

m = I.index('')
P1 = list(map(int, I[1:m]))
P2 = list(map(int, I[m+2:]))


# Part 1
def combat(P1, P2):
    while P1 and P2:
        a = P1.popleft()
        b = P2.popleft()
        if a>b:
            P1.append(a)
            P1.append(b)
        else:
            P2.append(b)
            P2.append(a)
    return P1 if P1 else P2

score = lambda P: sum(i*P[-i] for i in range(1,len(P)+1))
print(score(combat(deque(P1), deque(P2))))


# Part 2
def rcombat(P1, P2):
    Seen = set()
    while P1 and P2:
        K = (tuple(P1),tuple(P2))
        if K in Seen:
            return (1,P1)
        Seen.add(K)
        a = P1.popleft()
        b = P2.popleft()
        if len(P1)>=a and len(P2)>=b:
            Q1 = deque(P1[i] for i in range(a))
            Q2 = deque(P2[i] for i in range(b))
            w,_ = rcombat(Q1, Q2)
        else:
            w = 1 if a>b else 2
        if w==1:
            P1.append(a)
            P1.append(b)
        else:
            P2.append(b)
            P2.append(a)
    return (1,P1) if P1 else (2,P2)

_,P = rcombat(deque(P1), deque(P2))
print(score(P))
