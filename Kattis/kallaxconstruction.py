#!/usr/bin/env python3

INF = float('inf')

def dp_pack(PrevPack, TargPack):
    # PrevPack = sorted list of available (adv., real) values
    # TargPack = list of targeted values
    TargPack.sort()
    B = TargPack[-1] + PrevPack[-1][0]  # <= 2000
    # DP[b] = min real value of making adv. value b from previous packs
    DP = [INF]*(B+1)
    DP[0] = 0
    for a,r in PrevPack:
        for b in range(0, B-a+1):
            if DP[b]<INF:
                DP[b+a] = min(DP[b+a], DP[b]+r)
    # gathering real values for targeted adv. packs
    Pack = []
    b = B
    curr_r = None
    for t in reversed(TargPack):
        while b>=t:
            if DP[b]<INF:
                curr_r = DP[b]
            b -= 1
        Pack.append((t, curr_r))
    Pack.reverse()
    return Pack

def main():
    B = int(input())
    K = int(input())
    Pack = [list(map(int, input().split()[1:])) for _ in range(K)]
    Pack[0] = sorted((a,a) for a in Pack[0])
    for i in range(1,K):
        Pack[i] = dp_pack(Pack[i-1], Pack[i])
    res = INF
    for i in range(K):
        for a,r in Pack[i]:
            if r>=B and a<res:
                res = a
    print(res if res<INF else 'impossible')

main()
