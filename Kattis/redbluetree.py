#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def find(Repr, x):
    if Repr[x] is None:
        return x
    Repr[x] = find(Repr, Repr[x])
    return Repr[x]

def union(Repr, x, y):
    x0 = find(Repr, x)
    y0 = find(Repr, y)
    if x0==y0:
        return False
    Repr[y0] = x0
    return True

def kruskal_req_blue():
    Repr = [None]*N
    C = N
    # we first use all the red
    r = 0
    while C>1 and r<len(R):
        u,v = R[r]
        if union(Repr, u, v):
            C -= 1
        r += 1
    # then identify a min. set of req. blue to connect the red trees
    b = 0
    RequiredB = []
    while C>1:
        assert b<len(B)
        u,v = B[b]
        if union(Repr, u, v):
            C -= 1
            RequiredB.append(B[b])
        b += 1
    return RequiredB

def kruskal_k_blue(RequiredB):
    Repr = [None]*N
    # we first add the required blue
    k = 0
    for u,v in RequiredB:
        assert union(Repr, u, v)
        k += 1
    # then we try to add up to K blue edges in total
    # each of these additional blue edge closes a red loop
    # in a red tree from the first kruskal pass, so that
    # it can be swapped with a red edge to preserve a proper
    # red-blue spanning tree of the original component
    b = 0
    while k<K and b<len(B):
        u,v = B[b]
        if union(Repr, u, v):
            k += 1
        b += 1
    # if we reach K blues, no need to continue, we already
    # know from the first pass that reds can finish the job
    return k==K

def k_blue_span():
    if len(B)<K:
        return False
    ReqB = kruskal_req_blue()
    if len(ReqB)>K:
        return False
    return kruskal_k_blue(ReqB)

def main():
    global N,K,B,R
    N,M,K = map(int, input().split())
    B = []
    R = []
    for _ in range(M):
        c,u,v = input().split()
        u = int(u)-1
        v = int(v)-1
        if c=='B':
            B.append((u,v))
        else:
            R.append((u,v))
    print(int(k_blue_span()))

main()
