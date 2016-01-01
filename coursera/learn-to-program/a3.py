'''
http://spark-public.s3.amazonaws.com/programming1/a3/a3.html

A3 Problem Domain: Word Search Game

For A3, you will implement a word search game. 
The game involves an rectangular board of uppercase letters that is read from a file.
For example, here are the file contents representing a (tiny) 2 row by 4 column board:

ANTT
XSOB

The game also involves a non-empty words list read from a file. 
For example, here are example file contents for a list of three words:

ANT
BOX
SOB
TO

The object of the game is for the players to view the board and find words (the words list is unknown to the players). 
Words may be contained in rows (from left to right) or columns (from top to bottom). 
When a player correctly guesses a word that occurs in the list of words, that player is awarded points 
according to a scoring system described below. The game ends when all words from the list of words have been guessed.
The player with the highest score wins.

The words from the words list and the letters of the board are made up of alphabetic, uppercase characters.

Terminology in this handout

    A board is a list of list of str, such as [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']].
    A words list is a list of str such as ['ANT', 'SOB', TO'].
'''

def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    '''
    
    if word in wordlist:
        return True
    return False

def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    '''

    listOfCharsInRow = board[row_index]
    return ''.join(listOfCharsInRow)

def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 3)
    'TB'
    '''

    chars = ''
    for row in board:
        chars += row[column_index]
    
    return (chars) 

def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TT')
    True
    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TXS')
    False
    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'OBS')
    False
    '''

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False

def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    '''
    
    firstRow = board[0]
    for row_index in range(len(firstRow)):
        if word in make_str_from_column(board, row_index):
            return True
    return False 
            
def board_contains_word(board, word):
    '''(list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    '''

    wordInRow = board_contains_word_in_row(board, word)
    wordInColumn = board_contains_word_in_column(board, word)
    
    if (wordInRow == True) or (wordInColumn == True): 
        return True
    else:
        return False
    
def word_score(word):
    '''(str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character in word
                 7-9: 2 points per character in word
                 10+: 3 points per character in word

    >>> word_score('DRUDGERY')
    16
    '''
    
    length = len(word)
    if length < 3:
        return 0
    elif (length >= 3) and (length <= 6):
        return (1*length)
    elif (length >= 7) and (length <= 9):
        return (2*length)
    else:
        return (3*length)

def update_score(player_info, word):
    '''([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    '''

    score = word_score(word)
    player_info[1] += score
    
def num_words_on_board(board, words):
    '''(list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    '''
    
    counter = 0
    for word in words:
        if board_contains_word(board, word) == True:
            counter += 1
    
    return counter

def read_words(words_file):
    ''' (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    '''
    
    wordsList = []   
    
    for line in words_file:
        if line != '\n':
            line = line.strip('\n')
            wordsList.append(line)
        
    words_file.close()
        
    return wordsList

def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    '''
    
    board = [[line[i] for i in range(0, len(line.strip('\n')))] for line in board_file if line != '\n']
    
    board_file.close()
        
    return board