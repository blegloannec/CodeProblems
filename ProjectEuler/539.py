#!/usr/bin/env python

# on part de [1,...,n]
#  - si n est pair, on aura [2,4,...,n] apres une etape
#  - sinon on aura [2,4,...,n-1] apres une etape, soit la meme
#    chose que n-1 pair, on peut donc se ramener au cas pair :
#    P(n) = P(2k+1) = P(2k)
# on peut donc supposer n = 2k pair
# dans ce cas on a 2*[1,...,k] apres une etape et on part maintenant de droite
#  - si k est pair, on aura 2*[1,3,...,k-1]
#    ecrivons k = 2l, on a 2*([2,4,...,2l]-1) = 2*(2*[1,2,...,l]-1)
#    donc P(n) = P(4l) = 4*P(l)-2
#  - si k impair, on aura 2*[2,4,...,k-1]
#    ecrivons k = 2l+1, on a 4*[1,2,...,l]
#    donc P(n) = P(4l+2) = 4*P(l)

# Bilan :
# P(2n+1) = P(2n)
# P(4n) = 4*P(n)-2
# P(4n+2) = 4*P(n)
# et on se retrouve avec une relation de la forme de celle du pb 463
# on peut meme preciser
# P(4n+1) = P(4n) = 4*P(n)-2
# P(4n+3) = P(4n+2) = 4*P(n)

# Soit S(n) = sum( P(i), i<=n )
# S(4n+3) = sum( P(4k)+P(4k+1)+P(4k+2)+P(4k+3), k=0..n )
#         = 5 + sum( 16*P(k)-4, k=1..n )
#         = 16*S(n) - 4*n + 5
# S(4n+2) = S(4n+3) - P(4n+3) = 16*S(n) - 4*n + 5 - 4*P(n)
#                             = 16*S(n) - 4*n - 4*S(n) + 4*S(n-1) + 5
#                             = 12*S(n) + 4*S(n-1) - 4*n + 5
# S(4n+1) = S(4n+2) - P(4n+2) = 12*S(n) + 4*S(n-1) - 4*n + 5 - 4*P(n)
#                             = 8*S(n) + 8*S(n-1) - 4*n + 5
# S(4n) = S(4n+1) - P(4n+1) = 8*S(n) + 8*S(n-1) - 4*n + 5 - 4*P(n) + 2
#                           = 4*S(n) + 12*S(n-1) - 4*n + 7

memo = {0:0,1:1,2:3,3:5}
def S(n):
    if n in memo:
        return memo[n]
    if n%4==0:
        res = 4*S(n/4) + 12*S(n/4-1) - 4*(n/4) + 7
    elif n%4==1:
        res = 8*S(n/4) + 8*S(n/4-1) - 4*(n/4) + 5
    elif n%4==2:
        res = 12*S(n/4) + 4*S(n/4-1) - 4*(n/4) + 5
    else:
        res = 16*S(n/4) - 4*(n/4) + 5
    memo[n] = res
    return res

print S(10**18)%987654321
