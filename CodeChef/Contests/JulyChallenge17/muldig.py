#!/usr/bin/env python3

B = int(input())
x = B
y = B+2
z = B+4
ux = B+8  # de taille (B-1) + B(B-1) = B^2-1
uy = ux+B*B-1
aux = 10**5-2
aux0 = 10**5-1

L = []
def instr(a,b,c):
    L.append('%d %d %d' % (a,b,c))

def non_zero(a,c):
    instr(a,0,c)

def incr(a,c):
    instr(1,a,c)

def decr(a,c):
    incr(a,c)
    if B==3:
        instr(2,c,c)
    else:
        incr(c,c)
        instr(c,B-3,c)

def both(a,b,c):
    instr(a,b,c)
    decr(c,c)

def ret(x,i,c):
    instr(2,x,aux0)
    both(i,aux0,c)

def add(x,i,c):
    instr(i,x,c)

def gen():
    # conversion X en unaire
    for i in range(B-1):
        non_zero(x+1,ux+i)
        decr(x+1,x+1)
    for i in range(B-1):
        for j in range(B):
            non_zero(x,ux+B-1+B*i+j)
        decr(x,x)
    # conversion Y en unaire
    for i in range(B-1):
        non_zero(y+1,uy+i)
        decr(y+1,y+1)
    for i in range(B-1):
        for j in range(B):
            non_zero(y,uy+B-1+B*i+j)
        decr(y,y)
    # multiplication
    for i in range(B*B-1):
        for j in range(B*B-1):
            both(ux+i,uy+j,aux)
            for k in range(3,-1,-1):
                add(z+k,aux,z+k)
                ret(z+k,aux,aux)
            #instr(-1,0,0)

def prog():
    if B==3:
        print(0,1,2)
        print(1,2,0)
        print(1,0,0)
    elif B==5:
        print(0,1,2,3,4)
        print(1,2,3,4,0)
        print(1,0,0,0,0)
        print(1,0,0,0,0)
        print(1,0,1,0,0)
    else:
        print(0,1,2,3,4,5,6)
        print(1,2,3,4,5,6,0)
        print(1,0,0,0,0,0,0)
        print(1,0,0,0,0,0,0)
        print(1,0,0,0,1,0,0)
        print(1,0,0,0,2,0,0)
        print(1,0,0,0,3,0,0)
    gen()
    print(len(L))
    print('\n'.join(L))

prog()
