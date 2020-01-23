import unittest
from remove_the_time import shorten_to_date

class RemoveTheTime(unittest.TestCase):

    def test_first(self):
        self.assertEqual(shorten_to_date("Monday February 2, 8pm"), "Monday February 2")
    
    def test_second(self):
        self.assertEqual(shorten_to_date("Tuesday May 29, 8pm"), "Tuesday May 29")

    def test_third(self):
        self.assertEqual(shorten_to_date("Wed September 1, 3am"), "Wed September 1")

    def test_fourth(self):
        self.assertEqual(shorten_to_date("Friday May 2, 9am"), "Friday May 2")

    def test_fifth(self):
        self.assertEqual(shorten_to_date("Tuesday January 29, 10pm"), "Tuesday January 29")

if __name__ == '__main__':
    unittest.main()



