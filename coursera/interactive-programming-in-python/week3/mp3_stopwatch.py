"""
 Mini-project description - Stopwatch: The Game
http://www.codeskulptor.org/#user12_YalNzFrGpzAXrCz.py

Our mini-project for this week will focus on combining text drawing in the canvas 
with timers to build a simple digital stopwatch that keeps track of the time in tenths of a second.

The stopwatch should contain Start, Stop and Reset buttons.
"""

import simplegui

# globals
t = nVictories = nStops = 0
interval = 100 # 0.1 seconds
size = [200, 150]

# helper functions
def format(t):     
    DD = t % 10
    SS = (t // 10) % 60
    MM = t // 600
    
    DD = str(DD)
    SS = str(SS)
    MM = str(MM)
        
    # zero padding
    if len(SS) == 1: SS = "0" + SS         
        
    return (MM + ":" + SS + "." + DD)
   
# event handlers
def timer_handler():
    global t
    
    t += 1
    
def timer_start():
    timer.start()
    
def timer_stop():
    global nVictories, nStops
    
    timer.stop()
    nStops += 1
    check_if_victory()
    
def timer_reset():
    global t, nVictories, nStops
    
    timer.stop()    
    t = nVictories = nStops = 0

def check_if_victory():
    global t, nVictories
    
    time = format(t)
    if time[-1] == "0":    nVictories += 1 
    
def draw(canvas):  
    global t, size
    
    canvas.draw_text(format(t), [size[0]/4, size[1]/1.75], 35, "Yellow")
    canvas.draw_text(str(nVictories), [150, size[1]-130], 20, "Yellow")
    canvas.draw_text("/", [163, size[1]-130], 20, "Yellow")
    canvas.draw_text(str(nStops), [170, size[1]-130], 20, "Yellow")
                     
                     
# frame
frame = simplegui.create_frame("Testing", size[0], size[1])
frame.set_canvas_background("Green")
start = frame.add_button("Start", timer_start, 100)
stop = frame.add_button("Stop", timer_stop, 100)
stop = frame.add_button("Reset", timer_reset, 100)
frame.set_draw_handler(draw)

# register event handlers
timer = simplegui.create_timer(interval, timer_handler)

# start
frame.start()