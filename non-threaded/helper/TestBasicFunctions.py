__author__ = 'Janneck'

import unittest
from BasicFunctions import *


class TestBasicFunctions(unittest.TestCase):
    def test_modexp(self):
        self.assertEqual(modexp(2, 5, 7), 4)
        self.assertEqual(modexp(2, 10, 8), 0)

    def test_check_if_wieferich(self):
        self.assertEqual(check_if_wieferich(4), False)
        self.assertEqual(check_if_wieferich(12345), False)
        self.assertEqual(check_if_wieferich(1093), True)
        self.assertEqual(check_if_wieferich(3511), True)


if __name__ == '__main__':
    unittest.main()
