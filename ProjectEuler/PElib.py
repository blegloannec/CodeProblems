#!/usr/bin/env python

#from math import *
#from fractions import gcd
#sys.setrecursionlimit(100000)


# pas utile, x**n est plus efficace
def expo(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return expo(x*x,n/2)
    return x*expo(x*x,(n-1)/2)

# pas utile, pow(x,n,p) est plus efficace
def expmod(x,n,p):
    if n==0:
        return 1
    elif n%2==0:
        return expmod((x*x)%p,n/2)
    return (x*expmod((x*x)%p,(n-1)/2))%p


def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

# Les cribles suivants peuvent etre acceleres
# en n'allant que jusqu'a la racine
# le dernier facteur (>racine) manque potentiellement
# mais dans ce cas sa multiplicite est 1
# Voir en particulier pbs 70,72

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                Factors[k].append(i)
    return P,Factors

def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Decomp[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m += 1
                Decomp[k].append((i,m))
    return P,Decomp

# NB: phi(n) = n*Prod( 1 - 1/p, p facteur premier de n)
# donc eulerphi(n) est calculable a partir des facteurs seuls
# (sans leur multiplicite, ie avec sieve_factors au lieu de sieve_decomp)
# mais ce calcul est a base de float, alors qu'on le fait ici en int
def eulerphi(decomp):
    res = 1
    for (p,m) in decomp:
        res *= (p-1)*p**(m-1)
    return res

# Version acceleree
# le dernier facteur (>racine) manque potentiellement
# mais dans ce cas sa multiplicite est 1
def faster_sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    S = int(sqrt(N))+1 # pour accelerer
    for i in xrange(2,S):
        if P[i]:
            Decomp[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m += 1
                Decomp[k].append((i,m))
    return P,Decomp

# eulerphi associee :
def eulerphi(n,decomp): # decomp potentiellement partielle
    res = 1
    for (p,m) in decomp:
        f = expo(p,m-1)
        n /= f*p
        res *= (p-1)*f
    if n>1: # dernier facteur manquant
        res *= n-1
    return res

# ou encore
def sieve_totient(N):
    P = [True for _ in xrange(N)]
    Totient = [1 for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Totient[i] = i-1
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m *= i
                Totient[k] *= (i-1)*m
    return P,Totient


# generateur des diviseurs (a partir des decomp)
def divisors(F,i=0):
    if i==len(F):
        yield 1
    else:
        p,m = F[i]
        f = 1
        for _ in xrange(m+1):
            for d in divisors(F,i+1):
                yield f*d
            f *= p


# also defined by module fractions
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    assert(g==1)
    return u # ajouter %n pour solution >0

def somme_diviseurs(n): # for n>1!
    s = 1
    r = int(sqrt(n))
    if r*r==n: # n is a square
        s += r
        r -= 1
    for i in xrange(2,r+1):
        if n%i==0:
            s += i+n/i
    return s

def nb_diviseurs(n): # for n>1!
    s = 2
    r = int(sqrt(n))
    if r*r==n: # n is a square
        s += 1
        r -= 1
    for i in xrange(2,r+1):
        if n%i==0:
            s += 2
    return s

def sieve_nb_divisors(N):
    P = [True for _ in xrange(N)]
    Nbdiv = [1 for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Nbdiv[i] = 2
            for k in xrange(2*i,N,i):
                P[k] = False
                l = k/i
                j = 1
                while l%i==0:
                    l /= i
                    j += 1
                Nbdiv[k] *= j+1
    return P,Nbdiv


# mauvais test de primalite
def prime(n):
    if n%2==0:
        return False
    for i in xrange(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

# mauvaise factorisation
def decomp(n):
    F = []
    m = 0
    while n%2==0:
        n /= 2
        m += 1
    if m>0:
        F.append((2,m))
    i = 3
    s = int(sqrt(n))+1
    while n>1 and i<s:
        m = 0
        while n%i==0:
            n /= i
            m += 1
        if m>0:
            F.append((i,m))
        i += 2
    if n>1:
        F.append((n,1))
    return F

# mauvais crible filtre (lent mais parfois pratique)
def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in xrange(2,s):
        for k in xrange(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)


def mirror(n):
    m = 0
    while n>0:
        m = 10*m + n%10
        n /= 10
    return m

def is_palindrome(n):
    return mirror(n)==n


def taux_lettres(m):
    cpt = 0
    for c in m:
        if (ord('a')<=c and c<=ord('z')) or (ord('A')<=c and c<=ord('Z')):
            cpt += 1
    return float(cpt)/len(m)

def indice_coincidence(m):
    cpt = [0 for _ in xrange(26)]
    N = 0
    for c in m:
        if ord('a')<=c and c<=ord('z'):
            cpt[c-ord('a')] += 1
            N += 1
        elif ord('A')<=c and c<=ord('Z'):
            cpt[c-ord('A')] += 1
            N += 1
    return float(sum(map((lambda(x):x*(x-1)),cpt)))/(N*(N-1))


def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def digits_sum(n,b):
    return sum(digits(n,b))

# or, if the digits are not useful:
def digits_sum(n,b):
    s = 0
    while n>0:
        s += n%b
        n /= b
    return s

def nb_digits10(n):
    return int(log10(n))+1

def nb_digits(n,b):
    return int(log(n,b))+1


# t = n(n+1)/2
# n^2 + n - 2t = 0
# Given t, D = 1+8t must be a square
# then n = (-1+sqrt(D))/2
def is_triang(t):
    D = 1+8*t
    d = int(sqrt(1+8*t))
    return d*d==D

# p = n(3n-1)/2
# 3n^2 - n - 2p = 0
# D = 1+24p
# et n = (1+sqrt(D))/6
# mais les solutions pour n<0 ont n = (1-sqrt(D))/6
# dans ce cas (1-sqrt(D))%6 == 0
# donc (1+sqrt(D))%6 == 2 != 0
def is_penta(p):
    D = 1+24*p
    d = int(sqrt(D))
    return (d*d==D and (1+d)%6==0)


# Miller-Rabin (requires digits())
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

# version deterministe 32 bits
def det_miller_rabin_32(n):
    #if n<2:
    #    return False
    b = digits(n-1,2)
    for w in [2,7,61]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

# version deterministe 64 bits
def det_miller_rabin_64(n):
    b = digits(n-1,2)
    for w in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True


# permutation suivante (ordre lex) d'un tableau quelconque
# (repetitions autorisees)
# (pour prev_permutation, inverser les comparaisons de T[.])
def next_permutation(T):
    pivot = len(T)-2
    while pivot>=0 and T[pivot]>=T[pivot+1]:
        pivot -= 1
    if pivot<0:
        return False
    swap = len(T)-1
    while T[swap]<=T[pivot]:
        swap -= 1
    T[swap],T[pivot] = T[pivot],T[swap]
    i = pivot+1
    j = len(T)-1
    while i<j:
        T[i],T[j] = T[j],T[i]
        i += 1
        j -= 1
    return True


# generateur des sous-ensembles de 0..n-1 de cardinal c
def subsets(n,c):
    if c==0:
        yield 0
    else:
        for x in xrange(c-1,n):
            for S in subsets(x,c-1):
                yield S | (1<<x)

# Autre version
def parmi(n,p):
    if p==0:
        yield []
    else:
        for i in xrange(p-1,n):
            for S in parmi(i,p-1):
                S.append(i)
                yield S


# generateur des partitions de n a k composantes
def partitions(n,k):
    if k==1:
        yield [n]
    elif k<=n:
        for p in partitions(n-1,k-1):
            p.append(1)
            yield p
        for p in partitions(n-k,k):
            for i in xrange(k):
                p[i] += 1
            yield p


# recursive permutation generator using Heap's algo, quite ugly
# better in python 3: syntax "yield from <recursive call>"
def heap(n,A):
    if n==1:
        yield A
    else:
        for i in xrange(n-1):
            for B in heap(n-1,A):
                yield B
            if n%2==0:
                A[i],A[n-1] = A[n-1],A[i]
            else:
                A[0],A[n-1] = A[n-1],A[0]
        for B in heap(n-1,A):
            yield B


# Pollard's rho (D = defaultdict(int), requires miller_rabin)
# Attention : fait main il y a longtemps...
# pas forcement le "vrai" algo (mais marche vite et bien)
def pollard_rho(n):
    l = set()
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
