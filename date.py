def date(**kwargs):
    if kwargs.get('day'):
        day = kwargs['day']
    else:
        day = 1
    if kwargs.get('month'):
        month = kwargs['month']
    else:
        month = 9

    if kwargs.get('year'):
        year = kwargs['year']
    else:
        year = 2018
    return "today is {} of {} of {}".format(day, month, year)


print('month and year : ', date(month=11, year=2000))
print('nothing : ', date())
print('day only : ', date(day=8))
print('day and month : ', date(day=23, month=7))
