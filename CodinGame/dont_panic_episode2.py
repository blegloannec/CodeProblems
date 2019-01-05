#!/usr/bin/env python3

from heapq import *

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: number of additional elevators that you can build
# nb_elevators: number of elevators
H,W,_,fi,fj,_,e,nbe = map(int,input().split())
E = set(tuple(map(int,input().split())) for _ in range(nbe))

def dijkstra(i0,j0,d0,e0):
    u0 = (i0,j0,d0,e0)
    Dist = {u0: 0}
    Pred = {u0: (None,[])}
    Q = [(0,u0)]
    while Q:
        du,u = heappop(Q)
        i,j,d,e = u
        if (i,j)==(fi,fj):
            break
        if Dist[u]<du:
            continue
        if (i,j) in E:
            V = [((i+1,j,d,e),1,['WAIT'])]
        else:
            V = [((i,j-d,-d,e),4,['BLOCK','WAIT','WAIT','WAIT'])]
            if 0<=j+d<W:
                V.append(((i,j+d,d,e),1,['WAIT']))
            if e>0 and i<H-1:
                V.append(((i+1,j,d,e-1),4,['ELEVATOR','WAIT','WAIT','WAIT']))
        for v,w,l in V:
            if v not in Dist or Dist[v]>Dist[u]+w:
                Dist[v] = Dist[u]+w
                Pred[v] = u,l
                heappush(Q,(Dist[v],v))
    L = []
    while u is not None:
        u,l = Pred[u]
        L.extend(l[::-1])
    L.reverse()
    return L

# game loop
k = 0
while True:
    i,j,d = input().split()
    i = int(i)
    j = int(j)
    if k==0:
        L = dijkstra(i,j,(1 if d=='RIGHT' else -1),e)
    print(L[k] if k<len(L) else 'WAIT')
    k += 1
