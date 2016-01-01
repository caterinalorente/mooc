''' 
 -- Riddle 14 --
 http://www.pythonchallenge.com/pc/return/italy.html
 Walk around -- cat
 --------------
'''

from PIL import Image

def calculate_new_coords_and_direction(canvas, direction, coords):
    pixel = canvas.load()    
    
    if ((coords[0]+direction[0] == 100) or (coords[1]+direction[1] == 100) or (coords[0]+direction[0] < 0) or (coords[1]+direction[1] < 0) or (pixel[coords[0]+direction[0], coords[1]+direction[1]][0] != 255)):
        # snake has already gone through this pixel or it is about to crash with the wall
        if direction[0] == 1 and direction[1] == 0:   direction = [0, 1]    # Right->Down 
        elif direction[0] == 0 and direction[1] == 1: direction = [-1, 0]   # Down->Left 
        elif direction[0] == -1 and direction[1] == 0:  direction = [0, -1] # Left->Up 
        elif direction[0] == 0 and direction[1] == -1: direction = [1, 0]   # Up->Right 
    
    return(update_coords(coords, direction), direction)
    
def update_coords(coords, direction):
    coords[0] += direction[0]
    coords[1] += direction[1]
    return(coords)
    
def paint(canvas, coords, pixel):
    canvas.putpixel(coords, pixel)
    return(canvas)

im = Image.open('../Files/14wire.png') # Image has y=0
pixels = im.load() 
canvas = Image.new('RGB', (100,100), 'white')
direction = (1,0)
coords = [-1,0]

for i in range(0, 10000):
    coords, direction = calculate_new_coords_and_direction(canvas, direction, coords)
    hiddenMessage = pixels[i, 0]
    canvas = paint(canvas, coords, hiddenMessage)
canvas.show()

# The samet solution
#def spiral(source):
#    target = Image.new(source.mode, (100, 100))
#    left, top, right, bottom = (0, 0, 99, 99)
#    x, y = 0, 0
#    dirx, diry = 1, 0
#    for i in xrange(10000):
#        target.putpixel((x, y), source.getpixel((i, 0)))
#        if dirx == 1 and x == right:
#            dirx, diry = 0, 1
#            top += 1
#        elif dirx == -1 and x == left:
#            dirx, diry = 0, -1
#            bottom -= 1
#        elif diry == 1 and y == bottom:
#            dirx, diry = -1, 0
#            right -= 1
#        elif diry == -1 and y == top:
#            dirx, diry = 1, 0
#            left += 1
#        x += dirx
#        y += diry
#    return target
