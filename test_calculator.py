import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1,2,'+')
        self.assertEqual(r,3)


    def test_odejmowanie(self):
        r = calculate(50,80,'-')
        self.assertEqual(r,-30)


    def test_mozenie(self):
        r = calculate(5,4,'*')
        self.assertEqual(r,20)


    def test_dzielenie(self):
        r = calculate(60,5,'/')
        self.assertEqual(r,12)


    def test_reszta_dzielenie(self):
        r = calculate(23,5,'%')
        self.assertEqual(r,3)


    def test_potegowanie(self):
        r = calculate(2,10,'^')
        self.assertEqual(r,1024)
