#!/usr/bin/env python

from fractions import Fraction
#import matplotlib.pyplot as plt

# pour ce pb, il y a un algo de balayage permettant la detection
# d'une collision en O(n*log n), et l'enumeration des collisions
# a la louche en O(n*log n + nb de collisions) (a verifier)

# ceci dit, pour l'enumeration des intersections, dans le pire cas,
# il y en a de toutes facons O(n^2) donc l'algo naif reste "efficace"
# dans le cas d'un ensemble dense, ce qui semble etre le cas ici,
# on se contentera donc de l'algo naif en O(5000^2)
# 37s avec pypy...

# ATTENTION! Les donnees commencent a t1 et pas t0!...
def randgen():
    s = 290797
    T = []
    for _ in xrange(20000):
        s = (s*s)%50515093
        T.append(s%500)
    return T

# pour le fun, on affiche les segments
def plot(T):
    for i in xrange(0,len(T),4):
        X = T[i],T[i+2]
        plt.plot([T[i],T[i+2]],[T[i+1],T[i+3]],linewidth=0.2)
    plt.show()

def true_intersection((x1,y1,x2,y2),(x3,y3,x4,y4)):
    a,b,e = x2-x1,-(x4-x3),x3-x1
    c,d,f = y2-y1,-(y4-y3),y3-y1
    det = a*d-b*c
    if det==0:
        return None
    # Cramer
    t,tp = Fraction(e*d-b*f,det),Fraction(a*f-e*c,det)
    #assert(x1+t*a==x3-tp*b)
    #assert(y1+t*c==y3-tp*d)
    if 0<t<1 and 0<tp<1:
        return (x1+t*a,y1+t*c)
    return None

def main():
    T = randgen()
    #plot(T)
    P = set()
    for a in xrange(5000):
        A = tuple(T[4*a:4*a+4])
        for b in xrange(a+1,5000):
            B = tuple(T[4*b:4*b+4])
            I = true_intersection(A,B)
            if I!=None:
                P.add(I)
    print len(P)

main()
