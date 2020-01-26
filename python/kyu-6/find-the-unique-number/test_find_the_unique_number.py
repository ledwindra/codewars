from find_the_unique_number import find_uniq

class TestFindUniq:

    def test_0(self):
        assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    
    def test_1(self):
        assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

    def test_2(self):
        assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10