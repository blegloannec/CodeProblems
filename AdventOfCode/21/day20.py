#!/usr/bin/env python3

import sys


# Input
Rule = []
L = sys.stdin.readline().strip()
while L!='':
    Rule.extend(c=='#' for c in L)
    L = sys.stdin.readline().strip()
assert len(Rule)==1<<9
assert Rule[0]!=Rule[-1]
FLIP = Rule[0]  # the rule flips the background state

S0 = set()
for i,L in enumerate(sys.stdin.readlines()):
    for j,c in enumerate(L.strip()):
        if c=='#':
            S0.add((i,j))
S0 = (S0, 0)


# Cellular Automaton step
#  s0 the default state
#  S0 the set of non-s0-valued cells
def step(S0, s0=0):
    s1 = 1^s0
    S = set()  # new state
    V = set()  # neighborhood of S0 without S0
    for i,j in S0:
        r = 0
        for vi in range(i-1,i+2):
            for vj in range(j-1,j+2):
                r <<= 1
                if (vi,vj) in S0:
                    r |= s1
                else:
                    r |= s0
                    V.add((vi,vj))
        if FLIP^s0^Rule[r]:
            S.add((i,j))
    for i,j in V:
        r = 0
        for vi in range(i-1,i+2):
            for vj in range(j-1,j+2):
                r <<= 1
                if (vi,vj) in S0:
                    r |= s1
                else:
                    r |= s0
        if FLIP^s0^Rule[r]:
            S.add((i,j))
    return (S, FLIP^s0)

def steps(S, n):
    for _ in range(n):
        S = step(*S)
    return S


print(len(steps(S0, 2)[0]))  # Part 1
print(len(steps(S0,50)[0]))  # Part 2
