#!/usr/bin/env python3

class Genome:
    def __init__(self, t1,r1, t2,r2):
        self.T = (t1,t2)
        self.t = t1|t2
        self.Rh = (r1,r2)
        self.rh = r1|r2
    
    def __add__(self, G):
        for t1 in self.T:
            for r1 in self.Rh:
                for t2 in G.T:
                    for r2 in G.Rh:
                        yield Genome(t1,r1, t2,r2)
    
    def __repr__(self):
        return ('O','A','B','AB')[self.t] + '-+'[self.rh]
    
    @staticmethod
    def generate():
        for t1 in range(3):
            for r1 in range(2):
                for t2 in range(3):
                    for r2 in range(2):
                        yield Genome(t1,r1, t2,r2)

def precomp():
    Eqs = set()
    for G1 in Genome.generate():
        for G2 in Genome.generate():
            for G3 in G1+G2:
                Eqs.add((str(G1), str(G2), str(G3)))
    return list(Eqs)

def main():
    Eqs = precomp()
    N = int(input())
    for _ in range(N):
        I = input().split()
        k1,k2 = (i for i in range(3) if I[i]!='?')
        u = 3-k1-k2
        Sol = []
        for E in Eqs:
            if I[k1]==E[k1] and I[k2]==E[k2]:
                Sol.append(E[u])
        print(' '.join(sorted(Sol)) if Sol else 'impossible')

main()
