#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def interest(p, r, n=12, t=1):
    return p*(1+r/(100*n))**(n*t)

p = float(input("Enter Current Savings: "))
r = float(input("Enter Percent of Increase: "))
n = float(input("Enter number of times deposit increases per year (1 - yearly, 12 - monthly, 365 - daily): "))
t = float(input("Enter Amount of Years: "))

print("You will receive ${}".format(interest(p, r, n, t)))