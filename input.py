from functools import reduce
lst = [int(elem) for elem in input().split(" ")]
def max2(x, y):
    return x if x > y else y

max = reduce(max2, lst)
print(max)

# lst.append(x) - adding x to list
# dir - название всех аттрибутов объекта
# table
# is - равенство по ссылкам
# вычитание множеств
# todo: Вычитание на словарях?
# iteritems
#del lst[3] - удаление по позиции(ключу для словарей)
# if obj is not none ////// if not(object is none)
# Что не так с остатком от деления!?!?