#!/usr/bin/env python3

from itertools import chain
from collections import Counter

class Square:
    def __init__(self, x, y, s):
        # NB: we won't keep the position as it's not required in the output
        self.size = s
        C = Counter(chain(Grid[x][y:y+s], Grid[x+s-1][y:y+s],     \
                          (Grid[i][y] for i in range(x+1,x+s-1)), \
                          (Grid[i][y+s-1] for i in range(x+1,x+s-1))))
        self.valid = '.' not in C
        self.ready = False
        if self.valid:
            self.candidates = set(n for n,c in C.items() if Total[n]==c)
            self.intersects = set(C.keys()) - self.candidates
            self._status()

    def _status(self):
        self.valid = len(self.candidates)>0
        self.ready = len(self.candidates)==1 and len(self.intersects)==0

    def discard(self, n):
        self.candidates.discard(n)
        self.intersects.discard(n)
        self._status()


if __name__=='__main__':
    H,W = map(int,input().split())
    N = int(input())
    Grid = [input() for _ in range(H)]
    Total = Counter(chain(*Grid))
    # building lists of possible squares (naively in O(N^4))
    ReadySqr = []
    WaitingSqr = []
    for x in range(H):
        for y in range(W):
            smax = min(H-x, W-y)
            for s in range(2,smax+1):
                S = Square(x,y,s)
                if   S.ready: ReadySqr.append(S)
                elif S.valid: WaitingSqr.append(S)
    # building solution
    Sol = []
    Solved = set()
    while ReadySqr:
        assert len(ReadySqr)==1  # otherwise no total order
        S0 = ReadySqr.pop()
        n0 = S0.candidates.pop()
        assert n0 not in Solved
        Sol.append((n0,S0.size))
        Solved.add(n0)
        NewWaitingSqr = []
        for S in WaitingSqr:
            S.discard(n0)
            if   S.ready: ReadySqr.append(S)
            elif S.valid: NewWaitingSqr.append(S)
        WaitingSqr = NewWaitingSqr
    assert len(Solved)==N
    # printing solution
    for sol in reversed(Sol):
        print(*sol)
