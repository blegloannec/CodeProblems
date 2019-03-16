#!/usr/bin/env python3

from math import sqrt, log

class MCTNode:
    def __init__(self, score=None):
        if score is not None:
            self.visits = 1
            self.score = score
        else:
            self.visits = 0
            self.score = 0
        self.Children = {}

    def insert(self, S, score, i=0):
        self.visits += 1
        self.score += score
        if i<len(S):
            if S[i] in self.Children:
                self.Children[S[i]].insert(S, score, i+1)
            else:
                self.Children[S[i]] = MCTNode(score)

    def _UCB1(self, a):
        Child = self.Children[a]
        return Child.score/Child.visits + C*sqrt(log(self.visits)/Child.visits)

    def explore(self, C, Path):
        if self.Children:
            a = max(self.Children.keys(), key=(lambda a: (self._UCB1(a), -ord(a))))
            Path.append(a)
            self.Children[a].explore(C, Path)


if __name__=='__main__':
    N, C = input().split()
    N, C = int(N), float(C)
    T = MCTNode()
    for _ in range(N):
        Seq, score = input().split()
        score = float(score)
        T.insert(Seq, score)
    Path = []
    T.explore(C, Path)
    print(''.join(Path))
