#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

def c2f(c):
    return 9/5*c+32
def f2c(f):
    return (5/9)*(f-32)

n = input('Choose C2F (c) or F2C (f)')
if n == 'c':
    n = int(input('enter C*:'))
    print('this equals {}'.format(c2f(n)))
elif n == 'f':
    n = int(input('enter F*:'))
    print('this equals {}'.format(f2c(n)))
else:
	print('Bro, IDK what you want to do with this. You entered some rubbish I don\'t work with. Please, try your best the other time...')
