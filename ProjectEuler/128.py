#!/usr/bin/env python

import random
random.seed()

# On note que si un point n est sur l'interieur d'une arete de
# son hexagone de rayon r, alors ses voisins sont :
#  - n-1 et n+1 alignes sur l'hexagone (differences 1)
#  - 2 valeurs consecutives de l'hexagone de rayon r-1 cote interieur
#  - 2 valeurs consecutives de l'hexagone de rayon r+1 cote exterieur
# on a donc au plus 2 differences impaires > 1 et la difference 2,
# qui ne pourrait apparaitre que proche du centre, n'apparait jamais
# donc dans ce cas PD(n) <= 2 !

# + Cas particulier du dernier point de chaque hexagone
# pour lequel on doit a priori considerer 5 voisins (tous sauf le n-1)

# Si maintenant un point n est un sommet de
# son hexagone de rayon r, alors ses voisins sont :
#  - n-1 et n+1 sur l'hexagone (differences 1)
#  - 3 valeurs consecutives de l'hexagone de rayon r+1 cote exterieur
#    centrees sur le sommet correspondant de l'hexagone r+1
#  - le sommet correspondant de l'hexagone de rayon r-1 cote interieur
# on a donc au plus 3 differences impaires > 1 avec les 2 extremes
# des valeurs exterieures et la valeur interieure
# NB a posteriori : il semblerait qu'on n'atteigne en fait
# jamais 3 dans ce cas (mais il faudrait faire une analyse plus
# poussee pour le prouver)...

# + Cas particulier du premier sommet de chaque hexagone
# pour lequel on doit a priori considerer 5 voisins (tous sauf le n+1)

# les points des sommets 0<=k<6 sont les :
# 3n(n+1)+k(n+1)+2

def s(n,k):
    return 3*n*(n+1)+k*(n+1)+2

# Miller-Rabin
def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n):
    b = digits(n-1,2)
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s=15):
    for j in xrange(s):
        if witness(random.randint(1,n-1),n):
            return False
    return True

def prd(a,b):
    return miller_rabin(abs(a-b))

def main():
    # les 2 premiers elements sont des cas particuliers
    # de debut qu'on n'enumere pas
    cpt = 2
    n = 1
    N = 2000
    while True:
        # premier sommet
        p = s(n,0)
        pv = 0
        for v in [s(n-1,0),s(n+1,0)-1,s(n+1,0),s(n+1,0)+1,s(n+2,0)-1]:
            if prd(p,v):
                pv += 1
        if pv==3:
            cpt += 1
            #print cpt,p
            if cpt==N:
                print p
                return
        # 5 autres sommets (a posteriori inutile)
        #for k in xrange(1,6):
        #    p = s(n,k)
        #    p1 = s(n+1,k)
        #    if prd(p,p1-1) and prd(p,p1+1) and prd(p,s(n-1,k)):
        #        cpt += 1
        #        print cpt,p
        #        if cpt==N:
        #            print p
        #            return
        # dernier point
        p = s(n+1,0)-1
        pv = 0
        for v in [s(n-1,0),s(n,0)-1,s(n,0),s(n+2,0)-2,s(n+2,0)-1]:
            if prd(p,v):
                pv += 1
        if pv==3:
            cpt += 1
            #print cpt,p
            if cpt==N:
                print p
                return
        n += 1

main()
