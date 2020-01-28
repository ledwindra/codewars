from is_prime import is_prime

class TestIsPrime:

    def test_0(self):
        assert is_prime(0) == False

    def test_1(self):
        assert is_prime(1) == False

    def test_2(self):
        assert is_prime(2) == True

    def test_3(self):
        assert is_prime(73) == True

    def test_4(self):
        assert is_prime(75) == False

    def test_5(self):
        assert is_prime(-1) == False

    def test_6(self):
        assert is_prime(4) == False

    def test_7(self):
        assert is_prime(6) == False

    def test_8(self):
        assert is_prime(8) == False

    def test_9(self):
        assert is_prime(9) == False

    def test_10(self):
        assert is_prime(45) == False

    def test_11(self):
        assert is_prime(-5) == False

    def test_12(self):
        assert is_prime(-8) == False

    def test_13(self):
        assert is_prime(-41) == False
    
    def test_14(self):
        assert is_prime(3) == True

    def test_15(self):
        assert is_prime(5) == True

    def test_16(self):
        assert is_prime(7) == True

    def test_17(self):
        assert is_prime(41) == True
    
    def test_18(self):
        assert is_prime(5099) == True