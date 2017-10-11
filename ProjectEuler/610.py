#!/usr/bin/env python3

## conversion code from pb 89
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
    res = []
    while n>0:
        for (c,v) in D:
            if n>=v:
                res.append(c)
                n -= v
                break
    return ''.join(res)
##

P0 = 0.14

def valid_minform(S): # as clever as can be...
    return int2rom(rom2int(S))==S

def valid_count(S): # how many letters can validly extend S
    return sum(int(valid_minform(S+c)) for c in C)

def prob(A): # prob of a letter when A<=7 letters are acceptable
    return P0/(1.-(7-A)*P0)

def int2rom_prob(n):
    res = ''
    p = 1.
    while n>0:
        for (c,v) in D:
            if n>=v:
                for a in c:
                    p *= prob(valid_count(res))
                    res += a
                n -= v
                break
    a = valid_count(res)
    p *= 1.-a*prob(a)  # prob of the final "#"
    return p

def main():
    E = P = 0.
    for i in range(1000):
        # numbers of the form MM...M{i} where {i} is the roman minimal form of i
        Pi = int2rom_prob(i)
        E += sum((P0**k*Pi) * (1000*k+i) for k in range(50))
        P += sum(P0**k*Pi for k in range(50))
    print(E/P)

main()
