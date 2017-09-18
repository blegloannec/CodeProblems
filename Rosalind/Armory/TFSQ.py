#!/usr/bin/env python3

import sys
from Bio import SeqIO

records = SeqIO.parse(sys.stdin,'fastq')
SeqIO.write(records,sys.stdout,'fasta')
