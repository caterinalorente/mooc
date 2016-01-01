# RAT RACE

# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.
WALL = '#'      # The visual representation of a wall.
HALL = '.'      # The visual representation of a hallway.
SPROUT = '@'    # The visual representation of a brussels sprout.

# Constants for the directions. Use these to make Rats move.
LEFT = -1       # The left direction.
RIGHT = 1       # The right direction.
NO_CHANGE = 0   # No change in direction.
UP = -1         # The up direction.
DOWN = 1        # The down direction.

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'

class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col, num_sprouts_eaten = 0):
        """ 
        (Rat, str, int, int) -> NoneType

        Initialize the rat's four instance variables:

        symbol: the 1-character symbol for the rat
        row: the row where the rat is located
        col: the column where the rate is located
        num_sprouts_eaten: the number of sprouts that this rat has eaten, which is initially 0. 
        
        >>> rat = Rat('P', 1, 4)
        >>> rat.symbol
        P
        >>> rat.row
        1
        >>> rat.col
        4
        >>> rat.num_sprouts_eaten
        0
        """
        
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten
        
    def set_location(self, row, col):
        """ 
        (Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column. 
        
        >>> rat = Rat('J', 2, 5)
        >>> rat.row
        3
        >>> rat.col
        5
        >>> rat.set_location(1, 4)
        >>> rat.row
        1
        >>> rat.col
        4
        """
        
        self.row = row
        self.col = col
        
    def eat_sprout(self):
        """
        (Rat) -> NoneType
        
        Add one to the rat's instance variable num_sprouts_eaten. Yuck.
        >>> rat = Rat('P', 1, 4)
        >>> rat.num_sprouts_eaten
        0
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """ 
        
        self.num_sprouts_eaten += 1
        
    def __str__(self):
        """
        (Rat) -> str
        
        The first parameter represents a rat. Return a string representation of the rat, in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.

        For example: 'J at (4, 3) ate 2 sprouts.'
        Do not put a newline character ('\n') at the end of the string.
        
        >>> rat = Rat('P', 1, 4)
        >>> rat.__str__()
        'P at (1, 4) ate 0 sprouts.'
        """
        
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
               
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2, num_sprouts_left = 0):
        """
        (Maze, list of list of str, Rat, Rat) -> NoneType
        
        Initialize this maze's four instance variables:

        maze: a maze with contents specified by the second parameter.
        rat_1: the first rat in the maze.
        rat_2: the second rat in the maze.
        num_sprouts_left: the number of uneaten sprouts in this maze.

        Maze([['#', '#', '#', '#', '#', '#', '#'], 
              ['#', '.', '.', '.', '.', '.', '#'], 
              ['#', '.', '#', '#', '#', '.', '#'], 
              ['#', '.', '.', '@', '#', '.', '#'], 
              ['#', '@', '#', '.', '@', '.', '#'], 
              ['#', '#', '#', '#', '#', '#', '#']], 
              Rat('J', 1, 1),
              Rat('P', 1, 4))
        """
        
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        # We set the symbol of the rat in the maze according to the the rat coords        
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol
        self.maze[rat_1.row][rat_1.col] = rat_1.symbol

        self.num_sprouts_left = num_sprouts_left

        for row in maze:
            for item in row:
                if item == "@":
                    self.num_sprouts_left += 1
                          
    def is_wall(self, row, col):
        """
        (Maze, int, int) -> bool
        
        Return True if and only if there is a wall at the given row and column of the maze. 
        
        >>> maze.is_wall[0][1]
        True
        >>> maze.is_wall[1][1]
        False
        """

        if self.maze[row][col] == "#":   return True
        else:   return False
        
    def get_character(self, row, col):
        """
        (Maze, int, int) -> str
        
        Return the character in the maze at the given row and column. 
        If there is a rat at that location, then its character should be returned rather than HALL. 
        
        >>> maze.get_character[0][0]
        #
        >>> maze.get_character[1][1]
        J
        >>> maze.get_character[1][4]
        P
        """
        
        return self.maze[row][col]

    def move(self, rat, dirX, dirY):
        """
         (Maze, Rat, int, int) -> bool 
         
        The first parameter represents a maze.
        The second represents a rat.
        The third represents a vertical direction change (UP, NO_CHANGE or DOWN).
        And the fourth represents a horizontal direction change (LEFT, NO_CHANGE or RIGHT).

        Move the rat in the given direction:
            - Unless there is a wall in the way. 
            - Also, check for a Brussels sprout at that location and, if present:
                have the rat eat the Brussels sprout,
                make that location a HALL, and
                decrease the value that num_sprouts_left refers to by one.

        Return True if and only if there wasn't a wall in the way.
        """
        
        old_vector = [rat.row, rat.col]
        new_vector = [rat.row + dirX, rat.col + dirY]
        
        char = self.get_character(new_vector[0], new_vector[1])
        
        if char != WALL:
            # If we can move we have to:
            # 1- set current rat cords to .
            self.maze[old_vector[0]][old_vector[1]] = HALL
            # 2- Move the rat to its new position
            self.maze[new_vector[0]][new_vector[1]] = rat.symbol
            # 3- Update the rat's coordinates
            rat.row = new_vector[0]
            rat.col = new_vector[1]
             
            if char == SPROUT:
                rat.eat_sprout()            # Have the rat eat the Brussels sprout,
                self.num_sprouts_left -= 1  # Decrease the value that num_sprouts_left refers to by one.
        else:
            return False
                
        return True
        
    def __str__(self):
        """
        (Maze) -> str
        
        Return a string representation of the maze, using the format shown in this example:

            #######
            #J..P.#
            #.###.#
            #..@#.#
            #@#.@.#
            #######
            J at (1, 1) ate 0 sprouts.
            P at (1, 4) ate 0 sprouts.
            
        Do not put a newline character ('\n') at the end of the string.
        """
        
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol
        
        result = ''.join(self.maze[0])
        for row in self.maze[1:]:
            result = result + '\n' + ''.join(row)
            
        result = result + '\n{0}\n{1}'.format(self.rat_1, self.rat_2)
        
        return result