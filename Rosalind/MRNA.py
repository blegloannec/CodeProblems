#!/usr/bin/env python3

Dinv = {'R': ['CGU', 'CGA', 'AGG', 'CGG', 'CGC', 'AGA'], 'S': ['AGC', 'UCG', 'UCA', 'AGU', 'UCC', 'UCU'], 'D': ['GAC', 'GAU'], 'H': ['CAU', 'CAC'], 'A': ['GCU', 'GCG', 'GCA', 'GCC'], 'Y': ['UAC', 'UAU'], 'G': ['GGA', 'GGC', 'GGU', 'GGG'], 'I': ['AUC', 'AUU', 'AUA'], 'P': ['CCG', 'CCC', 'CCU', 'CCA'], 'V': ['GUC', 'GUU', 'GUG', 'GUA'], 'C': ['UGC', 'UGU'], 'K': ['AAA', 'AAG'], 'M': ['AUG'], 'L': ['CUA', 'UUA', 'CUU', 'CUC', 'UUG', 'CUG'], 'W': ['UGG'], 'N': ['AAC', 'AAU'], 'F': ['UUU', 'UUC'], 'T': ['ACA', 'ACU', 'ACG', 'ACC'], 'Stop': ['UAG', 'UGA', 'UAA'], 'E': ['GAG', 'GAA'], 'Q': ['CAG', 'CAA']}

def rev_count(P,M):
    res = len(Dinv['Stop'])
    for X in P:
        res = (res*len(Dinv[X]))%M
    return res

print(rev_count(input(),10**6))
