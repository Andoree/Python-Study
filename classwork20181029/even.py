class Even:
    def __init__(self, val):
        if Even.validate(val):
            self.val = int(val)
        else:
            raise Exception("type mismatch :  Even + and" + str(type(val)))
    
    def validate(val):
        if isinstance(val, int) and val % 2 == 0:
            return True
        elif isinstance(val, float) and val % 2 == 0.0:
            return True
        elif isinstance(val, str) and int(val) % 2 == 0:
            return True
        return False

    def __mul__(self, other):
        if (Even.validate(other)):
            return Even(other * self.val)
        elif (isinstance(other, Even)):
            return Even(other.val * self.val)
        raise Exception("type mismatch :  Even + and" + type(other))

    def __add__(self, other):
        if (Even.validate(other)):
            return Even(other + self.val)
        elif (isinstance(other, Even)):
            return Even(other.val + self.val)
        raise Exception("type mismatch :  Even + and" + type(other))

    def __sub__(self, other):
        if (Even.validate(other)):
            return Even(self.val - other)
        elif (isinstance(other, Even)):
            return Even(self.val - other.val)
        raise Exception("type mismatch :  Even + and" + type(other))

    def __str__(self):
        return str(self.val)


even2 = Even(2)
even4 = Even(4.0)
even6 = Even("6")

lst = [even2, even4, even6]
for i in lst:
    print(i, i * 2, i + 4, i - 10)
