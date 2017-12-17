#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def sortString(s):
	l = re.sub("[^\w]", " ",  s).split()
	l.sort(key = len)
	return ' '.join(l)

def app():
	print(sortString(input('Enter string: ')))

app()
