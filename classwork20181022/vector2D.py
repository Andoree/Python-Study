class Vector2D:
    n = 0

    @classmethod
    def whatistheclass(cls):
        return cls

    @staticmethod
    def getN():
        return

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        print("Zdarova, Ti vizval vektor. Zemlya te6e puhom.")

    def __str__(self):
        return "<%s, %s>" % (self.x, self.y)

    def __add__(self, v):
        return Vector2D(self.x + v.x, self.y + v.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        elif isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        raise Exception("Ayaya")



'''
v1 = Vector2D(1, 2)
v2 = Vector2D(100, 200)
v3 = v1 + v2
print(v3)
v3()
print(v3 * v1)
print(v3 * 24)

print(v2.n)
print(Vector2D.n)
v2.n = 3
print(v2.n)
print(Vector2D.n)
v2.owner = "Ai"
print(v2.owner)

print(v2.whatistheclass())
v2.getN()
'''