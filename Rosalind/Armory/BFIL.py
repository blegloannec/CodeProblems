#!/usr/bin/env python3

import sys
from Bio import SeqIO

q = int(input())
records = list(SeqIO.parse(sys.stdin,'fastq'))
cpt = 0
for i in range(len(records)):
    qual = records[i].letter_annotations['phred_quality']
    l = 0
    while l<len(records[i].seq) and qual[l]<q:
        l += 1
    r = len(records[i].seq)-1
    while r>0 and qual[r]<q:
        r -= 1
    # trimming the record
    del records[i].letter_annotations['phred_quality']
    records[i].seq = records[i].seq[l:r+1]
    records[i].letter_annotations['phred_quality'] = qual[l:r+1]
SeqIO.write(records,sys.stdout,'fastq')
