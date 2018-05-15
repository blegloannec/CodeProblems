#!/usr/bin/env python3

# voir aussi PE401 pour ce type de raisonnement

# l'etudiant i participe au jour N ssi N//i (=E(N/i)) est impair
# le nombre d'étudiants le jour N est donc sum_{i=1..N} (N//i)%2
# N//i = k ssi k <= N/i < k+1 ssi ik <= N < i(k+1) ssi N/(k+1) < i <= N/k
# ssi N//(k+1) < i <= N//k car i entier
# le nombre de i tels que N//i = k est donc N//k - N//(k+1) (eventuellement 0)
# on peut dont reecrire sum_{i=1..N} N//i = sum_{k=1..N} k*(N//k - N//(k+1))
# soit, modulo 2, sum_{k=1..N impair} N//k - N//(k+1)

# turns out that, mod 2, it's floor(sqrt(N))%2

from decimal import Decimal

T = int(input())
for _ in range(T):
    N = int(input())
    print('odd' if int(Decimal(N).sqrt())&1 else 'even')
