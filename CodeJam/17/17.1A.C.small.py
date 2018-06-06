#!/usr/bin/env python3

from collections import deque

# naive BFS here, runs in ~10s with python3 on the small case
# we could have used the following basic observations to
# speed up the process:
#  - it is optimal to do all debuffs *before* all attacks (hence stop
#    debuffing once an attack has been done)
#  - we should only heal when we are about to die, then if we have to heal
#    twice in a row, the knight deals more damage that half of our HP and
#    it is not possible to win anymore (the only potential solution would
#    be a debuff at the very first turn)

def bfs(Hd0,Ad0,Hk0,Ak0,B,D):
    S0 = (Hd0,Ad0,Hk0,Ak0)
    dist = {S0:0}
    Q = deque([S0])
    while Q:
        S = Q.popleft()
        Hd,Ad,Hk,Ak = S
        if Hk-Ad<=0:
            return dist[S]+1
        for T in [(Hd-Ak,Ad,Hk-Ad,Ak),(Hd-Ak,Ad+B,Hk,Ak),(Hd0-Ak,Ad,Hk,Ak),(Hd-max(0,Ak-D),Ad,Hk,max(0,Ak-D))]:
            if T[0]>0 and T not in dist:
                dist[T] = dist[S]+1
                Q.append(T)
    return None

def main():
    T = int(input())
    for t in range(1,T+1):
        Hd,Ad,Hk,Ak,B,D = map(int,input().split())
        d = bfs(Hd,Ad,Hk,Ak,B,D)
        print('Case #%d: %s' % (t,'IMPOSSIBLE' if d==None else str(d)))

main()
