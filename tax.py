#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from decimal import Decimal

tax = Decimal(0.18)
tax_army = Decimal(0.015)
income = Decimal(input("Введіть зарплатню (в грн): "))
print("Податок ФОП: {}, Військовий збір: {}".format(round(income*tax,2), round(income*tax_army,2)))
