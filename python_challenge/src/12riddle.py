''' 
 -- Riddle 12 --
 http://www.pythonchallenge.com/pc/return/evil.html
 Dealing Evil
 --------------
'''

import urllib

def get_challenge(s):
    return urllib.urlopen('http://www.pythonchallenge.com/pc/' + s).read()
gfx = get_challenge('return/evil2.gfx')

types = ['jpg','png','gif','png','jpg']
for i in range(5): open('evil2%d.%s' % (i, types[i]),'wb').write(gfx[i::5])


#The samet solution
#import Image
#from cStringIO import StringIO
#
#s = open("../Files/12evil2.gfx", "rb").read()
#for i in range(5):
#    piece = s[i::5]  # every fifth byte, starting at i
#    im = Image.open(StringIO(piece))
#    f = open("%d.%s" % (i, im.format.lower()), "wb")
#    f.write(piece)
#    f.close()

