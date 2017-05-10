#!/usr/bin/env python

# A(k) = proba pour Alice d'avoir T^kH
#      = p^k * (1-p)
# B(k) = esperance du nb de H d'un ami sur k tirages
#      = k*(1-p)
# comme les tirages des amis sont independants
# E(n,k) = esperance du resultat sur k tirages pour n amis
#        = B(k)^n
# e(n)(p) = sum(A(k)*E(n,k), k>=0)
#        = sum( p^k*(1-p)*k^n*(1-p)^n, k>=0)
#        = (1-p)^(n+1) * sum(k^n*p^k, k>=0)
#        = (1-p)^(n+1) * Q(n)(p)
# pour le polynome Q(n) = sum(k^n*X^k, k>=0)
# Q(n)' = sum(k^(n+1)*X^(k-1), k>=1)
#       = sum(k^(n+1)*X^k, k>=0) / X
#       = Q(n+1)/X
# ecrivons Q(n) = e(n) / (1-X)^(n+1)
# Q(n)' = ( e(n)' * (1-X)^(n+1) + e(n)*(n+1)*(1-X)^n )  / (1-X)^(2n+2)
#       = ( (1-X)*e(n)' + (n+1)*e(n) ) / (1-X)^(n+2)
# donc e(n+1) = X*( (1-X)*e(n)' + (n+1)*e(n) )
# posons c(n,i) le coeff de degre i de e(n)
# on a alors la formule de recurrence suivante
# c(n+1,i+1) = (i+1)*c(n,i+1) - i*c(n,i) + (n+1)*c(n,i)
#            = (i+1)*c(n,i+1) + (n+1-i)*c(n,i)

# on decouvre qu'il s'agit des nombres/polynomes euleriens
# http://oeis.org/A008292
# http://oeis.org/wiki/Eulerian_polynomials
# http://oeis.org/wiki/Eulerian_numbers
# ce qui donne une formule explicite (pas forcement evidente
# a deriver des calculs precedents)

# runs in 7s with pypy

P = 10**9+7

# recurrence pour de petites valeurs
memo = {(3,1):1,(3,2):4,(3,3):1}
def c(n,i):
    if (n,i) in memo:
        return memo[n,i]
    if i<=0 or i>n:
        return 0
    res = (i*c(n-1,i) + (n+1-i)*c(n-1,i-1))%P
    memo[n,i] = res
    return res

#for n in xrange(3,10):
#    print([c(n,i) for i in xrange(1,n+1)])


def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n=P):
    return bezout(a,n)[1]

N,M = 10**7,4*10**6

# pre-calcul des factorielles modulo
F = [1]
for n in xrange(1,N+2):
    F.append((n*F[-1])%P)

def binom(n,p):
    return (F[n]*(inv_mod(F[p])*inv_mod(F[n-p]))%P)%P

# formule explicite
def cform(n,m):
    res = 0
    for k in xrange(m):
        res = (res + (1-2*(k%2))*binom(n+1,k)*pow(m-k,n,P))%P
    return res

print(cform(N,M))
