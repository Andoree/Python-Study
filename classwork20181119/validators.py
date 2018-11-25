import os
import re


def validate_supercopy(f):
    def wrapper(input_data):
        if len(input_data) != 3:
            print('Incorrect number of arguments')
        elif not os.path.exists(input_data[1]):
            print('File % not found.' % input_data[1])
        elif not input_data[2].isdigit():
            print('%s is not a number.' % input_data[2])
        else:
            n = int(input_data[2])
            if n == 0:
                print('Zero copies entered. Nothing to copy')
            else:
                f(input_data)

    return wrapper


def validate_grep(input_data):
    length = len(input_data)
    pattern = input_data[1]
    search_item = input_data[-1]
    recursive = False
    if length != 3:
        if length != 4:
            print('Incorrect number of arguments')
            return None
        recursive = True

    if recursive == True and input_data[2] != '-r':
        print('invalid grep parameter : %' % input_data[2])
        return None
    if os.path.isdir(search_item):
        search_type = 'dir'
    elif os.path.isfile(search_item):
        search_type = 'file'
    else:
        return None
    try:
        re.compile(pattern)
        return search_type, search_item, pattern, recursive
    except re.error:
        print('%s is not a regex pattern' % pattern)
