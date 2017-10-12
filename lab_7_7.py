#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def swap(s) :
	sn = []
	words = s.split(' ')
	for w in words :
		for i, c in enumerate(list(w)) :
			if '_' in w and w[0] != '_' and w[-1] != '_' :
				sn += '{}'.format(c.upper()) if c.isupper() else c
			else:
				sn += '_{}'.format(c.lower()) if c.isupper() else c
			
	return ''.join(sn)
	
print("Result: {}".format(swap(input("Enter string: "))))
