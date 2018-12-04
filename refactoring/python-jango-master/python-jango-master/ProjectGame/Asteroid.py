from FlyingObjects import FlyingObjects


class Asteroid(FlyingObjects):
    # An: renamed cX, cY
    def __init__(self, c_x, c_y):
        FlyingObjects.__init__(self, "asteroid.png", c_x, c_y)
