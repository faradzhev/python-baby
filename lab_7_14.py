#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def checkEmail(s):
	check = 'abcdefghijklmnopqrstuvwxyz0123456789_'
	valid = True
	p = s.lower().split('@')
	if len(p) == 2 :
		p0 = p[0].split('.')
		p1 = p[1].split('.')
		for pt in p0 + p1 :
			for c in pt :
				if not c or not c in check :
					valid = False
		if valid and len(p1) > 1 and len(p1[-1]) > 1 :
			valid = True
		else :
			valid = False
	else :
		valid = False
	return valid

def app():
	print(checkEmail(input('Enter email: ')))

app()
