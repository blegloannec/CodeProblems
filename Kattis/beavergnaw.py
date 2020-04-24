#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi

# Vtot = πD(D/2)² = πD³/4
# Vrem = 2 ∫πr²dr + πd(d/2)²
#      = π/12(D³-d³) + πd³/4
#      = πD³/12 + πd³/6
# V = Vtot - Vrem
#   = πD³/6 - πd³/6
# d³ = D³ - 6V/π

while True:
    L = input().strip()
    if L=='0 0':
        break
    D,V = map(float, L.split())
    d = (D**3-6.*V/pi)**(1./3.)
    print(d)
