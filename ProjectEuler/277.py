#!/usr/bin/env python

def modco(n):
    if n%3==0:
        return n/3
    if n%3==1:
        return (4*n+2)/3
    return (2*n-1)/3

def strco(n,l):
    s = []
    for i in xrange(l):
        if n%3==0:
            n = n/3
            s.append('D')
        elif n%3==1:
            n = (4*n+2)/3
            s.append('U')
        else:
            n = (2*n-1)/3
            s.append('d')
    return ''.join(s)

# trouve le plus petit n>=m qui commence
# par la sequence s[i:]
def minstart(s,m,i=0):
    if i==len(s):
        return m
    if s[i]=='D':
        return 3*minstart(s,(m+2)/3,i+1)
    if s[i]=='U':
        a = minstart(s,(4*m+2+2)/3,i+1)
        while (3*a-2)%4!=0 or ((3*a-2)/4)%3!=1:
            a = minstart(s,a+1,i+1)
        return (3*a-2)/4
    a = minstart(s,(2*m-1+2)/3,i+1)
    while (3*a+1)%2!=0 or ((3*a+1)/2)%3!=2:
        a = minstart(s,a+1,i+1)
    return (3*a+1)/2

def main():
    #s,b = 'DdDddUUdDD',10**6
    s,b = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd',10**15
    a = minstart(s,b+1)
    print a
    #print s
    #print strco(a,len(s))

main()
