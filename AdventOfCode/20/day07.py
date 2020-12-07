#!/usr/bin/env python3

import sys, re
from functools import lru_cache

I = [L.strip() for L in sys.stdin.readlines()]


# Parsing the input (by far the hardest part...)
# The input graph is a DAG
G = {}
for L in I:
    L,R = L.split(' bags contain ')
    G[L] = [(c, int(k)) for k,c in re.findall(r'(\d+) (.+?) bag', R)]

U0 = 'shiny gold'


# Part 1
@lru_cache(maxsize=None)
def dag_dfs1(u):
    return u==U0 or any(dag_dfs1(v) for v,_ in G[u])

print(sum(dag_dfs1(u) for u in G) - 1)


# Part 2
@lru_cache(maxsize=None)
def dag_dfs2(u):
    return 1 + sum(k*dag_dfs2(v) for v,k in G[u])

print(dag_dfs2(U0) - 1)
