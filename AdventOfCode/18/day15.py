#!/usr/bin/env python3

import sys
from collections import *

Power = {'G':3,'E':3}

G = [list(L.strip()) for L in sys.stdin.readlines()]
H,W = len(G),len(G[0])

# Units is global for convenience
Units0 = []
for i in range(H):
    for j in range(W):
        if G[i][j]=='G' or G[i][j]=='E':
            Units0.append((i,j,G[i][j],200))
            G[i][j] = '.'

def reset_units():
    global Units
    Units = Units0[:]
    update_units()

Cnt = defaultdict(int)
def update_units():
    global Units, UnitSqr
    Units = sorted((x,y,g,h) for x,y,g,h in Units if h>0)
    UnitSqr = {(i,j):k for k,(i,j,_,_) in enumerate(Units)}
    Cnt.clear()
    for _,_,g,_ in Units:
        Cnt[g] += 1

def move_unit(u,p):
    x,y = p
    x0,y0,g,h = Units[u]
    Units[u] = (x,y,g,h)
    del UnitSqr[x0,y0]
    UnitSqr[p] = u

def attack_unit(u,d):
    x,y,g,h = Units[u]
    h -= d
    Units[u] = x,y,g,h
    if h<=0:
        del UnitSqr[x,y]
        Cnt[g] -= 1

def free(u):
    i,j = u
    return 0<=i<H and 0<=j<W and G[i][j]=='.' and u not in UnitSqr

def neigh(u):  # /!\ order matters for "reading order"!
    i,j = u
    return [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]

def bfs(u0, Uf):
    Dist = {u0: 0}
    Pred = {u0: None}
    Q = deque([u0])
    dmin = float('inf')
    while Q:
        u = Q.popleft()
        if u in Uf:
            if Dist[u]<=dmin:
                dmin = Dist[u]
            else:
                # we stop as soon as we know that targets are too far
                break
        for v in neigh(u):
            if free(v) and v not in Dist:
                Dist[v] = Dist[u]+1
                Pred[v] = u
                Q.append(v)
    return Dist,Pred


# Part 1
def move(u):
    i,j,g,_ = Units[u]
    Targets = set()
    for x,y,e,h in Units:
        if e!=g and h>0:
            for v in neigh((x,y)):
                if (i,j)==v:  # adjacent target
                    return
                if free(v):
                    Targets.add(v)
    Dist,Pred = bfs((i,j),Targets)
    Targets = [(Dist[v],v) for v in Targets if v in Dist]
    if Targets:
        _,v = min(Targets)
        Path = []
        while v is not None:
            Path.append(v)
            v = Pred[v]
        move_unit(u,Path[-2])

def attack(u):
    i,j,g,_ = Units[u]
    Adjacent = []
    for xy in neigh((i,j)):
        if xy in UnitSqr:
            v = UnitSqr[xy]
            x,y,e,h = Units[v]
            if e!=g:
                Adjacent.append((h,x,y,v))
    if Adjacent:
        _,_,_,v = min(Adjacent)
        attack_unit(v,Power[g])

def turn():
    for u in range(len(Units)):
        if Units[u][3]>0:  # alive
            move(u)
            attack(u)
            full_turn = (u==len(Units)-1 or (Cnt['E']!=0 and Cnt['G']!=0))
            if not full_turn:
                break
    update_units()
    return full_turn

def show(t=-1):
    O = [L[:] for L in G]
    for i,j,g,h in Units:
        O[i][j] = g
        O[i].append(' %s(%d)' % (g,h))
    if t>=0:
        print('t = %d' % t)
    print('\n'.join(''.join(L) for L in O))
    print()

def run():
    reset_units()
    t = 0
    while Cnt['E']!=0 and Cnt['G']!=0:
        if turn():
            t += 1
        #show(t)
    return t*sum(h for _,_,_,h in Units)

print(run())


# Part 2
def part2():
    cntE0 = -1
    while Cnt['E']!=cntE0:
        Power['E'] += 1
        reset_units()
        cntE0 = Cnt['E']
        s = run()
    return s

print(part2())
