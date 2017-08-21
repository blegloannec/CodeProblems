#!/usr/bin/env python3

import rosalib

# O(N^2)
def rev_pal(DNA,m=4,M=12):
    T = {'A':'T','T':'A','C':'G','G':'C'}
    for i in range(len(DNA)):
        for k in range(M//2):
            if i-k<0 or i+k+1>=len(DNA):
                break
            if DNA[i-k]!=T[DNA[i+k+1]]:
                break
            elif 2*(k+1)>=m:
                yield (i-k+1,2*(k+1))

def main():
    L = rosalib.parse_fasta()
    _,DNA = L[0]
    for (p,s) in rev_pal(DNA):
        print(p,s)

main()
