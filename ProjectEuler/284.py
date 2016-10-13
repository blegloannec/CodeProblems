#!/usr/bin/env python

# the approach seems ok, the implementation could be better,
# runs in 62s with pypy

# x a n chiffres est steady en base 14 = 2*7
# ssi x^2 = x mod 14^n
# ssi x(x-1) = 0 mod 2^n et 7^n
# ie ssi x pair et x = 0 mod 2^n et x-1 = 0 mod 7^n
#     ou x impair et x-1 = 0 mod 2^n et x = 0 mod 7^n
# Fixons n, les nombres que l'on cherche sont les x*y, y = x +/- 1
# 14^(n-1) <= x,y < 14^n et 2^n | x et 7^n | y
# ecrivons x = x'*2^n et y = y'*7^n
# 14^(n-1)/2^n = 7^(n-1)/2 <= x' < 14^n/2^n = 7^n
# 14^(n-1)/7^n = 2^(n-1)/7 <= y' < 14^n/2^n = 2^n
# mais alors si y = x + 1
# 7^n*y' - 2^n*x' = 1
# 7^n et 2^n sont p-e-e et l'on a donc une "relation de Bezout"
# soient u et v des coefficients de Bezout pour le couple (2^n,7^n)
# les solutions pour (x',y') sont de la forme (-(u+k*7^n),v-k*2^n), k relatif
# a cause des bornes plus haut, seules la solution minimale pour laquelle
# u<0 et v>0 est acceptable
# dans le cas y = x - 1 on tombe justement sur l'autre solution minimale

# NB (a posteriori): on resout ici les equations "a la main" avec Bezout
# mais x = 0 mod 2^n et x-1 = 0 mod 7^n <=> x = 0 mod 2^n et x = 1 mod 7^n
# et l'on pouvait donc arreter l'analyse ici et se contenter d'un coup de
# theoreme chinois pour obtenir la solution ;D (en termes de complexite, ca
# ne change rien, mais c'etait plus simple)

B = 14

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

# Approche decrite ci-dessus
def gen_steady(n):
    p02,p07 = 1<<(n-1),7**(n-1)
    p2,p7 = p02<<1,7*p07
    _,u,v = bezout(p2,p7)
    if u>0:
        u,v = u-p7,v+p2
    u2,v2 = u+p7,v-p2
    sol = []
    if p02<=7*v:
        sol.append(v*p7)
    if p07<=2*u2:
        sol.append(u2*p2)
    return sol

def to_base(n,b=B):
    d = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = []
    while n>0:
        res.append(d[n%b])
        n /= b
    return ''.join(res[::-1])

# Code de test base sur l'observation que si x est steady de taille n
# alors x prive de son premier chiffre est steady de taille <n
def bad_gen_steady():
    res = 0
    S = [(0,0)]
    for p in xrange(1,20):
        SS = []
        for (s,sd) in S:
            for a in xrange(1,B):
                n = s+a*B**(p-1)
                if pow(n,2,B**p)==n:
                    SS.append((n,sd+a))
                    res += sd+a
        print p,SS
        # verif resultats de l'autre algo
        print gen_steady(p)
        S += SS

# Resolution
def main():
    s = 1
    S = {0:0,1:1}
    p14 = 1
    for i in xrange(1,10001):
        for x in gen_steady(i):
            s1 = S[x%p14] + x/p14
            S[x] = s1
            s += s1
        p14 *= 14
    print to_base(s,14)

#bad_gen_steady()
main()
