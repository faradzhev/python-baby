#! /usr/bin/env python3
# -*- coding: utf-8 -*-

arr = [65, 3, 3, 53, 523, 6, 63, 2, 8, 6, 3, 23, 0]

def quickSort(array) :
	if len(array) > 1:
		less = []
		equal = []
		greater = []

		pivot = array[0]
		for i in array:
			if i < pivot:
				less.append(i)
			if i == pivot:
				equal.append(i)
			if i > pivot:
				greater.append(i)
		array = quickSort(less) + equal + quickSort(greater)
	
	return array

def mergeSort(array) :
	if len(array) > 1:
		mid = int(len(array) / 2)
		a1 = mergeSort(array[:mid])
		a2 = mergeSort(array[mid:])
		i = 0; j = 0
		array = list()
		while i < len(a1) and j < len(a2):
			if a1[i] > a2[j]:
				array.append(a2[j])
				j += 1
			else:
				array.append(a1[i])
				i += 1
		array += a1[i:]
		array += a2[j:]
	return array

def selectionSort(array) :
	for i in range(len(array)):
		m = min(array[i:])
		mi = array[i:].index(m)
		array[i + mi] = array[i]
		array[i] = m
	return array
	
def insertionSort(array):
	for i in range(1,len(array)):
		j = i
		tmp = array[j]
		while j > 0 and tmp < array[j-1]:
			array[j] = array[j-1]
			j -= 1
		array[j] = tmp
	return array

def app() :
	print('input: {}'.format(arr))
	print('quickSort: {}'.format(quickSort(arr)))
	print('mergeSort: {}'.format(mergeSort(arr)))
	print('selectionSort: {}'.format(selectionSort(arr)))
	print('insertionSort: {}'.format(insertionSort(arr)))

app()
