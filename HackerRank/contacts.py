#!/usr/bin/env python3

class Trie:
    def __init__(self):
        self.G = [{}]
        self.F = [False]
        self.Cnt = [0]

    def insert(self, w):
        s = 0
        self.Cnt[s] += 1
        for c in w:
            if c in self.G[s]:
                s = self.G[s][c]
                self.Cnt[s] += 1
            else:
                s0 = len(self.G)
                self.G.append({})
                self.F.append(False)
                self.Cnt.append(1)
                self.G[s][c] = s0
                s = s0
        self.F[s] = True

    def find(self, w):
        s = 0
        for c in w:
            if c in self.G[s]:
                s = self.G[s][c]
            else:
                return 0
        return self.Cnt[s]


def main():
    n = int(input())
    T = Trie()
    for _ in range(n):
        op,name = input().split()
        if op=='add':
            T.insert(name)
        else:
            print(T.find(name))

main()
