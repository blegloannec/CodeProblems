#!/usr/bin/env python3 

C = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def rom2int(s):
    res = i = 0
    while i<len(s):
        if i+1<len(s) and C[s[i]]<C[s[i+1]]:
            res += C[s[i+1]]-C[s[i]]
            i += 2
        else:
            res += C[s[i]]
            i += 1
    return res

D = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]

def int2rom(n):
    rom = []
    while n>0:
        c,v = next(((c,v) for c,v in D if n>=v))
        rom.append(c)
        n -= v
    return ''.join(rom)

print(int2rom(rom2int(input())+rom2int(input())))
