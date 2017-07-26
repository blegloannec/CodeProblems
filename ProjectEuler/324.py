#!/usr/bin/env python

from fractions import Fraction

# Not that easy for a 50% difficulty rate problem!
# Probably underrated because there seems to be a recurrence
# relation on OEIS, and simply picking it up makes things easier.
# However we will obtain a slightly simpler relation here, so it
# was worth the effort!
# runs in 9s using pypy

# n odd => f(n) = 0


## PART 1 ##
# DP to compute "small" values
def get(n,i):
    return (n>>(2*i))&3

def val(v,i):
    return v<<(2*i)

def getmax(top):
    for p in xrange(9):
        if get(top,p)==0:
            return p
    return None

def pos(x,y):
    return 3*y+x

# 111111111 en base 4
D = 87381

memo = {(0,0):1}
def dp(n,top=0):
    p = getmax(top)
    if p==None:
        return dp(n-1,top-D)
    if (n,top) in memo:
        return memo[n,top]
    y,x = p/3,p%3
    res = 0
    # cas 11
    if x<=1:
        q = pos(x+1,y)
        if get(top,q)==0:
            res += dp(n,top+val(1,p)+val(1,q))
    # cas 1
    #     1
    if y<=1:
        q = pos(x,y+1)
        if get(top,q)==0:
            res += dp(n,top+val(1,p)+val(1,q))
    # cas 2
    if n>=2:
        res += dp(n,top+val(2,p))
    memo[n,top] = res
    return res

# There must be a linear recurrence relation (as for
# 2xn grid, in which case the solution is Fibonacci)...
# Let us assume that the recurrence degree is k not too large.
# Let M the k x k matrix of [[f(2*0)..f(2*(k-1))][f(2*1)..dp(2*k)]...]
# and the column B = [f(2*k)..f(2*(2*k-1)]
# then if A is the recurrence coefficients column, MA = B


## PART 2 ##
# Some old matrix inversion code
def size(M):
    return len(M),len(M[0])

def id(n):
    return [[int(i==j) for j in xrange(n)] for i in xrange(n)]

def copy(M):
    h,_ = size(M)
    return [M[i][:] for i in xrange(h)]

def l_swap(M,i,j):
    w = len(M[0])
    for k in xrange(w):
        M[i][k],M[j][k] = M[j][k],M[i][k]

def first_non_zero(M,i):
    h = len(M)
    for j in xrange(i,h):
        if M[i][j]!=0:
            return j
    return None

def sline_prod(a,M,i):
    w = len(M[0])
    for j in xrange(w):
        M[i][j] *= a

def line_diff(a,M,i,j):
    # Mj <- Mj - a*Mi
    w = len(M[0])
    for k in xrange(w):
        M[j][k] -= a*M[i][k]

def inverse(M0):
    M = copy(M0)
    n = len(M)
    I = id(n)
    for i in xrange(n):
        j0 = first_non_zero(M,i)
        assert(j0!=None)
        if j0>i:
            l_swap(M,i,j0)
            l_swap(I,i,j0)
        a = Fraction(1,M[i][i]) # for exact Fraction computation
        sline_prod(a,M,i)
        sline_prod(a,I,i)
        for j in xrange(n):
            if j!=i:
                a = M[j][i]
                line_diff(a,M,i,j)
                line_diff(a,I,i,j)
    return I

def mv_prod(M,x):
    n = len(x)
    y = [0]*n
    for i in xrange(n):
        for j in xrange(n):
            y[i] += x[j]*M[i][j]
    return y

# the matrix is not invertible anymore for k>=20, the recurrence rank is then 19
k = 19
M = [[dp(2*j) for j in xrange(i,i+k)] for i in xrange(k)]
B = [dp(2*i) for i in xrange(k,2*k)]
Minv = inverse(M)
# integer recurrence coefficients:
A = map(int,mv_prod(Minv,B))

# NB (a posteriori): the sequence seems to be http://oeis.org/A028452
# yet the coefficients computed are not exactly the same as those found on
# OEIS and their recurrence is of degree 23 instead of 19?!...
# Yet this works, so their recurrence might not be optimal...


## PART 3 ##
# Matrix exponentiation to compute the result
P = 10**8+7

class Matrice:
    def __init__(self,M):
        self.M = M
        self.m = len(M)
        self.n = len(M[0])

    def __getitem__(self,i):
        return self.M[i]
        
    def __mul__(self,A):
        assert(self.n==A.m)
        C = Matrice([[0 for _ in xrange(A.n)] for _ in xrange(self.m)])
        for i in xrange(self.m):
            for j in xrange(A.n):
                for k in xrange(self.n):
                    C[i][j] = (C[i][j]+self[i][k]*A[k][j])%P
        return C

    def copy(self):
       return Matrice([self[i][:] for i in xrange(self.m)])
    
    def __pow__(self,b):
        assert(self.m==self.n)
        result = Matrice([[int(i==j) for j in xrange(self.n)] for i in xrange(self.n)])
        A = self.copy()
        while b:
            if b & 1:
                result *= A
            A *= A
            b >>= 1
        return result

L = [[int(i==j+1) for j in xrange(k)] for i in xrange(k)]
L[0] = map((lambda x: x%P), A[::-1])
L = Matrice(L)
V = Matrice([[dp(2*i)%P] for i in xrange(k-1,-1,-1)])
R = L**(5*10**9999-(k-1))*V
print R[0][0]
