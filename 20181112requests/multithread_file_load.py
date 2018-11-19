# download pdfs
import multiprocessing as mp
import re
import requests

pattern_without_extension = r'href="(?P<url>[a-zA-Z0-9_:/.]*\.'  # pdf"$'


class FileDownloader:
    pattern_without_extension = r'href="(?P<url>[a-zA-Z0-9_:/.]*\.'

    def __init__(self, url, extension):
        self.url = url
        self.pattern = pattern_without_extension + extension + ')"'
        mp.freeze_support()
        #      t1 = mp.Process(target=run, args=('thread 1 ONE ONE',))
        self.semaphore = mp.Semaphore(3)

    def download_file(self, file_url):
        self.semaphore.acquire()
        print('LOCK ON')
        r = requests.get(file_url)
        filename = file_url.split('/')[-1]
        f = open('downloads/' + filename, 'wb')
        f.write(r.content)
        f.close()
        print("LOCK IS ABOUT TO GET TURNED OFF")
        self.semaphore.release()

    def download_files(self):
        p = re.compile(self.pattern)
        r = requests.get(self.url)
        for line in r.iter_lines():
            for m in p.finditer(str(line)):
                mp.Process(target=FileDownloader.download_file,
                           args=(self, m.group('url'),)).start()



def main():
    fd = FileDownloader('https://wikipedia.org/wiki/London', 'pdf')
    fd.download_files()


if __name__ == '__main__':
    main()
