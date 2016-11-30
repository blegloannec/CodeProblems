#!/usr/bin/env python

from multiprocessing import Pool

# en affichant le triangle modulo un nb premier p,
# on remarque une regularite de motif "fractale"
# binom(n,k) n'est pas divisible par p ssi
# ni >= ki pour tout i
# ou ni et ki sont les chiffres dans l'ecriture
# de n et k en base p

# c'est en fait une consequence du theoreme de Lucas
# https://en.wikipedia.org/wiki/Lucas%27_theorem

# algo naif ici
def contrib(n):
    c = 1
    while n>0:
        c *= n%7 + 1
        n /= 7
    return c

# runs in 1 min 15 with multiprocessed pypy

CORES = 4

def compte(start,step=CORES):
    res = 0
    for n in xrange(start,10**9,step):
        res += contrib(n)
    return res

def main():
    p = Pool(CORES)
    print sum(p.map(compte,range(CORES)))

main()
