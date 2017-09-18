#!/usr/bin/env python3

from Bio import Seq

DNA = input()
P = input()
code = 1
while True:
    try:
        if Seq.translate(DNA, table=code, stop_symbol='') == P:
            break
    except KeyError:  # code non valide (e.g. 7 et 8)
        pass
    code += 1
print(code)
