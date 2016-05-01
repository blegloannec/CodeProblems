#!/usr/bin/env python

import sys
from collections import deque

def dist(n,conf):
    j = 0
    while j<len(conf[0]) and conf[0][j]==n-1-j:
        j += 1
    return j

def sgn(conf):
    return tuple(map(tuple,conf))

def hh(t):
    return t[-1] if t!=[] else None

def tri(conf):
    if hh(conf[1])<hh(conf[2]):
        conf[1],conf[2] = conf[2],conf[1]
    if hh(conf[1])<hh(conf[3]):
        conf[1],conf[3] = conf[3],conf[1]
    if hh(conf[2])<hh(conf[3]):
        conf[2],conf[3] = conf[3],conf[2]

def bfs(n,iconf):
    Q = deque()
    V = set()
    Q.append((iconf,0,dist(n,iconf)))
    while len(Q)>0:
        conf,d,vd = Q.popleft()
        if vd==n:
            return d
        i0 = 0
        if vd==len(conf[0]):
            i0 = 1
        for i in xrange(i0,4):
            if conf[i]==[]:
                continue
            for j in xrange(4):
                if j==i or (conf[j]!=[] and conf[i][-1]>conf[j][-1]):
                    continue
                nconf = [conf[k][:] for k in xrange(4)]
                nconf[j].append(nconf[i].pop())
                tri(nconf)
                sig = sgn(nconf)
                if j==0 and nconf[j][-1]==n-vd-1:
                    i = 4
                    if sig not in V:
                        V.add(sig)
                        Q.append((nconf,d+1,vd+1))
                    break
                if sig not in V:
                    V.add(sig)
                    Q.append((nconf,d+1,vd))

def main():
    global D
    N = int(sys.stdin.readline())
    D = map((lambda x: int(x)-1),sys.stdin.readline().split())
    conf = [[],[],[],[]]
    for i in xrange(N-1,-1,-1):
        conf[D[i]].append(i)
    print bfs(N,conf)

main()
