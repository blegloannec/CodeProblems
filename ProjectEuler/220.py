#!/usr/bin/env python

import cairo

## Drawing for fun
R = {(0,1):(),(0,-1):(-1,0)}
def draw_a(ctx,d,n):
    if n>0:
        d = draw_a(ctx,d,n-1)
        d = (d[1],-d[0])
        d = draw_b(ctx,d,n-1)
        ctx.rel_line_to(*d)
        d = (d[1],-d[0])
    return d

def draw_b(ctx,d,n):
    if n>0:
        d = (-d[1],d[0])
        ctx.rel_line_to(*d)
        d = draw_a(ctx,d,n-1)
        d = (-d[1],d[0])
        d = draw_b(ctx,d,n-1)
    return d

def draw_dragon(n):
    surf = cairo.PDFSurface('out.pdf',300,250)
    ctx = cairo.Context(surf)
    ctx.set_line_width(1.)
    ctx.set_source_rgb(1.,0.,0.)
    d = (0,5)
    ctx.move_to(90,90)
    ctx.rel_line_to(*d)
    draw_a(ctx,d,n)
    ctx.stroke()
    surf.finish()

#draw_dragon(10)


## Actual resolution
# not that difficult, yet rather technical!

# NB STEPS
def F(n):
    return 2**n-1

# ROTATIONS
# Ra(n) et Rb(n) les nombres de R dans "a" et "b" derive n fois
# Ra(0) = Rb(0) = 0
# Ra(n) = Ra(n-1)+Rb(n-1)+2
# Rb(n) = Ra(n-1)+Rb(n-1)
# Ra(n) = 2^n
# Rb(n) = 2^n - 2
# Par symetrie, Lb(n) = 2^n et La(n) = 2^n - 2
# Soit Rota(n) le rotation de direction (en nb de R) induite
# par "a" derive n fois
# Rota(n) = Ra(n)-La(n) = 2
# et Rotb(n)= -2
# autrement dit la direction est simplement *inversee* dans les 2 cas
# et independamment de la profondeur de derivation

# DEPLACEMENTS
# Soit (Vax(N,n),Vay(D,n)) le vecteur de deplacement associe
# a n derivations de "a" pour la direction initiale D in {N,S,E,W}
# pour a, partant de D=N, on a successivement D = [N,S,W,E,E,S]
# Vax(N,n) = Vax(N,n-1) + Vbx(W,n-1) + 1
# Vay(N,n) = Vay(N,n-1) + Vby(W,n-1)
# pour b, partant de D=N, on a successivement D = [N,W,W,E,N,S]
# Vbx(N,n) = -1 + Vax(W,n-1) + Vbx(N,n-1)
# Vby(N,n) = Vay(W,n-1) + Vby(N,n-1)
# et l'on a (pour a et b), Vx(W),Vy(W) = -Vy(N),Vx(N)
# on voit que Vb(S) = Va(N) donc Vb = -Va
# Vax(N,n) = Vax(N,n-1)+Vay(N,n-1) + 1
# Vay(N,n) = Vay(N,n-1)-Vax(N,n-1)

def R(x,y):
    return (y,-x)

def L(x,y):
    return (-y,x)

def Inv(x,y):
    return (-x,-y)

def Va(D,n):
    if D==(1,0):
        return R(*Va((0,1),n))
    if D==(-1,0):
        return L(*Va((0,1),n))
    if D==(0,-1):
        return Inv(*Va((0,1),n))
    if n==0:
        return (0,0)
    Va0 = Va(D,n-1)
    return (Va0[0]+Va0[1]+1,Va0[1]-Va0[0])

def Vb(D,n):
    return Inv(*Va(D,n))

def Pa(D,n,m):
    if D==(1,0):
        return R(*Pa((0,1),n,m))
    if D==(-1,0):
        return L(*Pa((0,1),n,m))
    if D==(0,-1):
        return Inv(*Pa((0,1),n,m))
    if m==0:
        return (0,0)
    tinf = F(n-1)
    # a
    if m<tinf:
        return Pa(D,n-1,m)
    x,y = Va(D,n-1)
    D = R(*Inv(*D))
    # b
    if m<2*tinf:
        x1,y1 = Pb(D,n-1,m-tinf)
        return (x+x1,y+y1)
    x1,y1 = Vb(D,n-1)
    D = Inv(*D)
    # F
    x,y = x+D[0],y+D[1]
    return (x,y)

def Pb(D,n,m):
    if D==(1,0):
        return R(*Pb((0,1),n,m))
    if D==(-1,0):
        return L(*Pb((0,1),n,m))
    if D==(0,-1):
        return Inv(*Pb((0,1),n,m))
    if m==0:
        return (0,0)
    tinf = F(n-1)
    # L
    D = L(*D)
    # F
    x,y = D
    if m==1:
        return (x,y)
    # a
    if m<tinf+1:
        x1,y1 = Pa(D,n-1,m-1)
        return (x+x1,y+y1)
    x1,y1 = Va(D,n-1)
    x,y = x+x1,y+y1
    D = L(*Inv(*D))
    # b
    x1,y1 = Pb(D,n-1,m-tinf-1)
    return (x+x1,y+y1)

# MAIN
#x,y = Pa((0,1),10,500-1)
x,y = Pa((0,1),50,10**12-1)
print '%d,%d' % (x,y+1)
