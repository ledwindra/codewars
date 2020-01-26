from regular_ball_super_ball import Ball

class TestBall:

    def test_0(self):
        assert Ball().ball_type == 'regular' 

    def test_1(self):
        assert Ball('super').ball_type == 'super'