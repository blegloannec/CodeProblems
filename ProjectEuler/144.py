#!/usr/bin/env python

import matplotlib.pyplot as plt

# si (x0,y0) est un point de l'ellipse, calcule l'autre
def next_inter(x0,y0,dx,dy):
    a = 4*dx*dx + dy*dy
    b = 8*x0*dx + 2*y0*dy
    t = -b/a
    return x0+t*dx,y0+t*dy

# pour le fun, on affiche le resultat
def plot(X,Y):
    plt.axis('scaled')
    plt.axis([-6,6,-11,11])
    plt.plot(X,Y,linewidth=0.2,color='red')
    plt.show()

def main():
    # attention, le pt de depart donne est hors de l'ellipse
    # on utilise le premier point de rebond a la place
    x,y = 1.4,-9.6
    dx,dy = 1.4,-9.6-10.1
    X,Y = [0.,x],[10.1,y]
    cpt = 0
    while not (y>=0 and -0.01<=x<=0.01):
        # vecteur tangent
        ex,ey = y,-4.*x
        # projection normalisee de (dx,dy)
        de = (dx*ex+dy*ey)/(ex*ex+ey*ey)
        # reflexion
        dx -= 2.*de*ex
        dy -= 2.*de*ey
        x,y = next_inter(x,y,dx,dy)
        cpt += 1
        X.append(x)
        Y.append(y)
    print cpt
    plot(X,Y)

main()
