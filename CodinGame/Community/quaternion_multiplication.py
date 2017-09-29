#!/usr/bin/env python3

class Quaternion:
    # a + bi + cj + dk
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a,self.b,self.c,self.d = a,b,c,d
    def __str__(self):
        S = []
        for (x,c) in [(self.b,'i'),(self.c,'j'),(self.d,'k'),(self.a,'')]:
            if x!=0:
                if S and x>0:
                    S.append('+')
                elif x<0:
                    S.append('-')
                y = abs(x)
                if y!=1:
                    S.append(str(y))
                S.append(c)
        return ''.join(S)
    def __add__(self,q):
        return Quaternion(self.a+q.a,self.b+q.b,self.c+q.c,self.d+q.d)
    def __sub__(self,q):
        return Quaternion(self.a-q.a,self.b-q.b,self.c-q.c,self.d-q.d)
    def __neg__(self):
        return Quaternion(-self.a,-self.b,-self.c,-self.d)
    def __mul__(self,q):
        return Quaternion(self.a*q.a-self.b*q.b-self.c*q.c-self.d*q.d,
                          self.a*q.b+self.b*q.a+self.c*q.d-self.d*q.c,
                          self.a*q.c+self.c*q.a+self.d*q.b-self.b*q.d,
                          self.a*q.d+self.d*q.a+self.b*q.c-self.c*q.b)


Tok = {'i':1,'j':2,'k':3,'+':0,'-':0,'$':0}

def parse_quaternion(S):
    S += '$'
    curr,sign = 0,1
    res = [0,0,0,0]
    for c in S:
        if '0'<=c<='9':
            curr = 10*curr + int(c)
        else:
            if 'i'<=c<='k' and curr==0:
                curr = 1
            if curr!=0:
                res[Tok[c]] = sign*curr
            curr,sign = 0,(-1 if c=='-' else 1)
    return Quaternion(*res)

def main():
    E = input()
    Q = list(map(parse_quaternion,E[1:-1].split(')(')))
    res = Quaternion(1)
    for q in Q:
        res = res*q
    print(res)

main()
