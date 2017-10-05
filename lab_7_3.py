#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def chkbrackets(s):
	stack = []
	openBracket, closeBracket = "<({[", ">)}]" #determine what is going to be checked
	for c in s: #go though all chars in the string
		if c in openBracket: #check if char is an opening bracket
			stack.append(c) #add it to stack
		elif c in closeBracket: #othrwise check if it's a closing bracket
			if not len(stack): #return false if stack is empty
				return False
			elif stack.pop() != openBracket[closeBracket.index(c)]: #return false if it's not the last bracket in stack
				return False
	return not len(stack) #return False if stack is not empty (some brackets aren't closed)

s = input("Enter string: ")
print("Result: {}".format(chkbrackets(s)))
