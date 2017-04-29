#!/usr/bin/env python3

class Trie:
    def __init__(self,W):
        self.G = [{}]
        for w in W:
            s = 0
            for c in w:
                if c in self.G[s]:
                    s = self.G[s][c]
                else:
                    s0 = len(self.G)
                    self.G.append({})
                    self.G[s][c] = s0
                    s = s0

def main():
    N = int(input())
    W = []
    for _ in range(N):
        W.append(input())
    T = Trie(W)
    print(len(T.G)-1) # la racine ne compte pas

main()
