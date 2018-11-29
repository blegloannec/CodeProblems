#!/usr/bin/env python3

import sys, struct
from collections import deque

M = 1<<15

ASM = [('halt',0),('set',2),('push',1),('pop',1),('eq',3),('gt',3),('jmp',1),('jt',2),('jf',2),('add',3),('mult',3),('mod',3),('and',3),('or',3),('not',2),('rmem',2),('wmem',2),('call',1),('ret',0),('out',1),('in',1),('noop',0)]


# CONTROL CHARS
MAZE_CHAR = '*'
DUMP_CHAR = '@'
REG8_CHAR = '&'


class Emulator:
    def __init__(self):
        self.i = 0
        self.Mem = [0]*M
        self.Reg = [0]*8
        self.Stk = []
        self.in_buffer = None
        self.out_buffer = None
        self.dump_file = None

    def load_program(self, bin_name):
        F = open(bin_name,'rb')
        B = F.read()
        F.close()
        self.S = len(B)//2
        for i in range(self.S):
            self.Mem[i] = struct.unpack('<H',B[2*i:2*(i+1)])[0]

    def save_state(self):
        return (self.i, tuple(self.Reg), tuple(self.Stk), tuple((a,self.Mem[a]) for a in range(M) if self.Mem[a]!=0))
            
    def load_state(self, state, inbuff=None):
        self.i = state[0]
        self.Reg = list(state[1])
        self.Stk = list(state[2])
        self.Mem = [0]*M
        for a,v in state[3]:
            self.Mem[a] = v
        if inbuff is None:
            self.in_buffer = None if inbuff is None else deque(inbuff)
            self.out_buffer = None
        else:
            self.in_buffer = deque(inbuff)
            self.out_buffer = []
        self.dump_file = None

    def get_output(self):
        assert(self.out_buffer is not None)
        return ''.join(self.out_buffer)
        
    def val(self, x):
        assert(0<=x<M+8)
        return x if x<M else self.Reg[x-M]

    def set(self, a, x):
        assert(0<=x<M+8)
        if a<M:
            # NB: of course the program modifies itself!...
            #if a<self.S:
            #    sys.stderr.write('##### PROGRAM MODIFIED! #####\n')
            self.Mem[a] = x
        else:
            self.Reg[a-M] = x

    def step(self):
        if self.dump_file is not None:
            self.dump_instr(self.i)
        I = self.Mem[self.i]
        if I==0:               # halt
            self.i = -1
        elif I==1:             # set
            a,b = self.Mem[self.i+1],self.val(self.Mem[self.i+2])
            self.set(a,b)
            self.i += 3
        elif I==2:             # push
            a = self.val(self.Mem[self.i+1])
            self.Stk.append(a)
            self.i += 2
        elif I==3:             # pop
            a = self.Mem[self.i+1]
            assert(self.Stk)
            self.set(a,self.Stk.pop())
            self.i += 2
        elif I==4:             # eq
            a,b,c = self.Mem[self.i+1],self.val(self.Mem[self.i+2]),self.val(self.Mem[self.i+3])
            self.set(a,int(b==c))
            self.i += 4
        elif I==5:             # gt
            a,b,c = self.Mem[self.i+1],self.val(self.Mem[self.i+2]),self.val(self.Mem[self.i+3])
            self.set(a,int(b>c))
            self.i += 4
        elif I==6:             # jmp
            a = self.val(self.Mem[self.i+1])
            self.i = a
        elif I==7:             # jt
            a,b = self.val(self.Mem[self.i+1]),self.val(self.Mem[self.i+2])
            self.i = b if a!=0 else self.i+3
        elif I==8:             # jf
            a,b = self.val(self.Mem[self.i+1]),self.val(self.Mem[self.i+2])
            self.i = b if a==0 else self.i+3
        elif I==9:             # add
            a,b,c = self.Mem[self.i+1],self.val(self.Mem[self.i+2]),self.val(self.Mem[self.i+3])
            self.set(a,(b+c)%M)
            self.i += 4
        elif I==10:            # mult
            a,b,c = self.Mem[self.i+1],self.val(self.Mem[self.i+2]),self.val(self.Mem[self.i+3])
            self.set(a,(b*c)%M)
            self.i += 4
        elif I==11:            # mod
            a,b,c = self.Mem[self.i+1],self.val(self.Mem[self.i+2]),self.val(self.Mem[self.i+3])
            assert(c!=0)
            self.set(a,b%c)
            self.i += 4
        elif I==12:            # and
            a,b,c = self.Mem[self.i+1],self.val(self.Mem[self.i+2]),self.val(self.Mem[self.i+3])
            self.set(a,b&c)
            self.i += 4
        elif I==13:            # or
            a,b,c = self.Mem[self.i+1],self.val(self.Mem[self.i+2]),self.val(self.Mem[self.i+3])
            self.set(a,b|c)
            self.i += 4
        elif I==14:            # not
            a,b = self.Mem[self.i+1],self.val(self.Mem[self.i+2])
            self.set(a,M-1-b)
            self.i += 3
        elif I==15:            # rmem
            a,b = self.Mem[self.i+1],self.val(self.Mem[self.i+2])
            self.set(a,self.Mem[b])
            self.i += 3
        elif I==16:            # wmem
            a,b = self.val(self.Mem[self.i+1]),self.val(self.Mem[self.i+2])
            self.set(a,b)
            self.i += 3
        elif I==17:            # call
            a = self.val(self.Mem[self.i+1])
            self.Stk.append(self.i+2)
            self.i = a
        elif I==18:            # ret
            self.i = self.Stk.pop() if self.Stk else -1
        elif I==19:            # out
            a = self.val(self.Mem[self.i+1])
            assert(0<=a<256)
            c = chr(a)
            if self.out_buffer is None:
                sys.stdout.write(c)
            else:
                self.out_buffer.append(c)
            self.i += 2
        elif I==20:            # in
            a = self.Mem[self.i+1]
            if self.in_buffer is None:
                c = sys.stdin.read(1)
            elif len(self.in_buffer)>0:
                c = self.in_buffer.popleft()
            else:                ## pause
                return 1
            if c==MAZE_CHAR:      ## maze solver
                return 2
            elif c==DUMP_CHAR:   ## dump switch
                return 3
            elif c==REG8_CHAR:   ## set reg 8
                return 4
            self.set(a,ord(c))
            self.i += 2
        else:
            assert(I==21)      # nop
            self.i += 1
        return 0

    def set_dump_file(self, dump_name):
        self.dump_file = open(dump_name,'w')
    
    def dump_instr(self, i):
        assert(self.dump_file is not None)
        #self.dump_file.write(str(self.Reg)+'\n')
        #self.dump_file.write(str(self.Stk)+'\n')
        self.dump_file.write('%05d\t' % i)
        I = self.Mem[i]
        assert(0<=I<=len(ASM))
        instr,arite = ASM[I]
        if arite==0:
            self.dump_file.write('%s\n' % instr)
        elif instr=='out':
            a = self.Mem[i+1]
            assert(a<256 or a>=M)
            arg = 'R%d (%s)'%(a-M,ascii(chr(self.Reg[a-M]))[1:-1]) if a>=M else ascii(chr(a))[1:-1]
            self.dump_file.write('%s %s\n' % (instr,arg))
        else:
            args = ' '.join('R%d'%(a-M) if a>=M else str(a) for a in self.Mem[i+1:i+1+arite])
            self.dump_file.write('%s %s\n' % (instr,args))
    
    def run(self):
        code = 0
        while code==0 and self.i>=0:
            code = self.step()
        if code==2:                                   # BFS for maze solving
            keyword = sys.stdin.readline().strip()    # eats until \n after *
            if keyword=='':
                keyword = ' interest '
            maze_bfs(self,keyword)
        elif code==3:                                 # dump trace
            dump_name = sys.stdin.readline().strip()  # eats until \n after '&'
            if dump_name=='':
                dump_name = 'trace.dump'
            if self.dump_file is None:
                self.set_dump_file(dump_name)
                sys.stderr.write("##### TRACE ON IN %s #####\n" % dump_name)
            else:
                self.dump_file.close()
                sys.stderr.write("##### TRACE OFF #####\n")
                self.dump_file = None
            self.run()
        elif code==4:                                 # set reg 8
            try:
                x = int(sys.stdin.readline().strip())
            except:
                x = 0
            self.Reg[7] = x
            sys.stderr.write("##### REGISTER 8 SET TO %d #####\n" % x)
            ##### BYPASS (see also README and ack.dump) #####
            # 5483: set R0 4
            # 5486: set R1 1
            # 5489: call 6027  ==>  Ackermann_R7(R0,R1)
            ## First step: noop the call
            self.set(5489,21)
            self.set(5490,21)
            ## No more huge computation, but teleportation is aborted and we get:
            # 5491: eq R1 R0 6
            # 5495: jf R1 5579  ==>  jumps to abortion as R0 = 4
            ## So we need a value R7 such that, after the bypassed computation, we would
            ## have R0 := Ackermann_R7(R0,R1) == 6
            ## A memoized brute-force computation in ack.cpp gives the answer fast enough
            ## (compile with -O3).
            ## Second step: we bypass the jump by setting R0 = 6 (inversing the jf also works),
            self.set(5485,6)
            ## NB: if R7 is not set to the right value (found by ack.cpp), teleportation works
            ##     but the given code is not valid and the rest of the game might be affected?...
            self.run()


def maze_bfs(E, Keyword):
    sys.stderr.write('\n##### MAZE SOLVER (please wait) #####\n\n')
    ErrMsg = "I don't understand; try 'help' for instructions."
    s0 = E.save_state()
    Seen = {s0: 0}
    State = [s0]
    Pred = [None]
    Move = ['']
    Prompt = ['']
    Q = deque([0])
    while Q:
        si = Q.popleft()
        s = State[si]
        if s[0]<0:   # halt state
            continue
        if Keyword in Prompt[si]:
            break
        # NB: options are made for the maze but could be read
        #     from the prompt of each state for the BFS to be
        #     be used in any other situation
        for d in ['north','south','east','west']:
            if si!=0 and '- '+d not in Prompt[si]:
                continue
            E.load_state(s,d+'\n')
            E.run()
            prompt = E.get_output().strip()
            assert(ErrMsg not in prompt)
            t = E.save_state()
            if t not in Seen:
                ti = len(State)
                Q.append(ti)
                Seen[t] = ti
                State.append(t)
                Pred.append(si)
                Move.append(d)
                Prompt.append(prompt)
    sys.stderr.write('### Interesting position discovered ###\n')
    sys.stderr.write(Prompt[si])
    sys.stderr.write('\n')
    Path = []
    while si!=0:
        Path.append(Move[si])
        si = Pred[si]
    Path.reverse()
    sys.stderr.write('\n### Path to that position: %s ###\n' % ' '.join(Path))
    sys.stderr.write('\n##### BACK TO THE GAME (your turn, e.g. look) #####\n\n')
    E.load_state(s)
    E.run()


if __name__=='__main__':
    E = Emulator()
    E.load_program(sys.argv[1])
    E.run()
