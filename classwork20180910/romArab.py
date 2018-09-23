#! coding: utf-8
map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}


def map_to_arab(r_num):
    i = 0
    sum = 0
    while (i < len(r_num) - 1):
        if map.get(r_num[i]) >= map.get(r_num[i + 1]):
            sum += map.get(r_num[i])
        else:
            sum -= map.get(r_num[i])
        i += 1
    sum += map.get(r_num[-1])
    return sum

f = open('data/3.txt')
for line in f:
    for str in line.split():
    #print(line)
        print(str, ' ', map_to_arab(str))
