'''
Created on Mar 10, 2013

@author: caterina
'''

import a3
import unittest

class TestA3(unittest.TestCase):
    
    def test_is_valid_word(self):
        # given
        wordlist = ['ANT', 'BOX', 'SOB', 'TO']
        word = 'TO'
        # when
        isValidWord = a3.is_valid_word(wordlist, word)
        # then
        self.assertEquals(isValidWord, True)
        
    def test_is_not_valid_word(self):
        # given
        wordlist = ['ANT', 'BOX', 'SOB', 'TO']
        word = 'AN'
        # when
        isValidWord = a3.is_valid_word(wordlist, word)
        # then
        self.assertEquals(isValidWord, False)
        
    def test_word_is_not_in_list(self):
        # given
        wordlist = ['ANT', 'BOX', 'SOB', 'TO']
        word = 'PEP'
        # when
        isValidWord = a3.is_valid_word(wordlist, word)
        # then
        self.assertEquals(isValidWord, False)
    
    def test_make_str_from_row_0(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        row_index = 0
        # when
        string = a3.make_str_from_row(board, row_index)
        # then
        self.assertEqual(string, 'ANTT')
        
    def test_make_str_from_row_1(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        row_index = 1
        # when
        string = a3.make_str_from_row(board, row_index)
        # then
        self.assertEqual(string, 'XSOB')

    def test_make_str_from_column_1(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        column_index = 1
        # when
        string = a3.make_str_from_column(board, column_index)
        # then
        self.assertEqual(string, 'NS')
        
    def test_make_str_from_column_3(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        column_index = 3
        # when
        string = a3.make_str_from_column(board, column_index)
        # then
        self.assertEqual(string, 'TB')
        
    def test_board_contains_word_in_row_1(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'TT'
        # when
        isWordInRow = a3.board_contains_word_in_row(board, word)
        # then
        self.assertEquals(isWordInRow, True)
        
    def test_board_contains_word_in_row_2(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'SOB'
        # when
        isWordInRow = a3.board_contains_word_in_row(board, word)
        # then
        self.assertEquals(isWordInRow, True)
        
    def test_word_is_a_mix_of_both_rows(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'TXS'
        # when
        isWordInRow = a3.board_contains_word_in_row(board, word)
        # then
        self.assertEquals(isWordInRow, False)
        
    def test_word_is_a_mix_of_row_2(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'OBS'
        # when
        isWordInRow = a3.board_contains_word_in_row(board, word)
        # then
        self.assertEquals(isWordInRow, False)
        
    def test_board_does_not_contain_word_in_column(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'NO'
        # when
        isWordInColumn = a3.board_contains_word_in_column(board, word)
        # then
        self.assertEquals(isWordInColumn, False)
        
    def test_board_contains_word_in_column(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'TO'
        # when
        isWordInColumn = a3.board_contains_word_in_column(board, word)
        # then
        self.assertEquals(isWordInColumn, True)
        
    def test_board_contains_word_1(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'ANT'
        # when
        isWordInBoard = a3.board_contains_word(board, word)
        # then
        self.assertEquals(isWordInBoard, True)
        
    def test_board_contains_word_2(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'SO'
        # when
        isWordInBoard = a3.board_contains_word(board, word)
        # then
        self.assertEquals(isWordInBoard, True)
        
    def test_board_contains_word_3(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'TO'
        # when
        isWordInBoard = a3.board_contains_word(board, word)
        # then
        self.assertEquals(isWordInBoard, True)

    def test_board_does_not_contain_word_1(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'TTX'
        # when
        isWordInBoard = a3.board_contains_word(board, word)
        # then
        self.assertEquals(isWordInBoard, False) 
        
    def test_board_does_not_contain_word_2(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'ANTS'
        # when
        isWordInBoard = a3.board_contains_word(board, word)
        # then
        self.assertEquals(isWordInBoard, False) 
        
    def test_board_does_not_contain_word_3(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'NO'
        # when
        isWordInBoard = a3.board_contains_word(board, word)
        # then
        self.assertEquals(isWordInBoard, False)
        
    def test_word_score_0(self):
        # given
        word = 'AT'
        # when
        score = a3.word_score(word)
        # then
        self.assertEquals(score, 0)

    def test_word_score_3(self):
        # given
        word = 'BUT'
        # when
        score = a3.word_score(word)
        # then
        self.assertEquals(score, 3)
        
    def test_word_score_5(self):
        # given
        word = 'SUNNY'
        # when
        score = a3.word_score(word)
        # then
        self.assertEquals(score, 5) 
        
    def test_word_score_6(self):
        # given
        word = 'SPRING'
        # when
        score = a3.word_score(word)
        # then
        self.assertEquals(score, 6)
        
    def test_word_score_14(self):
        # given
        word = 'ICEBERG'
        # when
        score = a3.word_score(word)
        # then
        self.assertEquals(score, 14)   
             
    def test_word_score_8(self):
        # given
        word = 'CHERRIES'
        # when
        score = a3.word_score(word)
        # then
        self.assertEquals(score, 16) 
        
    def test_word_score_9(self):
        # given
        word = 'ARMADILLO'
        # when
        score = a3.word_score(word)
        # then
        self.assertEquals(score, 18)
        
    def test_word_score_30(self):
        # given
        word = 'LONELINESS'
        # when
        score = a3.word_score(word)
        # then
        self.assertEquals(score, 30)      
        
    def test_num_words_in_board(self):
        # given
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        words = ['ANT', 'BOX', 'SOB', 'TO']
        # when
        numOfWords = a3.num_words_on_board(board, words)
        # then
        self.assertEquals(numOfWords, 3)  
        
    def test_read_words(self):
        # given
        wordsFile = open('wordlist1.txt', 'r')
        wordsList = ['CRUNCHY', 'COWS', 'EAT', 'GRASS']
        # when
        receivedWords = a3.read_words(wordsFile)
        # then
        self.assertEquals(receivedWords, wordsList)
        
    def test_read_board(self):
        # given
        boardFile = open('board1.txt', 'r')
        board = [['E','F','J','A','J','C','O','W','S','S'], ['S','D','G','K','S','R','F','D','F','F'], ['A','S','R','J','D','U','S','K','L','K'], ['H','E','A','N','D','N','D','J','W','A'], ['A','N','S','D','N','C','N','E','O','P'], ['P','M','S','N','F','H','H','E','J','E'], ['J','E','P','Q','L','Y','N','X','D','L']]
        # when
        receivedBoard = a3.read_board(boardFile)
        # then
        self.assertEquals(receivedBoard, board)
        
    def test_read_rectangular_assymetric_board(self):
        # given
        boardFile = open('board2.txt', 'r')
        board = [['E','F','J','A','J','C','O','W','S','S'], ['S','D','G','K','S','R','F','D'], ['A','S','R','J','D','U','S','K','L','K'], ['H','E','A','N'], ['A','N','S','D','N','C','N','E','O'], ['P','M','S','N','F','H','H','E','J','E'], ['J','E','P']]
        # when
        receivedBoard = a3.read_board(boardFile)
        # then
        self.assertEquals(receivedBoard, board)   

    def test_read_square_assymetric_board(self):
        # given
        boardFile = open('board3.txt', 'r')
        board = [['E','F','J','A','J','C','O','W','S','S'], ['S','D','G','K','S','R','F','D'], ['A','S','R','J','D','U','S','K','L','K','I']]
        # when
        receivedBoard = a3.read_board(boardFile)
        # then
        self.assertEquals(receivedBoard, board)
        
if __name__ == "__main__":
    unittest.main()  
