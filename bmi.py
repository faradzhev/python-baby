#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from decimal import Decimal

def bmi(weight,height):
	return weight/(height*height)
	
weight = Decimal(input("Введіть вагу (в кг): "))
height = Decimal(input("Введіть зріст (в м): "))
print(bmi(weight,height))
