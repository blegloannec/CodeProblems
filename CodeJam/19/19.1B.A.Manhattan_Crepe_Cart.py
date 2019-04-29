#!/usr/bin/env python3

def best_coord(A):
    CurrVal = sum(int(d==-1) for _,d in A)
    MaxPos, MaxVal = 0, CurrVal
    i = 0
    while i<len(A):
        CurrPos = A[i][0]
        CurrVal += A[i][1]
        i += 1
        while i<len(A) and A[i][0]==CurrPos:
            CurrVal += A[i][1]
            i += 1
        if CurrVal>MaxVal:
            MaxPos, MaxVal = CurrPos, CurrVal
    return MaxPos

if __name__=='__main__':
    T = int(input())
    for t in range(1,T+1):
        P,_ = map(int,input().split())
        X,Y = [],[]
        for _ in range(P):
            x,y,d = input().split()
            x,y = int(x),int(y)
            if d=='E':
                X.append((x+1,1))
            elif d=='W':
                X.append((x,-1))
            elif d=='N':
                Y.append((y+1,1))
            else:
                Y.append((y,-1))
        X.sort()
        Y.sort()
        print('Case #%d: %d %d' % (t, best_coord(X), best_coord(Y)))
