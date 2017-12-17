#! /usr/bin/env python3
# -*- coding: utf-8 -*-

arr = [65, 3, 3, 53, 523, 6, 63, 2, 8, 6, 3, 23, 0]

def median(array) :
	array.sort()
	length = len(array)
	mid = int(length / 2)
	med = array[mid] if length % 2 != 0 else (array[mid-1] + array[mid]) / 2
	return med

def mean(array) :
	return sum(array) / len(array)

def app() :
	print('median = {}'.format(median(arr)))
	print('mean = {}'.format(mean(arr)))

app()
