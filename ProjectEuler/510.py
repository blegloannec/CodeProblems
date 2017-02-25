#!/usr/bin/env python3

from math import sqrt
from fractions import gcd

# On ne considere dans un premier temps que 2 cercles
# tels que ceux de l'enonce, par exemple ceux de
# centres A et B (ou A et C, ou C et B).
# fixons xA = 0 et yA = rA
# on aura AB = rA+rB et yB = rB
# AB^2 = (xB-xA)^2 + (yB-yA)^2
#      = xB^2 + (rB-rA)^2
#      = xB^2 + rB^2 - 2*rA*rB + rA^2
# et AB^2 = (rA+rB)^2 = rA^2 + 2*rA*rB + rB^2
# donc xB^2 = 4*rA*rB

# Revenons au pb en choisissant maintenant xC = 0.
# Alors on a xA<0 et xA^2 = 4*rA*rC par le calcul precedent
# ainsi que xB>0 et xB^2 = 4*rB*rC
# Mais alors :
# AB^2 = (rA+rB)^2 = rA^2 + 2*rA*rB + rB^2
# AB^2 = (xB-xA)^2 + (yB-yA)^2
#      = xB^2 - 2*xA*xB + xA^2 + rA^2 - 2*rA*rB + rB^2
#      = 4*rB*rC + 8*sqrt(rA*rB)*rC + 4*rA*rC + rA^2 - 2*rA*rB + rB^2
# D'ou rC * (rA + rB + 2*sqrt(rA*rB)) = rA*rB avec rA*rB un carre.

# Au passage, c'est un cas particulier du th. de Descartes
# (pour un des cercles de rayon infini, courbure 0)
# https://en.wikipedia.org/wiki/Descartes'_theorem

# On note que si (rA,rB,rC) est un triplet solution, clairement
# tout (k*rA,k*rB,k*rC) est egalement solution, donc on peut
# supposer rA, rB et rC p-e-e globalement.
# Posons g = gcd(rA,rB), rA = g*rA' et rB = g*rB'
# g^2*rA'*rB' = rA*rB est un carre, rA' et rB' sont p-e-e
# donc rA' et rB' sont des carres, rA' = sA'^2 et rB' = sB'^2
# on a rC * g * (sA'+sB')^2 = g^2 * (sA'*sB')^2
# (sA'+sB')^2 et (sA'*sB')^2 sont p-e-e car sA'+sB' et sA'*sB' le sont
# Donc g divise rC et donc g = 1 sinon cela contredirait le fait que
# rA, rB et rC soient p-e-e globalement.
# Donc rA et rB sont p-e-e et sont des carres.

# sA+sB <= 2*sqrt(10^9) abordable --> solution naive
# (mais on devrait pouvoir faire mieux en arrivant a une solution parametree
#  par sA et sB p-e-e)
# runs in ~7s with pypy

N = 10**9
R = int(sqrt(N))
S = 0
for sApsB in range(1,2*R+1):
    sApsB2 = sApsB*sApsB
    # on veut rA <= rB <= N
    # donc sA <= sApsB/2
    # et sApsB-sA <= sqrt(N)
    # ie sA >= sApsB-sqrt(N)
    for sA in range(max(1,sApsB-R),sApsB/2+1):
        sB = sApsB-sA
        if (sA*sB)%sApsB==0:
            rA,rB = sA*sA,sB*sB
            rC = (rA*rB)//sApsB2
            if gcd(rA,gcd(rB,rC))==1:
                k = N//rB
                S += (rA+rB+rC)*k*(k+1)/2
print(S)
