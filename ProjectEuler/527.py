#!/usr/bin/env python3

from fractions import *
from decimal import Decimal

# prog. dyn. en O(log n) pour B
memoB = {0:Decimal(0),1:Decimal(1)}
def B(n):
    if n in memoB:
        return memoB[n]
    m = (n+1)//2
    res = ((m-1)*(B(m-1)+1) + 1 + (n-m)*(B(n-m)+1)) / n
    memoB[n] = res
    return res

# prog. dyn. en O(n^2) pour R
memoR = {0:Fraction(0),1:Fraction(1)}
def R(n):
    if n in memoR:
        return memoR[n]
    res = 0
    for m in range(1,n+1):
        res += ((m-1)*(R(m-1)+1) + 1 + (n-m)*(R(n-m)+1)) / n
    res /= n
    memoR[n] = res
    return res

# print([(i,str(R(i))) for i in range(2,10)])

# on decouvre empiriquement (OEIS) la formule
# (-3n + 2(1+n)*HarmonicNumber(n)) / n
# numerateurs : http://oeis.org/A093418
# denominateurs * n : http://oeis.org/A096620
# asymptotiquement, H(n) ~ gamma + ln(n)
# https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant
g = Decimal('0.5772156649015328606065120900824024310421')
def Rapprox(n):
    return -3+2*(1+n)*(g+Decimal(n).ln())/n

N = 10**10
print(Rapprox(N)-B(N))
