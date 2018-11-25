import os
import shutil

from file_downloader import FileDownloader
from grep_operations import grep_file, grep_dir_recursive, grep_dir_non_recursive
from validators import validate_supercopy, validate_wget
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


def process_grep(input_data):
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


def process_wget(input_data):
    data = validate_wget(input_data)
    if data:
        url = data[0]
        if data[1]:
            extension = data[1]
            # todo: а куда скачивать?
            file_downloader = FileDownloader(url, extension)
            file_downloader.download_files()
        else:
            # todo : download with url only
            pass
    #    print(data)
    #    print('op : ' + str(data[0]))
    #    print('url : ' + data[1])
    #    print('extension : ' + str(data[2]))
    pass


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
            process_wget(input_data)
        elif command == 'makenote':
            pass
        #   process_makenote(input_data)
        elif command == 'grep':
            process_grep(input_data)
            pass
        elif command == '':
            print('$')
        else:
            print('command not found')
    #


process_wget(('wget', 'dada', 'pdf'))
process_wget(('wget', 'dada',))
# if __name__ == '__main__':
#    main()
 