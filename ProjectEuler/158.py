#!/usr/bin/env python

# Le plus dur est vraiment de comprendre l'enonce !
# Il s'agit de chaines de longueur 2 <= n <= 26 dont
# les caracteres sont {a..z}, soit {0..25}, et tous les
# caractere sont distincts.
# On decoupe chaque chaine en 3 morceaux UVabW, a<b, ou :
#  - U est une chaine decroissante dont les elements sont >b
#  - V est une chaine decroissante dont les elements sont b>x>a
#  - W est une chaine decroissante dont les elements sont <b et
#    n'ont pas ete utilises par V

def binom(n,p):
    if p>n or n<0:
        return 0
    return 1 if p==0 else n*binom(n-1,p-1)/p

def p(n):
    res = 0
    for u in xrange(n-1):
        for v in xrange(n-u-1):
            w = n-u-v-2
            for a in xrange(26):
                for b in xrange(a+1,26):
                    res += binom(25-b,u)*binom(b-a-1,v)*binom(b-v-1,w)
    return res

print max(p(i) for i in xrange(3,27))
