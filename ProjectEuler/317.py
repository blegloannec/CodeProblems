#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,pi
import random
random.seed()

# trajectoire d'une particule en 2D :
# a = (0, -g)
# v = (v0x, -g*t + v0y)
# (x,y) = (v0x*t + x0, -g/2*t^2 + v0y*t + y0)
# impact au sol :
# y = 0 pour t = (v0y+sqrt(v0y^2+2.*g*y0))/g
# equation implicite (pour x0 = 0) :
# y = -g/(2*v0x^2)*x^2 + v0y/v0x*x + y0

# enveloppe en 2D :
# v0y = sqrt(v0^2 - v0x^2)
# y = -g/(2*v0x^2)*x^2 + sqrt(v0^2-v0x^2)/v0x*x + y0
# a x fixe, on cherche a maximiser y en fonction de v0x
# on calcule dy/dv0x et on resout dy/dv0x = 0 (fait avec Sage)
# on arrive a v0x = sqrt(v0^2 - v0x^2)*g*x/v0^2
# soit v0x^2 = (g*x*v0)^2 / (v0^4 + (g*x)^2)
# on en deduit la formule de l'enveloppe (cf hull plus bas)

g = 9.81
y0 = 100.
v0 = 20.


## Plotting for fun ##    
def rand_speed():
    x2 = random.uniform(0.,v0**2)
    y2 = v0**2-x2
    return (random.choice([-1.,1.])*sqrt(x2),sqrt(y2))

# trajectoire parametree d'une particule
def particle((v0x,v0y),t):
    return v0x*t, -g/2*t*t + v0y*t + y0

# formule (non simplifiee) de l'enveloppe
def hull(x):
    x = np.abs(x)
    v0x = np.sqrt((g*x*v0)**2 / (v0**4 + (g*x)**2))
    return -g/(2*v0x**2)*x**2 + np.sqrt(v0**2-v0x**2)*x/v0x + y0

# trace de trajectoires aleatoires
def trace():
    plt.axis([-110.,110.,0.,130.])
    for _ in xrange(40):
        V0 = rand_speed()
        tsol = (V0[1]+sqrt(V0[1]**2+2.*g*y0))/g
        plt.plot(*particle(V0,np.linspace(0.,tsol,100)),linewidth=0.5)
    x = np.linspace(-100.,100.,200)
    plt.plot(x,hull(x),color='blue',linewidth=2.5)
    plt.show()


## Actual resolution ##
# primitive de x -> x*hull(x) (calculee par Sage) :
def int_hull(x):
    return 1./4.*v0**2*x**2/g - 1./8.*g*x**4/v0**2 + 1./2.*x**2*y0

# calcul du volume par rotation autour de l'axe y
# valeur max de x obtenue avec Sage par resolution numerique
# de l'equation hull(x) = 0
print 2.*pi*int_hull(99.08340779)
trace()

