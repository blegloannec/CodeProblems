#!/usr/bin/env python3

import sys

D = {'GCU': 'A', 'UGA': 'Stop', 'UUC': 'F', 'AAG': 'K', 'AAA': 'K', 'UCC': 'S', 'GGG': 'G', 'CCG': 'P', 'CGU': 'R', 'UGC': 'C', 'GGC': 'G', 'CCA': 'P', 'AGC': 'S', 'UCG': 'S', 'CCC': 'P', 'UAC': 'Y', 'CUG': 'L', 'AGA': 'R', 'AUA': 'I', 'GAG': 'E', 'UCA': 'S', 'AAC': 'N', 'CUU': 'L', 'CAA': 'Q', 'GGU': 'G', 'UGG': 'W', 'GCG': 'A', 'GUC': 'V', 'ACA': 'T', 'CAU': 'H', 'UCU': 'S', 'CGC': 'R', 'GCA': 'A', 'AUC': 'I', 'GUU': 'V', 'UGU': 'C', 'GAA': 'E', 'UUU': 'F', 'CGG': 'R', 'GUG': 'V', 'ACG': 'T', 'CUC': 'L', 'AAU': 'N', 'AGU': 'S', 'UAA': 'Stop', 'CGA': 'R', 'UAU': 'Y', 'GAU': 'D', 'CAG': 'Q', 'UUG': 'L', 'AUU': 'I', 'CAC': 'H', 'ACU': 'T', 'CUA': 'L', 'AUG': 'M', 'UUA': 'L', 'GAC': 'D', 'AGG': 'R', 'GUA': 'V', 'UAG': 'Stop', 'GCC': 'A', 'ACC': 'T', 'GGA': 'G', 'CCU': 'P'}

start = 'AUG'

def dna2rna(DNA):
    return DNA.replace('T','U')

def rna2prot(RNA,start=0):
    res = []
    for i in range(start,len(RNA),3):
        C = RNA[i:i+3]
        if C not in D:
            return None
        DC = D[C]
        if DC=='Stop':
            return ''.join(res)
        res.append(DC)
    return None

def findall(S,T):
    p = S.find(T)
    while p!=-1:
        yield p
        p = S.find(T,p+1)

def revc(DNA):
    D = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    return ''.join(D[c] for c in reversed(DNA))

def find_orf(RNA):
    for p in findall(RNA,start):
        P = rna2prot(RNA,p)
        if P!=None:
            yield P

def main():
    L = sys.stdin.readlines()[1:]
    P = set()
    DNA = ''.join(s.strip() for s in L)
    RNA = dna2rna(DNA)
    for p in find_orf(RNA):
        P.add(p)
    RNA = dna2rna(revc(DNA))
    for p in find_orf(RNA):
        P.add(p)
    for p in P:
        print(p)

main()
