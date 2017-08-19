#!/usr/bin/env python3

D = {'GCU': 'A', 'UGA': 'Stop', 'UUC': 'F', 'AAG': 'K', 'AAA': 'K', 'UCC': 'S', 'GGG': 'G', 'CCG': 'P', 'CGU': 'R', 'UGC': 'C', 'GGC': 'G', 'CCA': 'P', 'AGC': 'S', 'UCG': 'S', 'CCC': 'P', 'UAC': 'Y', 'CUG': 'L', 'AGA': 'R', 'AUA': 'I', 'GAG': 'E', 'UCA': 'S', 'AAC': 'N', 'CUU': 'L', 'CAA': 'Q', 'GGU': 'G', 'UGG': 'W', 'GCG': 'A', 'GUC': 'V', 'ACA': 'T', 'CAU': 'H', 'UCU': 'S', 'CGC': 'R', 'GCA': 'A', 'AUC': 'I', 'GUU': 'V', 'UGU': 'C', 'GAA': 'E', 'UUU': 'F', 'CGG': 'R', 'GUG': 'V', 'ACG': 'T', 'CUC': 'L', 'AAU': 'N', 'AGU': 'S', 'UAA': 'Stop', 'CGA': 'R', 'UAU': 'Y', 'GAU': 'D', 'CAG': 'Q', 'UUG': 'L', 'AUU': 'I', 'CAC': 'H', 'ACU': 'T', 'CUA': 'L', 'AUG': 'M', 'UUA': 'L', 'GAC': 'D', 'AGG': 'R', 'GUA': 'V', 'UAG': 'Stop', 'GCC': 'A', 'ACC': 'T', 'GGA': 'G', 'CCU': 'P'}

def decode(RNA):
    res = []
    for i in range(0,len(RNA),3):
        DC = D[RNA[i:i+3]]
        if DC=='Stop':
            break
        res.append(DC)
    return ''.join(res)

print(decode(input()))
