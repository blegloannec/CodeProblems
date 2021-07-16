def temperature_statistics(T):
    mean = sum(t for t in T)/len(T)
    std  = (sum((t-mean)**2 for t in T)/len(T))**0.5
    return mean, std

import numpy as np
def temperature_statistics(T):
    return np.mean(T), np.std(T)

if __name__=='__main__':
    T = [4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5, 16.6, 11.2, 7.3]
    print(temperature_statistics(T))
