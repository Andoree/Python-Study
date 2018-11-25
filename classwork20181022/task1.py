import datetime
import re

filename = 'data.txt'
f = open(filename)
schedule = []
weekday = ""
str = ""
day_pattern = re.compile(r'^[A-Z]([a-z]){2}$')
entry_pattern = re.compile(r'^(?P<time>\d{2}:\d{2}(\-\d{2}:\d{2})?)'
                           r'    (?P<subject>[a-zA-z]+)    '
                           r'(?P<teacher>[a-zA-z ]+)$')

for line in f:
    if re.match(day_pattern, line):
        print(line)
        weekday = line
    else:
        t = re.match(entry_pattern, line)
        print(line)
        print(t)
        if t: '''
            time = t.group("time")
            subject = t.group("subject")
            teacher = t.group("teacher")
            schedule.append(entities.Entry(weekday, time, subject, teacher))
'''
for entity in schedule:
    print(entity)


def hours_per_day(schedule):
    stat = {}
    for i in range(len(schedule)):
        time_data = schedule[i].split("-")
        delta = datetime.timedelta()
        time1 = datetime.datetime.strptime(time_data[0], "%H:%M")
        time2 = datetime.datetime.strptime(time_data[1], "%H:%M") \
            if (len(time_data) == 2) \
            else datetime.datetime.strptime(schedule[i + 1].time.split("-")[0], "%H:%M")

        delta += time2 - time1
        weekday = schedule[i].weekday
        if weekday in stat:
            stat[weekday] = stat[weekday] + delta
        else:
            stat[weekday] = delta

    return stat


stat = hours_per_day(schedule)
print(stat)
'''
for k,v in stat.iteritems():
    print(k) #datetime)
'''
