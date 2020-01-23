import unittest
from mumbling import accum

class TestMumbling(unittest.TestCase):

    def test_first(self):
        self.assertEqual(
            accum("ZpglnRxqenU"), 
            "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
        )

    def test_second(self):
        self.assertEqual(
            accum("NyffsGeyylB"),
            "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
        )

    def test_third(self):
        self.assertEqual(
            accum("MjtkuBovqrU"),
            "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
        )

    def test_fourth(self):
        self.assertEqual(
            accum("EvidjUnokmM"), 
            "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
        )
    
    def test_fifth(self):
        self.assertEqual(
            accum("HbideVbxncC"),
            "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"
        )

if __name__ == '__main__':
    unittest.main()