import multiprocessing as mp


# аккуратно, переменные не шарятся между потоками


def run(value):
    for i in range(10000):
        print(value)


def main():
    mp.freeze_support()
    t1 = mp.Process(target=run, args=('thread 1 ONE ONE',))
    t2 = mp.Process(target=run, args=('thread2 TWO TWO',))
    t3 = mp.Process(target=run, args=('thread3 THREE THREE',))
    t4 = mp.Process(target=run, args=('thread4 FOUR FOUR',))
    t1.start()
    t2.start()
    t3.start()
    t4.start()


if __name__ == '__main__': main()
