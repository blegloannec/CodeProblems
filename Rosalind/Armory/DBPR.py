#!/usr/bin/env python3

from Bio import ExPASy,SwissProt

P = input()
handle = ExPASy.get_sprot_raw(P)
record = SwissProt.read(handle)
for X in record.cross_references:
    #  GO                Biological process
    if X[0]=='GO' and X[2][0]=='P':
        print(X[2][2:])
