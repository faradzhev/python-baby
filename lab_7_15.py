#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
from random import shuffle

def generatePassword(length = 8, useNumbers = True, useSpecial = True):
	letters = 'abcdefghijklmnopqrstuvwxyz'
	special = '!@#$%^&*()_+~-='
	numbers = '0123456789'
	password = list()
	while len(password) < length :
		if useSpecial:
			password.append(special[randint(0, len(special)-1)])
		if useNumbers:
			password.append(numbers[randint(0, len(numbers)-1)])
		password.append(letters[randint(0, len(letters)-1)])
		password.append(letters[randint(0, len(letters)-1)].upper())
	shuffle(password)
	return ''.join(password)

def app():
	print(generatePassword(randint(8, 15)))

app()
