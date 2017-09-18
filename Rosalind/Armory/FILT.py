#!/usr/bin/env python3

import sys
from Bio import SeqIO

thresh,perc = map(int,input().split())
records = SeqIO.parse(sys.stdin,'fastq')
cpt = 0
for r in records:
    qual = r.letter_annotations['phred_quality']
    nb_qual = sum(int(x>=thresh) for x in qual)
    if 100*nb_qual>=perc*len(qual):
        cpt += 1
print(cpt)
