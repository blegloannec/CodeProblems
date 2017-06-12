#!/usr/bin/env python3

import sys
sys.setrecursionlimit(5000)

# la sequence qu'on veut sommer
# http://oeis.org/A022843
# c'est la sequence de Beatty associee a e irrationnel
# la difference entre 2 termes est 2 ou 3
# la sequence des differences entre 2 termes consecutifs
# est une sequence sturmienne aperiodique

# la fraction continue de e
# http://oeis.org/A003417
# e = [2 ; 1,2,1,1,4,1,1,6,1,1,8,1,1,10,1,1,12,1,1,14,...]

# http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/words/word_generators.html
# https://en.wikipedia.org/wiki/Sturmian_word
# Pour la fraction [0 ; d1+1,d2,d3,...], le mot sturmien associe est
# la limite de s(0) = 1, s(1) = 0, s(n+1) = s(n)^dn.s(n-1)
# ici on remplace l'initialisation par 3 et 2 car 2 < e < 3

# si Sinf est le mot limite, la somme a calculer est simplement
# sum( Sinf_i * (n-i), 0<=i<n)
# on peut la voir comme un "triangle" donc la ligne i de taille n-i
# porte la valeur Sinf_i
# ce triangle a une structure recursive induite par celle des s(i)
# par exemple le triangle T(k) de rang k (correspondant a s(k)) est de la forme
#                              T(k-2)
#                      T(k-1) B'(k-1)
#               T(k-1) B(k-1) B'(k-1)
#        T(k-1) B(k-1) B(k-1) B'(k-1)
# T(k-1) B(k-1) B(k-1) B(k-1) B'(k-1)
# avec autant de fois T(k-1) que dk et ou les B(k-1) sont des blocs carres |s(k-1)|^2
# et les B'(k-1) des blocs |s(k)| x |s(k-2)| portant les memes valeurs sur les lignes que T(k-1)
# cela donne lieu a une prog. dyn. pour calculer les sommes
# pour calculer la somme au rang n, on calcule le rang k tel que |s(k)|>=n et on
# utilise la structure recursive pour calculer la somme des n premieres colonnes de T(k)

# NB : similaire au PE 325 (ici le calcul est un peu plus simple mais la structure recursive plus
#      compliquee)

# pour l'initialisation
from math import e
def E(n):
    return(int(n*e))

# coefficients de la fraction continue
def cf(n):
    if n==0:
        return 0
    elif n%3==1:
        return 2*(n//3+1)
    return 1

# tailles et sommes des mots s(n)
Size = [1,1]
Sums = [3,2]
for i in range(5000):
    d = cf(i)
    Size.append(d*Size[-1] + Size[-2])
    Sums.append(d*Sums[-1] + Sums[-2])

memo = {}
def _ST(k,n):
    if k<=3:
        return sum(E(i)-2 for i in range(1,n+1))
    if (k,n) in memo:
        return memo[k,n]
    #assert(Size[k]==Size[k-1]*cf(k-2)+Size[k-2])
    #assert(n<=Size[k])
    d = cf(k-2)
    x,y = n//Size[k-1],n%Size[k-1]
    #assert(x<=d)
    res = (x-1)*x//2 * Sums[k-1]*Size[k-1] + y*x*Sums[k-1] + x*_ST(k-1,Size[k-1])
    if x<d:
        res += _ST(k-1,y)
    else:
        res += _ST(k-2,y)
    memo[k,n] = res
    return res

def ST(n):
    k = 0
    while Size[k]<n:
        k += 1
    return 2*n + _ST(k,n)

print(ST(int(input())))
