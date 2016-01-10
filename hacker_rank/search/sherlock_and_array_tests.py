import unittest
from mooc.hacker_rank.search.sherlock_and_array import sherlock_and_array_elegant, sherlock_and_array_brute_force


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sherlock_and_array_brute_force("1\n1\n1"), "YES")
        self.assertEqual(sherlock_and_array_brute_force("1\n2\n1 0"), "YES")
        self.assertEqual(sherlock_and_array_brute_force("1\n2\n2 1"), "NO")
        self.assertEqual(sherlock_and_array_brute_force("1\n3\n55 1 55"), "YES")
        self.assertEqual(sherlock_and_array_brute_force("1\n3\n1 -1 32"), "YES")
        self.assertEqual(sherlock_and_array_brute_force("1\n3\n55 1 32"), "NO")
        self.assertEqual(sherlock_and_array_brute_force("1\n4\n1 2 3 3"), "YES")

        self.assertEqual(sherlock_and_array_elegant("1\n1\n1"), "YES")
        self.assertEqual(sherlock_and_array_elegant("1\n2\n1 0"), "YES")
        self.assertEqual(sherlock_and_array_elegant("1\n2\n2 1"), "NO")
        self.assertEqual(sherlock_and_array_elegant("1\n3\n55 1 55"), "YES")
        self.assertEqual(sherlock_and_array_elegant("1\n3\n1 -1 32"), "YES")
        self.assertEqual(sherlock_and_array_elegant("1\n3\n55 1 32"), "NO")
        self.assertEqual(sherlock_and_array_elegant("1\n4\n1 2 3 3"), "YES")

unittest.main()
