#!/usr/bin/env python3

# Sur une grille triangulaire, on enchaine les 6 vecteurs :
# a*(0,1) + b*(1,0) + c*(1,-1) + d*(0,-1) + e*(-1,0) + f*(-1,1) = 0
# (a-d)*(0,1) + (b-e)*(1,0) + (c-f)*(1,-1) = 0
# Pour A = a-d, B = b-e, C = c-f, on a donc A = C = -B.

# On remarque par ailleurs que l'on peut contracter un hexagone.
# Si a,d > 1 alors on peut contracter l'hexagone dans la direction (0,1)
# jusqu'a avoir min(a,d) = 1 et de la meme maniere dans les autres directions,
# on peut avoir min(b,e) = 1 et min(c,f) = 1.
# On appelera "minimal" un tel hexagone (compact dans les 3 directions).

# Pour un hexagone minimal, on peut supposer A = C >=0 et B = -A <=0
# et donc d = b = f = 1, mais alors a = e = c = A+1.
# Un hexagone minimal est un "quasi-triangle" et son perimetre est 3A+6.

# On peut facilement enumerer les hexagones minimaux (suivant le param. A)
# et compter le nombres d'hexagones qu'ils engendrent.
# En effet, pour un hexagone minimal de parametre A,
# i.e. (a,b,c,d,e,f) = (A+1,1,A+1,1,A+1,1),
# on engendre les (A+1+dx,1+dy,A+1+dz,1+dx,A+1+dy,1+dz), pour tous dx,dy,dz>=0.
# Modulo les symetries cela revient a considerer dx <= dy <= dz.
# Donc pour un perimetre maximal N, on doit avoir
# 3A+6+2(dx+dy+dz) <= N, i.e. dx+dy+dz <= (N-3A-6)/2.

# On se ramene donc au pb de compter les triplets x<=y<=z avec x+y+z<=K
# ou plus simplement x+y+z = K (on en deduira le resultat par accumulation).
# De facon equivalente, il s'agit du nb de partitions de K en au plus
# 3 morceaux (car on autorise x,y,z nul).
# On peut le calculer en O(3n) par prog. dyn. :
# P(K,M=3) = P(K,M-1) + P(K-M,M)
# (  partitions en <M morceaux
#  + partitions en M morceaux >0, en retirant 1 a tous les morceaux,
#    on se ramene aux partitions en <=M morceaux de K-M)
# Mais il existe aussi une formule explicite que l'on utilise ici.
# cf. http://oeis.org/A001399

N = 55106

P3 = [1]
for n in range(1,N//2):
    P3.append(P3[-1]+int(round((n+3)**2/12)))

def H(N):
    return sum(P3[(N-(3*A+6))//2] for A in range((N-6)//3+1))

print(H(N))
