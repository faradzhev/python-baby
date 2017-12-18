#! /usr/bin/env python3
# -*- coding: utf-8 -*-

max_length = 40
text_position = 160

def hideText(text):
	if len(text) <= max_length:
		try:
			f = open('./img.bmp', 'r+b')
			f.read(text_position)
			f.write(bytes(text, 'UTF-8'))
		except Exception as e:
			print("Something went wrong - {}".format(e))
		finally:
			f.flush()
			f.close()
		return True
	else:
		return False
		
def getText(length):
	text = ''
	try:
		f = open('./img.bmp', 'rb')
		f.read(text_position)
		text = f.read(length)
	except Exception as e:
		print("Something went wrong - {}".format(e))
	finally:
		f.flush()
		f.close()
	return str(text, 'UTF-8')

def app():
	s = input("Enter text (up to {} characters): ".format(max_length))
	print("I'm hiding the text...")
	print(hideText(s))
	print("I'm reading the text...")
	print(getText(len(s)))
	
app()
