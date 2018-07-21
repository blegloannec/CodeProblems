#!/usr/bin/env python

def chiffres10(n):
    c = []
    while n>0:
        c.append(n%10)
        n /= 10
    return c

def somme_chiffres10(n):
    return sum(chiffres10(n))

def problem65():
    f = [2]
    for i in range(34):
        f += [1,2*(i+1),1]
    # rationnels de la fraction continue
    p0,p1 = 0,1
    #q0,q1 = 1,0
    for i in range(100):
        p1,p0 = p1*f[i]+p0,p1
        #q1,q0 = q1*f[i]+q0,q1
    print somme_chiffres10(p1)

problem65()
