import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_single_simbol(self):
        self.assertEqual(romano_a_entero('M'),1000)
        self.assertEqual(romano_a_entero('D'),500)
        self.assertEqual(romano_a_entero('C'),100)
        self.assertEqual(romano_a_entero('L'),50)
        self.assertEqual(romano_a_entero('X'),10)
        self.assertEqual(romano_a_entero('V'),5)
        self.assertEqual(romano_a_entero('I'),1)

    '''
        self.assertEqual(romano_a_entero('MMM'),3000)
        self.assertEqual(romano_a_entero("CC"),200)
        self.assertEqual(romano_a_entero('III'),3)
        self.assertEqual(romano_a_entero('XX'),20)
    '''
        self.assertRaises(ValueError, romano_a_entero, 'Z')
        self.assertRaises(ValueError, romano_a_entero, 23)
        self.assertRaises(OverflowError, romano_a_entero,'VV')


if __name__ == "__main__":
    unittest.main()
