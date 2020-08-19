#!/usr/bin/env python3

# For each enemy i, we first compute the time Lᵢ it takes to eliminate it.
# Greedy optimal (exchange argument):
#   Consider two enemies 1 and 2,
#   C₁₂ = D₁L₁ + D₂(L₁+L₂)
#   C₂₁ = D₂L₂ + D₁(L₂+L₁)
#   C₁₂ ≤ C₂₁  <=>  D₂L₁ ≤ D₁L₂  <=>  L₁/D₁ ≤ L₂/D₂
#   It is always optimal to pick them in Lᵢ/Dᵢ order.
# NB: it is the same as the scheduling problem 1 || ∑ wⱼCⱼ

class Enemy:
    def __init__(self):
        typ, hp, arm, dmg = input().split()
        hp = int(hp); arm = int(arm); self.dmg = int(dmg)
        dmg_taken = max(1, (10 if typ[0]=='C' else 20)-arm)
        self.life = (hp + dmg_taken-1) // dmg_taken
    def __lt__(self, B):
        return self.life*B.dmg < self.dmg*B.life

def main():
    N = int(input())
    E = sorted(Enemy() for _ in range(N))
    hp = 5000
    dmg = sum(e.dmg for e in E)
    for e in E:
        hp -= dmg * e.life
        dmg -= e.dmg
    print('FLEE' if hp<0 else hp)

main()
