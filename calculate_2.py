#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def formula(x, u, q):
	return 1.0/(q*math.sqrt(2.0*math.pi)) * math.exp(-1.0 * ((x-u)*(x-u))/(2.0*q*q))

x = float(input("Введіть x: "))
u = float(input("Введіть u: "))
q = float(input("Введіть q: "))
print( "Результат: {}".format(formula(x,u,q)) )
