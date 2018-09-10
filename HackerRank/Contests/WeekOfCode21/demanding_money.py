#!/usr/bin/env python

# number of maximal independent sets of maximum weight
# (i.e. the sum of the weights of all vertices)
# and the corresponding weight


###  For the record, generators from the previous implementation  ###
###  (not used here)                                              ###
###  Ne[u] the neighborhood of u (included) as a python *set*     ###
###  R[u] the order of the vertices (lowest first, for instance   ###
###  R[u] = u if we do not care,                                  ###
###  R[u] = -len(Ne[u]) for a generally good heuristics)          ###
# MIS generator  (Maximal for inclusion)
def backtrack(I,V,S=0):
    if len(V)==0:
        yield (I,S)
    for v in V:
        if len(I)==0 or R[v]>R[I[-1]]:
            I.append(v)
            for i in backtrack(I,V-Ne[v],S+C[v]):
                yield i
            I.pop()

# IS generator
def backtrack2(I,V):
    yield I
    for v in V:
        if len(I)==0 or R[v]>R[I[-1]]:
            I.append(v)
            for i in backtrack2(I,V-Ne[v]):
                yield i
            I.pop()
###  =========================================================  ###


# mask-based IS generator
def IS(u,umax,I=0,W=0):
    if u>umax:
        yield (I,W)
    else:
        for X in IS(u+1,umax,I,W):
            yield X
        if Ne[u]&I==0:
            for X in IS(u+1,umax,I|(1<<u),W+C[u]):
                yield X

# for I1 the mask -> weight dict of the independent sets in the first half
# dp_max_count(M,b) = (max weight of an independent set which mask coincide
#                      with M on bits >b, and is a submask of M on bits <=b
#                      , nb of such sets)
memo = {}
def dp_max_count(mask,b):
    if mask==0:
        return (0,1)
    if b<0:
        return (I1[mask],1) if mask in I1 else (-1,0)
    if (mask,b) in memo:
        return memo[mask,b]
    w,c = dp_max_count(mask,b-1)
    if (mask>>b)&1:
        w0,c0 = dp_max_count(mask^(1<<b),b-1)
        if w0>w:
            w,c = w0,c0
        elif w0==w:
            c += c0
    memo[mask,b] = w,c
    return (w,c)

def main():
    global N,C,Ne,I1
    N,M = map(int,raw_input().split())
    C = map(int,raw_input().split())
    # neighborhood masks
    Ne = [1<<i for i in xrange(N)]
    for _ in xrange(M):
        A,B = map(int,raw_input().split())
        A -= 1
        B -= 1
        Ne[A] |= 1<<B
        Ne[B] |= 1<<A
    # meet in the middle
    # we generate the independent sets in the first half
    K = N/2
    I1 = {}
    for mask1,w1 in IS(0,K-1):
        I1[mask1] = w1
    # we go through the independent sets in the second half
    w = c = 0
    for mask2,w2 in IS(K,N-1):
        # compatible first-half mask
        comp_mask1 = (1<<K)-1
        v = K
        m = mask2>>K
        while m:
            if m&1:
                comp_mask1 &= ~Ne[v]
            m >>= 1
            v += 1
        # we get the weight and number of compatible first-half
        # independent sets of max weight
        w1,c1 = dp_max_count(comp_mask1,K-1)
        # we combine both halves
        if w1+w2>w:
            w = w1+w2
            c = c1
        elif w1+w2==w:
            c += c1
    print w,c

main()
