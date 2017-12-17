#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def shortestWord(s):
	l = re.sub("[^\w]", " ",  s).split()
	return min((w for w in l if w), key=len)

def app():
	w = shortestWord(input('Enter string: '))
	print('It\'s "{}" ({})'.format(w, len(w)))

app()
