from math import radians, sqrt, asin, sin, cos

R  = 6372.1  # Radius of the Earth [km]

def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1 = radians(lat1), radians(lon1)
    lat2, lon2 = radians(lat2), radians(lon2)
    d = 2.*R*asin(sqrt(sin((lat2-lat1)/2.)**2 + cos(lat1)*cos(lat2)*sin((lon2-lon1)/2.)**2))
    return d