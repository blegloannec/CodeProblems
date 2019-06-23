#!/usr/bin/env python3

def orbs(V, L, R):
    for X in range(L,R+1):
        X3 = X**3
        if X3>=V:
            break
        Y = round((V-X3)**(1./3.))
        if X>Y:
            break
        if X!=D1 and X3+Y**3==V:
            return X,Y
    return None

if __name__=='__main__':
    L,R = map(int,input().split())
    D1,D2 = map(int,input().split())
    V = D1**3 + D2**3
    sol = orbs(V,L,R)
    if sol:
        print(*sol)
    else:
        print('VALID')
