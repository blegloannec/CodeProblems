#!/usr/bin/env python3

import sys
from Bio import SeqIO

thresh = int(input())
records = SeqIO.parse(sys.stdin,'fastq')
cpt = 0
for r in records:
    qual = r.letter_annotations['phred_quality']
    # "below the threshold"? Inaccurate and misleading...
    if thresh*len(qual)>sum(qual):
        cpt += 1
print(cpt)
