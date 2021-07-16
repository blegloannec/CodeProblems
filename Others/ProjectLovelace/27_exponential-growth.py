import numpy as np
import matplotlib.pyplot as plt

def exponential_growth(x0, k, dt, N):
    X = [x0]
    for _ in range(N):
        X.append(X[-1]*(1+k*dt))
    return X

def eplot(x0, k, dt, N):
    X = np.linspace(0, N*dt, 1000)
    Y = x0*np.exp(k*X)
    plt.plot(X, Y)
    X = np.arange(0, (N+0.1)*dt, dt)
    Y = exponential_growth(x0, k, dt, N)
    print(Y)
    plt.plot(X, Y)

if __name__=='__main__':
    eplot(1, 1, 0.1, 10)
    #eplot(5, 1, 0.6, 3)
    #eplot(1, 2.5, 0.1, 5)
    plt.show()
