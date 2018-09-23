def myMax(lst):
    max = lst[0]
    for x in lst:
        if x > max:
            max = x
    return max


print(myMax([12, 21, -24, -31, 29, 0, -1]))
