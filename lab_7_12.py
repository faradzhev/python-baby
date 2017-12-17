#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def makeSpacesGreatAgain(s):
	return ' '.join((w for w in s.split(' ') if w))

def app():
	print(makeSpacesGreatAgain(input('Enter string: ')))

app()
