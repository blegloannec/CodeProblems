#!/usr/bin/env python

import sys
from math import *

# P(N) = proba d'avoir collision des dates dans un gp de N personnes
# Dans le cas classique ou l'on ne tient pas compte des annees bissextiles :
# P(N) = 1 - (365*364*...*(365-N+1))/365^N   # 1 - [proba toutes dates distinctes]
# En considerant maintenant que L=N/4 personnes sont nees une annee bissextile :
# 1. aucune d'entre-elles n'est nee le 29/02 avec proba F0 = (365/366)^L
# 2. une seule exactement d'entre-elles est nee le 29/02 avec proba F1 = L*365^(L-1)/366^L
# dans les autres cas (au moins 2 personnes nee le 29/01) il y a collision.
# La formule finale devient alors :
# P'(N) = 1- (F0*P(N) + F1*P(N-1))
# ie 1 - ([0 le 29/02]*[proba classique pour N] + [1 le 29/02]*[proba classique pour N-1])
# Ensuite pour l'efficacite on cherche la solution limite par recherche dichotomique
# mais ce n'est en fait pas vraiment utile vu qu'il n'y a que 70 valeurs avant d'atteindre 0.999.
# Attention simplement au cas particulier de l'input 1.000, pour lequel la solution est 367.

def prod(start,n):
    res = 1.
    for i in xrange(n):
        res *= (start-i)/365.
    return res

def proba(N):
    L = N/4
    return 1.-(((365./366.)**L)*prod(365,N)+(L*(365.**(L-1))/(366.**L))*prod(365,N-1))

def binsearch(P):
    m,M = 2,100
    while m<M:
        mid = (m+M)/2
        if proba(mid)<P:
            m = mid+1
        else:
            M = mid
    return m

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        P = float(sys.stdin.readline())
        if P==1.:
            print 367
        else:
            print binsearch(P)

main()
