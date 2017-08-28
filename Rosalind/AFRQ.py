#!/usr/bin/env python3

from math import sqrt

# Probas de (aa,Aa,AA) pour chaque type de croisement :
#     aa       Aa             AA
# aa (1,0,0)  (1/2,1/2,0)    (0,1,0)
# Aa          (1/4,1/2,1/4)  (0,1/2,1/2)
# AA                         (0,0,1)
# La population est a l'equilibre genetique donc en particulier :
# p(aa) = p(aa)^2 + 2*p(aa)*p(Aa)/2 + p(Aa)^2/4
# D = p(aa)^2 - 4(p(aa)^2-p(aa))/4 = p(aa)
# p(Aa) = (-p(aa)+sqrt(D)) / (2/4)
# et la proba recherchee est p(aa)+p(Aa)

A = list(map(float,input().split()))
B = []
for paa in A:
    pAa = 2*(sqrt(paa)-paa)
    B.append(paa+pAa)
print(' '.join(map(str,B)))
