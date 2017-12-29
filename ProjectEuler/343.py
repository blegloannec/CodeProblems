#!/usr/bin/env python

from fractions import gcd
from collections import defaultdict
import random
random.seed()

# Considerons la fraction x/y, on peut la positionner en x
# sur une ligne de taille z = x+y de maniere a separer
# la longueur x a gauche de y a droite.
# Alors faire un pas sans simplification (x := x+1, y := y-1)
# dans la sequence consiste a se deplacer d'un cran vers la
# droite sur la ligne.
# Si l'on marque tous les diviseurs de z et leurs multiples sur la ligne,
# la prochaine simplification aura lieu a la premiere marque
# a droite de la position de la fraction.
# Le nombre k de pas est borne par y-1 (fraction (x+y-1)/1).
# Si l'on fait k pas avant la prochaine simplification,
# alors, pour g = gcd(x+k,y-k), la nouvelle fraction est
# ((x+k)/g) / ((y-k)/g) et le nouveau z est z/g dont on peut
# deduire la factorisation de celle de l'ancien z !

# Mais ici, c'est encore plus simple car on commence avec 1/n,
# donc la premiere simplification a toujours lieu pour le plus
# petit diviseur d>1 de n et on retrouve apres simplification une
# fraction 1/(n/d). On continue avec le plus petit diviseur de n/d, etc.
# Autrement dit, on elimine les facteurs premiers dans l'ordre simplification
# apres simplification, et donc a la fin il ne reste que le plus grand facteur
# premier.

# En bref : f(n) = (plus grand facteur premier de n+1) - 1
# Ici, n = k^3 = (k+1)(k^2-k+1)
# On factorise k^2-k+1 avec Pollard's Rho, mais c'est lent...
# (TODO : faire mieux)

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n,b):
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s=15):
    b = digits(n-1,2)
    for j in xrange(s):
        if witness(random.randint(1,n-1),n,b):
            return False
    return True

def pollard_rho(n):
    c = random.randint(1,n-1)
    f = (lambda x: (x*x+c)%n)
    x = random.randint(0,n-1)
    y = x
    x = f(x)
    y = f(f(y))
    while x!=y:
        p = gcd(n,abs(x-y))
        if 1<p<n:
            return p
        x = f(x)
        y = f(f(y))
    return None

def factorisation(n,D):
    while n>1:
        if miller_rabin(n):
            D[n] += 1
            return D
        f = pollard_rho(n)
        if f!=None:
            factorisation(f,D)
            n /= f
    return D

# Retire les facteurs 2 avant (sinon ca boucle) :
def full_factorisation(n):
    D = defaultdict(int)
    while n%2==0:
        D[2] += 1
        n /= 2
    return factorisation(n,D)

N = 2*10**6

def sieve_max_factor(N):
    P = [True for _ in xrange(N)]
    Factor = [-1 for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factor[i] = i
            for k in xrange(2*i,N,i):
                P[k] = False
                Factor[k] = i
    return P,Factor

_,Factor = sieve_max_factor(N+2)

def max_fact(n):
    if n==1:
        return 0
    return max(full_factorisation(n).keys())

def main():
    s = 0
    for k in xrange(1,N+1):
        s += max(Factor[k+1],max_fact(k*k-k+1))-1
    print s

main()
