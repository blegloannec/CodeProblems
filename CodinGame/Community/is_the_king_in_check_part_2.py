#!/usr/bin/env python3

def Bcheck(i,j):
    for di,dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
        vi = i+di; vj = j+dj
        while 0<=vi<8 and 0<=vj<8:
            if B[vi][vj]=='k':
                return True
            elif B[vi][vj]!='_':
                break
            vi += di; vj += dj
    return False

def Rcheck(i,j):
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        vi = i+di; vj = j+dj
        while 0<=vi<8 and 0<=vj<8:
            if B[vi][vj]=='k':
                return True
            elif B[vi][vj]!='_':
                break
            vi += di; vj += dj
    return False

def Qcheck(i,j):
    return Bcheck(i,j) or Rcheck(i,j)

def Ncheck(i,j):
    for di,dj in ((-1,-2),(-2,-1),(1,-2),(-2,1),(1,2),(2,1),(-1,2),(2,-1)):
        vi = i+di; vj = j+dj
        if 0<=vi<8 and 0<=vj<8 and B[vi][vj]=='k':
            return True
    return False

Xcheck = {'B':Bcheck, 'R':Rcheck, 'Q':Qcheck, 'N':Ncheck}

def main():
    global B
    B = [input().split() for _ in range(8)]
    for i in range(8):
        for j in range(8):            
            if B[i][j] in Xcheck:
                if Xcheck[B[i][j]](i,j):
                    print('Check')
                    return
    print('No Check')

main()
