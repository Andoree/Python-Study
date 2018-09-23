def letterQuant(filename):
    f = open(filename)
    sum = 0
    for line in f:
        for c in line:
            if c.isalpha():
                sum += 1
    return sum


print(letterQuant('data/1.txt'))