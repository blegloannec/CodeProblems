#!/usr/bin/env python3

# fixons c le nb de couleurs
# les chiffres designent les couleurs des 4 coins
# les couleurs 1 et 2 sont fixees

# Type A1
# 13
# 24
# (c-2)(c-3) choix pour 3 et 4
# ((c-2)^2-(c-4))(c-2) remplissages du milieu avec 3 couleurs distinctes
# + (c-4)(c-1) remplissages avec les couleurs hautes et basses identiques

# Type A2 (2 cas symetriques)
# 13 ou 12
# 21    23
# c-2 choix pour 3
# ((c-2)^2-(c-3))(c-2) + (c-3)(c-1) remplissages

# Type A3
# 12
# 21
# aucun choix
# ((c-2)^2-(c-2))(c-2) + (c-2)(c-1) remplissages

# Types B1,B2,B3
# idem A1,A2,A3

# Type B4
# 13
# 22
# c-2 choix pour 3
# ((c-2)(c-1)-(c-3))(c-2) + (c-3)(c-1) remplissages


def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

def N(a,b,c):
    A = 2*(c-2)*(((c-2)**2-(c-3))*(c-2)+(c-3)*(c-1))          # A2
    A += ((c-2)**2-(c-2))*(c-2)+(c-2)*(c-1)                   # A3
    if c>=4:
        A += (c-2)*(c-3)*(((c-2)**2-(c-4))*(c-2)+(c-4)*(c-1)) # A1
    B = A
    B += (c-2)*(((c-2)*(c-1)-(c-3))*(c-2)+(c-3)*(c-1))        # B4
    # c(c-1) choix des 2 premieres couleurs
    # binom() pour le choix des positions des modules
    res = c*(c-1) * binom(a+b,a) * A**a * B**b
    return res

print(N(25,75,1984) % 10**8)
