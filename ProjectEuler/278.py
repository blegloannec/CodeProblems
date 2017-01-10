#!/usr/bin/env python

# https://en.wikipedia.org/wiki/Coin_problem
# pour 2 nombres a et b, la solution est ab-a-b
# pour 3 nombres a, b et c il n'y a pas de formule generale
# mais dans le cas ou c | ppcm(a,b) et pgcd(a,b,c) = 1
# on a la formule ppcm(c,a)+ppcm(c,b)-a-b-c
# ici a = pq, b = pr,c = qr donc c | ppcm(a,b) = pqr
# et gcd(a,b,c) = 1
# donc la solution est 2pqr-a-b-c

def sieve_list(N):
    P = [True for _ in xrange(N)]
    L = []
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

P = sieve_list(5000)
S = 0
for ip in xrange(len(P)):
    p = P[ip]
    for iq in xrange(ip+1,len(P)):
        q = P[iq]
        for ir in xrange(iq+1,len(P)):
            r = P[ir]
            S += 2*p*q*r-p*q-p*r-q*r
print S
