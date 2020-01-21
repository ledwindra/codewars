import unittest
from datetime import date
from is_your_period_late import is_late

class PeriodLate(unittest.TestCase):

    def test_first(self):
        self.assertEqual(is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
    
    def test_second(self):
        self.assertEqual(is_late(date(2016, 6, 13), date(2016, 7, 16), 28), True)
    
    def test_third(self):
        self.assertEqual(is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)

    def test_fourth(self):
        self.assertEqual(is_late(date(2016, 6, 13), date(2016, 6, 29), 28), False)

    def test_fifth(self):
        self.assertEqual(is_late(date(2016, 7, 12), date(2016, 8, 9), 28), False)

    def test_sixth(self):
        self.assertEqual(is_late(date(2016, 7, 12), date(2016, 8, 10), 28), True)

    def test_seventh(self):
        self.assertEqual(is_late(date(2016, 7, 1), date(2016, 8, 1), 30), True)

    def test_eigth(self):
        self.assertEqual(is_late(date(2016, 6, 1), date(2016, 6, 30), 30), False)

    def test_ninth(self):
        self.assertEqual(is_late(date(2016, 1, 1), date(2016, 1, 31), 30), False)

    def test_tenth(self):
        self.assertEqual(is_late(date(2016, 1, 1), date(2016, 2, 1), 30), True)

if __name__ == '__main__':
    unittest.main()