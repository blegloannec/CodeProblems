#!/usr/bin/env python3

import sys
from Bio import SeqIO

thresh = int(input())
records = list(SeqIO.parse(sys.stdin,'fastq'))
size = len(records[0].seq)
cpt = 0
for i in range(size):
    qual = sum(r.letter_annotations['phred_quality'][i] for r in records)
    if qual<thresh*len(records):
        cpt += 1
print(cpt)
