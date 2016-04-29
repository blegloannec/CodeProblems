#!/usr/bin/env python

import sys
import re

#Regex_Pattern = r'(te|b|a|t|r)$'

#Regex_Pattern = r'^(A{1,3})?(a{1,3}A{1,3})*(a{1,3})?$'

#Regex_Pattern = r'(.)\1\1.{,2}.{20}$|(.)\2\2.{,2}.{15}$|(.)\3\3.{,2}.{10}$|(.)\4\4.{,2}.{5}$|(.)\5\5.{,2}$|(.).{4}\6.{4}\6'

#Regex_Pattern = r'10(11|00)*$'

Regex_Pattern = r'(00|11(10(11)*00)*01)*'

#Regex_Pattern = r'(?=^.{20}$)(?!^.*\n)(?=^.*[a-z])(?=^.*[A-Z].*[A-Z])(?!^(..)*0)(?!^1)(?!^.{3}1)(?!^.{5}1)(?!^.{7}1)(?!^.{8}1)(?!^.{9}1)(?!^.{11}1)(?!^.{13}1)(?!^.{14}1)(?!^.{15}1)(?!^.{17}1)(?!^.{19}1)(?!^2)(?!^.*2$)(?!^.*345)(?!^.*354)(?!^.*435)(?!^.*453)(?!^.*534)(?!^.*543)(?!^(..)*.6)(?!^.*7.*7)(?!^.*8.*8.*8)(?!^.*9.*9.*9.*9)'

#Regex_Pattern = r'(?=^([^ab]*a[^ab]*b([^ab]*b[^ab]*a)*)*[^ab]*$|^([^ab]*b[^ab]*a([^ab]*a[^ab]*b)*)*[^ab]*$)(?=^([^cd]*c[^cd]*d([^cd]*d[^cd]*c)*)*[^cd]*$|^([^cd]*d[^cd]*c([^cd]*c[^cd]*d)*)*[^cd]*$)'

#Regex_Pattern = r'(?=.*P)(?!.*P.*P)(?=^(R(RL|UD|RT(UD|TT)*UL(LR|RL|P)*RD(UD+TT)*TL|RT(UD|TT)*UL(LR|RL|P)*LJD)*L)*$)'

print len(Regex_Pattern)
for l in sys.stdin.readlines():
    print str(bool(re.search(Regex_Pattern, l))).lower()
