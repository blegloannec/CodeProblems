#!/usr/bin/env python3

is_vowel = lambda c: c in 'aeiouAEIOU'

def split_word(word):
    S = []; syl = []
    def push_syl(): S.append(''.join(syl)); syl.clear()
    for c in word:
        if is_vowel(c):
            if syl and is_vowel(syl[-1]):
                push_syl()
            elif len(syl)>1:
                c0 = syl.pop()
                push_syl()
                syl.append(c0)
        elif syl and not is_vowel(syl[-1]):
            push_syl()
        syl.append(c)
    push_syl()
    return S

def fold_text(width, text):
    T = text.split()
    T.reverse()
    O = []; L = []; l = 0
    while T:
        w = T.pop()
        spc = 1 if L else 0
        if l+spc+len(w)<=width:
            L.append(w)
            l += spc+len(w)
        else:
            S = split_word(w)
            l += spc+1  # ' ' & '-'
            i = 0
            while l+len(S[i])<=width:
                l += len(S[i])
                i += 1
            if i>0:
                if i==1 and len(S[0])==1:
                    i = 0  # avoiding a-baba
                else:
                    L.append(''.join(S[:i]) + '-')
            O.append(' '.join(L))
            L.clear(); l = 0
            T.append(''.join(S[i:]))
    O.append(' '.join(L))
    return O

print('\n'.join(fold_text(int(input()), input())))
