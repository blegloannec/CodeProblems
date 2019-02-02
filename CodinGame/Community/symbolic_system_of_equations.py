#!/usr/bin/env python3

N = int(input())
Vars = input().split()
M = int(input())
Eqs = [input().split() for _ in range(M)]

Eqs = {E[0]:(E[2],E[4:-1]) for E in Eqs}
Pred = {v:0 for v in Vars}
Succ = {v:set() for v in Vars}
for v in Eqs:
    Pred[v] = len(Eqs[v][1])
    for vr in Eqs[v][1]:
        Succ[vr].add(v)

Q = [v for v in Vars if Pred[v]==0]
Sol = {}
while Q:
    v = Q.pop()
    if v in Eqs:
        Sol[v] = '%s ( %s )' % (Eqs[v][0],' '.join(Sol[vr] for vr in Eqs[v][1]))
    else:
        Sol[v] = '%s' % v
    for vs in Succ[v]:
        Pred[vs] -= 1
        if Pred[vs]==0:
            Q.append(vs)

if len(Sol)<N:
    print('No solution!')
else:
    for v in sorted(Vars):
        print('%s -> %s' % (v,Sol[v]))
