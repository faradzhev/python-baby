#! /usr/bin/env python3
# -*- coding: utf-8 -*-

roman = [
	(1000, "M"),
	(900, "CM"),
	(500, "D"),
	(400, "CD"),
	(100, "C"),
	(90, "XC"),
	(50, "L"),
	(40, "XL"),
	(10, "X"),
	(9, "IX"),
	(5, "V"),
	(4, "IV"),
	(1, "I")
]

def intToRoman(integer):
	res = ""
	for wholeNumber in roman:
		while integer >= wholeNumber[0]:
			integer -= wholeNumber[0]
			res += wholeNumber[1]
	return res

def romanToInt(numeral):
	index = 0
	res = 0
	for integer, rnum in roman:
		while numeral[index : index + len(rnum)] == rnum:
			res += integer
			index += len(rnum)
	return res

def app():
	t = int(input("Select conversion option: \n1 - Integet to Roman \n2 - Roman to Integer\n"))
	s = input("Enter number: ")
	if t == 1 and int(s) > 0 and int(s) < 4000:
		res = intToRoman(int(s))
	elif t == 2:
		res = romanToInt(s)
	else:
		res = "Invalid input. Try again."
	print(res)
	
app()
