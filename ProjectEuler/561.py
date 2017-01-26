#!/usr/bin/env python

# fixons n
# notons S' la meme chose que S pour des diviseurs
# non necessairement distincts
# S(n) = S'(n) - nb_div(n)
# notons C(m) = S'((p_m#)^n)
# On obtient C(m+1) en multipliant les couples de
# C(m) par des (p^a,p^b) 0<=a<=b<=n ou p est le m+1 ieme
# nb premier, donc C(m+1) = C(m) * (n+1)(n+2)/2
# ie C(m) = ((n+1)(n+2)/2)^m
# et nb_div((p_m#)^n) = (n+1)^m
# d'ou S((p_m#)^n) = ((n+1)(n+2)/2)^m - (n+1)^m
# 1. si n est impair, alors n+1 est pair, n+2 est impair
# dans ce cas (n+1)^m/2^m est entier et l'on a
# S((p_m#)^n) = ((n+1)/2)^m * (n+2)^m - (n+1)^m
#             = ((n+1)/2)^m * ((n+2)^m - 2^m)
# le second facteur est impair donc la valuation est (val2(n+1)-1)*m
# 2. si n est pair, on a cette fois (n+2)/2 entier et
# S((p_m#)^n) = (n+1)^m * (((n+2)/2)^m - 1)
# 2.1. si (n+2)/2 est pair (ie. n = 2 mod 4), alors les 2 facteurs sont impairs
# donc valuation 0
# 2.2. sinon le second facteur est pair et il faut evaluer sa valuation
# n = 0 mod 4 donc ecrivons n = 4k, (n+2)/2 = 2k+1
# on cherche la valuation de
# (2k+1)^m - 1 = (2k+1 - 1) * (1+(2k+1)+(2k+1)^2+...+(2k+1)^(m-1))
# si m est impair (cas du pb), le second terme est une somme impaire de
# termes impairs, donc est impair, donc la valuation est val2(2k) = val2(n/2)
# (si m est pair, on ne sait pas et on s'en fiche ici, mais on conjecture
# empiriquement que la valuation est val2((n+5)/8)+5)
# Finalement, si n pair, la valuation est toujours val2(n)-1

m = 904961 # odd
N = 10**12

s = 0
v,p2 = 2,4
while p2<=N:
    np2 = p2<<1
    nb = N/p2 - N/np2
    s += nb*(v-1)*(m+1)
    v += 1
    p2 = np2
print s
