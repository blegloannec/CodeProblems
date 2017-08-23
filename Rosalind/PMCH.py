#!/usr/bin/env python3

import rosalib

def fact(n):
    return 1 if n<=1 else n*fact(n-1)

_,RNA = rosalib.parse_fasta()[0]
print(fact(RNA.count('A'))*fact(RNA.count('C')))
