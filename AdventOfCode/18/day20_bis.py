#!/usr/bin/env python3

# Alternative version of Day 20, without the "same detours" assumption
# (a bit more sophisticated, but works with arbitrary RegEx)

from collections import deque

RE = input().strip()
#RE = '^ENWWW(NEEE|SSE(EE|N))$'

Dir = {'N':(-1,0),'S':(1,0),'E':(0,1),'W':(0,-1)}


# Parsing
def parse_options(RE,i):
    assert RE[i]=='('
    O,i = parse(RE,i+1)
    L = [O]
    while RE[i]=='|':
        O,i = parse(RE,i+1)
        L.append(O)
    assert RE[i]==')'
    return L,i+1

def parse(RE,i=1):
    L = []
    while RE[i] not in {')','|','$'}:
        if RE[i]=='(':
            L0,i = parse_options(RE,i)
            L.append(('|',L0))
        else:
            i0 = i
            while RE[i] in Dir:
                i += 1
            L.append(RE[i0:i])
    return (L[0] if len(L)==1 else ('+',L)), i


# Exploration
G,S,E = set(),set(),set()

def explore(R,P):
    Q = set()
    if isinstance(R,str):
        for x,y in P:
            for c in R:
                G.add((x,y))
                dx,dy = Dir[c]
                if c=='S':
                    S.add((x,y))
                elif c=='N':
                    S.add((x-1,y))
                elif c=='E':
                    E.add((x,y))
                else:
                    E.add((x,y-1))
                x,y = x+dx,y+dy
            Q.add((x,y))
            G.add((x,y))
    elif R[0]=='+':
        Q = P
        for r in R[1]:
            Q = explore(r,Q)
    else:
        for r in R[1]:
            Q |= explore(r,P)
    return Q


# Printing
def show():
    X0,X1 = min(x for x,_ in G),max(x for x,_ in G)
    Y0,Y1 = min(y for _,y in G),max(y for _,y in G)
    H,W = 2*(X1-X0+1)+1,2*(Y1-Y0+1)+1
    O = [['#']*W for _ in range(H)]
    for x,y in G:
        i,j = 2*(x-X0)+1,2*(y-Y0)+1
        O[i][j] = 'X' if x==y==0 else '.'
        if (x,y) in S:
            O[i+1][j] = '-'
        if (x,y) in E:
            O[i][j+1] = '|'
    print('\n'.join(''.join(L) for L in O))


# BFS
def neigh(x,y):
    if (x,y) in S:
        yield (x+1,y)
    if (x,y) in E:
        yield (x,y+1)
    if (x-1,y) in S:
        yield (x-1,y)
    if (x,y-1) in E:
        yield (x,y-1)

def bfs():
    u0 = (0,0)
    Dist = {u0: 0}
    Q = deque([u0])
    while Q:
        u = Q.popleft()
        for v in neigh(*u):
            if v not in Dist:
                Dist[v] = Dist[u] + 1
                Q.append(v)
    return Dist


# MAIN
TRE = parse(RE)[0]
explore(TRE,{(0,0)})
#show()
Dist = bfs()
print(max(Dist[u] for u in Dist))             # Part 1
print(sum(int(Dist[u]>=1000) for u in Dist))  # Part 2
