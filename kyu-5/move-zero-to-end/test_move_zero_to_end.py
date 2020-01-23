import unittest
from move_zero_to_end import move_zeros

class TestMoveZero(unittest.TestCase):

    def test_first(self):
        self.assertEqual(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
    
    def test_second(self):
        self.assertEqual(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])

    def test_third(self):
        self.assertEqual(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
    
    def test_fourth(self):
        self.assertEqual(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
    
    def test_fifth(self):
        self.assertEqual(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
    
    def test_sixth(self):
        self.assertEqual(move_zeros(["a","b"]),["a","b"])
    
    def test_seventh(self):
        self.assertEqual(move_zeros(["a"]),["a"])
    
    def test_eighth(self):
        self.assertEqual(move_zeros([0,0]),[0,0])
    
    def test_ninth(self):
        self.assertEqual(move_zeros([0]),[0])
    
    def test_tenth(self):
        self.assertEqual(move_zeros([False]),[False])
    
    def test_eleventh(self):
        self.assertEqual(move_zeros([]),[])

if __name__ == '__main__':
    unittest.main()