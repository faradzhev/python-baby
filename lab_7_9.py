#! /usr/bin/env python3
# -*- coding: utf-8 -*-
	
def isLucky(s):
	n = list(map(int, s))
	m = int(len(n)/2)
	return True if sum(n[:m]) == sum(n[-m:]) else False

def app():
	print(isLucky(input('Enter ticket number: ')))

app()
