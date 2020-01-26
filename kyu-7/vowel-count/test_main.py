import unittest
from main import get_count

class TestMain(unittest.TestCase):

    def test_0(self):
        self.assertEqual(get_count("abracadabra"), 5)

if __name__ == '__main__':
    unittest.main()