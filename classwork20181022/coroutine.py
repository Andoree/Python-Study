def f():
    s = 0
    while True:
        a = yield
        s += a
        print(s)


ff = f()
ff.__next__()
ff.send(5)
ff.send(100)
ff.send(150)
ff.close()