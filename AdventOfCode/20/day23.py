#!/usr/bin/env pypy3

I = list(map(int, input()))

class Link:
    def __init__(self, v):
        self.v = v
        self.l = self.r = None

def link_lr(L, R):
    L.r = R
    R.l = L

def crab(Cups, steps=100):
    N = len(Cups)
    # init. doubly-linked list
    Links = [Link(v) for v in Cups]
    for i in range(N): link_lr(Links[i-1], Links[i])
    # init. value -> link array
    V2L = [None]*(N+1)
    for L in Links: V2L[L.v] = L
    # do steps moves
    currL = Links[0]
    for _ in range(steps):
        # select the 3 following values
        R = currL.r
        V3 = []
        for _ in range(3):
            V3.append(R.v)
            R = R.r
        # remove them
        link_lr(currL, R)
        # find the destination
        destv = N if currL.v==1 else currL.v-1
        while destv in V3:
            destv = N if destv==1 else destv-1
        destL = V2L[destv]
        # insert them
        link_lr(V2L[V3[-1]], destL.r)
        link_lr(destL, V2L[V3[0]])        
        # next current link
        currL = currL.r
    return V2L[1]


# Part 1
L1 = crab(I)
L = L1.r
while L!=L1:
    print(L.v, end='')
    L = L.r
print()


# Part 2
I.extend(range(len(I)+1, 10**6+1))
Lstar = crab(I, 10**7).r
print(Lstar.v * Lstar.r.v)
