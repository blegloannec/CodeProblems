#!/usr/bin/env python3

import sys
from Bio import SeqIO
from Bio.Alphabet import IUPAC

DNAS = SeqIO.parse(sys.stdin,'fasta',IUPAC.unambiguous_dna)
cpt = 0
for DNA in DNAS:
    if DNA.seq==DNA.seq.reverse_complement():
        cpt += 1
print(cpt)
