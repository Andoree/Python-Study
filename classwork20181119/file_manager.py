import os
import shutil

from validators import validate_supercopy
from validators import validate_grep


@validate_supercopy
def process_supercopy(input_data):
    filename = input_data[1]
    n = int(input_data[2])
    size = len(input_data[2])
    k = filename.rfind(".")
    for i in range(1, n + 1):
        new_filename = filename[:k] + str(i).zfill(size) + '.' + filename[k + 1:]
        shutil.copy(filename, new_filename)

def process_makenote(input_data):
    try:
        search_type, search_item, pattern, recursive = validate_grep(input_data)
        if search_type == 'file':
            # todo: может, просто вернуть файл, не??
            grep_file(pattern, search_item)
        elif search_type == 'dir':
            if recursive:
                grep_dir_recursive(pattern, search_item)
            else:
                grep_dir_non_recursive(pattern, search_item)
    except Exception:
        pass
    '''
    3 или 4 слова.
    PATH re.compile - валидация
    '''
# validation


# processing

def main():
    while True:
        input_line = input(os.path.abspath(os.curdir) + '\n$')
        if not input_line:
            continue
        input_data = input_line.split()
        command = input_data[0]
        if command == 'exit':
            break
        elif command == 'supercopy':
            process_supercopy(input_data)
        elif command == 'wget':
            pass
        elif command == 'makenote':
            process_makenote(input_data)
        elif command == 'grep':
            pass
        else:
            print('command not found')
    # elif command == ''


if __name__ == '__main__':
    main()
