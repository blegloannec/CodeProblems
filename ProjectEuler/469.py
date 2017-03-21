#!/usr/bin/env python3

from fractions import *

# Chaque chevalier isole 2 parties d'un segment de table.
# Considerons donc le probleme pour un segment (table non torique).

T = [None]*1000
T[0] = Fraction(0)
T[1] = Fraction(0)
T[2] = Fraction(1)

# esperance du nb de places vides pour un segment de table
# DP en O(n^2)
def S(n):
    if T[n]!=None:
        return T[n]
    res = (1+S(n-2))*Fraction(2,n) # extremites
    for i in range(1,n-1): # chaises interieures
        res += (2+S(i-1)+S(n-i-2))*Fraction(1,n)
    T[n] = res
    return res

def E(n):
    return (2+S(n-3))*Fraction(1,n)

#print(E(4))
#print(E(6))
#print([float(E(i)) for i in range(3,30)])

# On remarque alors simplement que E converge tres tres vite.
# On a deja plus de 14 chiffres fixes des le rang 25.
# Le 10^18 de l'enonce est donc un petit piege !
print(float(E(25)))
