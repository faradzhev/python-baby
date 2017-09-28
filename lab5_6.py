#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def is_prime(n, i=2):
    while n > i:
        if n % i == 0:
            return False
        i += 1
    return True if n > 1 else False

n = int(input("Enter number: "))
print("{} is {}prime".format(n, "" if is_prime(n) else "NOT "))