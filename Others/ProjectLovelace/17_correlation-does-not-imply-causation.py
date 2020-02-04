def correlation_coefficient(x, y):
    n = len(x)
    xm = sum(x)/n
    ym = sum(y)/n
    sx = (sum((xi-xm)**2 for xi in x)/n)**0.5
    sy = (sum((yi-ym)**2 for yi in y)/n)**0.5
    cov = sum((xi-xm)*(yi-ym) for xi,yi in zip(x,y))/n
    r = cov / (sx*sy)
    return r

import numpy as np
def correlation_coefficient(x, y):
    return np.corrcoef(x,y)[0,1]
