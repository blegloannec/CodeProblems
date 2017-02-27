#!/usr/bin/env python3

gate_sym = ['@','~','&','|','+','^','-','=','<','>']
switch_sym = ['<','>']

GatesNum = {}
Gates = []
IS = []

def is_gate(x,y):
    if G[x][y] not in gate_sym:
        return False
    y -= 1
    while y>=0 and G[x][y]==' ':
        y -= 1
    return (y>=0 and G[x][y]=='[')

def follow(x,y,x0=None,y0=None):
    if G[x][y]==' ': # must be a switch
        yg = y+1
        while yg==' ':
            yg += 1
        if G[x][yg] not in switch_sym:
            yg = y-1
            while yg==' ':
                yg -= 1
        assert(G[x][yg] in switch_sym)
        # returning the number of the switch + the output direction
        return (follow(x,yg),'<' if y<yg else '>')
    elif is_gate(x,y):
        if (x,y) in GatesNum:
            return GatesNum[x,y]
        I = []
        yi = y
        while G[x][yi]!='[':
            if G[x-1][yi]=='|':
                I.append(follow(x-1,yi,x,y))
            yi -= 1
        yi = y+1
        while G[x][yi]!=']':
            if G[x-1][yi]=='|':
                I.append(follow(x-1,yi,x,y))
            yi += 1
        # sanity checks
        if G[x][y]=='~' or G[x][y] in switch_sym:
            assert(len(I)==1)
        elif G[x][y]!='@':
            assert(len(I)==2)
        # registering gate, at the end of the DFS so that
        # it is already in a topological order
        GatesNum[x,y] = len(Gates)
        Gates.append((G[x][y],I))
        if G[x][y] in switch_sym:
            IS.append((x,y))
        return GatesNum[x,y]
    elif G[x][y]=='|':
        return follow(x-1,y,x,y)
    elif G[x][y]=='-':
        assert(y!=y0)
        return follow(x,y+y-y0,x,y)
    elif G[x][y]=='+':
        if G[x-1][y] in ['|','+']:
            return follow(x-1,y,x,y)
        else:
            for yn in [y-1,y+1]:
                if yn!=y0 and 0<=yn<W and G[x][yn] in ['-','+']:
                    return follow(x,yn,x,y)
        assert(False)
    else:
        assert(G[x][y] in ['0','1'])
        if (x,y) in GatesNum:
            return GatesNum[x,y]
        GatesNum[x,y] = len(Gates)
        Gates.append(('i',int(G[x][y])))
        IS.append((x,y))
        return GatesNum[x,y]

def eval():
    V = []
    def val(j):
        if isinstance(j,tuple): # switch output
            j,d = j
            return V[j] if d==Gates[j][0] else 0
        else:
            return V[j]
    # evaluation follows the topological order
    for i in range(len(Gates)):
        t,x = Gates[i]
        if t=='i':
            V.append(x)
        elif t=='~':
            V.append(1-val(x[0]))
        elif t=='&':
            V.append(val(x[0])&val(x[1]))
        elif t=='|':
            V.append(val(x[0])|val(x[1]))
        elif t=='+':
            V.append(val(x[0])^val(x[1]))
        elif t=='^':
            V.append(1-(val(x[0])&val(x[1])))
        elif t=='-':
            V.append(1-(val(x[0])|val(x[1])))
        elif t=='=':
            V.append(1-(val(x[0])^val(x[1])))
        elif t=='-':
            V.append(1-(val(x[0])|val(x[1])))
        elif t=='@':
            # unclear if all/any in the pb statement
            V.append(all(val(j) for j in x))
        else: # switch
            assert(t in switch_sym)
            V.append(val(x[0]))
    return V[-1]

# subsets in lex order
def parmi(n,p,k=0):
    if p==0:
        yield []
    else:
        for i in range(k,n-p+1):
            for S in parmi(n,p-1,i+1):
                S.append(i)
                yield S

def main():
    global H,W,G,IS,Gates
    H,W = map(int,input().split())
    G = []
    for _ in range(H):
        G.append(input())
    G = G[::-1]
    x0,y0 = H-1,G[H-1].find('@')
    follow(x0,y0)
    # managing inputs/switches in top-bot, left-right order
    cptI,cptS = 1,1
    JS = []
    for x in sorted(IS,key=(lambda x: (H-x[0],x[1]))):
        n = GatesNum[x]
        if Gates[n][0]=='i':
            JS.append((n,'I%d'%cptI))
            cptI += 1
        else:
            JS.append((n,'K%d'%cptS))
            cptS += 1
    # testing solutions in order over size, then lex
    RevD = {'<':'>','>':'<'}
    n = len(JS)
    Gates0 = Gates[:]
    for k in range(1,n+1):
        for X in parmi(n,k):
            Gates = Gates0[:]
            for x in reversed(X):
                g = JS[x][0]
                t,v = Gates[g]
                if t=='i':
                    Gates[g] = (t,1-v)
                else:
                    Gates[g] = (RevD[t],v)
            if eval(): # solution found
                for x in reversed(X):
                    print(JS[x][1])
                return

main()
