#!/usr/bin/env python

# Partant de R^n_B^n
# il faut 1+1 + 1+2 + 1+3 + ... + 1+n = n(n+3)/2 etapes
# pour atteindre _(BR)^n
# (les termes vont par 2 : 1 deplacement + k sauts).
# Puis 1+(n-1) + ... + 1+2 + 1+1 + 1 = n(n+1)/2 etapes
# pour atteindre B^n_R^n.
# Soit n(n+2) etapes au total (et on conjecture que c'est optimal).

# on cherche alors les n tels que n(n+2) = k(k+1)/2
# ce qu'on peut reecrire 2(2(n+1))^2 = (2k+1)^2 + 7
# en posant x = 2k+1 impair et y = 2(n+1) pair,
# on a x^2 - 2.y^2 = -7 (equation de Pell generalisee)
# ou autrement dit l'equation diophantienne quadratique
# x^2 - 2.y^2 + 7 = 0 (dont les methodes de resolution sont
# connues mais un peu penibles, en l'occurrence, c'est comme
# Pell classique, mais avec plusieurs solutions fondamentales)
# [Comme a l'instant ou j'ecris ces lignes Sage est toujours
# aussi mal documente et Wolfram Alpha est offline ;), j'ai
# utilise ce solveur : https://www.alpertron.com.ar/JQUAD.HTM]

# solutions fondamentales positives trouvees
XY0 = [(1,2),(5,4)]

def main():
    S = []
    for x0,y0 in XY0:
        sols = []
        x,y = x0,y0
        while len(sols)<40:
            if x%2==1 and y%2==0:
                n = y/2-1
                if n>=1:
                    sols.append(n)
                x,y = 3*x+4*y,2*x+3*y
        S += sols
    S.sort()
    print sum(S[:40])

main()
