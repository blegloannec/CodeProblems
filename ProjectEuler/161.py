#!/usr/bin/env python

# L'approche dancing links ne fonctionne pas ici (enumeration
# trop longue).

# On utilise une prog dyn selon la frontiere de remplissage
# donnee par la liste des positions entre 0 et 12 sur chacune
# des 9 lignes, ce qui pourrait donner une complexite en O(13^9)
# soit environ 10^10, ce qui est presque abordable...
# Evidemment on va reduire drastiquement cette complexite en
# ne considerant que les frontieres dont l'ecart entre le point le plus
# a gauche et le point le plus a droite est faible, et ce en deconstruisant
# toujours une frontiere a partir de sa premiere ligne la plus large.
# On representera chaque frontiere par un nb en base 16 = 2^4 >= 12 a 9 chiffres.
# Cette approche tourne en 0.7s !

B = 4        # base 2^B
M = (1<<B)-1 # associated mask

def get_max(f):
    m,i = 0,0
    while f>0:
        d = f&M
        if d>m:
            m,imax = d,i
        f >>= B
        i += 1
    return imax,m

def get(f,i):
    return (f>>(B*i))&M

def val(i,v):
    return v<<(B*i)

H = 9 # lines
W = 12 # columns

memo = {0:1}
def count(f):
    if f in memo:
        return memo[f]
    # premiere ligne de valeur maximale
    i,m = get_max(f)
    res = 0
    # X
    # XX  <- i
    if i>0 and m>=2 and get(f,i-1)==m-1:
        res += count(f-val(i-1,1)-val(i,2))
    # XX  <- i
    # X
    if i<H-1 and m>=2 and get(f,i+1)==m-1:
        res += count(f-val(i+1,1)-val(i,2))
    # XX  <- i
    #  X
    if i<H-1 and m>=2 and get(f,i+1)==m:
        res += count(f-val(i,2)-val(i+1,1))
    #  X  <- i
    # XX
    if i<H-1 and m>=2 and get(f,i+1)==m:
        res += count(f-val(i,1)-val(i+1,2))
    # XXX  <- i
    if m>=3:
        res += count(f-val(i,3))
    # X  <- i
    # X
    # X
    if i<H-2 and get(f,i+1)==m and get(f,i+2)==m:
        res += count(f-val(i,1)-val(i+1,1)-val(i+2,1))
    # Combinaisons supplementaires pour examiner tous les
    # cas sans jamais laisser de "trou"
    # XX  <- i
    # XY
    #  Y
    #  Y
    if i<H-3 and m>=2 and get(f,i+1)==m and get(f,i+2)==m and get(f,i+3)==m:
        res += count(f-val(i,2)-val(i+1,2)-val(i+2,1)-val(i+3,1))
    # XX  <- i
    # XY
    # YY
    if i<H-2 and m>=2 and get(f,i+1)==m and get(f,i+2)==m:
        res += count(f-val(i,2)-val(i+1,2)-val(i+2,2))
    memo[f] = res
    return res

# W...W, H fois, en base 2^B
N = 0
for i in xrange(H):
    N |= val(i,W)
print count(N)
