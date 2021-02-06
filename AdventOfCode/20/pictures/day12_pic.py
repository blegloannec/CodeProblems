#!/usr/bin/env python3

import sys, math, cmath
import matplotlib.pyplot as plt
import matplotlib.animation as animation

DIR = {'N':complex(0,1), 'S':complex(0,-1), 'E':complex(1,0), 'W':complex(-1,0)}

I = [L.strip() for L in sys.stdin.readlines()]

def sail(d, part2=False):
    z = complex(0,0)
    X = []
    Y = []
    for L in I:
        o, v = L[0], int(L[1:])
        if   o=='L': d *= cmath.rect(1, math.radians( v))
        elif o=='R': d *= cmath.rect(1, math.radians(-v))
        elif o=='F': z += v*d
        elif part2:  d += v*DIR[o]
        else:        z += v*DIR[o]
        X.append(z.real)
        Y.append(z.imag)
    return X,Y

def animate(X, Y):
    minX, maxX = min(X), max(X)
    minY, maxY = min(Y), max(Y)
    fig, ax = plt.subplots()
    plt.rc('font', size=8)
    plt.tight_layout(pad=0.4)
    ax.set_xlim(minX, maxX)
    ax.set_ylim(minY, maxY)
    ax.set_facecolor('#0f0f23')
    line, = ax.plot([], [], marker='*', ls='--', color='#cccccc', lw=1., mfc='#ffff66', mec='#ffff66', ms=6., mew=0.)
    def frame(i):
        line.set_data(X[:i+1], Y[:i+1])
        return line,
    return animation.FuncAnimation(fig, frame, interval=10, blit=True, save_count=len(X)+1)

# Part 1
anim = animate(*sail(DIR['E']))
#anim.save('anim12_1.mp4')
plt.show()
plt.close()

# Part 2
anim = animate(*sail(complex(10,1), True))
#anim.save('anim12_2.mp4')
plt.show()
