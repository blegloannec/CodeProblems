def babylonian_sqrt(S):
    x = S/2.
    if x>0.:
        for _ in range(1000):
            x = (x+S/x)/2.
    return x