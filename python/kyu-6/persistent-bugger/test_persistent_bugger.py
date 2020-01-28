from persistent_bugger import persistence

class TestPersistence:
    
    def test_0(self):
        assert persistence(39) == 3
    
    def test_1(self):
        assert persistence(4) == 0
    
    def test_2(self):
        assert persistence(25) == 2

    def test_3(self):
        assert persistence(999) == 4