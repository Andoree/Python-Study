def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


print('20 : ', sign(2))
print('-121 : ', sign(-121))
print('0 : ', sign(0))
