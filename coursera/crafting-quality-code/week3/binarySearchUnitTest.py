import binarySearch
import unittest

class TestBinarySearch_v1(unittest.TestCase):
    
    def test_value_at_beginning(self):
        # given
        L = [2, 3, 5, 7]
        target = 2
        expected = 0
        # when
        returnedValue = binarySearch.binary_search_v1(L, target)
        # then
        self.assertEquals(returnedValue, expected, "2 is located at index 0 and we get %s" %returnedValue)

    def test_value_at_end(self):
        # given
        L = [2, 3, 5, 5]
        target = 5
        expected = 2
        # when
        returnedValue = binarySearch.binary_search_v1(L, target)
        # then
        self.assertEquals(returnedValue, expected, "5 is located at index 0 and we get %s" %returnedValue)
        
    def test_value_not_in_list(self):
        # given
        L = [2, 3, 5, 7]
        target = 8
        expected = -1
        # when
        returnedValue = binarySearch.binary_search_v1(L, target)
        # then
        self.assertEquals(returnedValue, expected, "-1 should be returned since 8 is not in list and we get %s" %returnedValue)

class TestBinarySearch_v2(unittest.TestCase):
    
    def test_value_at_beginning(self):
        # given
        L = [2, 3, 5, 7]
        target = 2
        expected = 0
        # when
        returnedValue = binarySearch.binar_search_v2(L, target)
        # then
        self.assertEquals(returnedValue, expected, "2 is located at index 0 and we get %s" %returnedValue)

    def test_value_at_end(self):
        # given
        L = [2, 3, 5, 5]
        target = 5
        expected = 2
        # when
        returnedValue = binarySearch.binar_search_v2(L, target)
        # then
        self.assertEquals(returnedValue, expected, "5 is located at index 0 and we get %s" %returnedValue)
        
    def test_value_not_in_list(self):
        # given
        L = [2, 3, 5, 7]
        target = 8
        expected = -1
        # when
        returnedValue = binarySearch.binar_search_v2(L, target)
        # then
        self.assertEquals(returnedValue, expected, "-1 should be returned since 8 is not in list and we get %s" %returnedValue)

if __name__ == "__main__":
    unittest.main()