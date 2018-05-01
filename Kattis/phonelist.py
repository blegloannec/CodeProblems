#!/usr/bin/env python3

class Trie:
    def __init__(self):
        self.G = [{}]
        self.F = [False]

    def insert(self, w):
        prefix = True
        extend = False
        s = 0
        for c in w:
            if c in self.G[s]:
                s = self.G[s][c]
                if self.F[s]:
                    extend = True
            else:
                prefix = False
                s0 = len(self.G)
                self.G.append({})
                self.F.append(False)
                self.G[s][c] = s0
                s = s0
        self.F[s] = True
        return not (prefix or extend)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        W = [input() for _ in range(n)]
        T = Trie()
        consistent = True
        for w in W:
            if not T.insert(w):
                consistent = False
                break
        print('YES' if consistent else 'NO')

main()
