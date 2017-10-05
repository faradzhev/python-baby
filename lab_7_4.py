#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def shchar(s) :
	sNew = ''
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
	alphabet += [a.upper() for a in alphabet]	
	for c in s :
		for a in alphabet :
			if c == a :
				sNew += alphabet[alphabet.index(a)+1]
				break
		else:
			sNew += c
	return sNew

s = input("Enter string: ")
print("Result: {}".format(shchar(s)))
