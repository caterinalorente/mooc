'''
 -- Riddle 9 --
 http://www.pythonchallenge.com/pc/return/good.html
 Connect the dots. first+second=?
 --------------
'''

import Image,ImageDraw

first = open("../Files/09first.txt", "r").read().split(",")
second = open("../Files/09second.txt", "r").read().split(",")
im = Image.open("../Files/09good.jpg")
draw = ImageDraw.Draw(im)

for i in range(0, len(first)):
    first[i] = int(first[i])
    if i < len(second):
        second[i] = int(second[i])

draw.line(first, 'black')
draw.line(second, 'grey')
im.show()