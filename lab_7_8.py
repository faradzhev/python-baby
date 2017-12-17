#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re
	
def app():
	for i in range(1, 101) :
		r = ''
		if i % 3 == 0 : r += 'Fizz'
		if i % 5 == 0 : r += 'Buzz'
		if not r : r = i
		print(r)

app()
