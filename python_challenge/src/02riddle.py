'''
 -- Riddle 2 --
 http://www.pythonchallenge.com/pc/def/ocr.html
 Find letters in all the mess
 --------------
'''

from string import ascii_lowercase

f = open('../Files/02ocr.txt', 'r').read()
print filter(lambda x: x in ascii_lowercase, f)