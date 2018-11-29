#!/usr/bin/env python3

S = 4  # size
# ord is (0,0), vault is (S-1,S-1)
# north is down
G = [[ 22,'-',  9,'*'],
     ['+',  4,'-', 18],
     [  4,'*', 11,'*'],
     ['*',  8,'-',  1]]
W = 30  # target value

# Notes:
#  - going back to the first room resets the orb
#  - going to the end without the right value resets the orb
#  - the expression is evaluated progressively along the path
#    (not globally at the end)
#  - other than that you can reuse rooms/operators/numbers as you please
#  - as there is an hourglass, you (probably) have to find the shortest path

from collections import deque
from operator import add,sub,mul
Opp = {'+':add, '-':sub, '*':mul}

def bfs():
    U0 = 0,0,G[0][0]
    Pred = {U0: None}
    Q = deque([U0])
    while Q:
        U = Q.popleft()
        i,j,w = U
        if i==j==S-1 and w==W:
            break
        for vi,vj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=vi<S and 0<=vj<S and not vi==vj==0:  # avoid the start
                vw = Opp[G[i][j]](w,G[vi][vj]) if (vi+vj)%2==0 else w
                if vi==vj==S-1 and vw!=W:
                    # avoid the end without the target value
                    continue
                V = vi,vj,vw
                if V not in Pred:
                    Pred[V] = U
                    Q.append(V)
    Path = []
    while Pred[U] is not None:
        U,V = Pred[U],U
        Path.append('north' if U[0]<V[0] else 'south' if U[0]>V[0] else 'east' if U[1]<V[1] else 'west')
    Path.reverse()
    return Path

print('\n'.join(bfs()))
