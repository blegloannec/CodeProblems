#!/usr/bin/env python3

# Very classic "trick", used in many puzzles...
# Peter Winkler, Mathematical Mind-Benders
# http://cristal.univ-lille.fr/~jdelahay/pls/2017/288.pdf
# http://images.math.cnrs.fr/Fourmis-auto-tamponneuses.html

L = int(input())
N = int(input())
print(max(max(p, L-p) for p in map(int, input().split())))
