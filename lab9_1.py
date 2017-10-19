#! /usr/bin/env python3
# -*- coding: utf-8 -*-

demo1 = [2, 3, 4, 5, 6, 'J', 'T']
demo2 = [2, 3, 4, 5, 6, 'J', 'J', 'J', 'J', 'J']
demo3 = [2, 3, 4, 'J', 'A']
demo4 = ['A', 'A', 'A', 'A']

def Blackjack(cards) :
	if not checkcards(cards) : print("Duplicated cards!"); exit
	source = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 'T':10, 'J':10, 'Q':10, 'K':10, 'A':1} #A
	summ = sum([source[c] for c in cards])
	for a in range(cards.count('A')) :
		if summ + 10 < 21 : summ += 10
	return summ if summ <= 21 else "Bust"

def checkcards(cards) :
	unique = set(cards)
	for i in unique :
		if cards.count(i) > 4 :
			return False
	return True

print(Blackjack(demo1))
print(Blackjack(demo2))
print(Blackjack(demo3))
print(Blackjack(demo4))
