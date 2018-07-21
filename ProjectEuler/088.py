#!/usr/bin/env python

# La solution pour k est :
# - >= k car la somme vaut au moins k*1
# - <= 2k car (k-2)*1 + 2 + k = 1^(k-2) * 2^1 * k^1

# Si p = a1 * ... * ak et s = a1 + ... + ak et p >= s
# alors p est un sum-prod number d'ordre k+p-s
# en completant s avec (p-s) 1
# Si p>s en revanche on ne pourra jamais rien faire de
# p (car p restera plus grand que s quoi qu'on fasse)
# Inutile donc de considerer donc les 1 dans l'enumeration
# des decompositions, on les obtient avec cette remarque
# Cela permet de limiter considerablement la profondeur de
# l'enumeration

# on considerera l'enumeration des facteurs dans l'ordre croissant
# (role de a0 dans loop)

K = 12000
M = [2*k for k in xrange(K+1)]
M[1] = 0 # car k>=2 dans le pb
MMAX = M[-1]

def loop(k=0,p=1,s=0,a0=2):
    # ordre du sum-prod p obtenu en completant s
    # avec des 1 pour atteindre p
    k0 = k+p-s
    if k0<=K:
        if p<M[k0]:
            M[k0] = p
        # MMAX/p borne valable sur le prochain facteur
        for a in xrange(a0,MMAX/p):
            loop(k+1,p*a,s+a,a)

def main():
    loop()
    print sum(set(M))

main()
