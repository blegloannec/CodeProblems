#!/usr/bin/env python

# Pour 2^n, on a tout d'abord les 2 partitions 2^n et 2.2^(n-1)
# on ne peut pas decomposer les deux 2^(n-1) car le plus grand
# nombre que l'on peut former avec les puissances <=2^(n-2) est
# 2(2^(n-1)-1) = 2^n-2, donc une partition de 2^n est soit 2^n,
# soit 2^(n-1) + [une partition de 2^(n-1)].
# Il y a donc n+1 partitions de 2^n.

# Ce raisonnement partant du bit de poids fort n'est pas tres
# commode dans le cas general...
# Il est en fait plus simple de raisonner a partir du bit de
# poids faible. Une partition de n est formee de :
#  - 0 fois 2^0 (n pair) + 2*[partition de n/2]
#  - 1 fois 2^0 (n impair) + 2*[partition de (n-1)/2]
#  - 2 fois 2^0 (n pair) + 2*[partition de (n-2)/2]

memo = {0:1,1:1}
def f(n):
    if n in memo:
        return memo[n]
    if n%2==0:
        res = f(n/2)+f((n-2)/2)
    else:
        res = f((n-1)/2)
    memo[n] = res
    return res

print f(10**25)
