#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def countSonant(s):
	sonant = ['a', 'o', 'u', 'j', 'i', 'e', 'y']
	return len([(1) for c in s if c.lower() in sonant])

s = input("Enter string: ")
print("Result: {}".format(countSonant(s)))
