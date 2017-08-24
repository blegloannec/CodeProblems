#!/usr/bin/env python3

import rosalib

def sign(DNA):
    REV = rosalib.revc(DNA)
    return (DNA,REV) if DNA<=REV else (REV,DNA)

DBI = {}     # Incorrect
DBC = set()  # Correct

def correct(DNA):
    for (A,B) in DBC:
        if rosalib.hamming(DNA,A)==1:
            return A
        elif rosalib.hamming(DNA,B)==1:
            return B
    assert(False) # correction impossible, ne devrait pas se produire

def main():
    for _,DNA in rosalib.parse_fasta():
        S = sign(DNA)
        if S in DBC:
            continue
        elif S in DBI:
            del DBI[S]
            DBC.add(S)
        else:
            DBI[S] = DNA
    for S in DBI:
        DNA = DBI[S]
        print('%s->%s' % (DNA,correct(DNA)))

main()
