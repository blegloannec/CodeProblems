#!/usr/bin/env python

import sys,re

instr = re.compile('([a-zA-Z]+) to ([a-zA-Z]+) = ([0-9]+)$')

N = 10
dist = [[-1 for _ in xrange(N)] for _ in xrange(N)]
memo = {}

# Held–Karp algorithm for the TSP
# ideally would use a bitmask for the sets, yet good enough
def D(S,c):
    h = (tuple(sorted(S)),c)
    if h in memo:
        return memo[h]
    if len(S)==1: # S = {c}
        res1,res2 = 0,0
    else:
        S.remove(c)
        # iterate over list(S) as S is modified during iterations
        res1 = min(D(S,x)[0]+dist[x][c] for x in list(S))
        res2 = max(D(S,x)[1]+dist[x][c] for x in list(S))
        S.add(c)
    memo[h] = (res1,res2)
    return res1,res2

def TSP(n):
    S = set(range(n))
    res1 = min(D(S,c)[0] for c in xrange(n))
    res2 = max(D(S,c)[1] for c in xrange(n))
    return res1,res2

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    cpt = 0
    nums = {}
    for l in cases:
        p = instr.match(l.strip())
        for g in [1,2]:
            if not (p.group(g) in nums):
                nums[p.group(g)] = cpt
                cpt += 1
        d = int(p.group(3))
        dist[nums[p.group(1)]][nums[p.group(2)]] = d
        dist[nums[p.group(2)]][nums[p.group(1)]] = d
    print TSP(cpt)

main()
