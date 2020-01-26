from datetime import date
from is_your_period_late import is_late

class TestIsLate:

    def test_0(self):
        assert is_late(date(2016, 6, 13), date(2016, 7, 16), 35) == False
    
    def test_1(self):
        assert is_late(date(2016, 6, 13), date(2016, 7, 16), 28) == True
    
    def test_2(self):
        assert is_late(date(2016, 6, 13), date(2016, 7, 16), 35) == False

    def test_3(self):
        assert is_late(date(2016, 6, 13), date(2016, 6, 29), 28) == False

    def test_4(self):
        assert is_late(date(2016, 7, 12), date(2016, 8, 9), 28) == False

    def test_5(self):
        assert is_late(date(2016, 7, 12), date(2016, 8, 10), 28) == True

    def test_6(self):
        assert is_late(date(2016, 7, 1), date(2016, 8, 1), 30) == True

    def test_7(self):
        assert is_late(date(2016, 6, 1), date(2016, 6, 30), 30) == False

    def test_8(self):
        assert is_late(date(2016, 1, 1), date(2016, 1, 31), 30) == False

    def test_9(self):
        assert is_late(date(2016, 1, 1), date(2016, 2, 1), 30) == True