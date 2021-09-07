#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib

rpc = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print rpc.system.listMethods()
print rpc.phone('Bert')
