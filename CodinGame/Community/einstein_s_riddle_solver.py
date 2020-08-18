#!/usr/bin/env python3

class Riddle:
    def __init__(self, nbChar, nbItem):
        self.nbChar = nbChar
        self.nbItem = nbItem
        self.size = self.nbChar * self.nbItem
        # union-find-like structure to represent the current state
        self.Repr = [None]*self.size
        # characteristics masks
        self.Mask = [1<<(i//nbItem) for i in range(self.size)]
        self.full_mask = (1<<nbChar)-1
        # merge stack to reverse union operations
        self.MergeStack = []
        self.Forb = []
    
    def find(self, x):
        # without flattening (for union to be reversible)
        return x if self.Repr[x] is None else self.find(self.Repr[x])
    
    def assoc(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if self.Mask[x0]&self.Mask[y0]==0:
            self.Repr[y0] = x0
            self.Mask[x0] |= self.Mask[y0]
            self.MergeStack.append((x0,y0))
            return True
        return False
    
    def unassoc(self):
        x0,y0 = self.MergeStack.pop()
        self.Repr[y0] = None
        self.Mask[x0] ^= self.Mask[y0]
    
    def forbid(self, x, y):
        self.Forb.append((x,y))
    
    def backtrack(self):
        try:
            # find the first representative that is not characteristic-full
            i = next(i for i in range(self.size) if self.Repr[i] is None and self.Mask[i]!=self.full_mask)
        except StopIteration:
            return True
        # find the first missing characteristic of this element
        c = next(c for c in range(self.nbChar) if (self.Mask[i]>>c)&1==0)
        for j in range(c*self.nbItem, (c+1)*self.nbItem):
            # try compatible items of this characteristic
            if self.assoc(i,j):
                # checking that no forbidden association is made
                if all(self.find(a)!=self.find(b) for a,b in self.Forb):
                    if self.backtrack():
                        return True
                self.unassoc()
        return False

def main():
    nbChar, nbItem = map(int,input().split())
    Items = [input().split() for _ in range(nbChar)]
    Items[0].sort()  # for output format
    ItemIdx = {Items[c][i]: c*nbItem+i for c in range(nbChar) for i in range(nbItem)}
    S = Riddle(nbChar, nbItem)
    N = int(input())
    for _ in range(N):
        item1, rel, item2 = input().split()
        i1 = ItemIdx[item1]; i2 = ItemIdx[item2]
        if rel=='&':
            S.assoc(i1, i2)
        else:
            S.forbid(i1, i2)
    assert S.backtrack()
    for c in range(nbChar):
        O = [None]*nbItem
        for i in range(nbItem):
            j = next(j for j in range(nbItem) if S.find(c*nbItem+i)==S.find(j))
            O[j] = Items[c][i]
        print(*O)

main()
