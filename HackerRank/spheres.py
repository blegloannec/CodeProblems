#!/usr/bin/env python3

# V(t) = A*t
# X(t) = A/2*t^2 + X0
# D2(t) = ((Ax1-Ax2)/2*t^2 + x01-x02)^2 + idem y et z
#       = (Kx*t^2 + Lx)^2 + ...
# D2'(t) = 4*Kx*(Kx*t^2+Lx)*t + ...
#        = 4*t*((Kx^2+Ky^2+Kz^2)*t^2 + Kx*Lx+Ky*Ly+Kz*Lz)
#        = 4*t*(K*t^2+L)
# nulle en 0 et +/-sqrt(-L/K)
# donc seul t = sqrt(-L/K) est un extrema a considerer

def main():
    T = int(input())
    for _ in range(T):
        R1,R2 = map(int,input().split())
        x1,y1,z1 = map(int,input().split())
        ax1,ay1,az1 = map(int,input().split())
        x2,y2,z2 = map(int,input().split())
        ax2,ay2,az2 = map(int,input().split())
        Kx,Ky,Kz = (ax1-ax2)/2,(ay1-ay2)/2,(az1-az2)/2
        Lx,Ly,Lz = x1-x2,y1-y2,z1-z2
        K = Kx*Kx + Ky*Ky + Kz*Kz
        L = Kx*Lx + Ky*Ly + Kz*Lz
        coll = False
        if K!=0 and -L/K>=0:
            t = (-L/K)**0.5
            d2 = (Kx*t*t + Lx)**2 + (Ky*t*t + Ly)**2 + (Kz*t*t + Lz)**2
            coll = (d2<=(R1+R2)**2)
        print('YES' if coll else 'NO')

main()
