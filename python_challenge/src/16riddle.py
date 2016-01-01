''' 
 -- Riddle 15 --
 http://www.pythonchallenge.com/pc/return/mozart.html
 Let me get this straight
 --------------
'''

from PIL import Image

def paint(canvas, hiddenMessage, paintCoords):
    canvas.paste(hiddenMessage, paintCoords)
    return(canvas)

im = Image.open('../Files/16mozart.gif') # Image has y=0
pixels = im.load() 
canvas = Image.new('RGB', (640,480), 'white')
coords = [0,1]


for i in range(0, 149940): 
    coords[0] += 1
    if pixels[coords[0],coords[1]] == 195:
        pinkSection = im.crop((coords[0], coords[1], 640, coords[1]+1))   # (left, upper, right, lower)
        paintCoords = (0, coords[1], 640-coords[0], coords[1]+1)
        canvas = paint(canvas, pinkSection, paintCoords)
        
        nonPinkSection = im.crop((0, coords[1], coords[0], coords[1]+1))
        paintCoords = (640-coords[0], coords[1], 640, coords[1]+1)
        canvas = paint(canvas, nonPinkSection, paintCoords)
        
        coords[0] = 0
        coords[1] += 1
            
canvas.show()

#The samet solution
#
#>>> import Image
#>>> def straighten(source):
#...     target = source.copy()
#...     for y in range(source.size[1]):
#...         line = [source.getpixel((x, y)) for x in range(source.size[0])]
#...         pink = line.index(195)
#...         line = line[pink:] + line[:pink]
#...         for x, pixel in enumerate(line):
#...             target.putpixel((x, y), pixel)
#...     return target
#>>> out = straighten(Image.open("mozart.gif"))
#>>> out.save("out.gif")
