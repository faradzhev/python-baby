#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def shstr(string, num):
	strlen = len(string)
	while num >= strlen:
		num -= strlen
	return string[num::] + string[0:num:]
	
s = input("Enter string: ")
k = int(input("Enter shifting index: "))
print("Result: {}".format(shstr(s,k)))
