"""
 Mini-project description - Pong

In this project, we will build a version of Pong, one of the first arcade video games (1972).
While Pong is not particularly exciting compared to today's video games, Pong is relatively simple to build 
and provides a nice opportunity to work on the skills that you will need to build a game like Asteroids.
"""

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
SCORE1_POS = [WIDTH/3, HEIGHT/4]
SCORE2_POS = [WIDTH/1.6, HEIGHT/4]
SCORE1_SIZE = 60
SCORE2_SIZE = 60
BALL_SPEED_BOOST_FACTOR = 0.1
PADDLE_VELOCITY_FACTOR = 0.2

paddle1_pos = (HEIGHT/2.0) - HALF_PAD_HEIGHT
paddle2_pos = (HEIGHT/2.0) - HALF_PAD_HEIGHT
paddle1_vel = paddle2_vel = score1 = score2 = 0

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    score1 = score2 = 0
    ball_init(random.choice(['right', 'left']))

def ball_init(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    horizontal = random.randrange(120, 240)/60
    vertical = random.randrange(60, 180)/60
    
    ball_pos = [WIDTH/2, HEIGHT/2] 
    if direction == "right":
        ball_vel = [horizontal, -vertical]
    else:
        ball_vel = [-horizontal, -vertical]

def update_paddle_position(paddle_pos, paddle_vel):
    if paddle_pos <= -paddle_vel:
        paddle_pos = 0.0
    elif paddle_pos >= HEIGHT - PAD_HEIGHT - paddle_vel:
        paddle_pos = HEIGHT - PAD_HEIGHT
    else:
        paddle_pos += paddle_vel
    
    return (paddle_pos)

def check_if_user_scored(ball_pos, paddle_pos, direction):
    global ball_vel, score1, score2

    ball_diameter = BALL_RADIUS * 2
    paddle_bottom_margin = paddle_pos + PAD_HEIGHT
    paddle_top_margin = paddle_pos
    
    if  ((ball_pos + ball_diameter - 1) >= paddle_top_margin) and ((ball_pos - 1) <= paddle_bottom_margin):
        # Increase by 10% the velocity of the ball
        ball_vel[0] += ball_vel[0]*BALL_SPEED_BOOST_FACTOR
        ball_vel[1] += ball_vel[1]*BALL_SPEED_BOOST_FACTOR
        ball_vel[0] *= -1
    else: 
        update_score(direction)
        ball_init(direction)
        
def update_score(direction):
    global score1, score2
    
    if direction == 'right':     score2 += 1
    else:                        score1 += 1
        
def collision_detection():
    global ball_pos, ball_vel
    
    # LEFT
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS): 
        check_if_user_scored(ball_pos[1], paddle1_pos, 'right')
    # RIGHT            
    elif ball_pos[0] >= ((WIDTH - PAD_WIDTH) - BALL_RADIUS):  
        check_if_user_scored(ball_pos[1], paddle2_pos, 'left')
    # TOP
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # BOTTOM  
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1] 
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
     
    # draw mid line and left/right gutters
    c.draw_line([WIDTH/2, 0], [WIDTH/2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collision detection
    collision_detection()
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle position
    paddle1_pos = update_paddle_position(paddle1_pos, paddle1_vel)
    paddle2_pos = update_paddle_position(paddle2_pos, paddle2_vel)
    
    # draw paddles   
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, 'White')
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, 'White')
    
    # draw scores
    c.draw_text(str(score1), SCORE1_POS, SCORE1_SIZE, 'White' 'sans-serif')
    c.draw_text(str(score2), SCORE2_POS, SCORE2_SIZE, 'White', 'sans-serif')
                
def keydown(key):
    global paddle1_vel, paddle2_vel, percentage
    
    velocity = HALF_PAD_HEIGHT * PADDLE_VELOCITY_FACTOR
    if key == simplegui.KEY_MAP["w"]:       paddle1_vel = -velocity
    elif key == simplegui.KEY_MAP["s"]:     paddle1_vel = velocity
    elif key == simplegui.KEY_MAP["up"]:    paddle2_vel = -velocity
    elif key == simplegui.KEY_MAP["down"]:  paddle2_vel = velocity                   
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:       paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:     paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:    paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:  paddle2_vel = 0     

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 100)

# start frame
new_game()
frame.start()