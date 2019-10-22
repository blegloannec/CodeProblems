#!/usr/bin/env python3

from collections import deque

# Aho-Corasick, Efficient String Matching, 1975
# using dictionnaries (fast but memory expensive)
class ACTrie:
    def __init__(self,W):
        self.W = W[:]   # copy for safety
        self.G = [{}]   # transitions
        self.O = [[]]   # final states
        self.F = [None] # fail function
        self.B = [None] # dict backlink
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
                    # IMPLEM. 1 - on complete la sortie de s0
                    #self.O[s0] += self.O[f0]
                    # IMPLEM. 2 - backlink
                    self.B[s0] = f0 if self.O[f0] else self.B[f0]
            
    def g(self,s,c): # transition function completed for 0 -*-> 0
        if c in self.G[s]:
            return self.G[s][c]
        return 0 if s==0 else None

    def new_state(self):
        s = len(self.G)
        self.G.append({})
        self.O.append([])
        self.F.append(None)
        self.B.append(None)
        return s

    def find(self,S):
        s = 0
        for i in range(len(S)):
            c = S[i]
            while self.g(s,c)==None:
                s = self.F[s]
            s = self.g(s,c)
            # IMPLEM. 1 dans laquelle on complete l'output
            # if self.O[s]: # motif(s) trouve(s)
                # renvoie les indices des motifs
                # yield (i,self.O[s])
                # renvoie les motifs
                # yield (i,list(map(lambda iw: self.W[iw], self.O[s])))
            # IMPLEM. 2 dans laquelle on utilise des backlinks
            if self.O[s] or self.B[s]: # motif direct ou backlink
                # renvoie le noeud du trie
                yield (i,s)

    # IMPLEM. 2 - calculer l'output d'un noeud
    # (version iterative, parce que Python)
    def output(self,s):
        while s:
            yield from self.O[s]
            s = self.B[s]

A = ACTrie(['he','she','is','hers'])
for (i,s) in A.find('ishers'):
    print(i,[A.W[a] for a in A.output(s)])

B = ACTrie(['aaa','a','aa'])
for (i,s) in B.find('aaaaa'):
    print(i,[B.W[a] for a in B.output(s)])


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
        self.B = [None]         # dict backlink
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
                    self.B[s0] = f0 if self.O[f0] else self.B[f0]
            
    def g(self,s,c): # transition function completed for 0 -*-> 0
        if self.G[s][c]!=None:
            return self.G[s][c]
        return 0 if s==0 else None

    def new_state(self):
        s = len(self.G)
        self.G.append([None]*Alpha)
        self.O.append([])
        self.F.append(None)
        self.B.append(None)
        return s

    def find(self,S):
        s = 0
        for i in range(len(S)):
            c = num(S[i])
            while self.g(s,c)==None:
                s = self.F[s]
            s = self.g(s,c)
            if self.O[s] or self.B[s]: # motif(s) trouve(s)
                yield (i,s)
    
    def output(self,s):
        while s:
            yield from self.O[s]
            s = self.B[s]


A = ACTrie(['he','she','is','hers'])
for (i,s) in A.find('ishers'):
    print(i,[A.W[a] for a in A.output(s)])

B = ACTrie(['aaa','a','aa'])
for (i,s) in B.find('aaaaa'):
    print(i,[B.W[a] for a in B.output(s)])
