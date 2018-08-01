#!/usr/bin/env python3

import sys

def is_digit(c):
    return c is not None and "0"<=c<="9"


class CGXParser:
    def __init__(self, S):
        self.S = S
        self.p = 0
        self.T = self.parse()
        self.indent = " "*4

    # BASIC CONTROLS
    def _curr_(self):
        return self.S[self.p] if self.p<len(self.S) else None
    
    def curr(self):
        self.skip_blanks()  # !! side effect !!
        return self._curr_()
    
    def nxt(self):
        assert(self.p<len(self.S))
        self.p += 1
    
    def skip_blanks(self):
        while self.p<len(self.S) and self._curr_() in [' ','\n','\t']:
            self.nxt()

    # PARSING
    def parse_elements(self):
        L = []
        while True:
            X = self.parse_element()
            if X is not None:
                L.append(X)
            if self.curr()==";":
                self.nxt()
            else:
                break
        return L
    
    def parse_element(self):
        if self.curr()=="(":
            return self.parse_block()
        elif self.curr()=="'":
            L = self.parse_string()
            if self.curr()=="=":
                self.nxt()
                R = self.parse_block() if self.curr()=="(" else self.parse_primitive()
                return (L,R)
            return L
        else:
            return self.parse_primitive()
        
    def parse_string(self):
        assert(self.curr()=="'")
        l = self.p
        r = self.S.find("'",l+1)
        self.p = r+1
        return self.S[l:r+1]
    
    def parse_int(self):
        i = []
        while is_digit(self._curr_()):
            i.append(self._curr_())
            self.nxt()
        return ''.join(i)  # we do not actually convert to an int here
    
    def parse_primitive(self):
        if self.curr()=="'":
            return self.parse_string()
        elif is_digit(self.curr()):
            return self.parse_int()
        else:
            for W in ["null","true","false"]:
                if self.S[self.p:self.p+len(W)]==W:
                    self.p += len(W)
                    return W
            return None
    
    def parse_block(self):
        assert(self.curr()=="(")
        self.nxt()
        L = self.parse_elements()
        assert(self.curr()==")")
        self.nxt()
        return L
    
    def parse(self):
        return self.parse_elements()

    # PRETTY PRINTING
    def pprint_block(self, B, off=0):
        sys.stdout.write(self.indent*off + "(\n")
        for i in range(len(B)):
            self.pprint(B[i],off+1,(i<len(B)-1))
        sys.stdout.write(self.indent*off + ")")
    
    def pprint(self, E, off=0, semicol=False):
        if isinstance(E,str):
            sys.stdout.write(self.indent*off + E)
        elif isinstance(E,tuple):
            L,R = E
            sys.stdout.write(self.indent*off + ("%s=" % L))
            if isinstance(R,list):
                sys.stdout.write("\n")
                self.pprint_block(R,off)
            else:
                sys.stdout.write("%s" % R)
        else:
            self.pprint_block(E,off)
        sys.stdout.write(";\n" if semicol else "\n")
    
    def pretty_print(self):
        for i in range(len(self.T)):
            self.pprint(self.T[i],0,(i<len(self.T)-1))


def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    S = '\n'.join(S)
    P = CGXParser(S)
    P.pretty_print()

main()
