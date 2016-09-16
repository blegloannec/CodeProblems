#!/usr/bin/env python

# on pourrait envisager d'utiliser un arbre lexico contenant les nb
# premiers sans doublon de chiffre, mais bof...
# on backtrack pour trouver les decompositions sur chaque permutation
# runs in 9s (using pypy)

# algo de Heap pour les permutations
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

# Miller-Rabin deterministe 32 bits
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
            
def prime(n):
    if n<2:
        return False
    b = digits(n-1,2)
    for w in [2,7,61]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

# backtracking pour decomposer une permutation
def backtrack(A,i=0,x=0,X=[]):
    if i==len(A):
        if x==0:
            yield X
    else:
        x = 10*x+A[i]
        if (len(X)==0 or x>X[-1]) and prime(x):
            X.append(x)
            for B in backtrack(A,i+1,0,X):
                yield B
            X.pop()
        for B in backtrack(A,i+1,x,X):
            yield B

def main():
    cpt = 0
    for A in heap(9,range(1,10)):
        for _ in backtrack(A):
            cpt += 1
    print cpt

main()
