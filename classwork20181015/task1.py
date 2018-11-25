import datetime
import shutil
import os

'''
for f in os.listdir('music'):
    #  print(f)
    #  fd = open(f)

    print(os.path.abspath(os.curdir))
    if os.path.isdir(f):
        os.chdir(f)
        os.mkdir("def")

    if f.endswith(".txt"):
        os.rename(f, "text" + f)

# print(str(fd.readlines()))
'''
os.path.getmtime('music')


def musicRange(dateFrom, dateTo):
    filename = 'audios %s %s.m3u' % (dateFrom.strip(':'), dateTo.strip(':'))
    playlist = open('music/' + filename, "w")
    dt_from = datetime.datetime.strptime(dateFrom, "%Y-%m-%d %H:%M").timestamp()
    dt_to = datetime.datetime.strptime(dateTo, "%Y-%m-%d %H:%M").timestamp()
    files = []
    for f in os.listdir('music'):
        if dt_from <= os.path.getmtime('music/' + f) <= dt_to:
            files.append(f)

    for str in files:
        print(str)
        playlist.write(str + '\n')


    timeFrom = datetime.datetime


musicRange('2018-03-11 16:00', '2018-03-15 23:22')
