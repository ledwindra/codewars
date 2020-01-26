from detect_pangram import is_pangram

class TestPangram:

    def test_0(self):

        assert is_pangram('The quick, brown fox jumps over the lazy dog!') == True