from playing_with_digits import dig_pow

class TestDigPow:

    def test_0(self):
        assert dig_pow(89, 1) == 1
    
    def test_1(self):
        assert dig_pow(92, 1) == -1

    def test_2(self):
        assert dig_pow(46288, 3) == 51