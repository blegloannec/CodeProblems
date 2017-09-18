#!/usr/bin/env python3

import sys
from Bio import Entrez,SeqIO

GID = input().split()
Entrez.email = 'none@none.net'
handle = Entrez.efetch(db='nucleotide', id=GID, rettype='fasta')
records = list(SeqIO.parse(handle,'fasta'))
rmin = min((len(records[i].seq),i) for i in range(len(records)))[1]
SeqIO.write(records[rmin],sys.stdout,'fasta')
