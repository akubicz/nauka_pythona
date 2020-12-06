import unittest

from calculator import str_calculator

class TestStringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculator("a","b",'concat')
        self.assertEqual(r,"ab")

    def test_contain_pos(self):
        r = str_calculator("abcd","cde",'contain')
        self.assertEqual(r,-1)

    def test_contain_neg(self):
        r = str_calculator("abcd","cd",'contain')
        self.assertTrue(r)

    def test_enda_pos(self):
        r = str_calculator("dm","abcdm",'enda')
        self.assertTrue(r)

    def test_enda_neg(self):
        r = str_calculator("f","abcd",'enda')
        self.assertFalse(r)

    def test_startb(self):
        r = str_calculator("abcd","ab",'startb')
        self.assertTrue(r)

        p = str_calculator("abcd","f",'startb')
        self.assertFalse(p)
