#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math

a, b, c = (map(float,input("Enter a b c: ").split(' ')))

s = 0.5*(a+b+c)
area = math.sqrt( s * (s-a) * (s-b) * (s-c) )
print("Area of the traingle = {}".format(area))