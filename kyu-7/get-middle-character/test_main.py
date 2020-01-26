import unittest
from main import get_middle

class TestMain(unittest.TestCase):

    def test_0(self):
        self.assertEqual(get_middle("test"), "es")

    def test_1(self):
        self.assertEqual(get_middle("testing"), "t")

    def test_2(self):
        self.assertEqual(get_middle("middle"), "dd")

    def test_3(self):
        self.assertEqual(get_middle("A"), "A")
    
    def test_4(self):
        self.assertEqual(get_middle("of"), "of")

if __name__ == '__main__':
    unittest.main()