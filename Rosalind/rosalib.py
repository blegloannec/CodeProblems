import sys

D = {'GCU': 'A', 'UGA': 'Stop', 'UUC': 'F', 'AAG': 'K', 'AAA': 'K', 'UCC': 'S', 'GGG': 'G', 'CCG': 'P', 'CGU': 'R', 'UGC': 'C', 'GGC': 'G', 'CCA': 'P', 'AGC': 'S', 'UCG': 'S', 'CCC': 'P', 'UAC': 'Y', 'CUG': 'L', 'AGA': 'R', 'AUA': 'I', 'GAG': 'E', 'UCA': 'S', 'AAC': 'N', 'CUU': 'L', 'CAA': 'Q', 'GGU': 'G', 'UGG': 'W', 'GCG': 'A', 'GUC': 'V', 'ACA': 'T', 'CAU': 'H', 'UCU': 'S', 'CGC': 'R', 'GCA': 'A', 'AUC': 'I', 'GUU': 'V', 'UGU': 'C', 'GAA': 'E', 'UUU': 'F', 'CGG': 'R', 'GUG': 'V', 'ACG': 'T', 'CUC': 'L', 'AAU': 'N', 'AGU': 'S', 'UAA': 'Stop', 'CGA': 'R', 'UAU': 'Y', 'GAU': 'D', 'CAG': 'Q', 'UUG': 'L', 'AUU': 'I', 'CAC': 'H', 'ACU': 'T', 'CUA': 'L', 'AUG': 'M', 'UUA': 'L', 'GAC': 'D', 'AGG': 'R', 'GUA': 'V', 'UAG': 'Stop', 'GCC': 'A', 'ACC': 'T', 'GGA': 'G', 'CCU': 'P'}

#start = 'AUG'

W = {'C': 103.00919, 'F': 147.06841, 'L': 113.08406, 'V': 99.06841, 'I': 113.08406, 'H': 137.05891, 'P': 97.05276, 'R': 156.10111, 'E': 129.04259, 'W': 186.07931, 'Q': 128.05858, 'A': 71.03711, 'T': 101.04768, 'S': 87.03203, 'Y': 163.06333, 'K': 128.09496, 'D': 115.02694, 'M': 131.04049, 'G': 57.02146, 'N': 114.04293}

def parse_fasta():
    I = sys.stdin.readlines()
    J = []
    i = 0
    while i<len(I):
        N = I[i].strip()[1:]
        i += 1
        A = [I[i].strip()]
        i += 1
        while i<len(I) and I[i][0]!='>':
            A.append(I[i].strip())
            i += 1
        J.append((N,''.join(A)))
    return J

def dna2rna(DNA):
    return DNA.replace('T','U')

def rna2prot(RNA, start=0, stop_required=False):
    res = []
    for i in range(start,len(RNA),3):
        C = RNA[i:i+3]
        if C not in D:
            print(C)
            return None
        DC = D[C]
        if DC=='Stop':
            return ''.join(res)
        res.append(DC)
    return None if stop_required else ''.join(res)

def revc(DNA):
    D = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    return ''.join(D[c] for c in reversed(DNA))

def hamming(A,B):
    assert(len(A)==len(B))
    return sum(int(A[i]!=B[i]) for i in range(len(A)))
