#!/usr/bin/env python3

from math import sqrt

# soit C le point de depart du ballon de vitesse Sc
# soit H le point du panier
# soit 0 <= l <= 1 parametrant la position du ballon B(l) le segment [CH]
# notons P la position initiale d'un adversaire de vitesse Sp
# l'adversaire peut intercepter la balle ssi
# il existe 0 < l < 1 tel que PB(l) / Sp <= CB(l) / Sc
# (ie l'adversaire atteint le point B(l) sur la trajectoire avant la balle)

# on a B(l) = (Xc+(Xh-Xc)*l,Yc+(Yh-Yc)*l)
# CB(l)^2 = ((Xh-Xc)*l)^2 + ((Yh-Yc)*l)^2
# PB(l)^2 = (Xc+(Xh-Xc)*l - Xp)^2 + (Yc+(Yh-Yc)*l - Yp)^2
#         = (Xh-Xc)^2*l^2 + 2*(Xh-Xc)*(Xc-Xp)*l + (Xc-Xp)^2 + (Yh-Yc)^2*l^2 + 2*(Yh-Yc)*(Yc-Yp)*l + (Yc-Yp)^2
# on veut  PB(l)^2 * Sc^2 <= CB(l)^2 * Sp^2
# ie (((Xh-Xc)^2+(Yh-Yc)^2)*l^2 + 2*((Xh-Xc)*(Xc-Xp)+(Yh-Yc)*(Yc-Yp))*l + ((Xc-Xp)^2 + (Yc-Yp)^2)) * Sc^2 <= ((Xh-Xc)^2+(Yh-Yc)^2)*l^2 * Sp^2
# CH^2*(Sc^2-Sp^2)*l^2 + 2*((Xh-Xc)*(Xc-Xp)+(Yh-Yc)*(Yc-Yp))*Sc^2*l + CP^2*Sc^2 <= 0

def shoot(Xh,Yh,Xc,Yc,Sc,P):
    for (Xp,Yp,Sp) in P:
        A = ((Xh-Xc)**2+(Yh-Yc)**2)*(Sc**2-Sp**2)
        B = 2*((Xh-Xc)*(Xc-Xp)+(Yh-Yc)*(Yc-Yp))*Sc**2
        C = ((Xc-Xp)**2+(Yc-Yp)**2)*Sc**2 # toujours >= 0
        if A==0:
            if B<0 and -C/B<1: # interception possible pour -C/B <= l < 1
                return False
            continue
        D = B**2-4*A*C
        if D<0: # le joueur ne peut rien faire
            continue
        else:
            # on espere ne pas avoir de pb avec la precision flottante
            l1,l2 = (-B-sqrt(D))/(2*A),(-B+sqrt(D))/(2*A)
            l1,l2 = min(l1,l2),max(l1,l2) # car A peut etre negatif
            # si A>0, il faut l1<=l<=l2 pour intercepter la balle
            # si A<0, il faut l<=l1 ou l>=l2 pour intercepter la balle
            if (A>0 and not (l1>=1 or l2<0)) or (A<0 and l2<=1):
                return False
    return True

def main():
    T = int(input())
    for _ in range(T):
        Xh,Yh = map(int,input().split())
        Xc,Yc,Sc = map(int,input().split())
        P = []
        for _ in range(5):
            Xp,Yp,Sp = map(int,input().split())
            P.append((Xp,Yp,Sp))
        print('YES' if shoot(Xh,Yh,Xc,Yc,Sc,P) else 'NO')

main()
