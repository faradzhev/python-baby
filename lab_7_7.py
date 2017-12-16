#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re
	
def toSnake(s) :
	sr = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', sr).lower()
	
def toCamel(s) :
	res = []
	for word in s.split(' ') :
		ws = word.split('_')
		res.append( ws[0] + ''.join( i.title() for i in ws[1:] ) )
	return ' '.join(res)

def app():
	s = input("Enter string: ")
	method = input("Select method:\n1 - convert variables to camelCase\n2 - convert variables to snake_case\n")
	if method == '1' :
		res = toCamel(s)
	elif method == '2' :
		res = toSnake(s)
	else :
		res = "Unknown method, try again"
	print(res)

app()
