"""
 Mini-project description Rock-paper-scissors-lizard-Spock game

http://www.codeskulptor.org/#user29_YCBP2jUbhOfBhQV_0.py

The key idea of this program is to equate the strings 
rock, paper, scissors, lizard, Spock to numbers as follows:

0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors
"""

import random

def number_to_name(number):
    if number == 0:     name = "rock"
    elif number == 1:   name = "Spock"
    elif number == 2:   name = "paper"
    elif number == 3:   name = "lizard"
    elif number == 4:   name = "scissors"
       
    return (name)

def name_to_number(name):
    if name == "rock":      number = 0
    elif name == "Spock":   number = 1
    elif name == "paper":   number = 2
    elif name == "lizard":  number = 3
    elif name == "scissors":number = 4
    else:   
        print ("%s is not rock, Spock, paper, lizard or scissors." %name)
        number = -1
    
    return (number)
    

def rpsls(player_choice): 
    
    # Parse player's choice and check if valid
    player_number = name_to_number(player_choice)
    if (player_number != -1):
        print ("Player chooses %s" %player_choice)
        
        # Generate computer's choice
        comp_number = random.randrange(0,5)
        comp_name = number_to_name(comp_number)
        print ("Computer chooses %s" %comp_name)
        
        # Check who's the winner and print appripiate message
        difference =  (player_number - comp_number) % 5
        if 1 <= difference <= 2:    print ("Player wins!\n")
        elif 3 <= difference <= 4:  print ("Computer wins!\n") 
        else:   print ("Player and computer tie!\n")

#test    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls(lambda heroes = ["Batman", "Spiderman", "Wonderwoman", "Hulk"]: heroes[random.randint(0, len(heroes))])