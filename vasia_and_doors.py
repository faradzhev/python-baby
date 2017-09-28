#! /usr/bin/env python3
# -*- coding: utf-8 -*-

w = float(input("Введіть door w: "))
h = float(input("Введіть door h: "))
a = float(input("Введіть box a: "))
b = float(input("Введіть box b: "))
c = float(input("Введіть box c: "))

print( (w>a and h>b or w>b and h>a) or (w>a and h>c or w>c and h>a) or (w>b and h>c or w>c and h>b) )
