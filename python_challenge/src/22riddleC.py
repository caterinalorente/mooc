'''
 -- Riddle 22 --
Emulate
http://www.pythonchallenge.com/pc/hex/copper.html
'''

# Here's another solution which uses PIL and differs from 
# the other solutions in that it draws the answer into a single image. 
# I also used getbbox() which was a pretty easy way to find 
# the location of the pixel in each frame to key off.

import Image
import ImageDraw

im = Image.open("../Files/22white.gif")
new = Image.new("RGB", (200, 200))
draw = ImageDraw.Draw(new)
cx, cy = 0, 100
for frame in range(133):
    im.seek(frame)
    left, upper, right, lower = im.getbbox()
    dx = (left - 100)//2
    dy = (upper - 100)//2
    if cx:
        draw.point([cx, cy])
    cx += dx
    cy += dy
    if dx == dy == 0:
        cx += 25
        cy = 100
new.show()
