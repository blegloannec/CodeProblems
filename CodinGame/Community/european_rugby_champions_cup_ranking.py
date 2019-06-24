#!/usr/bin/env python3

from itertools import groupby

class Game:
    def __init__(self, Desc):
        self.teamA, ptsA, triesA, self.teamB, ptsB, triesB = Desc.split(',')
        self.ptsA, self.triesA = int(ptsA), int(triesA)
        self.ptsB, self.triesB = int(ptsB), int(triesB)
        # game ranking points
        self.rnkPtsA = self.rnkPtsB = 2
        if   self.ptsA > self.ptsB: self.rnkPtsA, self.rnkPtsB = 4, 0
        elif self.ptsA < self.ptsB: self.rnkPtsA, self.rnkPtsB = 0, 4
        if self.triesA >= 4: self.rnkPtsA += 1
        if self.triesB >= 4: self.rnkPtsB += 1
        if   0 < self.ptsA-self.ptsB <= 7: self.rnkPtsB += 1
        elif 0 < self.ptsB-self.ptsA <= 7: self.rnkPtsA += 1


class Pool:
    def __init__(self, Desc):
        self.Teams = Desc.split(',')

    def process_ranking(self):
        self.rnkPts   = {T:0 for T in self.Teams}
        self.aggrDiff = {T:0 for T in self.Teams}
        for A in self.Teams:
            for B in self.Teams:
                if A!=B:
                    G = GameDB[A,B]
                    self.rnkPts[A]   += G.rnkPtsA
                    self.rnkPts[B]   += G.rnkPtsB
                    self.aggrDiff[A] += G.ptsA - G.ptsB
                    self.aggrDiff[B] += G.ptsB - G.ptsA
        # first pass of sort
        rnk_pts = lambda T: self.rnkPts[T]
        self.Ranking = sorted(self.Teams, key=rnk_pts, reverse=True)
        # refining points to break ties
        self.subRnkPts   = {T:0 for T in self.Teams}
        self.subAggrDiff = {T:0 for T in self.Teams}
        for _, tied_pool in groupby(self.Ranking, key=rnk_pts):
            self._process_subpool(list(tied_pool))
        # second pass of sort
        rnk_key = lambda T: (self.rnkPts[T], self.subRnkPts[T], self.subAggrDiff[T])
        self.Ranking = sorted(self.Teams, key=rnk_key, reverse=True)

    def _process_subpool(self, SubPool):
        for A in SubPool:
            for B in SubPool:
                if A!=B:
                    G = GameDB[A,B]
                    self.subRnkPts[A]   += G.rnkPtsA
                    self.subRnkPts[B]   += G.rnkPtsB
                    self.subAggrDiff[A] += G.ptsA - G.ptsB
                    self.subAggrDiff[B] += G.ptsB - G.ptsA


if __name__=='__main__':
    GameDB = {}
    Pools = [Pool(input()) for _ in range(5)]
    for _ in range(60):
        G = Game(input())
        GameDB[G.teamA,G.teamB] = G
    for P in Pools:
        P.process_ranking()
    top_key = lambda i: lambda P: (P.rnkPts[P.Ranking[i]], P.aggrDiff[P.Ranking[i]])
    Top10 = [P.Ranking[0] for P in sorted(Pools, key=top_key(0), reverse=True)] + \
            [P.Ranking[1] for P in sorted(Pools, key=top_key(1), reverse=True)]
    print('\n'.join('{} - {}'.format(Top10[i],Top10[7-i]) for i in range(4)))
