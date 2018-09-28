#!/usr/bin/env python3

# l'arnaque est dans la generation de la sequence de points
# Xi = [xi] = [0 1]^2i [0] = F^2i * I
#      [yi]   [1 1]    [C]
# Xi.Xj = tXi * Xj = t(F^2i*I)*(F^2j*I) = tI * tF^2i * F^2j * I
# or F est symetrique tF = F
# Xi.Xj = tI * F^2(i+j) * I
# il suffit donc de calculer les tI * F^2(i+j) * I = F^2(i+j)_{2,2} * C^2
# pour tous 1 <= i,j <= n avec i =/= j, i.e. tous les 2 < k < 2n

class Matrix2:
    def __init__(self,a=1,b=0,c=0,d=1):
        self.m00,self.m01,self.m10,self.m11 = a,b,c,d
    def __mul__(self,B):
        return Matrix2((self.m00*B.m00+self.m01*B.m10)%P,(self.m00*B.m01+self.m01*B.m11)%P,(self.m10*B.m00+self.m11*B.m10)%P,(self.m10*B.m01+self.m11*B.m11)%P)
    def __pow__(self,n):
        if n==0:
            return Matrix2()
        if n&1==0:
            return (self*self)**(n>>1)
        return self*(self*self)**(n>>1)

def main():
    global P
    C,P,n = map(int,input().split())
    C %= P
    F2 = Matrix2(0,1,1,1)**2
    M = F2**2
    S = set()
    for ipj in range(3,2*n):
        M *= F2
        S.add((M.m11*C*C)%P)
    print(len(S)%P)

main()
