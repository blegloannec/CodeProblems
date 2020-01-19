#!/usr/bin/env python3

from math import pi, sqrt

G = 32.2 * 12
No = 1

def scenario(UP, D, L, B, P, DOWN, V):
    O = ['Scenario {:d}:'.format(No),
         'up hill {: 18.2f} sec'.format(UP),
         'well diameter {: 12.2f} in'.format(D),
         'water level {: 14.2f} in'.format(L),
         'bucket volume {: 12.2f} cu ft'.format(B),
         'bucket ascent rate {: 7.2f} in/sec'.format(P),
         'down hill {: 16.2f} sec'.format(DOWN),
         'required volume {: 10.2f} cu ft'.format(V)]
    B *= 12**3  # foot -> inch
    V *= 12**3  #
    T = 0.
    DL = B / (pi * (D/2.)**2)
    while V>1e-6:
        T += UP + sqrt(2.*L/G) + L/P + DOWN
        L += DL
        V -= B
    O.append('TIME REQUIRED {: 12.2f} sec'.format(T))
    print('\n     '.join(O))

if __name__=='__main__':
    first = True
    I = input().split()
    while len(I)>1:
        if first:
            first = False
        else:
            print()
        scenario(*map(float,I))
        No += 1
        I = input().split()
