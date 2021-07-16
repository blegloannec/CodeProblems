from math import sqrt

def habitable_exoplanet(L, r):
    ri = sqrt(L/1.1)
    ro = sqrt(L/0.54)
    habitability = 'too hot' if r<ri else 'too cold' if r>ro else 'just right'
    return habitability