#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def lastOfUs(amount, step) :
	guys = [i for i in range(1, amount+1)]
	while len(guys) > 1 :
		fakeStep = step
		while fakeStep > len(guys) : fakeStep -= len(guys)
		guys = guys[fakeStep:] + guys[:fakeStep-1]
		#print(guys)
	return guys[0]
		
a = int(input("Enter amount of guys: "))
c = int(input("Enter step: "))
print("The last guy is {}".format(lastOfUs(a,c) if a > 0 else "nobody"))
