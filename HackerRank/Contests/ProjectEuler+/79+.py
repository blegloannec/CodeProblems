#!/usr/bin/env python

import sys
from heapq import *

N = 126-33+1
M = [[False for _ in range(N)] for _ in range(N)]
ens = set()

#toposort = []
# DFS based algo (Tarjan) won't work for lex-min solution
#visited = [False for _ in range(N)]
#visiting = [False for _ in range(N)]
#def dfs(u):
#    visiting[u] = True
#    for v in xrange(N):
#        if M[u][v] and not visited[v]:
#            if visiting[v]:
#                print 'SMTH WRONG'
#                sys.exit(0)
#            dfs(v)
#    visited[u] = True
#    toposort.append(u)

nbpred = [0 for _ in range(N)]
prioq = []
def greedylex():
    toposort = []
    while prioq!=[]:
        u = heappop(prioq)
        toposort.append(u)
        for v in ens:
            if M[u][v]:
                nbpred[v] -= 1
                if nbpred[v]==0:
                    heappush(prioq,v)
    return toposort
            

def c2i(c):
    return ord(c)-33

def i2c(c):
    return chr(c+33)
    
def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        x,y,z = map(c2i,sys.stdin.readline().strip())
        ens.add(x)
        ens.add(y)
        ens.add(z)
        M[x][y] = True
        M[y][z] = True
    for u in ens:
        for v in ens:
            if M[v][u]:
                nbpred[u] += 1
        if nbpred[u]==0:
            heappush(prioq,u)
    toposort = greedylex()
    if len(toposort)==len(ens):
        print ''.join(map(i2c,toposort))
    else:
        print 'SMTH WRONG'

main()
