import requests


# download file
# https://wikipedia.org/wiki/London
def download_file_by_url(url):
    filename = url.split('/')[-1]
    print(filename)
    r = requests.get(url)
    # r.text

    f = open(filename, 'wb')
    f.write(r.content)
    # print(r.headers.get('content-type'))

    # менеджер контекста. При выходе из него будет вызван деструктор дескриптора.
    # f - дескриптор.
    # with open('', 'wb') as f:
    #    f.write(r.content)
    f.close()


download_file_by_url \
    ('http://www.bestprintingonline.com/help_resources/Image/Ducky_Head_Web_Low-Res.jpg')
