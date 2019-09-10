#!/usr/bin/env python3

def alternate(o=0):
    i = 0
    while True:
        yield o+i
        i = -i
        if i<=0:
            i -= 1


class Room:
    def __init__(self, H, W):
        self.H, self.W = H, W
        self.G = [[0]*self.W for _ in range(self.H)]
        self.group_score = self.seat_score = 0

    def _free(self, i, j, n):
        return 0<=i<self.H and 0<=j and j+n<=self.W and \
            self.G[i][j+n-1] - (0 if j==0 else self.G[i][j-1]) == 0

    def _set(self, i, j, n):
        assert j+n<=self.W
        for k in range(j,self.W):
            self.G[i][k] += min(k-j+1,n)

    def _sit(self, i, j, n):
        rskip = 0
        for r in alternate(i):
            if not 0<=r<self.H:
                rskip += 1
                if rskip==2:
                    break
            else:
                rskip = 0
            cskip = 0
            for c in alternate(j):
                if not 0<=c<c+n<=self.W:
                    cskip += 1
                    if cskip==2:
                        break
                else:
                    cskip = 0
                if self._free(r,c,n):
                    self._set(r,c,n)
                    return r,c
        return None

    def sit(self, i, j, n, group=None):
        assert n>0
        if group is None:
            group = (i,j,n)
        pos = self._sit(i,j,n)
        if pos is not None:
            i,j = pos
            self.score(i, j, n, group)
        else:
            assert n>1
            m = n//2
            self.sit(i, j, n-m, group)
            self.sit(i, j,   m, group)

    def score(self, i, j, n, group):
        if (i,j,n)==group:
            self.group_score += 1
        gi,gj,gn = group
        if i==gi:
            for k in range(j,j+n):
                if gj<=k<gj+gn:
                    self.seat_score += 1


def main():
    H,W = map(int,input().split())
    N = int(input())
    Groups = [tuple(map(int,input().split())) for i in range(N)]
    Cinema = Room(H,W)
    for n,r,c in Groups:
        Cinema.sit(r,c,n)
    print(Cinema.group_score, Cinema.seat_score)

main()
