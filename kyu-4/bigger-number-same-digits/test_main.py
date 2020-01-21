import unittest
from main import next_bigger

class NextBigger(unittest.TestCase):

    def test_first(self):
        self.assertEqual(next_bigger(12), 21)

    def test_second(self):        
        self.assertEqual(next_bigger(513), 531)

    def test_third(self):
        self.assertEqual(next_bigger(2017), 2071)

    def test_fourth(self):
        self.assertEqual(next_bigger(414), 441)

    def test_fifth(self):
        self.assertEqual(next_bigger(144), 414)

if __name__ == '__main__':
    unittest.main()