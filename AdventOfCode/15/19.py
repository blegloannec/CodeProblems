#!/usr/bin/env python

import sys
import re

re1 = re.compile('([a-zA-Z]+) => ([a-zA-Z]+)')

M = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    rules = []
    for l in cases:
        s = l.strip()
        r = re1.match(s)
        rules.append((r.group(1),r.group(2)))
    mol = set()
    for r in rules:
        m = M.split(r[0])
        for i in range(len(m)-1):
            mol.add(r[0].join(m[:i+1])+r[1]+r[0].join(m[i+1:]))
    print len(mol)

main()
