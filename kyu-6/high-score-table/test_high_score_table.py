import unittest
from main import HighScoreTable

table = HighScoreTable(3)

class TestMain(unittest.TestCase):

    def test_scores(self):
        self.assertEqual(table.scores, [])

    def test_update_0(self):
        table.update(10)
        self.assertEqual(table.scores, [10])

    def test_update_1(self):
        table.update(8)
        table.update(12)
        self.assertEqual(table.scores, [12, 10, 8])

    def test_update_2(self):
        table.update(5)
        self.assertEqual(table.scores, [12, 10, 8])

    def test_update_3(self):
        table.update(10)
        self.assertEqual(table.scores, [12, 10, 10])

    def test_update_4(self):
        table.update(10)
        self.assertEqual(table.scores, [12, 10, 10])

    def test_update_5(self):
        table.update(20)
        self.assertEqual(table.scores, [20, 12, 10])

    def test_update_6(self):
        table.update(20)
        self.assertEqual(table.scores, [20, 20, 12])

    def test_reset(self):
        table.reset()
        self.assertEqual(table.scores, [])

if __name__ == '__main__':
    unittest.main()