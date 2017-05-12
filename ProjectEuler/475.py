#!/usr/bin/env python

# Soit X43(n) = le nb de repartitions des 12n personnes en 4n groupes de 3
#               sans que deux personnes n'appartiennent precedemment au meme
#               gp de 4 (pour une repartition initiale en 3n groupes de 4 fixee)
# Soit X34(n) = la meme chose en echangeant 3 et 4, i.e. le nb de repartitions
#               en gp de 4 partant de gp de 3
# Ces 2 valeurs se calculent par une prog. dyn. identique
# DP43(n4,n3,n2,n1) = nb de repartitions *ordonnees* en gp de 3 partant de
#                     n4 gp de 4, n3 gp de 3 (i.e. les gp de 4 dont on a
#                     deja precedemment utilise un membre), n2 gp de 2 et
#                     n1 gp de 1
# X43(n) = DP43(3n,0,0,0) / (4n)!
# (on divise par la factorielle du nb de gp pour eliminer l'ordre)
# X34(n) se calcule de la meme facon mais avec seulement 3 parametres
# donc en O((4n)^3) au lieu de O((3n)^4)
# pour Rk(n) = le nb de repartitions de 12n personnes en gp de k
#            = (12n)! / (((12/k)n)! * (k!)^((12/k)n))
# on a la relation
# R4(n) * X43(n) = R3(n) * X34(n)
# ce qui permet de deduire immediatement X43 connaissant X34, ce dernier
# s'obtenant avec une prog. dyn. en ^3 au lieu de ^4.

# runs in 4s with pypy (contre ~2 min pour un calcul direct de X43)

# enumeration naive des (a,b,c) tq a+b+c = 4
T34 = []
for a in xrange(5):
    for b in xrange(5):
        for c in xrange(5):
            if a+b+c==4:
                T34.append((a,b,c))

P = 10**9+7

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n=P):
    return bezout(a,n)[1]

N = 50  # 12*50 = 600

# pre-calcul des factorielles et leurs inverses
F,Finv = [1],[1]
for n in xrange(1,4*N+1):
    F.append((F[-1]*n)%P)
    Finv.append(inv_mod(F[-1]))

def binom(n,p):
    return (F[n]*(Finv[p]*Finv[n-p])%P)%P

memo = {(0,0,0):1}
def dp34(n3,n2=0,n1=0):
    if (n3,n2,n1) in memo:
        return memo[n3,n2,n1]
    res = 0
    for (d3,d2,d1) in T34:
        if d3<=n3 and d2<=n2 and d1<=n1:
            res = (res + pow(3,d3,P)*(binom(n3,d3)*(pow(2,d2,P)*(binom(n2,d2)*(binom(n1,d1)*dp34(n3-d3,n2-d2+d3,n1-d1+d2))%P)%P)%P)%P)%P
    memo[n3,n2,n1] = res
    return res

def f(n):
    return (dp34(4*n)*pow(F[4],3*n,P)*pow(Finv[3],4*n,P)*Finv[4*n])%P

print f(N)
