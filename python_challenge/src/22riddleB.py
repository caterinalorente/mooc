'''
 -- Riddle 22 --
Emulate
http://www.pythonchallenge.com/pc/hex/copper.html
'''

import Image, ImageSequence, turtle, time

# First a handy function to return an iterator over the frames of the GIF: 

def get_iterator():
    return ImageSequence.Iterator(Image.open('../Files/22white.gif'))

# Poking around suggests the following: 
# for each frame, one pixel uses color 8 and all the rest use color 0. 
# Also, color 0 is (0, 0, 0), and color 8 is (8, 8, 8). 
# So this is an animation of a 1-pixel, very dark dot, moving on a black background. 
#Here's code to verify all that: 

for frame in get_iterator():
    assert frame.getcolors() == [(39999, 0), (1, 8)]
    p = frame.getpalette()
    assert p[0:3] == [0, 0, 0]
    assert p[8*3:9*3] == [8, 8, 8]

# Since only colors 0 and 8 are ever used, 
# and only 1 pixel per frame uses color 8, the only real info here is 
# which pixel uses color 8? So let's make a list of all color 8 locations. 
# by using the very fast getdata() method.

locations = []
for frame in get_iterator():
    c = list(frame.getdata())
    assert len(c) == 40000
    i = c.index(8)
    y, x = divmod(i, 200)
    locations.append((x, y))

# Staring at the list of locations shows that only 9 are used, 
# the cross-product of (98, 100, 102) with itself, centered on (100, 100). 
# Remember the photo of the joystick? Can't be a coincidence! 
# As the page title said, we should emulate a joystick. But a joystick doing what? 
# I eventually pictured a very simple line-drawing app, drawing a line at a constant speed, and moving in the current direction of the joystick. 
# Another twist is needed to make that work smoothly: whenever the joystick returns to the netural (center) position, the screen should reset.

# PIL's ImageDraw module can be used for this, but it's easier to use the standard turtle.py library. 
# This requires some coordinate conversion: 
# PIL, like most standard graphics packages, puts (0, 0) in the upper left corner and has y increasing "down".
# But turtle puts (0, 0) smack in the middle of the canvas and has y increasing "up". 
# This is all that's needed: 

EXP = 2    # make bigger to draw larger letters
x = y = 0  # center of turtle canvas
for pilx, pily in locations:
    dx = (pilx - 100) // 2  # -1, 0, +1
    dy = (100 - pily) // 2  # -1, 0, +1
    x += dx * EXP
    y += dy * EXP
    turtle.goto(x, y)
    if dx == dy == 0: # joystick at center
        time.sleep(1) # so we can read the letter
        turtle.reset()
        x = y = 0
