#! /usr/bin/env python3
# -*- coding: utf-8 -*-

a, b, c = (map(float,input("Enter a b c: ").split(' ')))
print("Seems to be a triangle..." if a+b>c and a+c>b and b+c>a else "No, man, this one definitely NOT exist!")