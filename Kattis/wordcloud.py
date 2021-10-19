#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Tag_cloud

import sys
input = sys.stdin.readline

ceil_div = lambda p,q: (p+q-1)//q
P = lambda cmax: lambda c: 8 + ceil_div(40*(c-4), cmax-4)

def cloud(Words, width, sep=10):
    # NB: words already given in order
    cmax = max(c for _,c in Words)
    Pts = P(cmax)
    Cloud = []
    l = width
    for (word,c) in Words:
        h = Pts(c)
        w = ceil_div(9*len(word)*h, 16)
        if l+sep+w > width:
            Cloud.append([(w,h, word)])
            l = w
        else:
            Cloud[-1].append((w,h, word))
            l += sep+w
    height = sum(max(h for _,h,_ in L) for L in Cloud)
    return (width,height, Cloud)

def svg(width,height, Cloud, sep=10, out='cloud.svg'):
    SVG = [f'<svg width="{width}pt" height="{height}pt">']
    y = 0
    for L in Cloud:
        x = 0
        y += max(h for _,h,_ in L)
        for w,h,word in L:
            SVG.append(f'<text x="{x}pt" y="{y}pt" style="font-family: Courier New; font-size: {h}pt;">{word}</text>')
            x += sep+w
    SVG.append('</svg>')
    with open(out, 'w') as F:
        F.write('\n'.join(SVG))

def main():
    T = 1
    while True:
        W,N = map(int, input().split())
        if W==N==0:
            break
        Words = []
        for _ in range(N):
            w,c = input().split()
            c = int(c)
            #assert c >= 5  # already filtered
            Words.append((w,c))
        _,H, Cloud = cloud(Words, W)
        #svg(W,H, Cloud, out=f'cloud{T}.svg')
        print(f'CLOUD {T}: {H}')
        T += 1

main()
