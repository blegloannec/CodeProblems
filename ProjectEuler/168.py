#!/usr/bin/env python

# on genere les nb recherches en "generalisant" un peu la propriete
# appelons "acceptable" un nb n tel qu'il existe 1 <= m <= 9 tel que
# les derniers chiffres de n*m coincident avec int(n/10) (n shifte
# d'un chiffre en base 10)
# Exemples : pour m = 5,
#   57*5 = 285 et 57/10 = 5 est suffixe de 285 donc 57 est acceptable
#   857*5 = 4285 donc 857 est acceptable
#   2857*5 = 14285 donc 2857 est acceptable
#   42857*5 = 214285 donc 42857 est acceptable
#   142857*5 = 714285 est un nb recherche
# tout nb recherche est construit sur une sequence de nb acceptables

L = 100
M = 10**5

# on teste avec m sinon on a quelques doublons dans la generation
# (ie. on teste n*m==r au lieu de r%n==0)
def test(n,k,m):
    r = (n%10)*10**k + n/10
    return n*m==r

def acceptable(m,n=0,k=0):
    for d in xrange(10):
        n0 = d*10**k+n
        if n0/10==(n0*m)%(10**k):
            # n0 acceptable
            if n0>10 and d>0 and test(n0,k,m):
                # n0 recherche
                yield n0
            if n0>0 and k<L-1:
                # on continue avec n0
                for x in acceptable(m,n0,k+1):
                    yield x

def main():
    S = 0
    for m in xrange(1,10):
        for x in acceptable(m):
            S += x
    print S%M

main()
