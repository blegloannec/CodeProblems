#!/usr/bin/env python

# https://oeis.org/A030101
# https://oeis.org/A239447
# (using the latter would be pure cheat, the sequence
#  seems to be in the OEIS only because of this PE problem,
#  and it explicitely gives a solution?!)

# Approche 1 :
# on a une bijection sur les nb impairs de taille n en binaire
# et une bijection entre les nb pairs de taille n (en binaire)
# et les nb impairs de taille <= n-1 (car pour chaque tel nb impair,
# la seule maniere de l'obtenir est de le retourner et de le
# completer avec des 0 jusqu'a la taille n)
# le pb reste donc de trouver la somme des miroirs des nb impairs
# entre 2^58 et 3^37... Et pour ca ?...

# Approche 2 : suggeree par l'enonce, sommer la relation de recurrence
# Tout d'abord, f(2n) = f(n) => f(4n) = f(n) et f(4n+2) = f(2n+1)
# Posons de plus pour simplifier f(0) = 0 et S(n) = sum( f(i), i=0..n )
# Alors, pour tout n et r<4,
# S(4n+r) =   sum( f(4i), i=0..n )   + sum( f(4i+1), i=0..n1 )
#           + sum( f(4i+2), i=0..n2) + sum( f(4i+3), i=0..n3 )
# ou n_j, pour 1 <= j <= 3, vaut n si r>=j et n-1 sinon
#         = sum( f(i), i=0..n ) + sum( 2f(2i+1)-f(i), i=0..n1 )
#           + sum( f(2i+1), i=0..n2) + sum( 3f(2i+1)-2f(i), i=0..n3 )
# posons T(n) = sum( f(2i+1), i=0..n )
#        = S(n) + 2T(n1) - S(n1) + T(n2) + 3T(n3) - 2S(n3)
# reste a exprimer T en fonction de S, pour ca on remarque que
# S(2n+1) = sum( f(2i), i=0..n ) + sum( f(2i+1), i=0..n )
#         = sum( f(i), i=0..n ) + T(n)
#         = S(n) + T(n)
# donc T(n) = S(2n+1) - S(n)
# avec une exception, pour n=1, T(n) = f(1)+f(3) = 4, mais cette
# formule donne S(3)-S(1) = 5, d'ou le -1 dans ce qui suit
# d'ou S(4n+r) = S(n) + 2S(2n1+1) - 2S(n1) - S(n1)
#                + S(2n2+1) - S(n2) + 3S(2n3+1) - 3S(n3) - 2S(n3) - 1
#              = S(n) + 2S(2n1+1) - 3S(n1) + S(2n2+1) - S(n2)
#                + 3S(2n3+1) - 5S(n3) - 1

memo = {0:0,1:1,2:2,3:5}
def S(N):
    if N in memo:
        return memo[N]
    n,r = N/4,N%4
    n1,n2,n3 = n-int(r<1),n-int(r<2),n-int(r<3)
    res = S(n)+2*S(2*n1+1)-3*S(n1)+S(2*n2+1)-S(n2)+3*S(2*n3+1)-5*S(n3)-1
    memo[N] = res
    return res

#print S(8)
#print S(100)
print S(3**37)%10**9
