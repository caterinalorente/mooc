'''
 -- Riddle 23 --
What is this module
http://www.pythonchallenge.com/pc/hex/bonus.html

<!--
TODO: do you owe someone an apology? now it is a good time to
tell him that you are sorry. Please show good manners although
it has nothing to do with this level.
-->

<!--it can't find it. this is an undocumented module.-->

<!--'va gur snpr bs jung?'-->
'''

#text = 'va gur snpr bs jung, gur snpr'
#print text.decode('rot13')

import sys, StringIO, re

capture = StringIO.StringIO()
save_stdout, sys.stdout = sys.stdout, capture

import this

sys.stdout = save_stdout
guts = capture.getvalue().lower()
searchfor = "va gur snpr bs ".decode("rot-13")
m = re.search(searchfor + r"(\w+)", guts)
print m.group(1)