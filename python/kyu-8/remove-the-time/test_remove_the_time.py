from string import punctuation
from remove_the_time import shorten_to_date

class RemoveTheTime:

    def test_0(self):
        assert shorten_to_date("Monday February 2, 8pm") == "Monday February 2"
    
    def test_1(self):
        assert shorten_to_date("Tuesday May 29, 8pm") == "Tuesday May 29"

    def test_2(self):
        assert shorten_to_date("Wed September 1, 3am") == "Wed September 1"

    def test_3(self):
        assert shorten_to_date("Friday May 2, 9am") == "Friday May 2"

    def test_4(self):
        assert shorten_to_date("Tuesday January 29, 10pm") == "Tuesday January 29"



