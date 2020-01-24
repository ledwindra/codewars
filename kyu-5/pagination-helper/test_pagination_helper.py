import unittest
from pagination_helper import PaginationHelper

collection = range(1,25)
helper = PaginationHelper(collection, 10)

class TestPaginationHelper(unittest.TestCase):

    def test_first(self):
        self.assertEqual(helper.page_count(), 3)
    
    def test_second(self):
        self.assertEqual(helper.page_index(23), 2)

    def test_third(self):
        self.assertEqual(helper.item_count(), 24)

if __name__ == '__main__':
    unittest.main()