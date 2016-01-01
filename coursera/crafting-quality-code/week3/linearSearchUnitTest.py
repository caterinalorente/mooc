import unittest
import linearSearch

class TestLinearSearch_ForLoop(unittest.TestCase):
    
    def test_value_at_the_beginning(self):
        "The value to be searched is at the beginning of the list"
        #given
        L = [2, 3, 5, 3]
        value = 2
        expected = 0
        # when
        valueAtIndex = linearSearch.for_loop(L, value)
        # then
        self.assertEqual(valueAtIndex, expected)
        
    def test_value_at_the_end(self):
        "The value to be searched is at the end of the list"
        #given
        L = [2, 3, 5, 3]
        value = 5
        expected = 2
        # when
        valueAtIndex = linearSearch.for_loop(L, value)
        # then
        self.assertEqual(valueAtIndex, expected) 
        
    def test_value_not_in_list(self):
        "The value to be searched is at the end of the list"
        #given
        L = [2, 3, 5, 3]
        value = 8
        expected = -1
        # when
        valueAtIndex = linearSearch.for_loop(L, value)
        # then
        self.assertEqual(valueAtIndex, expected)
  
class TestLinearSearch_WhileLoop(unittest.TestCase):
    
    def test_value_at_the_beginning(self):
        "The value to be searched is at the beginning of the list"
        #given
        L = [2, 3, 5, 3]
        value = 2
        expected = 0
        # when
        valueAtIndex = linearSearch.while_loop(L, value)
        # then
        self.assertEqual(valueAtIndex, expected)
        
    def test_value_at_the_end(self):
        "The value to be searched is at the end of the list"
        #given
        L = [2, 3, 5, 3]
        value = 5
        expected = 2
        # when
        valueAtIndex = linearSearch.while_loop(L, value)
        # then
        self.assertEqual(valueAtIndex, expected) 
        
    def test_value_not_in_list(self):
        "The value to be searched is at the end of the list"
        #given
        L = [2, 3, 5, 3]
        value = 8
        expected = -1
        # when
        valueAtIndex = linearSearch.while_loop(L, value)
        # then
        self.assertEqual(valueAtIndex, expected)  
        
if __name__ == "__main__":
    unittest.main()