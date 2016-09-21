#!/usr/bin/env python

# Decomposons N! = 2^a * 5^b * C
# Le nb de 0 a la fin de l'ecriture decimale est le
# nb de 10 que l'on peut former, soit min(a,b) = b.
# On cherche donc a calculer 2^(a-b) * C mod 10^5
# Dans C il y a 2 types de facteurs, ceux qui ne sont
# divisibles ni par 2 ni par 5, et les autres.
# Pour les premiers (i.e. en ignorant les seconds), on retrouve
# une periodicite modulo 10^5 :
# on retrouve les memes valeurs modulo 10^5 entre 1 et 10^5,
# qu'entre 10^5+1 et 2*10^5, etc.
# Pour les seconds, comptons ensemble les nombres de la forme
# 2^x*5^y*c avec x et y fixes (et c premier avec 2 et 5).
# Leurs valeurs une fois les facteurs 2 et 5 retires sont exactement
# les nombres c de la premiere categorie, on peut donc facilement
# calculer leur contribution.

# puissance de p dans la decomposition de n!
def fact_power(n,p):
    res = 0
    q = p
    while q<=n:
        res += n/q
        q *= p
    return res

def main():
    N = 10**12
    M = 10**5
    F = [1]
    for a in xrange(1,M):
        if a%2==0 or a%5==0:
            F.append(F[-1])
        else:
            F.append((F[-1]*a)%M)
    # contribution du 2^(a-b)
    res = pow(2,fact_power(N,2)-fact_power(N,5),M)
    # contribution des nombres de la premiere categorie
    res  = (res * pow(F[-1],N/M,M) * F[N%M])%M
    # contributions de la seconde categorie
    X = 1
    for x in xrange(45):
        Y = X
        for y in xrange(20):
            if Y>N:
                break
            if Y>1:
                # contribution des 2^x*5^y*c avec c premier avec 2 et 5
                Z = N/Y
                res = (res * pow(F[-1],Z/M,M) * F[Z%M])%M
            Y *= 5
        X *= 2
    print res

main()
