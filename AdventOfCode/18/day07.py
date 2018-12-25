#!/usr/bin/env python3

import sys
from collections import defaultdict
from heapq import *

I = [L.strip().split() for L in sys.stdin.readlines()]
I = [(L[1],L[7]) for L in I]

# building DAG
G = defaultdict(list)
for u,v in I:
    G[u].append(v)

# constants (for Part 2)
Delay = 60
Procs = 5
duration = lambda c: Delay + ord(c)-ord('A')+1


# Part 1 (+ critical path)
def lexmin_toposort(G):
    nbpred = defaultdict(int)
    for u in G:
        for v in G[u]:
            nbpred[v] += 1
    prioq = []
    for u in G:
        if nbpred[u]==0:
            heappush(prioq,u)
    # here we additionally compute done[u] = min time to complete task u
    # assuming we have enough procs to lauch every task as soon
    # as possible (when all preds are done)
    done = {}
    for u in prioq:
        done[u] = duration(u)
    toposort = []
    while prioq!=[]:
        u = heappop(prioq)
        toposort.append(u)
        for v in G[u]:
            nbpred[v] -= 1
            if v in done:
                done[v] = max(done[v],done[u]+duration(v))
            else:
                done[v] = done[u]+duration(v)
            if nbpred[v]==0:
                heappush(prioq,v)
    critical_path = max(done[u] for u in done)
    return ''.join(toposort), critical_path

print('%s  (critical path = %d)' % lexmin_toposort(G))


# Part 2 (lex-min order)
# This is, in the most general case, a "P | prec; pi qcq | Cmax" scheduling
# problem, which is NP-hard.
# NB: The critical path computed in Part 1 is a lower-bound in general,
#     but was actually the optimal in my input file.
# However the statement mentions that steps are completed in the lex-min
# order (computed in Part 1): "If multiple steps are available, workers should
# still begin them in alphabetical order."
# Hence we are simply asked to compute the schedule using a shortest-first
# greedy choice (as duration = letter + constant here).

def shortest_first_scheduling(G,NbProcs):
    nbpred = defaultdict(int)
    for u in G:
        for v in G[u]:
            nbpred[v] += 1
    Tasks = []
    for u in G:
        if nbpred[u]==0:
            heappush(Tasks,(duration(u),u))
    Procs = [(0,None)]
    while Procs:
        t,u = heappop(Procs)
        if u is not None:
            for v in G[u]:
                nbpred[v] -= 1
                if nbpred[v]==0:
                    heappush(Tasks,(duration(v),v))
        while Tasks and len(Procs)<NbProcs:
            d,u = heappop(Tasks)
            heappush(Procs,(t+d,u))
    return t

print(shortest_first_scheduling(G,Procs))
