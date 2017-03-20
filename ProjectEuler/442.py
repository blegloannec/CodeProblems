#!/usr/bin/env python3

from collections import deque
import numpy

# Aho-Corasick, Efficient String Matching, 1975
Alpha = 10 # alphabet size

def num(c): # char to num
    return ord(c)-ord('0')

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

def main():
    W = [str(11**i) for i in range(1,18)]
    # on utilise Aho-Corasick pour construire un automate
    # deterministe associe (on aurait aussi pu construire
    # un automate non-deterministe naivement et determiniser)
    # en l'etat, l'automate reconnait tous les mots
    # *se terminant* par un facteur interdit
    # (un etat q est final si A.O[q] est non vide ou
    #  A.B[q]!=None)
    A = ACTrie(W)
    # on complete l'automate en calculant les arcs retour
    # Aho-Corasick ne fait qu'une construction partielle de 
    # ces arcs en utilisant une fail function a la place
    # on commence par ajouter un nouvel etat final pour reconnaitre
    # les mots *contenant* un facteur interdit
    qf = A.new_state()
    nbQ = len(A.G)
    for q in range(nbQ):
        if A.O[q] or A.B[q] or q==qf: # q etat final
            for a in range(Alpha):
                A.G[q][a] = qf
        else:
            for a in range(Alpha):
                if A.g(q,a)==None:
                    f = A.F[q]
                    while A.g(f,a)==None:
                        f = A.F[f]
                    A.G[q][a] = A.g(f,a)
    # maintenant l'automate est deterministe complet et reconnait
    # les mots contenant un facteur interdit
    # on constuit la matrice pour compter les mots
    M = [[0]*nbQ for _ in range(nbQ)]
    for q in range(nbQ):
        for a in range(Alpha):
            M[q][A.g(q,a)] += 1
    M = numpy.matrix(M)
    # on inverse les etats finaux pour reconnaitre
    # le complementaire
    finals = []
    for q in range(nbQ-1):
        if not (A.O[q] or A.B[q]):
            finals.append(q)
    # on calcule le resultat
    N = 10**18
    MM = [M**0]
    for k in range(18): # pour une reponse de taille <=18, suffisant ici
        MM.append(MM[-1]*M)
    # MM[k][q1,q2] compte le nb de mots de taille k de l'etat
    # q1 a l'etat q2
    # comme le chiffre 0 boucle sur l'etat 0, cela compte
    # tous les nombres de <=k chiffres
    n,q0,k,res = 0,0,len(MM)-1,0
    while n<N:
        for a in range(10):
            n0 = n
            n += sum(MM[k][A.g(q0,a),f] for f in finals)
            if n>N:
                # on a trouve le chiffre suivant a, on prend
                # pour nouvel etat initial q0 l'etat dans lequel on
                # arrive apres la lecture du prefixe courant
                # et on reduit la taille k du suffixe recherche
                q0 = A.g(q0,a)
                n = n0
                res = 10*res+a
                break
        k -= 1
    print(res)
    
main()
