#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def ispalindr(s):
	s = s.lower()
	s = s.replace(" ", "")
	return True if s == s[::-1] else False

s = input("Enter string: ")
print("Result: {}".format(ispalindr(s)))
