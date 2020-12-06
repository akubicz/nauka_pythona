import unittest

from koszyk_wartosc import koszyk_wartosc

class TestKoszykWartosc(unittest.TestCase):
    def test_koszyk1(self):

        koszyk1 = [{'nazwa': 'miod', 'cena': 50, 'ilosc': 1},
            {'nazwa': 'mleko', 'cena': 50, 'ilosc': 2},
            {'nazwa': 'sliwki', 'cena': 600, 'ilosc': 1},
            {'nazwa': 'toster', 'cena': 100, 'ilosc':2}]

        r = koszyk_wartosc(koszyk1,'brutto')
        self.assertEqual(r,1168.5)

        p = koszyk_wartosc(koszyk1,'netto')
        self.assertEqual(p,950)
