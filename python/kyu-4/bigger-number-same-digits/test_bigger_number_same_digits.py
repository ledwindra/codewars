from bigger_number_same_digits import next_bigger

class NextBigger:

    def test_first(self):
        assert next_bigger(12) == 21

    def test_second(self):        
        assert next_bigger(513) == 531

    def test_third(self):
        assert next_bigger(2017) == 2071

    def test_fourth(self):
        assert next_bigger(414) == 441

    def test_fifth(self):
        assert next_bigger(144) == 414

if __name__ == '__main__':
    unittest.main()