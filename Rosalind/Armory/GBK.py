#!/usr/bin/env python3

from Bio import Entrez

genus = input()
date1 = input()
date2 = input()              

Entrez.email = 'none@none.net'
handle = Entrez.esearch(db='nucleotide', term=('"%s"[Organism] AND ("%s"[Publication Date] : "%s"[Publication Date])' % (genus,date1,date2)))
record = Entrez.read(handle)
print(record['Count'])
