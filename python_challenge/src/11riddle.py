'''
 -- Riddle 11 --
 http://www.pythonchallenge.com/pc/return/5808.html
 Odd Even
 --------------
'''

import Image

im = Image.open('../Files/11cave.jpg')
pixels = im.load()
canvas = Image.new("RGB", (im.size[0], im.size[1]), color = "white")

# rows 0,2,4...
for x in range(0, im.size[0], 2):
    for y in range(0, im.size[1], 2):
        canvas.putpixel((x,y), im.getpixel((x,y)))
# rows 1,3,5...
for x in range(1, im.size[0], 2):
    for y in range(1, im.size[1], 2):
        canvas.putpixel((x,y), im.getpixel((x,y)))
canvas.show()

#Another solution
#from PIL import Image, ImageEnhance
#im = Image.open('../Files/11cave.jpg')
#final = ImageEnhance.Brightness(im)
#final.enhance(8).show()

#Yet another solution
#from PIL import ImageEnhance
#Image.open(../Files/11cave.jpg').resize((320, 240)).show()

