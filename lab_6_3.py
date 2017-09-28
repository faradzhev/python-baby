#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def interest(p, r, n=12, t=1):
    return p*(1+r/(100*n))**(n*t)

def calculate_years(p, a, r, n):
    y = 1
    while interest(p, r, n, y) < a:
        y += 1
    return y

p = float(input("Enter Current Savings: "))
a = float(input("Enter Amount of Interest: "))
r = float(input("Enter Percent of Increase: "))
n = float(input("Enter number of times deposit increases per year (1 - yearly, 12 - monthly, 365 - daily): "))

print("You will receive the needed amount in {} years".format(calculate_years(p, a, r, n)))