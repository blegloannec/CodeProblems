#!/usr/bin/env python2

import re

# Vowels in the Back
Regex_Pattern = r"^[a-z]*[aeiouy][a-z]{9}$"


# Balanced Strings
Regex_Pattern = r"^(ab|ba)*$"


# Match Maker
Accept = ['bhdgffhfa', 'aggjjaaga', 'hbefebhfi', 'dbceeabih', 'ihifdbhhf', 'djacfjbae', 'ibjbeigac', 'jaffigdad', 'aaaaaaaaj', 'dgifecchi', 'dcbhgjaaf', 'eedfbcedb', 'aaaaaaabf', 'beaajbihg', 'aaaaaaaag', 'eacccdjeh', 'aaaaaaaad', 'hehcijfhc', 'aaaaaaaaa', 'aaaaaaabc', 'jfdhdeice']

Reject = ['aaaaaaaai', 'ehigcbgjd', 'hgjdeajec', 'aaaaaaabe', 'haebgiggc', 'aaaaaaaba', 'aaaaaaaaf', 'bfjhehbcf', 'diieabefh', 'jhjcaeead', 'ifbjdgibf', 'dddbgcgai', 'bbcafhcif', 'hfjciccbi', 'fdbgidjdj', 'aaaaaaabb', 'jhdibgbfj', 'cfjbaijad', 'bhgjfacgi', 'ehhieihhh', 'abijjabda']

def test_positions():
    for i in range(9):
        for j in range(i+1,9):
            SA = set(s[i]+s[j] for s in Accept)
            SR = set(s[i]+s[j] for s in Reject)
            S = SA&SR
            if len(S)<=2:
                print(S)
                make_dot([i,j])
                return

def make_dot(P):
    DOT = ['digraph {']
    for w in Accept:
        for i in range(len(P)-1):
            DOT.append('{}{} -> {}{}'.format(w[P[i]],i,w[P[i+1]],i+1))
    DOT.append('}')
    F = open('graph.dot','w')
    F.write('\n'.join(DOT))
    F.close()

#test_positions()

Regex_Pattern = r'^(a+([adjg]|b[cf])$|ag|bhd|d[bcgj]|ea|hb|i[hb]|j[af]|[beh]e)'
assert len(Regex_Pattern)<=60
for w in Accept:
    assert re.search(Regex_Pattern, w)
for w in Reject:
    assert not re.search(Regex_Pattern, w)


# Winning Tic Tac Toe
Regex_Pattern = r'(O|X)(\1\1(...)*$|..\1..\1|...\1...\1|.\1.\1..$)'


# Restricted Repetitions
Regex_Pattern = r'^(hh+)\1+(aaa+)\2+(cc)+k(kk){2,10}$'
Test_String = lambda x: 'h'*(100003*x) + 'a'*(100003*x) + 'c'*100 + 'k'*5
#print bool(re.search(Regex_Pattern, Test_String(1)))
