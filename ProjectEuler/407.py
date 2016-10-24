#!/usr/bin/env python

# solution lente (> 1 min)...
# a^2 = a [n]
# a(a-1) = 0 [n]
# 1 est toujours solution
# comme a et a-1 p-e-e (et a<n), il faut n = uv
# avec u et v p-e-e et u|a et v|a-1
# (en particulier si n est puissance d'un nb premier
# a = 1 est la seule solution, pour u=1, v=n)
# si on ecrit a = uu', comme a = 1 [v]
# alors u' = u^(-1) [v] (et u toujours inversible modulo v
# car u et v p-e-e)
# on peut donc essayer tous les u produit d'un sous-ensemble
# de la decomposition de n en facteurs premiers, calculer u' par
# inversion modulaire et garder celui qui donne le a = uu' maximal
# see also: http://math.stackexchange.com/questions/264290/division-into-xx-1


def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Decomp[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                m = i
                l = k/i
                while l%i==0:
                    l /= i
                    m *= i
                Decomp[k].append(m)
    return P,Decomp

# sous-ensembles de la decomp
def gen(d,i=0,n=1):
    if i==len(d):
        yield n
    else:
        for a in gen(d,i+1,n):
            yield a
        for a in gen(d,i+1,n*d[i]):
            yield a

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    return u%n # %n pour valeur >0

def s(n,d):
    return max(u*inv_mod(u,n/u) for u in gen(d))

def main():
    N = 10**7+1
    _,D = sieve_decomp(N)
    res = 0
    for i in xrange(2,N):
        if len(D[i])==1:
            res += 1
        else:
            res += s(i,D[i])
    print res

main()
