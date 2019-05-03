#!/usr/bin/env pypy2

# O(n log N) 2 passes prev/next greater element + dicho search approach
#                    i                              max C[i..] > Ci
# C --[--------------|-----------------------------]--------------
# D -----[-----]-----|--------[-------------------------]---------
#                              max D[i..] >= Ci-K        max D[i..] > Ci+K
# To index i, we associate the intervals [l,r] for which
# l <= i <= r  and  Ci is *the first* max of C[l..r]
# (represented by the bounds on C on the figure)
# Within these intervals, the intervals we are looking for are easily
# described by the 4 bounds on D on the figure.
# The 3 left bounds are computed on a first pass from left to right.
# The 3 right bounds are computed on a second pass from right to left.
# NB: The official analysis recommends the use of a Range Max Query structure
#     (typically sparce tables in O(1) here) for a single pass simpler approach.

def dicho(A, S, v, default):
    l,r = 0,len(S)-1
    while l<r:
        m = (l+r+1)//2
        if A[S[m]]>=v:
            l = m
        else:
            r = m-1
    return S[l] if A[S[l]]>=v else default

if __name__=='__main__':
    T = int(raw_input())
    for t in xrange(1,T+1):
        N,K = map(int,raw_input().split())
        C = map(int,raw_input().split())
        D = map(int,raw_input().split())
        # --> pass
        SC = []
        SD = []
        LeftLowerBound = [None]*N  # excluded
        LeftUpperBound = [None]*N  # included
        for i in xrange(N):
            while SC and C[SC[-1]]<C[i]:
                SC.pop()
            LeftLowerBound[i] = SC[-1] if SC else -1
            SC.append(i)
            while SD and D[SD[-1]]<=D[i]:
                SD.pop()
            SD.append(i)
            LeftLowerBound[i] = max(LeftLowerBound[i], dicho(D,SD,C[i]+K+1,-1))
            LeftUpperBound[i] = max(LeftLowerBound[i], dicho(D,SD,C[i]-K,-1))
        # <-- pass
        SC = []
        SD = []
        RightLowerBound = [None]*N  # included
        RightUpperBound = [None]*N  # excluded
        for i in xrange(N-1,-1,-1):
            while SC and C[SC[-1]]<=C[i]:
                SC.pop()
            RightUpperBound[i] = SC[-1] if SC else N
            SC.append(i)
            while SD and D[SD[-1]]<=D[i]:
                SD.pop()
            SD.append(i)
            RightUpperBound[i] = min(RightUpperBound[i], dicho(D,SD,C[i]+K+1,N))
            RightLowerBound[i] = min(RightUpperBound[i], dicho(D,SD,C[i]-K,N))
        # result
        res = 0
        for i in xrange(N):
            res += (LeftUpperBound[i]-LeftLowerBound[i]) * (RightLowerBound[i]-i)
            res += (i-LeftUpperBound[i]) * (RightUpperBound[i]-RightLowerBound[i])
            res += (LeftUpperBound[i]-LeftLowerBound[i]) * (RightUpperBound[i]-RightLowerBound[i])
        print('Case #%d: %d' % (t,res))
