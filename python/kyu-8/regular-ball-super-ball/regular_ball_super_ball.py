class Ball(object):

    """
    Description:
    Create a class Ball.

    Ball objects should accept one argument for "ball type" when instantiated.

    If no arguments are given, ball objects should instantiate with a "ball type" of "regular."    

    Example:
    ball1 = Ball()
    ball2 = Ball("super")
    ball1.ball_type  #=> "regular"
    ball2.ball_type  #=> "super"    
    """
    
    def __init__(self, btype = "regular"):
        self.ball_type = btype