#!/usr/bin/env python3

def simulate(N):
    N = min(N, 100)
    Top = list(range(19,0,-2))
    TopFull = [True]*10
    n = N
    r = 0
    while n>0:
        if TopFull[r]:
            TopFull[r] = False
            Top[r] -= 1
            n -= 1
            r = 0
        else:
            x = min(n, 4, Top[r])
            Top[r] -= x
            n -= x
            r += 1
    Bot = [int(i<N) for i in range(10)]
    BotTrail = [True]*10
    n = N-10
    r = 9
    while n>0:
        if BotTrail[r]:
            BotTrail[r] = False
            r = 9
        else:
            x = min(n, 2)
            Bot[r] += x
            n -= x
            r -= 1
    return Top, Bot

def draw(Top, Bot):
    O = ['+=====================+']
    for i in range(10):
        r = Top[i]//2
        l = Top[i]-r
        m = 19-2*i-l-r
        O.append(' '*(i+1) + '\\' + 'o'*l + ' '*m + 'o'*r  + '/')
    O.append('           X')
    for i in range(10):
        l = 1+2*i
        r = (l-Bot[i])//2
        l -= Bot[i]+r
        O.append(' '*(10-i) + '/' + ' '*l + 'o'*Bot[i] + ' '*r + '\\')
    O.append('+=====================+')
    return '\n'.join(O)

if __name__=='__main__':
    input()
    top = sum(input().count('o') for _ in range(10))
    input()
    bot = sum(input().count('o') for _ in range(10))
    input()
    N = int(input())
    if top+bot!=100:
        print('BROKEN HOURGLASS')
    else:
        print(draw(*simulate(bot+N)))
