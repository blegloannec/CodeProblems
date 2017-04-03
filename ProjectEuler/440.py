#!/usr/bin/env python

from fractions import gcd
from collections import defaultdict

# T(0) = 1, T(1) = 10, T(n+2) = 10*T(n+1) + T(n)
# T(n) is a Lucas sequence : u(n+2) = A*u(n+1) + B*u(n)
# Lucas sequences are divisibility sequences : a | b => u(a) | u(b)
# Moreover, from https://mathoverflow.net/questions/181307/strong-divisibility-of-lucas-sequences
# we know that if u(n) is a Lucas sequence with gcd(A,B) = 1, u(0) = 0 and u(1) = 1,
# then u(n) is a *strong* divisibility sequence : gcd(u(a),u(b)) = u(gcd(a,b))
# Hence considering T'(0) = 0 and T'(n) = T(n-1), T'(n) is a strong divisibility sequence.
# Thus we have gcd(T(a),T(b)) = T(gcd(a+1,b+1)-1)

# We also observe that the sequence T(n) mod P, which is obviously
# ultimately periodic, actually always seems periodic.
# Mod P = 987898789, the period is exactly P-1...!
# Hence T(n) = T(n%(P-1)) mod P

# Que dire de gcd(c^a+1,c^b+1) ?
# un resultat utile : si a,b,m,n entiers relatifs non nuls avec a>=b et gcd(a,b) = 1
# alors gcd(a^m-b^m,a^n-b^n) = a^gcd(m,n) - b^gcd(m,n)
# en particulier, si m et n impairs, on peut ecrire
# gcd(a^m+1,a^n+1) = gcd(a^m-(-1)^m,a^n-(-1)^n)
#                  = a^gcd(m,n) - (-1)^gcd(m,n)
#                  = a^gcd(m,n) + 1
# on remarque que cela reste vrai pour tous m et n de meme valuation 2-adique
# ainsi gcd(T(c^a),T(c^b)) = T(gcd(c^a+1,c^b+1)-1) = T(c^gcd(a,b) % (P-1)) mod P
# et sinon gcd(a^m+1,a^n+1) = 1 si a pair et 2 sinon
# ainsi gcd(T(c^a),T(c^b)) = T(c%2)

# runs in ~11s with pypy

P = 987898789

class Matrix2:
    def __init__(self,a=1,b=0,c=0,d=1):
        self.m00,self.m01,self.m10,self.m11 = a,b,c,d
    def __mul__(self,B):
        return Matrix2((self.m00*B.m00+self.m01*B.m10)%P,(self.m00*B.m01+self.m01*B.m11)%P,(self.m10*B.m00+self.m11*B.m10)%P,(self.m10*B.m01+self.m11*B.m11)%P)
    def __pow__(self,n):
        if n==0:
            return Matrix2()
        elif n%2==0:
            return (self*self)**(n/2)
        return self*(self*self)**((n-1)/2)


A = Matrix2(0,1,1,10)
def T(n):
    return (A**n).m11

def val2(n):
    v = 0
    while not n&1:
        n >>= 1
        v += 1
    return v

def S(L):
    G = defaultdict(int)
    V = 0
    for a in xrange(1,L+1):
        for b in xrange(1,L+1):
            if val2(a)==val2(b):
                G[gcd(a,b)] += 1
            else:
                V += 1
    res = 0
    for c in xrange(1,L+1):
        res = (res + V*T(c%2))%P
        for v in G:
            res = (res + G[v]*T(pow(c,v,P-1)))%P
    return res

print S(2000)
