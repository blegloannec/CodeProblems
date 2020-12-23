#!/usr/bin/env pypy3

I = list(map(int, input()))

class Link:
    def __init__(self, v):
        self.v = v
        self.l = self.r = None

def crab(Cups, steps=100):
    N = len(Cups)
    # init. doubly-linked list
    Links = [Link(v) for v in Cups]
    for i in range(N):
        Links[i].l = Links[i-1]
        Links[i-1].r = Links[i]
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
        currL.r = R
        R.l = currL
        # find the destination
        destv = currL.v - 1
        if destv==0: destv = N
        while destv in V3:
            destv -= 1
            if destv==0: destv = N
        destL = V2L[destv]
        # insert them
        destR = destL.r
        destL.r = V2L[V3[0]]
        V2L[V3[0]].l = destL
        destR.l = V2L[V3[-1]]
        V2L[V3[-1]].r = destR
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
I.extend(range(10, 10**6+1))
Lstar = crab(I, 10**7).r
print(Lstar.v * Lstar.r.v)
