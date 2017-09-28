#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
 
def rpc(a, b):
	if a == b:
		return 0
	elif a > b:
		if a == 3:
			return b
		else:
			return a
	else:
		if a == 3:
			return a
		else:
			return b 

options = ["Нічия", "Камінь", "Ножиці", "Папір"]

human = int(input("{} (1) / {} (2) / {} (3): ".format(options[1], options[2], options[3])))
bot = randint(1, 3)

if human >= 1 and human <= 3:
	print( "Ви вибрали: {}".format(options[human]) )
	print( "Бот вибрав: {}".format(options[bot]) )
	print( "Виграє: {}".format(options[rpc(human,bot)]) )
else:
	print( "Так не піде, виберіть щось нормальне..." )
