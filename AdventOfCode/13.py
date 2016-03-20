#!/usr/bin/env python

import sys
import re

instr = re.compile('([a-zA-Z]+) would ([a-zA-Z]+) ([0-9]+) happiness units by sitting next to ([a-zA-Z]+).$')

N = 10
dist = [[0 for j in range(N)] for i in range(N)]
memo = {}

def D(S,c):
    h = (tuple(S),c)
    if h in memo:
        return memo[h]
    if len(S)==1:
        res = dist[0][c]
        memo[h] = res
        return res
    else:
        res = 0
        S.remove(c)
        for x in S:
            res = max(res,D(S,x)+dist[x][c])
        S.add(c)
        memo[h] = res
        return res

def TSP(n):
    S = set(range(1,n))
    return max([D(S,c)+dist[0][c] for c in range(1,n)])

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    cpt = 0
    nums = {}
    for l in cases:
        p = instr.match(l.strip())
        for g in [1,4]:
            if not (p.group(g) in nums):
                nums[p.group(g)] = cpt
                cpt += 1
        d = (1 if p.group(2)=='gain' else -1)*int(p.group(3))
        dist[nums[p.group(1)]][nums[p.group(4)]] = d
    for i in range(cpt-1):
        for j in range(i+1,cpt):
            dist[i][j] += dist[j][i]
            dist[j][i] = dist[i][j]
    print TSP(cpt),TSP(cpt+1)

main()
