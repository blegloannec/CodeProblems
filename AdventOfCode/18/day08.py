#!/usr/bin/env python3

I = list(map(int,input().split()))

# Part 1 & 2
def parse_tree(I,i=0):
    C,M = I[i],I[i+1]
    S = 2
    Meta = 0
    CVal = []
    for _ in range(C):
        cs,cmeta,cval = parse_tree(I,i+S)
        S += cs
        Meta += cmeta
        CVal.append(cval)
    Meta += sum(I[i+S:i+S+M])
    Val = sum(I[i+S:i+S+M]) if C==0 else sum(CVal[c-1] for c in I[i+S:i+S+M] if 1<=c<=C)
    S += M
    return S,Meta,Val

_,meta,val = parse_tree(I)
print(meta)
print(val)
