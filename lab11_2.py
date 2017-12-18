#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def randValue(seed = "654321"):
	while True:
		yield seed
		seed = str(seed) #X
		l = len(seed); mid = int(l / 2)
		temp = seed[mid:]+seed[:mid] if l % 2 == 0 else seed[mid+1:]+seed[mid:mid+1]+seed[:mid] #Y
		seed = str(int(seed) * int(temp)) #X * Y
		offset = int((len(seed) - l) / 2) #offsetSEEDoffset
		seed = int(seed[offset:l+offset]) #SEED

def app():
	r = randValue()
	for i in range(15):
		print(next(r))
	
app()
