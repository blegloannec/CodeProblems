#!/usr/bin/env python3

def conv(x):
    try:
        return int(x)
    except:
        return x

def op(a,b):
    if isinstance(a,str) or isinstance(b,str):
        a,b = str(a),str(b)
    return a+b

E,L,N = map(int,input().split())
X = list(map(conv,input().split()))
X += [X[-1]]*(N-len(X))
for l in range(1,L):
    for i in range(min(N-1,E-2+l),max(0,N-(L-l)-1),-1):
        X[i] = op(X[i-1],X[i])
print(X[N-1])
