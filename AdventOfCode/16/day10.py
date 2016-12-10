#!/usr/bin/env python

import sys
from collections import defaultdict

# a lot of "assert" as the problem statement is unclear about the graph
# properties (actually a DAG with in-degree 2 and out-degree 2 for bots,
# out-degree 1 for inputs and in-degree 1 for outputs)

def main():
    # Parsing input
    Succ = {}
    In = defaultdict(list)
    for L in sys.stdin.readlines():
        L = L.split()
        if L[0]=='value':
            v,b = int(L[1]),int(L[5])
            In[b].append(v)
            assert(len(In[b])<=2) # just to make sure
        else:
            b = int(L[1])
            assert(b not in Succ) # just to make sure
            l = (L[5],int(L[6]))
            h = (L[10],int(L[11]))
            Succ[b] = (l,h)
    # Solving problem
    Out = {}
    Q = [] # bots for which input values are currently known
    for b in In:
        if len(In[b])==2:
            Q.append(b)
    while Q:
        b = Q.pop()
        vl,vh = sorted(In[b])
        if (vl,vh)==(17,61): # output for Part One
            print b
        assert(b in Succ) # just to make sure
        l,h = Succ[b]
        if l[0]=='bot':
            l = l[1]
            assert(len(In[l])<2) # just to make sure
            In[l].append(vl)
            if len(In[l])==2:
                Q.append(l)
        else:
            assert(l[1] not in Out) # just to make sure
            Out[l[1]] = vl
        if h[0]=='bot':
            h = h[1]
            assert(len(In[h])<2) # just to make sure
            In[h].append(vh)
            if len(In[h])==2:
                Q.append(h)
        else:
            assert(h[1] not in Out) # just to make sure
            Out[h[1]] = vh
    # output for Part Two
    print Out[0]*Out[1]*Out[2]

main()
