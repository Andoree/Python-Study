import requests
from bs4 import BeautifulSoup

from task_1.download import download_all


class FileFinder:
    def __init__(self, url, extension):
        self.url = url
        self.extension = extension
        self.found = []

    def save_file(self):
        filename = self.url.split('/')[-1] + '.html'
        print(filename)
        r = requests.get(self.url)
        with open(filename, 'wb') as output_file:
            output_file.write(r.text.encode('UTF-8'))
        return filename

    def validate_url(self, url_found):
        length = len(self.extension)
        if url_found[-length:] == self.extension:
            return True

    def start(self):
        filename = self.save_file()
        self.find_files(filename)
        #for item in self.found:
        #    print(item)
        download_all(self.found)
        # todo: do something with found urls

    def find_files(self, filename):
        with open(filename, 'rb') as input_file:
            text = input_file.read()
        soup = BeautifulSoup(text)
        citation_list = soup.find_all('cite', {'class': 'citation web'})
        for c in citation_list:
            url = c.find('a').get('href')
            if self.validate_url(url):
                self.found.append(url)
                # todo
                pass
        #  print(c.find('a').get('href'))
        #  print(type(c.find('a').get('href')))


def main():
    url = 'https://en.wikipedia.org/wiki/London'
    file_finder = FileFinder(url, 'pdf')
    file_finder.start()


if __name__ == '__main__':
    main()
