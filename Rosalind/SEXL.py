#!/usr/bin/env python3

# Par hypothese, la distribution des alleles sur les chromosomes X
# portes par des hommes est la meme que sur les chromosomes X portes
# par des femmes.
# On connait p(a) la proba qu'un chromosome X porte l'allele "a" recessif.
# Une femme est "carrier", i.e. porteuse saine, si elle a un genotype "Aa"
# sur ses deux chromosomes X.
# p(Aa) = 2*p(a)*p(A) = 2*p(a)*(1-p(a))

A = map(float,input().split())
B = [2*a*(1-a) for a in A]
print(' '.join(map(str,B)))
