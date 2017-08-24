#!/usr/bin/env python3

from collections import Counter

# cf RSTR pour le calcul de proba

n = int(input())
A = input()
B = list(map(float,input().split()))
C = Counter(A)
CG,CA = C['C']+C['G'],C['A']+C['T']
k = n-len(A)+1  # nb de positions possibles pour A dans une chaine de taille n
E = [k * (x/2)**CG * ((1-x)/2)**CA for x in B]
print(' '.join(map(str,E)))
