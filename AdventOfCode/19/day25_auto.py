#!/usr/bin/env python3

import sys
from collections import deque

P = list(map(int,sys.stdin.readline().strip().split(',')))

to_ascii = lambda s: list(map(ord,s))
to_str = lambda l: ''.join(map(chr,l))

class IntcodeComputer:
    def __init__(self, P, In=None):
        self.P = P[:] + [0]*10**3  # program copy & padding
        self.i = 0
        if In is None:
            self.In = deque()
        elif isinstance(In, list):
            self.In = deque(In)
        else:
            assert isinstance(In, deque)
            self.In = In
        self.Out = deque()
        self.halt = False
        self.base = 0
    
    def push_in(self, s):
        self.In += to_ascii(s)
    
    def clear_out(self):
        self.Out.clear()
    
    def flush_out(self):
        s = to_str(self.Out)
        self.clear_out()
        return s
    
    def run(self):
        assert not self.halt
        value = lambda k: self.P[self.i+k]
        mode  = lambda k: (value(0)//10**(1+k))%10
        addr  = lambda k: self.base+value(k) if mode(k)==2 else value(k)
        param = lambda k: value(k) if mode(k)==1 else self.P[addr(k)]
        while True:
            op = value(0) % 100
            if   op==1:  # add
                self.P[addr(3)] = param(1) + param(2)
                self.i += 4
            elif op==2:  # mul
                self.P[addr(3)] = param(1) * param(2)
                self.i += 4
            elif op==3:  # input
                #if not self.In:
                #   self.In += to_ascii(sys.stdin.readline())
                if self.In:
                    x = self.In.popleft()
                    #sys.stdout.write(chr(x))
                    self.P[addr(1)] = x
                    self.i += 2
                else:
                    break
            elif op==4:  # output
                self.Out.append(param(1))
                #sys.stdout.write(chr(self.Out[-1]))
                self.i += 2
            elif op==5:  # jnz
                if param(1)!=0:
                    self.i = param(2)
                else:
                    self.i += 3
            elif op==6:  # jz
                if param(1)==0:
                    self.i = param(2)
                else:
                    self.i += 3
            elif op==7:  # lt
                self.P[addr(3)] = 1 if param(1)<param(2) else 0
                self.i += 4
            elif op==8:  # eq
                self.P[addr(3)] = 1 if param(1)==param(2) else 0
                self.i += 4
            elif op==9:  # incr base
                self.base += param(1)
                self.i += 2
            else:
                assert op==99
                self.halt = True
                break


Dir = ['north', 'south', 'east', 'west']
InvDir = {'north':'south', 'south':'north', 'east':'west', 'west':'east', None:None}
DoNotTake = ['photons', 'molten lava', 'giant electromagnet', 'escape pod', 'infinite loop']
SecCheck = '== Security Checkpoint =='

Inventory = []
Pred = {}
def dfs(IC, pred=None, move=None):
    IC.run()
    prompt = IC.flush_out().strip().split('\n')
    room = prompt[0]
    Pred[room] = (pred,move)
    Neigh = []
    Items = []
    for l in prompt:
        if l and l[0]=='-':
            o = l[2:]
            if o in Dir:
                if o!=InvDir[move]:
                    Neigh.append(o)
            elif o not in DoNotTake:
                Items.append(o)
                Inventory.append(o)
    for it in Items:
        IC.push_in('take %s\n' % it)
        IC.run()
        IC.clear_out()
    if room!=SecCheck:
        for v in Neigh:
            IC.push_in('%s\n' % v)
            dfs(IC, room, v)
            IC.push_in('%s\n' % InvDir[v])
            IC.run()
            IC.clear_out()

# exploring and collecting items
IC = IntcodeComputer(P)
dfs(IC)

# going back to final room
room = SecCheck
Path = []
while room is not None:
    room,move = Pred[room]
    Path.append(move)
Path.reverse()
for move in Path:
    IC.push_in('%s\n' % move)
IC.run()
IC.clear_out()

# trying every subset of items
S = (1<<len(Inventory))-1
for i in range(1<<len(Inventory)):
    # using gray code to enumerate subsets
    b = 0
    while i&1:
        b += 1
        i >>= 1
    IC.push_in('%s %s\n' % (('drop' if S>>b&1 else 'take'), Inventory[b]))
    S ^= 1<<b
    # trying the current subset
    IC.run()
    IC.clear_out()
    #IC.push_in('inv\n')
    IC.push_in('north\n')
    IC.run()
    O = IC.flush_out()
    if 'lighter' not in O and 'heavier' not in O:
        break
print(O.strip())
