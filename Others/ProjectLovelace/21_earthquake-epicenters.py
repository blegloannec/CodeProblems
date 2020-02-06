import numpy as np

# (x-xi)^2 + (y-yi)^2 = ri^2 (i)
# (i)-(j) gives:
#      (2x-xi-xj)(xj-xi) + (2y-yi-yj)(yj-yi) = ri^2-rj^2
# i.e. 2(xj-xi)x + 2(yj-yi)y = ri^2-rj^2 + xj^2-xi^2 + yj^2-yi^2

v = 6.0  # velocity of seismic waves [km/s]

def earthquake_epicenter(x1, y1, t1, x2, y2, t2, x3, y3, t3):
    r1, r2, r3 = t1*v, t2*v, t3*v
    M = [[2.*(x2-x1), 2.*(y2-y1)],
         [2.*(x3-x1), 2.*(y3-y1)]]
    B = [r1**2-r2**2 + x2**2-x1**2 + y2**2-y1**2,
         r1**2-r3**2 + x3**2-x1**2 + y3**2-y1**2]
    A = np.linalg.solve(M,B)
    return tuple(A)

if __name__=='__main__':
    print(earthquake_epicenter(8.382353226, -58.003720814, 12.860754193, -13.590571819, 73.976069096, 22.847488548, 77.291172370, 7.508764456, 5.767809783))
