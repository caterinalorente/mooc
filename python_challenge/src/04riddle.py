'''
 -- Riddle 4 --
 http://www.pythonchallenge.com/pc/def/linkedlist.php
 Nothing = 12345 and the next nothing = 92512 -- peak.html
 --------------
 First time the latest number before sequence repeats is 
'''

from urllib import  urlopen
import re

number = '12345'
while True:
    content = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + number).read()
    print content
    if 'next nothing' in content:
        number = re.findall(r' (\d*)$', content)[0]
    elif 'Divide' in content:
        number = str(int(number)/2)
    else:
        print 'Solution is', content
        break 


# Other solution
# while True:
#    content = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing).read()
#    findnothing = re.compile(r"nothing is (\d+)").search
#    number = findnothing(content)
#    if number:
#        nothing = number.group(1)
#        print "   going to", nothing
#    else:
#        break
