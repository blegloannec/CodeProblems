#!/usr/bin/env python3

from math import *

# Calculer l'enveloppe convexe des points.
# "Dilater" l'enveloppe en gonflant ses points en des cercles de rayon R = 3.
# Cela ne change pas la longueur des segments de l'enveloppe mais ajoute
# la longueur des arcs de cercle en chacun des points. L'angle total forme
# par ces arcs vaut 2pi (tour complet exterieur, independant du nb de points
# de l'enveloppe, contrairement a la somme des angles interieurs valant (k-2)pi
# pour un polygone convexe a k sommets), donc la longueur totale ajoutee
# est 2pi*R.

R = 3
L = 5

def left_turn(a,b,c):
    return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0]) > 0

def andrew(S):
    S.sort()
    top = []
    bot = []
    for p in S:
        while len(top)>=2 and not left_turn(p,top[-1],top[-2]):
            top.pop()
        top.append(p)
        while len(bot)>=2 and not left_turn(bot[-2],bot[-1],p):
            bot.pop()
        bot.append(p)
    return bot[:-1]+top[:0:-1]

def dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def main():
    N = int(input())
    P = [tuple(map(int,input().split())) for _ in range(N)]
    H = andrew(P)
    d = sum(dist(H[i],H[(i+1)%len(H)]) for i in range(len(H))) + 2*pi*R
    print(ceil(d/L))

main()
