from functools import reduce


def func_sum(lst):
    return reduce((lambda a, b: a + b), lst)


print(func_sum((21, 31, 2, 1, 1, 1)))
