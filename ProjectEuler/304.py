#!/usr/bin/env python

# runs in 11s with pypy

# Miller-Rabin deterministe 64 bits
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

def miller_rabin(n):
    b = digits(n-1,2)
    for w in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True


# Fibonacci
P = 1234567891011

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

def fibo(n):
    F = Matrice([[1,1],[1,0]])**n
    return F[0][0],F[0][1]


# Main
def main():
    a = 10**14+1
    cpt = 0
    s = 0
    while cpt<10**5:
        if cpt>0: # 2 steps
            f1,f0 = (f1+f0)%P,f1
            f1,f0 = (f1+f0)%P,f1
        if miller_rabin(a):
            if cpt==0:
                # in the problem statement fibo(0) = 0, so -1 shift
                f1,f0 = fibo(a-1)
            s = (s+f1)%P
            cpt += 1
        a += 2
    print s

main()
