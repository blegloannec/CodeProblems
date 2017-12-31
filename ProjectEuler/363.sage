v,t = var('v,t')
Px0,Py0 = 1,0
Px1,Py1 = 1,v
Px2,Py2 = v,1
Px3,Py3 = 0,1

Qx0,Qy0 = Px0+(Px1-Px0)*t,Py0+(Py1-Py0)*t
Qx1,Qy1 = Px1+(Px2-Px1)*t,Py1+(Py2-Py1)*t
Qx2,Qy2 = Px2+(Px3-Px2)*t,Py2+(Py3-Py2)*t

Rx0,Ry0 = Qx0+(Qx1-Qx0)*t,Qy0+(Qy1-Qy0)*t
Rx1,Ry1 = Qx1+(Qx2-Qx1)*t,Qy1+(Qy2-Qy1)*t

# parametric equations of the curve
Bx(v,t) = Rx0+(Rx1-Rx0)*t
By(v,t) = Ry0+(Ry1-Ry0)*t

# area
A(v) = integral( By(v,t)*diff(Bx(v,t),t) , t,1,0)

# value for v
v0 = solve(A(v) == pi/4, v)[0].rhs()

# arc length
L(t) = sqrt( diff(Bx(v0,t),t)^2 + diff(By(v0,t),t)^2 )
l,_ = numerical_integral(L,0,1)

# result
p = 100*(l-pi/2)/(pi/2)
print p.numerical_approx()
