#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def lastOfUs(amount, step) :
	guys = [i for i in range(1, amount+1)]
	nguys = []
	print(guys)
	while(len(guys) > 1) :
		for i, v in enumerate(guys) :
			if i+1 + step > len(guys) :
			elif (i+1) % step :
				nguys[] = v

a = int(input("Enter amount of guys: "))

if a > 0 and a < 1000 :
	lastOfUs(a,3)
	#print("The last guys is {}".format(lastOfUs(a,3)))
else:
	print("How am I supposed to calculate this?")
