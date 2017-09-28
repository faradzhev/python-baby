#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import cmath

def dysc(a,b,c):
    d = b*b-4*a*c
    return math.sqrt(d) if d >= 0 else cmath.sqrt(d)

def calculate(a,b,c):
    d = dysc(a,b,c)
    x1 = (-1*b + d) / 2*a
    x2 = (-1*b - d) / 2*a
    return [x1] if x1 == x2 else [x1,x2]

a, b, c = (float(i) for i in input("Enter a b c: ").split(' '))

text = "Result:"
for x in calculate(a, b, c):
    text += " {}".format(x)
print(text)