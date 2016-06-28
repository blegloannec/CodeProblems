#!/usr/bin/env python3

# en affichant le triangle modulo un nb premier p,
# on remarque une regularite de motif "fractale"
# binom(n,k) n'est pas divisible par p ssi
# ni >= ki pour tout i
# ou ni et ki sont les chiffres dans l'ecriture
# de n et k en base p

# c'est en fait une consequence du theoreme de Lucas
# https://en.wikipedia.org/wiki/Lucas%27_theorem

# algo naif ici
# TODO : prog dyn efficace

def contrib(n):
    c = 1
    while n>0:
        c *= n%7 + 1
        n //= 7
    return c

def main():
    res = 0
    for n in range(10**9):
        res += contrib(n)
    print res

main()
