#!/usr/bin/env python3

import sys, re
from urllib.request import urlopen

DB_URL = 'http://www.uniprot.org/uniprot/'
pattern = re.compile('N[^P][ST][^P]')

def get_prot(ID):
    X = urlopen(DB_URL+ID+'.fasta').read().decode('utf-8').split('\n')
    return ''.join(X[1:])

# re.finditer does not find overlapping occurrences
# you can either use a lookahead pattern
# https://stackoverflow.com/questions/3027718/overlapping-matches-with-finditer-in-python#3027785
# or manually restart the search at the right position as we do here
def findall(S,pattern):
    p = pattern.search(S)
    while p!=None:
        yield p.start()
        p = pattern.search(S,p.start()+1)

def main():
    for ID in sys.stdin.readlines():
        ID = ID.strip()
        P = get_prot(ID)
        pos = [p+1 for p in findall(P,pattern)]
        if pos:
            print(ID)
            print(' '.join(map(str,pos)))

main()
