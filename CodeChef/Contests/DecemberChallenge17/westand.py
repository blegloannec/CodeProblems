#!/usr/bin/env pypy

# this is a actually a scheduling problem
# the main idea is to reduce it to a flow problem
# we don't give details here (too long, needs pictures)
# see instead Peter Brucker - Scheduling Algorithms (5th edition)
#   subtask #2: section 5.1.1, p108
#   general pb: section 5.1.2, p129

import sys

def solve1(SP,D,M):
    for (S,P) in SP:
        if D<=M*P:
            return S
    return -1


# Ford-Fulkerson
def aug(graph,capacity,flow,val,u,target,visit):
    visit[u] = True
    if u==target:
        return val
    for v in graph[u]:
        cuv = capacity[u][v]
        if not visit[v] and cuv>flow[u][v]:
            res = min(val,cuv-flow[u][v])
            delta = aug(graph,capacity,flow,res,v,target,visit)
            if delta>0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta
    return 0

def ford_fulkerson(graph,capacity,s,t,flow=None):
    n = len(graph)
    if flow==None:
        flow = [[0]*n for _ in xrange(n)]
    INF = float('inf')
    while aug(graph,capacity,flow,INF,s,t,[False]*n)>0:
        pass
    return flow
##

def add_edge(u,v):
    G[u].append(v)
    #G[v].append(u)

def Job(i):
    return i+1

def Int2(i):
    return N+1+i

def solve2(S,P,DM):
    global G
    F = sum(D for (D,_) in DM)
    MD = sorted((M*P,D) for (D,M) in DM)
    if any(M<D for (M,D) in MD):
        return -1
    # building the graph
    Z = 2*N+1
    G = [[] for _ in xrange(Z+1)]
    C = [[0]*(Z+1) for _ in xrange(Z+1)]
    dT = []
    for i in xrange(N):
        M,D = MD[i]
        add_edge(0,Job(i))
        C[0][Job(i)] = D
        dT.append(M - (MD[i-1][0] if i>0 else 0))
        for j in xrange(i+1):
            add_edge(Job(i),Int2(j))
            C[Job(i)][Int2(j)] = dT[j]
        add_edge(Int2(i),Z)
    flow = None
    for k in xrange(1,K+1):
        # we update the capacities to add the k-th least expensive cook
        for i in xrange(N):
            C[Int2(i)][Z] = k*dT[i]
        flow = ford_fulkerson(G,C,0,Z,flow)
        if sum(flow[0])==F:  # solution found
            return sum(S[:k])
    return -1

def enum(n):
    i = 0
    while n:
        if n&1:
            yield i
        n >>= 1
        i += 1

def cop(T):
    return [L[:] for L in T]

def IntProc(i,j):
    return N+1+(K+1)*i+j+1

def Int(i):
    return N+1+(K+1)*i

# kinda dp to memoize flows
memo = {}
def get_flow(ss):
    if ss in memo:
        return memo[ss]
    I = list(enum(ss))  # selected cooks
    ss0 = ss^(1<<I[0])  # selection without the fastest cook
    C,flow = map(cop,get_flow(ss0))
    ds = lambda k: PS[I[k]][0] - (PS[I[k+1]][0] if k+1<len(I) else 0)
    sall = sum(PS[i][0] for i in I)
    # we update the capacities to add the fastest selected cook
    for i in xrange(N):
        dt = MD[i][0] - (MD[i-1][0] if i>0 else 0)
        i0 = N-1
        while i0>=0 and MD[i0][0]>=MD[i][0]:
            C[Job(i0)][IntProc(i,I[0])] = ds(0)*dt
            i0 -= 1
        for k in xrange(len(I)):
            C[IntProc(i,I[k])][Int(i)] = (k+1)*ds(k)*dt
        C[Int(i)][Z] = sall*dt
    flow = ford_fulkerson(G,C,0,Z,flow)
    memo[ss] = (C,flow)
    return memo[ss]

def solve3(SP,DM):
    global PS,MD,Z,G
    F = sum(D for (D,_) in DM)
    MD = sorted((M,D) for (D,M) in DM)
    PS = sorted(((P,S) for (S,P) in SP), reverse=True)
    # sorting the cooks subsets
    SS = []
    for i in xrange(1,1<<K):
        SS.append((sum(PS[j][1] for j in enum(i)),i))
    SS.sort()
    # building the graph
    Z = Int(N)
    G = [[] for _ in xrange(Z+1)]
    C = [[0]*(Z+1) for _ in xrange(Z+1)]
    for i in xrange(N):
        M,D = MD[i]
        add_edge(0,Job(i))
        C[0][Job(i)] = D
        for j in xrange(K):
            add_edge(IntProc(i,j),Int(i))
        i0 = N-1
        while i0>=0 and MD[i0][0]>=MD[i][0]:
            for j in xrange(K):
                add_edge(Job(i0),IntProc(i,j))
            i0 -= 1
        add_edge(Int(i),Z)
    memo.clear()
    memo[0] = (C,[[0]*(Z+1) for _ in xrange(Z+1)])
    # first we check if there is a solution using all cooks
    _,fmax = get_flow((1<<K)-1)
    if sum(fmax[0])<F:
        return -1
    # then we look for the least expensive solution
    for (v,ss) in SS:
        _,flow = get_flow(ss)
        if sum(flow[0])==F:  # solution found
            return v
    return -1

def main():
    global N,K
    T = int(raw_input())
    for _ in xrange(T):
        K = int(raw_input())
        SP = []
        for _ in xrange(K):
            P,S = map(int,raw_input().split())
            SP.append((S,P))
        SP.sort()
        N = int(raw_input())
        DM = [tuple(map(int,raw_input().split())) for _ in xrange(N)]
        if N==1:
            print(solve1(SP,DM[0][0],DM[0][1]))
        elif all(SP[0][1]==SP[i][1] for i in xrange(1,K)):
            print(solve2([s for (s,_) in SP],SP[0][1],DM))
        else:
            print(solve3(SP,DM))

main()
