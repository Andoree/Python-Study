from functools import reduce

def func_max(lst):
    return reduce(lambda a, b: a if a > b else b, lst)


print(func_max((10, 21, 31, 41, 5, 3131, 322322, -4)))
