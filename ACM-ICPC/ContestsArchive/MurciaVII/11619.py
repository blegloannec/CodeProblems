#!/usr/bin/env python3

import sys
from collections import defaultdict

nb_spam = nb_ham = 0
seen_spam = defaultdict(int)
seen_ham = defaultdict(int)

def P(w):
    if w not in seen_spam and w not in seen_ham:
        return 0.4
    PwS = seen_spam[w]/nb_spam if nb_spam>0 else 0.
    PwH = seen_ham[w]/nb_ham if nb_ham>0 else 0.
    p = PwS / (PwS+PwH)
    return max(0.01,min(0.99,p))

def classify(W):
    p1 = p2 = 1.
    for w in W:
        p = P(w)
        p1 *= p
        p2 *= 1-p
    p = p1 / (p1+p2)
    if p>=0.6:
        return 'Spam'
    elif p<=0.4:
        return 'Ham'
    return 'Unsure'

def main():
    global nb_spam,nb_ham
    I = sys.stdin.readlines()
    new = True
    W = []
    for L in I:
        L = L.split()
        if L[0]=='==':
            if t=='CLASSIFY':
                print(classify(W))
            else:
                if t=='HAM':
                    nb_ham += len(W)
                else:
                    nb_spam += len(W)
                for w in W:
                    if t=='HAM':
                        seen_ham[w] += 1
                    else:
                        seen_spam[w] += 1
            new = True
        elif new:
            t = L[1]
            new = False
            W.clear()
        else:
            for w in L:
                W.append(w.lower())

main()
