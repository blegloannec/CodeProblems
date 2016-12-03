#!/usr/bin/env python

import re

reMol = re.compile('[A-Z][a-z]?')
reRn = re.compile('Rn')
reY = re.compile('Y')
reAr = re.compile('Ar')

M = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

def main():
    mol = len(reMol.findall(M))
    nbRn = len(reRn.findall(M))
    nbY = len(reY.findall(M))
    print 'Mol',mol
    print 'Rn',nbRn
    print 'Y',nbY
    print 'Ar',len(reAr.findall(M))
    print mol-1-2*nbRn-2*nbY

main()
