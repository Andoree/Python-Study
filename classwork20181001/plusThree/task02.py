def task2(lst):
    if lst[0] > 0:
        return False
    for i in range(0, len(lst) - 1):
        if lst[i + 1] > 0:
            if lst[i] % 2 == 0:
                return False
    return True


print(task2((0, 2)))
