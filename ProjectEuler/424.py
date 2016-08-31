#!/usr/bin/env python

import sys,subprocess,os

# example grid
G = '6,X,X,(vCC),(vI),X,X,X,(hH),B,O,(vCA),(vJE),X,(hFE,vD),O,O,O,O,(hA),O,I,(hJC,vB),O,O,(hJC),H,O,O,O,X,X,X,(hJE),O,O,X'

# generate a Prolog program to solve the given kakuro puzzle
# (using finite domain constraint solver)
def parse_grid(G):
    G = G.replace(',v',';v').split(',')
    S = int(G[0])
    P = (lambda i,j: i*S+j+1)
    White = [chr(i+ord('A')) for i in xrange(10)]+['O']
    Squares = []
    Constraints = []
    for i in xrange(S):
        for j in xrange(S):
            C = G[P(i,j)]
            if C=='O':
                Squares.append('C%d%d'%(i,j))
            elif len(C)==1 and ord('A')<=ord(C)<=ord('J'):
                Squares.append('C%d%d'%(i,j))
                Constraints.append('C%d%d #= %s'%(i,j,C))
            elif C[0]=='(':
                for D in C[1:-1].split(';'):
                    s = D[1] if len(D)==2 else '10*%s+%s'%(D[1],D[2])
                    if len(D)>2: # useful?
                        Constraints.append('%s #>= 1'%D[1])
                    if D[0]=='h':
                        y = j+1
                        sqr = []
                        while y<S and G[P(i,y)] in White:
                            sqr.append('C%d%d'%(i,y))
                            y += 1
                    else:
                        x = i+1
                        sqr = []
                        while x<S and G[P(x,j)] in White:
                            sqr.append('C%d%d'%(x,j))
                            x += 1
                    Constraints.append('fd_all_different([%s])'%','.join(sqr))
                    Constraints.append('%s #= %s'%(s,'+'.join(sqr)))
    Prolog = 'kakuro(Sub,Sqr) :-\nSub = [%s],\nfd_domain(Sub,0,9),\nfd_all_different(Sub),\nSqr = [%s],\nfd_domain(Sqr,1,9),\n%s,\nfd_labeling(Sub),\nfd_labeling(Sqr),!.\n\nprint_list([]) :- nl.\nprint_list([H|T]) :- write(H),print_list(T).\n\nmain :- kakuro(X,_),print_list(X),halt.\n\n:- initialization(main).' % (','.join(White[:-1]),','.join(Squares),',\n'.join(Constraints))
    return Prolog

def main():
    # en Python 3, utiliser subprocess.DEVNULL a la place
    devnull = open(os.devnull,'w')
    s = 0
    for G in sys.stdin.readlines():
        # write the Prolog program to a file
        f = open('tmp424.pl','w')
        f.write(parse_grid(G.strip()))
        f.close()
        # compile it (requires gprolog)
        subprocess.check_call(['gplc','tmp424.pl'],stdout=devnull,stderr=devnull)
        # execute it and get the result
        s += int(subprocess.check_output(['./tmp424']))
    print s
    devnull.close()
    # cleaning
    os.remove('tmp424.pl')
    os.remove('tmp424')

#print parse_grid(G)
main()
