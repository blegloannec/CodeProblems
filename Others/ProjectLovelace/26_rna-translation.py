# see also: http://rosalind.info/problems/prot/

cod2aa = {'GCU': 'A', 'UGA': 'Stop', 'UUC': 'F', 'AAG': 'K', 'AAA': 'K', 'UCC': 'S', 'GGG': 'G', 'CCG': 'P', 'CGU': 'R', 'UGC': 'C', 'GGC': 'G', 'CCA': 'P', 'AGC': 'S', 'UCG': 'S', 'CCC': 'P', 'UAC': 'Y', 'CUG': 'L', 'AGA': 'R', 'AUA': 'I', 'GAG': 'E', 'UCA': 'S', 'AAC': 'N', 'CUU': 'L', 'CAA': 'Q', 'GGU': 'G', 'UGG': 'W', 'GCG': 'A', 'GUC': 'V', 'ACA': 'T', 'CAU': 'H', 'UCU': 'S', 'CGC': 'R', 'GCA': 'A', 'AUC': 'I', 'GUU': 'V', 'UGU': 'C', 'GAA': 'E', 'UUU': 'F', 'CGG': 'R', 'GUG': 'V', 'ACG': 'T', 'CUC': 'L', 'AAU': 'N', 'AGU': 'S', 'UAA': 'Stop', 'CGA': 'R', 'UAU': 'Y', 'GAU': 'D', 'CAG': 'Q', 'UUG': 'L', 'AUU': 'I', 'CAC': 'H', 'ACU': 'T', 'CUA': 'L', 'AUG': 'M', 'UUA': 'L', 'GAC': 'D', 'AGG': 'R', 'GUA': 'V', 'UAG': 'Stop', 'GCC': 'A', 'ACC': 'T', 'GGA': 'G', 'CCU': 'P'}

aa2long = ('Ala', None, 'Cys', 'Asp', 'Glu', 'Phe', 'Gly', 'His', 'Ile', None, 'Lys', 'Leu', 'Met', 'Asn', None, 'Pro', 'Gln', 'Arg', 'Ser', 'Thr', None, 'Val', 'Trp', None, 'Tyr', None)

def amino_acid_sequence(rna):
    res = []
    for i in range(0, len(rna), 3):
        aa = cod2aa[rna[i:i+3]]
        if aa=='Stop':
            break
        res.append(aa2long[ord(aa)-ord('A')])
    return ''.join(res)

if __name__=='__main__':
    print(amino_acid_sequence('CCU'))
    print(amino_acid_sequence('AUGCCAAAGGGUUGA'))
    print(amino_acid_sequence('GCAAGAGAUAAUUGU'))
