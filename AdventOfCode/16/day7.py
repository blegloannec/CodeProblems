#!/usr/bin/env python

import sys

def tls(S):
    res = False
    brack = False
    for i in xrange(len(S)-3):
        if S[i] in ['[',']']:
            brack = not brack
        elif (S[i]!=S[i+1] and S[i]==S[i+3] and S[i+1]==S[i+2]):
            if brack:
                return False
            res = True
    return res

def ssl(S):
    aba,bab = set(),set()
    brack = False
    for i in xrange(len(S)-2):
        if S[i] in ['[',']']:
            brack = not brack
        elif (S[i]!=S[i+1] and S[i]==S[i+2]):
            if brack:
                if S[i+1]+S[i]+S[i+1] in aba:
                    return True
                bab.add(S[i:i+3])
            else:
                if S[i+1]+S[i]+S[i+1] in bab:
                    return True
                aba.add(S[i:i+3])
    return False

def main():
    cpt1,cpt2 = 0,0
    for L in sys.stdin.readlines():
        L = L.strip()
        if tls(L):
            cpt1 += 1
        if ssl(L):
            cpt2 += 1
    print cpt1
    print cpt2

main()
