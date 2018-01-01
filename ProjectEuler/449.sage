z,t = var('z,t')
a,b = 3,1

# parametric equations of the ellipsoid in the plane y=0
Z(t) = 2*b*t-b
X(t) = sqrt(a^2*(1-Z(t)^2/b^2))

# parametric equations of the covered ellipsoid in the plane y=0
DZ(t) = diff(Z(t),t)
DX(t) = diff(X(t),t)
DN(t) = sqrt(DZ(t)^2+DX(t)^2)
CZ(t) = Z(t) - DX(t)/DN(t)
CX(t) = X(t) + DZ(t)/DN(t)

# volumes
V = integral(pi*X(t)^2*DZ(t),t,0,1)
CV = integral(pi*CX(t)^2*diff(CZ(t),t),t,0,1)
print (CV-V).numerical_approx()
