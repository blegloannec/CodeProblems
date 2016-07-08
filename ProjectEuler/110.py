#!/usr/bin/env python

# cf pb 108
# On remarque que x,y > 0 donc x,y > n
# On peut reecrire X = x-n > 0 et Y = y-n > 0
# 1/(X+n) + 1/(Y+n) = 1/n
# <=> n(2n+X+Y) = (X+n)(Y+n)
# <=> n^2 = XY
# On a dont autant de solutions (X,Y) que de diviseurs de n^2
# carre <=> nb impair de diviseurs
# Comme on veut eliminer la symetrie X/Y, il faut faire attention
# a la solution (n,n)
# nb sol = ((nb div de n^2)-1)/2 + 1

# le crible ne sera pas assez efficace cette fois
# si n = p1^a1..pk^ak
# alors le nb de diviseurs est (a1+1)*...*(ak+1)
# si l'on veut minimiser n a nb de diviseurs constant, on peut commencer par
# choisir les pi les plus petits possibles 2,3,5,7,... dans l'ordre
# puis ranger les ai dans l'ordre decroissant, afin que le plus grand ai
# soit sur le plus petit pi

# si on a k facteurs premiers distincts, alors on a
# au moins 3^k diviseurs du carre, donc ~3^k/2 solutions
# donc on aura k<=15

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
nblim = 2*(4*10**6-1)+1

def loop(p=0,amax=10,n=1,nbdiv=1):
    if p<len(P):
        for a in xrange(1,amax+1):
            n *= P[p]
            nb = nbdiv*(2*a+1)
            if nb>=nblim:
                yield n
                break
            else:
                for x in loop(p+1,a,n,nb):
                    yield x

print min(loop())
