'''
 -- Riddle 22 --
Emulate
http://www.pythonchallenge.com/pc/hex/copper.html
'''

import Image, ImageEnhance, ImageSequence

im = Image.open('../Files/22white.gif')
print im.info

# After checking all the pixels, it turns out all are black (0)
# except for pixel(100,100)=8. If we enhance the brightness we see that pixel

enh = ImageEnhance.Brightness(im)
enh.enhance(50).show()

# If we play the animation, the pixel moves
# We extract those pixel movements with the getbbox method, which calculates
# the bounding box of the non-zero regions in the image

path = [i.getbbox()[0:2] for i in ImageSequence.Iterator(im)]
   
dummy = Image.new(im.mode, im.size, 0)
letter = 0
pos = (100, 100)
for p in path:
    if p == (100,100): 
        letter += 1
        pos = (letter * 30,) * 2
    else:
        pos = (pos[0] + p[0] - 100, pos[1] + p[1] - 100)
    dummy.putpixel(pos, 255)
dummy.show()