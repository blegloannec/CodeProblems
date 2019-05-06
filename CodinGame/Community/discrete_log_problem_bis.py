#!/usr/bin/env python3

from math import sqrt, gcd
import random, sys
random.seed(54)

def decomp(n):
    F = []
    m = 0
    while n&1==0:
        n >>= 1
        m += 1
    if m>0:
        F.append((2,m))
    i = 3
    while n>1 and i*i<=n:
        m = 0
        while n%i==0:
            n //= i
            m += 1
        if m>0:
            F.append((i,m))
        i += 2
    if n>1:
        F.append((n,1))
    return F

def lcm(a,b):
    return a*b//gcd(a,b)

def multiplicative_order(G,P):
    assert gcd(G,P)==1
    Phi = P-1
    D = decomp(Phi)
    o = 1
    for Q,M in D:
        G0 = pow(G,Phi//Q**M,P)
        o0 = 1
        while G0!=1:
            G0 = pow(G0,Q,P)
            o0 *= Q
        o = lcm(o,o0)
    return o

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    #assert g==1
    return u%n

def pollard_rho_discrete_log(G, P, X, OG=None):
    if OG is None:
        OG = P-1
    rnd = lambda: random.randint(0,OG-1)
    r = 30
    AB = [(rnd(),rnd()) for _ in range(r)]
    C = [(pow(G,a,P)*pow(X,b,P))%P for a,b in AB]
    
    def F(x,a,b):
        k = x%r
        return (x*C[k])%P, (a+AB[k][0])%OG, (b+AB[k][1])%OG
    
    ax,bx = rnd(),rnd()
    x = (pow(G,ax,P)*pow(X,ax,P))%P
    y,ay,by = x,ax,bx
    while True:
        x,ax,bx = F(x,ax,bx)
        y,ay,by = F(y,ay,by)
        y,ay,by = F(y,ay,by)
        if x==y:
            break
    # x = G^ax * X^bx mod P and y = G^ay * X^by mod P
    # if x = y mod P and X = G^k mod P, then
    # ax-ay = k(by-bx) mod order(G)
    da = (ax-ay) % OG
    db = (by-bx) % OG
    if gcd(db,OG)==1:
        x = (da*inv_mod(db,OG))%OG
        if pow(G,x,P)==X:
            return x
    return -1

if __name__=='__main__':
    G,X,P = map(int,input().split())
    OG = multiplicative_order(G,P)
    print('Order', OG, file=sys.stderr)
    x = pollard_rho_discrete_log(G,P,X,OG)
    tries = 10
    while x==-1 and tries>0:
        x = pollard_rho_discrete_log(G,P,X,OG)
        tries -= 1
    print(x)
