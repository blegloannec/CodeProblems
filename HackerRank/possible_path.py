#!/usr/bin/env python3

from fractions import gcd

# clairement les operations preservent PGCD(a,b)
# plus etonnant, la reciproque est vraie !
# l'editorial utilise l'astuce suivante pour le voir :
# tout chemin est reversible donc il suffit de montrer (par une descente
# inductive assez evidente, cf. NB ci-dessous) que tout point (a,b)
# avec g = PGCD(a,b) permet d'atteindre l'un des 4 points (0,+/-g) ou (+/-g,0)
# et ces 4 points etant connectes on peut donc joindre tout
# point (c,d) avec PGCD(c,d) = g

# NB: meme argument que pour le pb "Salary Blues"
# on peut interpreter 1 pas en arriere comme
# 1 premiere etape "naive" du modulo (a%b ou b%a calcule naivement par
# soustractions iterees de b a a ou a a b) de l'algorithme d'euclide

T = int(input())
for _ in range(T):
    a,b,x,y = map(int,input().split())
    print('YES' if gcd(a,b)==gcd(x,y) else 'NO')
