#!/usr/bin/env python3

S = 4

def find(w,i,x,y,used=0):
    if B[x][y]!=w[i]:
        return False
    if i==len(w)-1:
        return True
    used |= 1<<(S*x+y)
    for vx in range(x-1,x+2):
        if 0<=vx<S:
            for vy in range(y-1,y+2):
                if 0<=vy<S and (used>>(S*vx+vy))&1==0:
                    if find(w,i+1,vx,vy,used):
                        return True
    return False

def boggle(w):
    return any(find(w,0,i,j) for i in range(S) for j in range(S))

def main():
    global B
    B = [input() for _ in range(S)]
    N = int(input())
    for _ in range(N):
        w = input()
        print('true' if boggle(w) else 'false')

main()
