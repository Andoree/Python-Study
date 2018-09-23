import re
#re.search(p, s)
#re.fullsearch(p, s)
'''
re.compile("regularka")'
for t in re.finditer(p,"10:10:Int, 11:50:BD")
    t.group(2)
    ?p<hours>
    ?p<minutes>[0-5]\d
    t.group('minutes')

'''
def check(str):
    pattern = '^[qwrtpsdfghjklzxcvbnm].*[aiueoy]{2}$'
    print(re.fullmatch(pattern, str))

f = open('4.txt')
for line in f:
    for str in line.split():
        check(str)

