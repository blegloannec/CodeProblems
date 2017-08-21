#!/usr/bin/env python3

import rosalib

# pretty naive and lazy approach here, yet good enough
# (for sure there are more efficient and still relatively simple
#  approaches using string hashing)
# see also https://en.wikipedia.org/wiki/Longest_common_substring_problem
# for a really good approach using suffix trees

def LCSub(DNAS):
    L0 = len(DNAS[0])
    for k in range(L0,-1,-1):
        for i in range(L0-k+1):
            P = DNAS[0][i:i+k]
            if all(DNAS[j].find(P)>=0 for j in range(1,len(DNAS))):
                return P

DNAS = sorted((DNA for _,DNA in rosalib.parse_fasta()), key=len)
print(LCSub(DNAS))
