#!/usr/bin/env python3

# il y a exactement 25 nombres premiers entre 1 et 100
# 22 deplaces, 3 a leur place

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

def fact(n):
    return 1 if n<=1 else n*fact(n-1)

# fixons les 3 nb premiers a leur place
# comptons alors par inclusion-exclusion le
# nb de permutations des 97 autres nombres
# telles qu'aucun des 22 nb premiers restants
# soient a leur place
res = 0
for i in range(23):
    # pour chaque ensemble de i parmi 22 premiers
    # on ajoute/retire le nb de permutations fixant
    # ces i premiers
    res += (1-2*(i%2))*binom(22,i)*fact(97-i)
# choix possibles pour les 3 fixes / nb total de permutations
res *= binom(25,3)/fact(100)
print('%.12f' % res)
