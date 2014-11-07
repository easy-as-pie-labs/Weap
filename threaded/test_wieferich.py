__author__ = 'thomas'

import unittest
from MathFunctions import *

class TestHelperFunctions(unittest.TestCase):

    '''
    check modexp of a  number
    '''
    def test_modexp(self):
        self.assertEqual(MathFunctions.modexp(2, 5, 7), 4)
        self.assertEqual(MathFunctions.modexp(2, 10, 8), 0)

    '''
    check if a number is a wieferich number
    the only known wieferich numbers so far are 1093 and 3511
    '''
    def test_is_wieferich(self):
        self.assertEqual(MathFunctions.is_wieferich(2), False)
        self.assertEqual(MathFunctions.is_wieferich(3), False)
        self.assertEqual(MathFunctions.is_wieferich(7), False)
        self.assertEqual(MathFunctions.is_wieferich(1093), True)
        self.assertEqual(MathFunctions.is_wieferich(3511), True)
        self.assertEqual(MathFunctions.is_wieferich(1012393), False)


if __name__ == '__main__':
    unittest.main()
