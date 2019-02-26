#!/usr/bin/env python3

from collections import defaultdict

def parse_compound(C,i):
    assert C[i]=='('
    Elems, elem = defaultdict(int), None
    i += 1
    while C[i]!=')':
        if C[i]=='(':
            i,SubElems = parse_compound(C,i)
            for e,c in SubElems:
                Elems[e] += c
        elif 'A'<=C[i]<='Z':
            if elem is not None:
                Elems[elem] += max(1,count)
            elem, count = C[i], 0
            i += 1
        elif '0'<=C[i]<='9':
            count = 10*count + ord(C[i])-ord('0')
            i += 1
        else:
            elem += C[i]
            i += 1
    Elems[elem] += max(1,count)
    i += 1
    mult = 0
    while i<len(C) and '0'<=C[i]<='9':
        mult = 10*mult + ord(C[i])-ord('0')
        i += 1
    if mult>1:
        for e in Elems:
            Elems[e] *= mult
    comp = (lambda e: e[0])
    if 'C' in Elems:
        comp = (lambda e: 'A' if e[0]=='C' else 'AA' if e[0]=='H' else e[0])
    return i, sorted(Elems.items(), key=comp)

def hill(C):
    return parse_compound('('+C+')',0)[1]

if __name__=='__main__':
    N = int(input())
    C = sorted(hill(input()) for _ in range(N))
    C = [C[i] for i in range(N) if i==0 or C[i]!=C[i-1]]
    for X in C:
        print(''.join(e+(str(c) if c>1 else '') for e,c in X))
