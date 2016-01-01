'''
 -- Riddle 3 --
 http://www.pythonchallenge.com/pc/def/equality.html
 One small letter, surrounded by EXACTLY three big bodyguards on each of its sides. -- listedlist
 --------------
'''
 
import re
f = ''.join(open('../Files/03equality.txt', 'r').read().splitlines())
#It is not necessary to replace new lines and treat the whole block as a long string, but leave it to remember the function
pat = '[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
print "".join(re.findall(pat, open('../Files/03equality.txt', 'r').read()))

#Another solution would be,
#.join(x[1] for x in re.findall('(^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}([^A-Z]|$)', text))
#because the text could theoretically start or end with 3 capital letters. Though it does not