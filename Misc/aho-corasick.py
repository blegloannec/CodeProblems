#!/usr/bin/env python3

# see HR 101Hack46 dna_health.cpp for a C++ version

from collections import deque

# Aho-Corasick, Efficient String Matching, 1975
# using dictionnaries (fast but memory expensive)
class ACTrie:
    def __init__(self,W):
        self.W = W[:]   # copy for safety
        self.G = [{}]   # transitions
        self.O = [[]]   # final states
        self.F = [None] # fail function
        for iw in range(len(self.W)):
            w = self.W[iw]
            s = 0
            for c in w:
                if c in self.G[s]:
                    s = self.G[s][c]
                else:
                    s0 = self.new_state()
                    self.G[s][c] = s0
                    s = s0
            self.O[s].append(iw)
        # failure computation (BFS)
        Q = deque([0])
        while Q:
            s = Q.popleft()
            for c in self.G[s]:
                s0 = self.G[s][c]
                Q.append(s0)
                if s==0: # s0 at depth 1
                    self.F[s0] = 0
                else:
                    f = self.F[s]
                    while self.g(f,c)==None:
                        f = self.F[f]
                    f0 = self.g(f,c)
                    self.F[s0] = f0
                    # on complete la sortie de s0
                    self.O[s0] += self.O[f0]
            
    def g(self,s,c): # transition function completed for 0 -*-> 0
        if c in self.G[s]:
            return self.G[s][c]
        return 0 if s==0 else None

    def new_state(self):
        s = len(self.G)
        self.G.append({})
        self.O.append([])
        self.F.append(None)
        return s

    def find(self,S):
        s = 0
        for i in range(len(S)):
            c = S[i]
            while self.g(s,c)==None:
                s = self.F[s]
            s = self.g(s,c)
            if self.O[s]: # motif(s) trouve(s)
                # renvoie les indices des motifs
                #yield (i,self.O[s])
                # renvoie les motifs
                yield (i,list(map(lambda iw: self.W[iw], self.O[s])))
                

A = ACTrie(['he','she','is','hers'])
for o in A.find('ishers'):
    print(o)

B = ACTrie(['aaa','a','aa'])
for o in B.find('aaaaa'):
    print(o)


# =============================================
# Aho-Corasick, Efficient String Matching, 1975
# version with fixed alphabet size
# using lists instead of dictionnaries
# (slighly slower but potentially less memory
#  exensive, depending on the cases however)
Alpha = 26 # alphabet size

def num(c): # char to num
    return ord(c)-ord('a')

class ACTrie:
    def __init__(self,W):
        self.W = W
        self.G = [[None]*Alpha] # transitions
        self.O = [[]]           # final states
        self.F = [None]         # fail function
        for iw in range(len(self.W)):
            w = self.W[iw]
            s = 0
            for c in w:
                c = num(c)
                if self.G[s][c]!=None:
                    s = self.G[s][c]
                else:
                    s0 = self.new_state()
                    self.G[s][c] = s0
                    s = s0
            self.O[s].append(iw)
        # failure computation (BFS)
        Q = deque([0])
        while Q:
            s = Q.popleft()
            for c in range(Alpha):
                s0 = self.G[s][c]
                if s0==None:
                    continue
                Q.append(s0)
                if s==0: # s0 at depth 1
                    self.F[s0] = 0
                else:
                    f = self.F[s]
                    while self.g(f,c)==None:
                        f = self.F[f]
                    f0 = self.g(f,c)
                    self.F[s0] = f0
                    # on complete la sortie de s0
                    self.O[s0] += self.O[f0]
            
    def g(self,s,c): # transition function completed for 0 -*-> 0
        if self.G[s][c]!=None:
            return self.G[s][c]
        return 0 if s==0 else None

    def new_state(self):
        s = len(self.G)
        self.G.append([None]*Alpha)
        self.O.append([])
        self.F.append(None)
        return s

    def find(self,S):
        s = 0
        for i in range(len(S)):
            c = num(S[i])
            while self.g(s,c)==None:
                s = self.F[s]
            s = self.g(s,c)
            if self.O[s]: # motif(s) trouve(s)
                # renvoie les indices des motifs
                yield (i,self.O[s])
                # renvoie les motifs
                #yield (i,list(map(lambda iw: self.W[iw], self.O[s])))
