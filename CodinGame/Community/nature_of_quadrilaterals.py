#!/usr/bin/env python3

class Point:
    def __init__(self,x,y):
        self.x,self.y = x,y
    def __sub__(self,A):  # B-A le vecteur AB
        return Point(self.x-A.x,self.y-A.y)
    def norm2(self):      # norme au carre
        return self.x*self.x+self.y*self.y
    def __mul__(self,B):  # produit scalaire
        return self.x*B.x+self.y*B.y
    def __xor__(self,B):  # determinant
        return self.x*B.y-self.y*B.x

def parallelogram(A,B,C,D):
    AB,BC,CD,DA = B-A,C-B,D-C,A-D
    return AB^CD==BC^DA==0

def rhombus(A,B,C,D):
    AB,BC,CD,DA = B-A,C-B,D-C,A-D
    return AB.norm2()==BC.norm2()==CD.norm2()==DA.norm2()

def rectangle(A,B,C,D):
    AB,BC,CD,DA = B-A,C-B,D-C,A-D
    return AB*BC==BC*CD==CD*DA==0

def square(A,B,C,D):
    return rhombus(A,B,C,D) and rectangle(A,B,C,D)

def main():
    n = int(input())
    for _ in range(n):
        a,xa,ya,b,xb,yb,c,xc,yc,d,xd,yd = input().split()
        xa,ya,xb,yb,xc,yc,xd,yd = map(int,[xa,ya,xb,yb,xc,yc,xd,yd])
        Q = a+b+c+d
        A,B,C,D = Point(xa,ya),Point(xb,yb),Point(xc,yc),Point(xd,yd)
        if square(A,B,C,D):
            print(Q,'is a square.')
        elif rectangle(A,B,C,D):
            print(Q,'is a rectangle.')
        elif rhombus(A,B,C,D):
            print(Q,'is a rhombus.')
        elif parallelogram(A,B,C,D):
            print(Q,'is a parallelogram.')
        else:
            print(Q,'is a quadrilateral.')

main()
