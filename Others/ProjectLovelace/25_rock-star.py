def rock_temperature(S, a, e):
    T = ((1.-a)*S/(4.*e*5.670374419e-8))**(1./4.)
    return T-273.15