#!/usr/bin/env python

from multiprocessing import Pool

# rather naive solution, terribly slow
# linear code runs in 6-7 min with pypy
# multiprocessed code (4 cores) runs in 2 min with pypy

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

def det_miller_rabin_64(n):
    b = digits(n-1,2)
    for w in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

# code de test pour generer les petites valeurs
def test(xmax=10000):
    for x in xrange(1,xmax):
        for y in xrange(1,x):
            a,b = x**4-y**4,x**3+y**3
            if a%b==0 and det_miller_rabin_64(a/b):
                print a/b,x,y

# il semble qu'il s'agisse des premiers de la forme n^2 + (n+1)^2
# http://oeis.org/A027862

# Une courte preuve (a posteriori, via le premier post du forum) :
# soit p = (x^4-y^4) / (x^3+y^3) suppose premier
# x^4-y^4 = (x^2)^2 - (y^2)^2
#         = (x^2-x^2)(x^2+y^2)
#         = (x-y)(x+y)(x^2+y^2)
# x^3+y^3 = x^3 - (-y)^3
#         = (x-(-y))(x^2 + x(-y) + (-y)^2)
#         = (x+y)(x^2-xy+y^2)
# p(x^3+y^3) = (x^4-y^4)
# p(x^2-xy+y^2) = (x-y)(x^2+y^2)
# soit d = gcd(x,y), x=dx', y = dy' et divisons par d^2
# p(x'^2-x'y'+y'^2) = d(x'-y')(x'^2+y'^2)  (1)
# on observe que (x'^2-x'y'+y'^2) et (x'-y')(x'^2+y'^2) p-e-e
# (car, en les notant A et B, on a B = (x'-y')A + (x'-y')x'y'
#  donc gcd(A,B) = gcd(A,C) pour C = (x'-y')x'y'
#  puis on a Ay' = C + y'^3 donc gcd(A,C) = gcd(A,y'^3)
#  donc si un nb premier q | gcd(A,B) alors q | y'^3 donc q | y'
#  donc comme q | A, alors q | x'^2 et donc q | x' ce qui contredit
#  le fait que x' et y' p-e-e)
# comme de plus p est premier, alors on peut identifier dans (1)
# (x'-y')(x'^2+y'^2) = p (et d = (x'^2-x'y'+y'^2)) mais p etant
# premier on doit alors avoir x'-y' = 1 d'ou p = x'^2 + (x'+1)^2

CORES = 4

def compte(start=1,step=CORES):
    N = 5*10**15
    cpt = 0
    n = start
    while True:
        p  = n*n + (n+1)*(n+1)
        if p>=N:
            break
        if det_miller_rabin_64(p):
            cpt += 1
        n += step
    return cpt

def main():
    p = Pool(CORES)
    print sum(p.map(compte,range(1,CORES+1)))
    
main()
