#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *
import solution  # solver
import time

N = 5
N2 = N*N

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
    
    def input_grid(self):
        G = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                try:
                    v = int(self.V[i][j].get())
                    assert(1<=v<=N*N)
                    G[i][j] = v
                except:
                    pass
        return G
    
    def print_grid(self, G):
        for L in G:
            self.text_print(' '.join(map(str,L)))
    
    def search(self):
        G = self.input_grid()
        S = set(range(len(self.Grids)))
        for i in range(N):
            for j in range(N):
                if G[i][j]>0:
                    S &= self.Sets[i][j][G[i][j]]
        self.text_clear()
        self.print_grid(G)
        self.text_print()
        self.text_print('%d grid(s) found' % len(S))
        if len(S)<=10:
            for n in S:
                self.text_print()
                self.print_grid(self.Grids[n])
    
    def solve(self):
        G0 = self.input_grid()
        G = [None]*(N2+1)
        Avail = (1<<N2)-1
        for i in range(N):
            for j in range(N):
                if G0[i][j]>0:
                    G[G0[i][j]] = N*i+j
                    Avail ^= 1<<(N*i+j)
        self.text_clear()
        self.print_grid(G0)
        self.text_print()
        S = [None]*(N2+1)
        t0 = time.clock()
        succ = solution.backtrack(G,Avail,S)
        t1 = time.clock()
        if succ:
            self.text_print('Success -- %.3fs\n' % (t1-t0))
            Sol = solution.grid(S)
            self.print_grid(Sol)
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
