import palindrome
import unittest

class TestPalindrome_v1(unittest.TestCase):
    
    def test_even_word_palindrome(self):
        # given
        word = 'noon'
        # when
        isPalindrome = palindrome.is_word_palindrome_v1(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_odd_word_palindrome(self):
        # given
        word = 'racecar'
        # when
        isPalindrome = palindrome.is_word_palindrome_v1(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_word_is_not_palindrome(self):
        # given
        word = 'dented'
        # when
        isPalindrome = palindrome.is_word_palindrome_v1(word)
        # then
        self.assertEquals(isPalindrome, False) 
        
class TestPalindrome_v2_1(unittest.TestCase):
    
    def test_even_word_palindrome(self):
        # given
        word = 'noon'
        # when
        isPalindrome = palindrome.is_word_palindrome_v2_1(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_odd_word_palindrome(self):
        # given
        word = 'racecar'
        # when
        isPalindrome = palindrome.is_word_palindrome_v2_1(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_word_is_not_palindrome(self):
        # given
        word = 'dented'
        # when
        isPalindrome = palindrome.is_word_palindrome_v2_1(word)
        # then
        self.assertEquals(isPalindrome, False)       

class TestPalindrome_v2_2(unittest.TestCase):
    
    def test_even_word_palindrome(self):
        # given
        word = 'noon'
        # when
        isPalindrome = palindrome.is_word_palindrome_v2_2(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_odd_word_palindrome(self):
        # given
        word = 'racecar'
        # when
        isPalindrome = palindrome.is_word_palindrome_v2_2(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_word_is_not_palindrome(self):
        # given
        word = 'dented'
        # when
        isPalindrome = palindrome.is_word_palindrome_v2_2(word)
        # then
        self.assertEquals(isPalindrome, False) 
        
class TestPalindrome_v3_1(unittest.TestCase):
    
    def test_even_word_palindrome(self):
        # given
        word = 'noon'
        # when
        isPalindrome = palindrome.is_word_palindrome_v3_1(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_odd_word_palindrome(self):
        # given
        word = 'racecar'
        # when
        isPalindrome = palindrome.is_word_palindrome_v3_1(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_word_is_not_palindrome(self):
        # given
        word = 'dented'
        # when
        isPalindrome = palindrome.is_word_palindrome_v3_1(word)
        # then
        self.assertEquals(isPalindrome, False)  
        
class TestPalindrome_v3_2(unittest.TestCase):
    
    def test_even_word_palindrome(self):
        # given
        word = 'noon'
        # when
        isPalindrome = palindrome.is_word_palindrome_v3_2(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_odd_word_palindrome(self):
        # given
        word = 'racecar'
        # when
        isPalindrome = palindrome.is_word_palindrome_v3_2(word)
        # then
        self.assertEquals(isPalindrome, True)
        
    def test_word_is_not_palindrome(self):
        # given
        word = 'dented'
        # when
        isPalindrome = palindrome.is_word_palindrome_v3_2(word)
        # then
        self.assertEquals(isPalindrome, False) 
            
if __name__ == "__main__":
    unittest.main()  
