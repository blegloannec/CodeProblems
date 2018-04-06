#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *
import solution  # solver
import time

N = 5

class IHM(Frame):
    def __init__(self, fname, master=None):
        self.load_grids(fname)
        Frame.__init__(self, master)
        self.V = [[StringVar() for _ in range(N)] for _ in range(N)]
        self.G = [[Entry(self, textvariable=self.V[i][j], width=3) for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                self.G[i][j].grid(row=i,column=j)
        self.but_valid = Button(self, text='Search', command=self.search)
        self.but_valid.grid(row=N, column=0, columnspan=2, sticky=W)
        self.but_test = Button(self, text='Solve', command=self.solve)
        self.but_test.grid(row=N, column=3, columnspan=2)
        self.text_res = Text(self, width=7*N, state=DISABLED)
        self.text_res.grid(row=N+1, column=0, columnspan=5)
        self.text_print('%d grids loaded' % len(self.Grids))
        self.grid()

    def load_grids(self, fname):
        f = open(fname,'r')
        self.Grids = []
        for L in f.readlines():
            L = list(map(int,L.split()))
            self.Grids.append([[L[N*i+j] for j in range(N)] for i in range(N)])
        f.close()
        self.Sets = [[[set() for _ in range(N*N+1)] for _ in range(N)] for _ in range(N)]
        for n in range(len(self.Grids)):
            for i in range(N):
                for j in range(N):
                    self.Sets[i][j][self.Grids[n][i][j]].add(n)

    def text_print(self, s=''):
        self.text_res.config(state=NORMAL)
        self.text_res.insert(END,s+'\n')
        self.text_res.config(state=DISABLED)
    
    def text_clear(self):
        self.text_res.config(state=NORMAL)
        self.text_res.delete(1.0,END)
        self.text_res.config(state=DISABLED)
        
    def search(self):
        self.text_clear()
        S = set(range(len(self.Grids)))
        for i in range(N):
            L = []
            for j in range(N):
                try:
                    v = int(self.V[i][j].get())
                    S &= self.Sets[i][j][v]
                    L.append(str(v))
                except:
                    L.append('0')
                    #pass
            self.text_print(' '.join(L))
        self.text_print()
        self.text_print('%d grid(s) found' % len(S))
        if len(S)<=10:
            for n in S:
                self.text_print()
                for i in range(N):
                    self.text_print(' '.join(map(str,self.Grids[n][i])))

    def solve(self):
        self.text_clear()
        M = N*N
        G = [None]*(M+1)
        Avail = (1<<M)-1
        for i in range(N):
            L = []
            for j in range(N):
                try:
                    v = int(self.V[i][j].get())
                    assert(1<=v<=M)
                    G[v] = N*i+j
                    Avail ^= 1<<(N*i+j)
                    L.append(str(v))
                except:
                    L.append('0')
                    #pass
            self.text_print(' '.join(L))
        self.text_print()
        S = [None]*(M+1)
        t0 = time.clock()
        succ = solution.backtrack(G,Avail,S)
        t1 = time.clock()
        if succ:
            self.text_print('Success -- %.3fs\n' % (t1-t0))
            Sol = solution.grid(S)
            for L in Sol:
                self.text_print(' '.join(map(str,L)))
        else:
            self.text_print('Failed! -- %.3fs' % (t1-t0))


def main():
    f = sys.argv[1]
    root = Tk()
    root.style = Style()
    #('clam', 'alt', 'default', 'classic')
    root.style.theme_use('clam')
    ihm = IHM(f, master=root)
    ihm.master.title('Grid Explorer')
    ihm.mainloop()
    #root.destroy()

main()
