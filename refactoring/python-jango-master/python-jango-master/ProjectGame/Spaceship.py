from FlyingObjects import FlyingObjects


class Spaceship(FlyingObjects):
    # An: renamed cX, cY
    def __init__(self, c_x, c_y):
        FlyingObjects.__init__(self, "shuttle.png", c_x, c_y)
