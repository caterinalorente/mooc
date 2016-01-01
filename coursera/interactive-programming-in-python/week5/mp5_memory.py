# implementation of card game - Memory

import simplegui
import random
import math

CARD_WIDTH = 50
CARD_HEIGHT = 100
NUM_CARDS = 16
LINE_WIDTH = 2
LINE_COLOR = "White"
FILL_COLOR = "Red"
FONT_SIZE = CARD_HEIGHT
FONT_COLOR = "White"

# helper function
def new_game():
    
    global number_of_flipped_cards, deck, cards_exposed, last_two_cards
    
    number_of_flipped_cards = 0
    last_two_cards = [-1, -1]
    
    cards_exposed = [False]* 16
    deck = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
    random.shuffle(deck)
        
# Define event handlers
def mouseclick(pos): 
    
    global number_of_flipped_cards, deck, cards_exposed, last_two_cards
    
    index = pos[0]/CARD_WIDTH  
    
    # If card is up ignore mouse click
    if not cards_exposed[index]:
        if number_of_flipped_cards == 0:
            print "zero"
            number_of_flipped_cards = 1
            last_two_cards[0] = index
            cards_exposed[index] = True
            
        elif number_of_flipped_cards == 1:
            print "one"
            number_of_flipped_cards = 2 
            last_two_cards[1] = index
            cards_exposed[index] = True
                            
        else:
            print "two"
            number_of_flipped_cards = 1
            
            # Check if cards match
            if deck[last_card_index] == deck[index]:
                cards_exposed[last_card_index] = cards_exposed[index] = True
            cards_exposed[last_card_index] = cards_exposed[index] = False             
            
            last_card_index = index
            
        print last_card_index, index
        print cards_exposed
                                                     
def draw(canvas):
    
    for i in range(NUM_CARDS):
        if cards_exposed[i]:
            canvas.draw_text(str(deck[i]), [i*CARD_WIDTH, CARD_HEIGHT-15], FONT_SIZE, FONT_COLOR)
        else:
            canvas.draw_polygon(
                                [[i*CARD_WIDTH,0],[i*CARD_WIDTH,CARD_HEIGHT],[CARD_WIDTH*(i+1),CARD_HEIGHT],[CARD_WIDTH*(i+1),0]],
                                LINE_WIDTH,
                                LINE_COLOR,
                                FILL_COLOR)
      
        

# Frame, button and labels
frame = simplegui.create_frame("Memory", NUM_CARDS * CARD_WIDTH, CARD_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# Event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# Start
new_game()
frame.start()
