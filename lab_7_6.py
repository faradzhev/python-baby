#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def framelize(s):
	stars = '*' * len(s)
	print('**{}**\n* {} *\n**{}**'.format(stars, s, stars))
	
framelize(input("Enter string: "))
