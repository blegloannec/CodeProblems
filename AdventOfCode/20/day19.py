#!/usr/bin/env python3

import sys, re
from functools import lru_cache

I = [L.strip() for L in sys.stdin.readlines()]

Rule = {}
i = 0
while I[i]:
    n,R = I[i].split(': ')
    R = R.strip()
    n = int(n)
    if R[0]=='"':
        Rule[n] = R[1:-1]
    else:
        Rule[n] = tuple(tuple(map(int, C.split())) for C in R.split('|'))
    i += 1
I = I[i+1:]


# Part 1 - Building a regex
@lru_cache(maxsize=None)
def rule_re(r=0):
    if isinstance(Rule[r], str):
        return Rule[r]
    else:
        return '('+'|'.join(''.join(rule_re(j) for j in C) for C in Rule[r])+')'

re0 = re.compile(rule_re()+'$')
part1 = 0
for w in I:
    if re0.match(w):
        part1 += 1
print(part1)


# Part 2 - Ad-hoc matching backtracking
Rule[8] = ((42,), (42, 8))
Rule[11] = ((42, 31), (42, 11, 31))

def match_chain(S, i, C, j=0):
    if j==len(C):
        yield i
    else:
        for l in match_rule(S, i, C[j]):
            yield from match_chain(S, l, C, j+1)

def match_rule(S, i=0, r=0):
    if i<len(S):
        if isinstance(Rule[r], str):
            if S[i]==Rule[r]:
                yield i+1
        else:
            for C in Rule[r]:
                yield from match_chain(S, i, C)

part2 = sum(len(w) in match_rule(w) for w in I)
print(part2)
