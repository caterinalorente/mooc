from PIL import Image

def can_snake_move(canvas, direction, coords):
    pixel = canvas.load()
    
#    if ((coords[0]+direction[0] == 10) or (coords[1]+direction[1] == 10) or (coords[0]+direction[0] < 0) or (coords[1]+direction[1] < 0) or (pixel[coords[0]+direction[0], coords[1]+direction[1]][0] == 0)):
    if ((coords[0]+direction[0] == 100) or (coords[1]+direction[1] == 100) or (coords[0]+direction[0] < 0) or (coords[1]+direction[1] < 0) or (pixel[coords[0]+direction[0], coords[1]+direction[1]][0] == 0)):
        # snake has already gone through this pixel or it is about to crash with the wall
        if direction[0] == 1 and direction[1] == 0:   direction = [0, 1]  # Right->Down 
        elif direction[0] == 0 and direction[1] == 1: direction = [-1, 0]  # Down->Left 
        elif direction[0] == -1 and direction[1] == 0:  direction = [0, -1]  # Left->Up 
        elif direction[0] == 0 and direction[1] == -1: direction = [1, 0]  # Up->Right 
        print 'can_snake_move', direction
        return(update_coords(coords, direction), direction)
    else:
        return(update_coords(coords, direction), direction)
       
def update_coords(coords, direction):
    coords[0] += direction[0]
    coords[1] += direction[1]
    return(coords)
    
def snakeMove(canvas, position):
    canvas.putpixel(coords, 0)
    return(canvas)

canvas = Image.new('RGB', (100,100), 'white')
direction = (1,0)
coords = [-1,0]

for i in range(0, 10000):
    print i
    coords, direction = can_snake_move(canvas, direction, coords)
    canvas = snakeMove(canvas, coords)
canvas.show()