#!/usr/bin/env python3

from math import log2

Spec = 4

class DataPoint:
    def __init__(self, idx, val, spec):
        self.idx, self.val, self.spec = idx, val, spec
    def __lt__(self, B):
        return (self.val, self.idx) < (B.val, B.idx)

def E2(S):
    T = sum(S)
    assert T>0
    return -sum(s/T*log2(s/T) if s!=0 else 0 for s in S)

Trace = []
def split(Data, l, r):
    # l included, r excluded
    assert r-l>0
    SL, SR = [0]*Spec, [0]*Spec
    for i in range(l,r):
        SR[Data[i].spec] += 1
    e2 = E2(SR)
    if e2==0:
        return
    E = []
    for i in range(l+1,r):
        s = Data[i-1].spec
        SL[s] += 1
        SR[s] -= 1
        if Data[i].val > Data[i-1].val:
            e2l, e2r = E2(SL), E2(SR)
            ew = (i-l)/(r-l)*e2l + (r-i)/(r-l)*e2r
            E.append((ew,Data[i].idx,i))
    if E:  # E2>0 yet it might not be possible to split anymore
        _,midx,m = min(E)
        Trace.append(midx)
        split(Data,l,m)
        split(Data,m,r)

if __name__=='__main__':
    N = int(input())
    Data = []
    for i in range(N):
        idx,val,spec  = map(int,input().split())
        assert idx==i
        Data.append(DataPoint(idx,val,spec-1))
    Data.sort()
    split(Data,0,N)
    print(Trace.pop())
