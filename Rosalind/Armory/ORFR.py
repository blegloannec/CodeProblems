#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# In ORF (Stronghold) we did enumerate ORFs in a straightforward O(n^2) way
# (as there are anyway O(n) of them of total size O(n^2) in the worst case).
# Here we enumerate *maximal* ORFs (that cannot be extended to the left
# from an earlier start) in O(n) (there are O(n) of them of total size O(n)
# in the worst case).

start = 'M'
stop = '*'

DNA = Seq(input(),IUPAC.unambiguous_dna)
DNArc = DNA.reverse_complement()
N = len(DNA)
# on traduit integralement les 3 decalages (reading frames) de la chaine
# et de son complementaire inverse
P = []
for i0 in range(3):
    P.append(DNA[i0:N-((N-i0)%3)].translate())
    P.append(DNArc[i0:N-((N-i0)%3)].translate())
# on recherche les ORF maximaux (non prolongeables sur la gauche)
ir,ml,mr = None,0,0
for rf in range(6):
    l = None
    for i in range(len(P[rf])):
        if P[rf][i]==start and l==None:
            l = i
        elif P[rf][i]==stop and l!=None:
            if i-l>mr-ml:
                ir,ml,mr = rf,l,i
            l = None
assert(ir!=None)  # au moins un ORF trouve
print(P[ir][ml:mr])
