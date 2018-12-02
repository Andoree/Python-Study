import multiprocessing as mp

import requests


def download_file(url, semaphore):
    semaphore.acquire()
    print('semaphore acquire')
    filename = (url.split('/')[-1])
    r = requests.get(url)
    file = open('files/' + filename, 'wb')
    file.write(r.content)
    file.close()
    print('semaphore release')
    semaphore.release()


def download_all(urls):
    mp.freeze_support()
    semaphore = mp.Semaphore(3)
    for url in urls:
        mp.Process(target=download_file,
                   args=(url, semaphore,)).start()
