#!/sur/bin/env python

# Considerons un chemin sur une grille et une ligne verticale placee
# a la frontiere entre 2 colonnes quelconques.
# On oriente le chemin du superieur gauche a l'inferieur gauche.
# On note a,b,c,d les quatre lignes, on indique par un numero l'ordre
# (suivant l'orientation) des franchissements de la frontiere par le
# chemin (et par x le non franchissement).

# Nomenclature des frontieres possibles :
#   1 2 3 4 5 6 7 0
# a 1 x x 1 1 3 1 x
# b 2 1 x x 2 2 4 x
# c x 2 1 x 3 1 3 x
# d x x 2 2 4 4 2 x
# (0 est la "frontiere" finale)

# Transitions possibles
# T[f] = les frontieres possibles 1 case apres une frontiere f
T = {1:[4,7],2:[4],3:[4,6],4:[1,2,3,5,0],5:[5,1,3,0],6:[6,4],7:[7,4]}

M = 10**8

# prog. dyn. facon diviser pour regner
memo = {}
def path(n,fl=4,fr=0):
    if n==0:
        return int(fl==fr)
    if n==1:
        return int(fr in T[fl])
    if (n,fl,fr) in memo:
        return memo[n,fl,fr]
    nl = n/2
    nr = n-nl
    res = 0
    for fm in xrange(1,8):
        res = (res + path(nl,fl,fm)*path(nr,fm,fr))%M
    memo[n,fl,fr] = res
    return res

print path(10**12)
