#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from decimal import Decimal
import math

def formula(a, b):
	return math.sqrt(a*b) / math.exp(a)*b + a * math.exp(2.0*a/b)

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
if a >= 0 and b > 0:
	print( "Результат: {}".format(formula(a, b)) )
else:
	print("Маєте ввести невід'ємні дійсні числа a та b, причому b не дорівнює 0")
