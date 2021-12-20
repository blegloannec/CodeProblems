#!/usr/bin/env python3

import sys


# Input
Scan = []
for L in sys.stdin.readlines():
    L = L.strip()
    if L=='':
        continue
    elif L.startswith('---'):
        Scan.append([])
    else:
        Scan[-1].append(tuple(map(int, L.split(','))))
N = len(Scan)


# Gen. all 24 orientations for each scanner
def gen_orient_scans():
    OScan = [[] for _ in range(N)]
    for i,Pts in enumerate(Scan):
        for d in range(3):
            for o in range(2):
                for r in range(4):
                    OPts = []
                    for x,y,z in Pts:
                        if d==1:
                            x,y,z = y,z,x
                        elif d==2:
                            x,y,z = z,x,y
                        if o==1:
                            x,y,z = -x,z,y
                        if r==1:
                            y,z = -z,y
                        elif r==2:
                            y,z = -y,-z
                        elif r==3:
                            y,z = z,-y
                        OPts.append((x,y,z))
                    OScan[i].append(OPts)
    return OScan

OScan = gen_orient_scans()


# Puzzle
def intersect(Dir,Pos,Q, i,j):
    assert Dir[j]<0<=Dir[i]
    # scanner i already has a fixed orientation/position
    Oi = OScan[i][Dir[i]]
    # we try each orientation for scanner j
    for o,Oj in enumerate(OScan[j]):
        # we try to find a common point to both scans by
        # identifying a pair of points from each scan
        # and recompute the oriented coordinates relatively
        # to these points
        for xi,yi,zi in Oi:
            Si = set((x-xi,y-yi,z-zi) for x,y,z in Oi)
            for xj,yj,zj in Oj:
                Sj = set((x-xj,y-yj,z-zj) for x,y,z in Oj)
                if len(Si & Sj) >= 12:                       # given threshold reached
                    Dir[j] = o                               # guessed orient. of scanner j
                    x0,y0,z0 = Pos[i]                        # known pos. of scanner i
                    Pos[j] = (x0+xi-xj, y0+yi-yj, z0+zi-zj)  # guessed pos. of scanner j
                    Q.append(j)
                    return

def traversal():
    Dir = [-1]*N
    Pos = [None]*N
    # we arbitrarily set the orient./pos. of scanner 0
    Dir[0] = 0
    Pos[0] = (0,0,0)
    Q = [0]
    print('Scanners:', end=' ', flush=True)
    while Q:
        i = Q.pop()
        print(i, end=', ', flush=True)
        for j in range(N):
            if j!=i and Dir[j]<0:
                intersect(Dir,Pos,Q, i,j)
    print('done.')
    assert None not in Pos
    return (Dir, Pos)


# Part 1
Dir, Pos = traversal()
Beacons = set()
for i in range(N):
    x0,y0,z0 = Pos[i]
    # compute the absolute positions of beacons from scan i
    Beacons.update((x+x0,y+y0,z+z0) for x,y,z, in OScan[i][Dir[i]])
print(len(Beacons))


# Part 2
dmax = 0
for i in range(N):
    for j in range(i):
        dmax = max(dmax, sum(abs(a-b) for a,b in zip(Pos[i],Pos[j])))
print(dmax)
