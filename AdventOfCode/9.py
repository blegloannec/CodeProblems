#!/usr/bin/env python

import sys
import re

instr = re.compile('([a-zA-Z]+) to ([a-zA-Z]+) = ([0-9]+)$')

N = 10
dist = [[-1 for j in range(N)] for i in range(N)]
memo = {}

def D(S,s,c):
    h = (tuple(S),s,c)
    if h in memo:
        return memo[h]
    if len(S)==1:
        res = dist[s][c]
        memo[h] = res
        return res
    else:
        #res = 100000000
        res = -1
        S.remove(c)
        for x in S:
            #res = min(res,D(S,s,x)+dist[x][c])
            res = max(res,D(S,s,x)+dist[x][c])
        S.add(c)
        memo[h] = res
        return res

def TSP(n):
    S = set(range(n))
    #res = 100000000
    res = -1
    for s in range(n):
        S.remove(s)
        #res = min(res,min([D(S,s,c) for c in S]))
        res = max(res,max([D(S,s,c) for c in S]))
        S.add(s)
    return res

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
