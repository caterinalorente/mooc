"""
Mini-project description - Guess the number game

The first player thinks of a secret number in some known range 
while the second player attempts to guess the number.
After each guess, the first player answers either Higher, Lower or Correct! 
depending on whether the secret number is higher, lower or equal to the guess. 
"""

import simplegui
import random
import math

# globals
low = high = answer = attempts = 0

# helper functions
def init():
    global low, high, answer, attempts
    
    answer = random.randrange(low, high)
    attempts = math.ceil(math.log((high - low + 1),2))    # attempts >= log(base2)N
    
    print (attempts)
    
    print ("New game. Range is from %d to %d." %(low, high))
    print ("Number of remaining guesses is %d" %(attempts))
    print ("")
    
def compare_guess_with_number(guess, answer):
    if guess < answer:      print ("Higher!")
    elif guess > answer:    print ("Lower!")
    else:                   print ("Correct! Secret number was %d" %(answer))

# event handlers for control panel
def set_range_100():
    global high
    
    high = 100
    init() 

def set_range_1000():
    global high
    
    high = 1000
    init()
   
def get_input(guess):
    global attempts, low, high
    
    if not guess.isdigit() or (guess < str(low)) or (guess > str(high)) or (guess == ""):
        print ("Please enter a valid number widthin the range %d - %d" %(low,high))
        print ("")
    
    else:
        guess = int(guess)
        print ("Guess was %d" %(guess))
    
        attempts -= 1
        print ("Number of remaining guesses is %d" %(attempts))
        if attempts == 0: 
            print ("You ran out of guesses. The answer was %d" %(answer))
            print ("")        
            set_range_100()
        else:
            compare_guess_with_number(guess, answer)
            print ("")            
    
# GUI generation    
f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("Range is [0, 100)", set_range_100, 150)
f.add_button("Range is [0, 1000)", set_range_1000, 150)
f.add_input("Guess!", get_input, 200)

# start
set_range_100()