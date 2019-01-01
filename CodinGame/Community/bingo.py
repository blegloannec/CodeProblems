#!/usr/bin/env python3

class BingoCard:
    S = 5
    NOTHING,MARKED,BINGO,FULL = 0,1,2,3
    
    def __init__(self):
        self.P = {}
        self.R = [0]*self.S
        self.C = [0]*self.S
        self.D = self.AD = self.Filled = 0
        self.parse()
    
    def _mark(self, i, j):
        bingo = False
        self.R[i] += 1
        if self.R[i]==self.S:
            self.Filled += 1
            bingo = True
        self.C[j] += 1
        if self.C[j]==self.S:
            self.Filled += 1
            bingo = True
        if i==j:
            self.D += 1
            if self.D==self.S:
                self.Filled += 1
                bingo = True
        if i==self.S-1-j:
            self.AD += 1
            if self.AD==self.S:
                self.Filled += 1
                bingo = True
        return bingo
    
    def parse(self):
        for i in range(self.S):
            L = list(map(int,input().split()))
            for j in range(self.S):
                self.P[L[j]] = (i,j)
                if L[j]==0:
                    self._mark(i,j)
    
    def call(self, k):
        if k in self.P:
            if self._mark(*self.P[k]):
                if self.Filled==2*self.S+2:
                    return self.FULL
                return self.BINGO
            return self.MARKED
        return self.NOTHING


def main():
    n = int(input())
    BC = [BingoCard() for _ in range(n)]
    Calls = list(map(int,input().split()))
    bingo = False
    for i in range(len(Calls)):
        for C in BC:
            code = C.call(Calls[i])
            if not bingo and code==BingoCard.BINGO:
                print(i+1)
                bingo = True
            elif code==BingoCard.FULL:
                print(i+1)
                return

main()
