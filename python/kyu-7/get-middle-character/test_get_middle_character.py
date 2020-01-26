from get_middle_character import get_middle

class TestGetMiddleCharacter:

    def test_0(self):
        assert get_middle("test") == "es"

    def test_1(self):
        assert get_middle("testing") == "t"

    def test_2(self):
        assert get_middle("middle") == "dd"

    def test_3(self):
        assert get_middle("A") == "A"
    
    def test_4(self):
        assert get_middle("of") == "of"