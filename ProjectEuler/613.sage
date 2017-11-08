# si (x,y) est un point a l'interieur du triangle rectangle de cotes
# X = 40 et Y = 30
# alors l'angle sous lequel l'hypotenuse est visible est
# alpha(x,y) = 3pi/2 - arctan((X-x)/y) - arctan((Y-y)/x)
# (decouper l'angle complementaire en trois parties facilement calculables)
# la proba en (x,y) est alpha(x,y) / 2pi
# a x fixe, on a 0 < y < ymax(x) = (X-x)*Y/X (par Thales)
# la proba sur tout le triangle (d'aire XY/2) est donc
# 1/(XY/2) Int_0^X Int_0^ymax(x) alpha(x,y) dy dx
# calculee explicitement ici avec Sage

X = 40
Y = 30
var("x,y")
assume(0<x)
assume(x<X)
res = integrate(integrate(3*pi/2-arctan((X-x)/y)-arctan((Y-y)/x),y,0,Y*(X-x)/X),x,0,X) / (2*pi * X*Y/2)
print res
print float(res)
