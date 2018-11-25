def our_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


def my_range(end, start=0, step=1):
    i = start
    while i < end:
        yield i
        i += step


for k in my_range(100, 0, 3):
    print(k)
'''
i = our_range(5)
print(i.next())

for k in our_range(5):
    print(k)
'''