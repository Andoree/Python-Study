# download pdfs
import re, requests

# <a [a-zA-Z_ ]*
pattern_without_extension = r'href="(?P<url>[a-zA-Z0-9_:/.]*\.'  # pdf"$'


def start_search(url, extension):
    pattern = pattern_without_extension + extension + ')"'
    download_files(url, pattern)


def download_files(url, pattern):
    p = re.compile(pattern)
    print(pattern)
    m = p.search(r'<a href="doc.pdf">')
    print(p.search(r'<a href="doc.pdf">'))
    #  m = p.match(r'<a href="doc.pdf">')
    print(m.group('url'))
    r = requests.get(url)

    for line in r.iter_lines():
        #    print(line)
        for m in p.finditer(str(line)):
            #  print(m)
            print(m.group("url"))
            download_file(m.group('url'))


def download_file(file_url):
    r = requests.get(file_url)
    filename = file_url.split('/')[-1]
    print(filename)
    f = open('downloads/' + filename, 'wb')
    f.write(r.content)
    f.close()


start_search('https://wikipedia.org/wiki/London', 'pdf')
