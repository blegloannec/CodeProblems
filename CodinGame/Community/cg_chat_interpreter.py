#!/usr/bin/env python3

import re, sys
from collections import defaultdict

Context = {}
Stack = defaultdict(list)

def nick(w):
    return w[0]==w[-1]=='*'

def constStart(w):
    return w in ('a','an','me','you','u') or nick(w)

assignStart = ('youre','your','ur')

def parseExpr(i):
    x,i = parseConst(i)
    while x is not None and i<len(line):
        if line[i]=='squared':
            x *= x
            i += 1
        elif line[i]=='and':
            y,i = parseExpr(i+1)
            assert line[i]=='too'
            x += y
            i += 1
        elif line[i]=='but' and i+1<len(line) and line[i+1]=='not':
            y,i = parseExpr(i+2)
            assert line[i]=='though'
            x -= y
            i += 1
        elif line[i]=='by':
            y,i = parseExpr(i+1)
            assert line[i]=='multiplied'
            x *= y
            i += 1
        else:
            break
    return x,i

def parseConst(i):
    if line[i]=='me':
        assert len(Stack[speaker])>0
        return Stack[speaker][-1], i+1
    elif line[i] in ('you','u'):
        assert speaker in Context
        who = Context[speaker]
        assert len(Stack[who])>0
        return Stack[who][-1], i+1
    elif nick(line[i]):
        who = line[i][1:-1]
        assert len(Stack[who])>0
        return Stack[who][-1], i+1
    assert line[i] in ('a','an')
    i0 = i
    i += 1
    x = 1
    while i<len(line) and line[i] not in Noun:
        x <<= 1
        i += 1
    if i<len(line):
        if line[i] in Bad:
            x = -x
        i += 1
    else:
        x = None
        i = i0+1
    return x,i

def main():
    global speaker, line, Noun, Bad
    numGood,numBad = map(int,input().split())
    Noun = input().lower().split()
    Bad = input().lower().split()
    Noun += Bad
    numLines = int(input())
    for _ in range(numLines):
        line = re.sub(r"[,;.?!']", '', input().lower()).split()
        #print(line, file=sys.stderr)
        speaker = line[0]
        assert speaker[0]=='<' and speaker[-1]=='>'
        speaker = speaker[1:-1]
        i = 1
        currAssign = False
        while i<len(line):
            w = line[i]
            if not currAssign and nick(w):  # set context
                Context[speaker] = w[1:-1]
            elif w in assignStart:
                assert speaker in Context
                currAssign = True
            elif currAssign and constStart(w):  # expression
                x,i = parseExpr(i)
                if x is not None:
                    Stack[Context[speaker]].append(x)
                    currAssign = False
                continue
            elif w=='listen':
                assert speaker in Context
                who = Context[speaker]
                assert len(Stack[who])>0
                Stack[who].append(Stack[who][-1])
            elif w=='forget':
                assert speaker in Context
                who = Context[speaker]
                assert len(Stack[who])>0
                Stack[who].pop()
            elif w=='flip':
                assert speaker in Context
                who = Context[speaker]
                assert len(Stack[who])>=2
                Stack[who][-1],Stack[who][-2] = Stack[who][-2],Stack[who][-1]
            elif w in ('tell','telling'):
                assert speaker in Context
                who = Context[speaker]
                assert len(Stack[who])>0
                sys.stdout.write(str(Stack[who].pop()))
            i += 1
    sys.stdout.write('\n')
            
main()
