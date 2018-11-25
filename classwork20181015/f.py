import os
import shutil

for d, ds, fs in os.walk('.'):
    print(d, " : ", fs)

#shutil.copy('q.txt', 'r.txt')
#shutil.copy2('q.txt', 's.txt')

import datetime


print(datetime.datetime.fromtimestamp(1539608403))


# print(os.walk('.'))
