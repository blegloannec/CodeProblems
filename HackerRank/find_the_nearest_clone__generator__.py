#!/usr/bin/env python3

# Proper testcases for this problem as the HR cases are extremely weak
# and the editorial is nonsense.

from collections import deque
import random, time
random.seed()

def solution(G, U0):
    N = len(G)
    Dist = [[-1]*2 for _ in range(N)]
    From = [[None]*2 for _ in range(N)]
    inU0 = [False]*N
    for u in U0:
        Dist[u][0] = 0
        From[u][0] = u
        inU0[u] = True
    Q = deque([(u,0) for u in U0])
    while Q:
        u,bis = Q.popleft()
        if inU0[u] and bis:
            return Dist[u][1]
        for v in G[u]:
            if Dist[v][0]==-1:  # first visit
                assert bis==0
                Dist[v][0] = Dist[u][bis]+1
                From[v][0] = From[u][bis]
                Q.append((v,0))
            elif Dist[v][1]==-1 and From[v][0]!=From[u][bis]:  # second visit
                Dist[v][1] = Dist[u][bis]+1
                From[v][1] = From[u][bis]
                Q.append((v,1))
    return -1

def naive(G, U0):  # bfs from each vertex of U0
    N = len(G)
    inU0 = [False]*N
    for u in U0:
        inU0[u] = True
    dmin = float('inf')
    for u0 in U0:
        Dist = [-1 for _ in range(N)]
        Dist[u0] = 0
        Q = deque([u0])
        while Q:
            u = Q.popleft()
            if u!=u0 and inU0[u]:
                dmin = min(dmin, Dist[u])
                break
            for v in G[u]:
                if Dist[v]==-1:
                    Dist[v] = Dist[u]+1
                    Q.append(v)
    return -1 if dmin==float('inf') else dmin

def test(t):
    N = 10**random.randint(2,4)
    #M = min(10**random.randint(1,4), N*(N-1)//2)
    M = N
    G = [[] for _ in range(N)]
    E = set()
    while len(E)<M:
        u = random.randint(0,N-1)
        v = random.randint(0,N-1)
        if u>v:
            u,v = v,u
        if u!=v and (u,v) not in E:
            G[u].append(v)
            G[v].append(u)
            E.add((u,v))
    U0 = random.sample(range(N), random.randint(1,N//10))
    t0 = time.time()
    res1 = solution(G,U0)
    t1 = time.time()-t0
    t0 = time.time()
    res2 = naive(G,U0)
    t2 = time.time()-t0
    print('Test #{:03d} -- {:.3f}s {:.3f}s'.format(t, t1, t2))
    print('  {:2d} ?= {:2d}  {}'.format(res1, res2, res1==res2))
    assert res1 == res2

if __name__=='__main__':
    for t in range(1000):
        test(t)
