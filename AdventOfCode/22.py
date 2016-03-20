#!/usr/bin/env python

start_bh = 71
bd = 10
start_ph = 50
start_pm = 500
MM = 10000000
hard_mode = False

memo = {}

def bossturn(bh,ph,pm,st,pt,rt):
    if pt>0:
        bh -= 3
        pt -= 1
    if bh<=0:
        return 0
    if st>0:
        ph -= max(1,bd-7)
        st -= 1
    else:
        ph -= bd
    if rt>0:
        pm += 101
        rt -= 1
    return playerturn(bh,ph,pm,st,pt,rt)

def playerturn(bh,ph,pm,st,pt,rt):
    h = (bh,ph,pm,st,pt,rt)
    if h in memo:
        return memo[h]
    if hard_mode:
        ph -= 1 # hard mode
    if ph<=0:
        return MM
    if st>0:
        st -= 1
    if pt>0:
        bh -= 3
        pt -= 1
        if bh<=0:
            return 0
    if rt>0:
        pm += 101
        rt -=1
    if pm<53:
        return MM
    spells = [bossturn(bh-4,ph,pm-53,st,pt,rt)+53]
    if pm>=73:
        spells.append(bossturn(bh-2,ph+2,pm-73,st,pt,rt)+73)
    if st==0 and pm>=113:
        spells.append(bossturn(bh,ph,pm-113,6,pt,rt)+113)
    if pt==0 and pm>=173:
        spells.append(bossturn(bh,ph,pm-173,st,6,rt)+173)
    if rt==0 and pm>=229:
        spells.append(bossturn(bh,ph,pm-229,st,pt,5)+229)
    res = min(spells)
    memo[h] = res
    return res

def main():
    global hard_mode
    print playerturn(start_bh,start_ph,start_pm,0,0,0)
    hard_mode = True
    memo.clear()
    print playerturn(start_bh,start_ph,start_pm,0,0,0)
    

main()
