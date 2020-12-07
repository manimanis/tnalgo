import unittest
from tnalgo import *

class TnAlgoTest(unittest.TestCase):
    def test_alea(self):
        a, b = 5, 10
        mn, mx = 10, 5
        for i in range(3*(b-a)):
            x = alea(a, b)
            if x < mn:
                mn = x
            if x > mx:
                mx = x
        self.assertEqual(mn, a)
        self.assertEqual(mx, b)

    def test_arrondi(self):
        for i in range(5):
            self.assertEqual(arrondi(1+i/10), 1)
        for i in range(5):
            self.assertEqual(arrondi(1.5+i/10), 2)
        for i in range(5):
            self.assertEqual(arrondi(2+i/10), 2)
        for i in range(5):
            self.assertEqual(arrondi(2.5+i/10), 3)
        for i in range(5):
            self.assertEqual(arrondi(-1+i/10), -1)
        for i in range(5):
            self.assertEqual(arrondi(-1.5-i/10), -2)
        for i in range(5):
            self.assertEqual(arrondi(-2-i/10), -2)
        for i in range(5):
            self.assertEqual(arrondi(-2.5-i/10), -3)