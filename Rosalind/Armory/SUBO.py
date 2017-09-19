#!/usr/bin/env python3

# Method used here:
# 1. Use one LALIGN web interface to discover the pattern
# http://www.ebi.ac.uk/Tools/psa/lalign/nucleotide.html
# http://fasta.bioch.virginia.edu/fasta_www2/fasta_www.cgi?rm=lalign&pgm=lald
# 2. Append the discovered pattern to the FASTA input and use this script
# to count occurrences with errors

import sys
from Bio import SeqIO

# O(n*m)
def count_with_errors(S,P,errors=3):
    o = 0
    for i in range(len(S)-len(P)+1):
        j = e = 0
        while j<len(P) and e<=errors:
            if P[j]!=S[i+j]:
                e += 1
            j += 1
        if e<=errors:
            o += 1
    return o

DNAS = list(SeqIO.parse(sys.stdin,'fasta'))
print(count_with_errors(DNAS[0].seq,DNAS[2].seq),count_with_errors(DNAS[1].seq,DNAS[2].seq))
