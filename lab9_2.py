#! /usr/bin/env python3
# -*- coding: utf-8 -*-

onewords = {
	0: 'нуль',
	1: 'одна',
	2: 'дві',
	3: 'три',
	4: 'чотири',
	5: 'п\'ять',
	6: 'шість',
	7: 'сім',
	8: 'вісім',
	9: 'дев\'ять',
	10: 'десять',
	11: 'одинадцять',
	12: 'дванадцять',
	13: 'тринадцять',
	14: 'чотирнадцять',
	15: 'п\'ятнадцять',
	16: 'шістнадцять',
	17: 'сімнадцять',
	18: 'вісімнадцять',
	19: 'дев\'ятнадцять'
}

tenwords = {
	1: 'костиль',
	2: 'двадцять',
	3: 'тридцять',
	4: 'сорок',
	5: 'п\'ятдесят',
	6: 'шістдесят',
	7: 'сімдесят',
	8: 'вісімдесят',
	9: 'дев\'яносто'
}

hunwords = {
	1: 'сто',
	2: 'двісті',
	3: 'триста',
	4: 'чотириста',
	5: 'п\'ятсот',
	6: 'шістсот',
	7: 'сімсот',
	8: 'вісімсот',
	9: 'дев\'ятсот'
}

thowords = {
	0: 'тисяч',
	1: 'тисяча',
	2: 'тисячі',
	3: 'тисячі',
	4: 'тисячі',
	5: 'тисяч',
	6: 'тисяч',
	7: 'тисяч',
	8: 'тисяч',
	9: 'тисяч'
}

uahwords = {
	0: 'гривень',
	1: 'гривня',
	2: 'гривні',
	3: 'гривні',
	4: 'гривні',
	5: 'гривень',
	6: 'гривень',
	7: 'гривень',
	8: 'гривень',
	9: 'гривень'
}

coinwords = {
	0: 'копійок',
	1: 'копійка',
	2: 'копійки',
	3: 'копійки',
	4: 'копійки',
	5: 'копійок',
	6: 'копійок',
	7: 'копійок',
	8: 'копійок',
	9: 'копійок'
}

def num_to_words(num):
	num = str(float(num)).split(".")
	fiata = [int(n) for n in num[0]]
	if len(num[1]) < 2: 
		num[1] += '0'
	coins = num[1][:2]
	kostyl = int(num[0][-2:])
	text = ''
	
	if len(fiata) > 1:
		text = '{}'.format(onewords[kostyl]) if kostyl < 20 else '{} {}'.format(tenwords[fiata[-2]], onewords[fiata[-1]])
	else:
		text = '{}'.format(onewords[fiata[-1]])
	if len(fiata) > 2:
		text = '{}'.format(hunwords[fiata[-3]]) + ' ' + text
	if len(fiata) > 3:
		if len(fiata) > 4:
			kostyl2 = int(''.join(list(map(str, fiata[-5:-3]))))
			text = '{} {}'.format(onewords[kostyl2], thowords[9]) + ' ' + text if kostyl2 < 20 else '{} {} {}'.format(tenwords[fiata[-5]], onewords[fiata[-4]], thowords[fiata[-4]]) + ' ' + text
		else:
			text = '{} {}'.format(onewords[fiata[-4]], thowords[fiata[-4]]) + ' ' + text
	if len(fiata) > 5:
		text = '{}'.format(hunwords[fiata[-6]]) + ' ' + text
	
	return "{} {} {} {}".format(text, uahwords[fiata[-1]] if not (kostyl < 20 and kostyl > 10) else "гривень", coins, coinwords[int(coins[-1])])




print(num_to_words("0.10"))
print(num_to_words("13.19"))
print(num_to_words("21.32"))
print(num_to_words("365.54"))
print(num_to_words("2467.75"))
print(num_to_words("15648.16"))
print(num_to_words("54183.87"))
print(num_to_words("322234.56"))
print(num_to_words("999999.99"))
