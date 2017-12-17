#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def oneFromAnother(s1, s2):
	real = True
	for c in ''.join(set(s2)) : #set removes duplicated characters to boost the code :)
		if not c in s1 :
			real = False
			break
	return real

def app():
	print(oneFromAnother(input('Enter first string: '), input('Enter second string: ')))

app()
