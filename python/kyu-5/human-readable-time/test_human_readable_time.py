from human_readable_time import make_readable

class TestHumanReadableTime:

    def test_0(self):
        assert make_readable(0) == "00:00:00"
    
    def test_1(self):
        assert make_readable(5) == "00:00:05"

    def test_2(self):
        assert make_readable(60) == "00:01:00"

    def test_3(self):
        assert make_readable(86399) == "23:59:59"

    def test_4(self):
        assert make_readable(359999) == "99:59:59"