#!/usr/bin/env python

# enumerations (naive) des partitions possibles en chiffres
# sous la forme (n1,n2,n3)
# ni est le nombres de chiffres apparaissant i fois
# 18 = n1 + 2*n2 + 3*n3 et n1+n2+n3 <= 10
def part(N):
    for n3 in xrange(N/3+1):
        for n2 in xrange(N/2+1):
            n1 = N-2*n2-3*n3
            if n1>=0 and n1+n2+n3<=10:
                yield (n1,n2,n3)

def fact(n):
    return 1 if n<2 else n*fact(n-1)

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)/p

def main():
    N = 18
    C = 0
    for (n1,n2,n3) in part(N):
        C0 = binom(10,n1)*binom(10-n1,n2)*binom(10-n1-n2,n3)*fact(N)/(2**n2*6**n3)
        # 0 en premiere position, parmi les n1
        if n1>=1:
            C0 -= binom(9,n1-1)*binom(9-(n1-1),n2)*binom(9-(n1-1)-n2,n3)*fact(N-1)/(2**n2*6**n3)
        # 0 en premiere position, parmi les n2
        if n2>=1:
            C0 -= binom(9,n1)*binom(9-n1,n2-1)*binom(9-n1-(n2-1),n3)*fact(N-1)/(2**(n2-1)*6**n3)
        # 0 en premiere position, parmi les n3
        if n3>=1:
            C0 -= binom(9,n1)*binom(9-n1,n2)*binom(9-n1-n2,n3-1)*fact(N-1)/(2**(n2+1)*6**(n3-1))
        C += C0
    print C

main()
