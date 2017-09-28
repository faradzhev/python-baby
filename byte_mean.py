#! /usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input("Введіть ціле додатнє число: "))
print( a > 0 and not a & (a - 1) )
