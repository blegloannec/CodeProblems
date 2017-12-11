#!/usr/bin/env python3

# 2D hex grid as the projection of 3D discrete plane x+y+z = 0

class P:
    def __init__(self,x,y,z):
        self.x,self.y,self.z = x,y,z
    def __add__(self,B):
        return P(self.x+B.x,self.y+B.y,self.z+B.z)
    def dist(self):
        return max(abs(self.x),abs(self.y),abs(self.z))

D = {'n':P(0,1,-1),'s':P(0,-1,1),'ne':P(1,0,-1),'sw':P(-1,0,1),'nw':P(-1,1,0),'se':P(1,-1,0)}

I = input().split(',')
X = P(0,0,0)
dmax = 0
for d in I:
    X += D[d]
    dmax = max(dmax,X.dist())
print(X.dist())  # Part 1
print(dmax)      # Part 2
