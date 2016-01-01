import unittest
import sherlock_and_array


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sherlock_and_array(1,[1]), "YES")
        self.assertEqual(sherlock_and_array(2,[1,0]), "YES")
        self.assertEqual(sherlock_and_array(2,[2,1]), "NO")
        self.assertEqual(sherlock_and_array(3,[55,1,55]), "YES")
        self.assertEqual(sherlock_and_array(3,[1,-1,32]), "YES")
        self.assertEqual(sherlock_and_array(3,[55,1,32]), "NO")
        self.assertEqual(sherlock_and_array(4, [1,2,3,3]), "YES")

unittest.main()