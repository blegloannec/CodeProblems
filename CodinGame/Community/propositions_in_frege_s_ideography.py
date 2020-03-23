#!/usr/bin/env python3

import itertools

is_var = lambda c: 'A'<=c<='Z'
num = lambda c: ord(c)-ord('A')
lett = lambda i: chr(i+ord('A'))

class FormVar:
    def __init__(self, var_idx):
        self.var = var_idx
    def eval(self, I):
        return I[self.var]

class FormNot:
    def __init__(self, form):
        self.child = form
    def eval(self, I):
        return not self.child.eval(I)

class FormImp:
    def __init__(self, left_form, right_form):
        self.left = left_form
        self.right = right_form
    def eval(self, I):
        return not self.left.eval(I) or self.right.eval(I)

def parse_form(Ideo, i=0, j=0):
    if Ideo[i][j]=='+':
        return FormNot(parse_form(Ideo, i, j+1))
    elif Ideo[i][j]=='-' and i+1<len(Ideo) and Ideo[i+1][j] in "'|":
        return FormImp(parse_form(Ideo, i+1, j), parse_form(Ideo, i, j+1))
    elif Ideo[i][j]=='|':
        return parse_form(Ideo, i+1, j)
    elif is_var(Ideo[i][j]):
        return FormVar(num(Ideo[i][j]))
    return parse_form(Ideo, i, j+1)

def main():
    n = int(input())
    Ideo = [input() for _ in range(n)]
    Form = parse_form(Ideo)
    var_cnt = max(num(c) for c in itertools.chain(*Ideo) if is_var(c)) + 1
    Bad = []
    for I in itertools.product((False,True), repeat=var_cnt):
        if not Form.eval(I):
            Bad.append(I)
    if Bad:
        for I in Bad:
            print(' '.join(f'{lett(i)} {I[i]}' for i in range(var_cnt)))
    else:
        print('TAUTOLOGY')

main()
