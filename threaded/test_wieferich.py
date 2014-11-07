import unittest
from Wieferich import *

class TestHelperFunctions(unittest.TestCase):

    '''
    check if a number is a wieferich number
    the only known wieferich numbers so far are 1093 and 3511
    '''
    def test_is_wieferich(self):
        self.assertEqual(is_wieferich(2), False)
        self.assertEqual(is_wieferich(3), False)
        self.assertEqual(is_wieferich(7), False)
        self.assertEqual(is_wieferich(1093), True)
        self.assertEqual(is_wieferich(3511), True)
        self.assertEqual(is_wieferich(1012393), False)


if __name__ == '__main__':
    unittest.main()
