#!/usr/bin/env python3

import rosalib
import re

# "lazy" solution using python regex
# we could have used Aho-Corasick instead...

L = rosalib.parse_fasta()
_,DNA = L[0]
pattern = re.compile('|'.join(I for (_,I) in L[1:]))
DNA = pattern.sub('',DNA)
print(rosalib.rna2prot(rosalib.dna2rna(DNA)))
