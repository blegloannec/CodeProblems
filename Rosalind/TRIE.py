#!/usr/bin/env python3

import sys

num = {'A':0, 'C':1, 'G':2, 'T':3}
let = 'ACGT'

class DNATrie:
    def __init__(self,W):
        self.G = [[None]*4]  # transitions
        self.F = [False]     # final states
        for w in W:
            s = 0
            for c in w:
                c = num[c]
                if self.G[s][c]!=None:
                    s = self.G[s][c]
                else:
                    s0 = self.new_state()
                    self.G[s][c] = s0
                    s = s0
            self.F[s] = True

    def new_state(self):
        s = len(self.G)
        self.G.append([None]*4)
        self.F.append(False)
        return s

def main():
    DNAS = [L.strip() for L in sys.stdin.readlines()]
    T = DNATrie(DNAS)
    for i in range(len(T.G)):
        for a in range(4):
            if T.G[i][a]!=None:
                print(i+1,T.G[i][a]+1,let[a])

main()
