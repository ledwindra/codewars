from find_the_odd_int import find_it

class TestFindIt:

    def test_0(self):
        assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5

    def test_1(self):
        assert find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) == -1

    def test_2(self):
        assert find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) == 5

    def test_3(self):
        assert find_it([10]) == 10

    def test_4(self):
        assert find_it([1,1,1,1,1,1,10,1,1,1,1]) == 10

    def test_5(self):
        assert find_it([5,4,3,2,1,5,4,3,2,10,10]) == 1