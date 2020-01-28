from iq_test import iq_test

class TestIqTest:
    def test_0(self):
        assert iq_test("2 4 7 8 10") == 3
    
    def test_1(self):
        assert iq_test("1 2 2") == 1